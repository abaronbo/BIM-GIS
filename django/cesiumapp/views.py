from django.shortcuts import render

# Create your views here.

def cesium_viewer(request):
    return render(request, 'cesium.html')