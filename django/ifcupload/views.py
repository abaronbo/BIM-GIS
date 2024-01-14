
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import DatasetUploadForm, IFCUploadForm
from django.http import JsonResponse, HttpResponse
from .models import BuildingIFC
import csv
from io import TextIOWrapper

# Handles requests to the upload form page. 
def upload_form(request):
    ref_bag_id = request.GET.get('ref_bag_id', '') 
    print("Received ref_bag_id:", ref_bag_id)

    # Initial value for ref_bag_id.
    form = IFCUploadForm(initial={'ref_bag_id': ref_bag_id}) if ref_bag_id else IFCUploadForm()
    
    # Creates a BuildingIFC Object.
    if request.method == 'POST':
        form = IFCUploadForm(request.POST, request.FILES)
        if form.is_valid():
            ref_bag_id = int(form.cleaned_data['ref_bag_id'])
            BuildingIFC.objects.update_or_create(
                ref_bag_id=ref_bag_id,
                defaults={'ifc_file': form.cleaned_data['ifc_file']}
            )
            return redirect('upload_success') 

    return render(request, 'ifcupload/upload_form.html', {'form': form})

# Handles requests to the upload file (IFC) page.
def upload_ifc(request):
    if request.method == 'POST':
        ref_bag_id = request.POST.get('ref_bag_id')
        ifc_file = request.FILES.get('ifc_file')
        BuildingIFC.objects.create(ref_bag_id=ref_bag_id, ifc_file=ifc_file)
        return render(request, 'ifcupload/upload_success.html')
    return HttpResponse('Invalid request', status=400)

# Returns the URL of a building based on its bag_id when the building is left clicked in 
def get_ifc_url(request):
    ref_bag_id = request.GET.get('ref_bag_id')
    try:
        building_ifc = BuildingIFC.objects.get(ref_bag_id=ref_bag_id)
        return JsonResponse({'status': 'success', 'ifc_url': building_ifc.ifc_file.url})
    except BuildingIFC.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Not found'}, status=404)

# Handles the upload of CSV files.
def upload_dataset(request):
    if request.method == 'POST':
        form = DatasetUploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_dataset_file(request.FILES['dataset_file'])
            return render(request, 'upload_dataset_success.html')
    else:
        form = DatasetUploadForm()

    return render(request, 'upload_dataset.html', {'form': form})

# Processes CSV files, creating BuildingIFC objects based on the headers for the bag id and path.
def handle_dataset_file(f):
    text_file = TextIOWrapper(f, encoding='utf-8')
    reader = csv.reader(text_file)

    headers = next(reader, None)
    if headers is None:
        return
    try:
        ref_bag_id_index = headers.index('ref_bag_id')
        file_path_index = headers.index('file_path')
    except ValueError as e:
        print("Column names not found in CSV header. Error:", e)
        return
    for row in reader:
        try:
            ref_bag_id = int(row[ref_bag_id_index])
            file_path = row[file_path_index]
            BuildingIFC.objects.update_or_create(ref_bag_id=ref_bag_id, defaults={'ifc_file': file_path})
        except (ValueError, IndexError) as e:
            print("Error processing row:", row, "Error:", e)

    text_file.detach()
