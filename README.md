# BIM-GIS
This repository contains the source code of BIM-GIS, a web platform based on Django that aims to improve the interoperabilty between Building Information Modeling and Geographic Information System applications.

**Andres Baron Botero**
[a.g.baron.botero@student.tue.nl](mailto:a.g.baron.botero@student.tue.nl)

The BIM-GIS Tutorial by Andres Baron Botero is licensed under the [MIT license](https://mit-license.org).

## Introduction 

Welcome to the BIM-GIS Tutorial! This repository teaches how to build and implement a web platform based on [The Dango Framework](https://www.djangoproject.com) and [web-ifc-viewer](https://github.com/IFCjs/web-ifc-viewer). This platform improves the geometric representation of building entities within an urban environmnet (Semantic 3D city model) by linking databases using viewers with querying capabilities and Unique Resource Locators. Students, researchers and Built Environment enthusiasts are encouraged to recreate and further develop the platform.

## Structure

The project consists of two main components: A web platform and a browser-supported IFC viewer. The web platform contains three main applications, which are:

**cesiumapp:** Based on [CesiumJS](https://cesium.com/learn/cesiumjs-learn/cesiumjs-quickstart/) and used to represent geospatial data.

**ifcupload:** Handles the upload of datasets and IFC files and links them with the geospatial model.

**queryifcapp:** Based on [IfcOpenShell](http://ifcopenshell.org). Provides querying capabilities and enables the download of inventory lists of IfcBuildingElements.

## Tutorial

### Step 1
Download [Visual Studio Code](https://code.visualstudio.com) and the extension **Live Server.**

<img width="1435" alt="Screenshot 2024-01-14 at 12 50 29" src="https://github.com/abaronbo/BIM-GIS/assets/124626975/b7efee1a-c4b7-4ce9-ab87-fcac01cd63c5">

### Step 2
Create a folder. 

`File > Open Folder > New Folder`

### Step 3
Open a new terminal.

`Terminal > New Terminal`

### Step 4
Create and activate a virtual environment.

To create a virtual environment in Unix/Linux/macOS execute the following command:

`python3 -m venv env`

To create a virtual environment in Windows execute the following command:

`py -m venv env`

To activate a virtual environment in Unix/Linux/macOS execute the following command:

`source env/bin/activate`

To activate a virtual environment in Windows execute the following command:

`.\env\Scripts\activate`

### Step 5 
Clone this GitHub Repository by executing the following command:

`git clone https://github.com/abaronbo/BIM-GIS`

### Step 6
Update the directory of the project. First, copy the path of the imported "BIM-GIS" folder:

<img width="503" alt="image" src="https://github.com/abaronbo/BIM-GIS/assets/124626975/6b7dda76-bac3-4094-a9a9-66a5cdbca394">

Then, go to the terminal and type "cd" followed by a space, and paste the path you just copied. Execute the command.

`cd Users/.../NewFolder/BIM-GIS`

Your terminal should now be pointing to the BIM-GIS folder.

### Step 7
Install the requirements. These are a list of packages or libraries (such as Django and IfcOpenShell) that are needed for the development of the platform.

Install the requirements by executing the following command:

`pip install -r requirements.txt`

Additionally, install three and the web-ifc-viewer by executing the commands:

`npm i three@0.135`

`npm i three@0.135 web-ifc-viewer`

### Step 8
Create a Cesium account and get an access token. A detailed tutorial is available [here.](https://cesium.com/learn/cesiumjs-learn/cesiumjs-quickstart/)

Once you have an access token, open the file "cesium.html" located in: 

`BIM-GIS/django/cesiumapp/templates/cesium.html`

Replace the text "YOUR ACCESS TOKEN" found in line 74 with your actual access token:

```javascript
        Cesium.Ion.defaultAccessToken = 'YOUR ACCESS TOKEN';
        const viewer = new Cesium.Viewer('cesiumContainer', {
            terrain: Cesium.Terrain.fromWorldTerrain(),
            animation: false,
            timeline: false,
            baseLayerPicker: false
        });
```

Moreover, you can configure the original destination of the viewer by modifying the coordinates. Currently, it takes us to the city of Eindhoven in the Netherlands:

```javascript
        viewer.camera.flyTo({
            destination: Cesium.Cartesian3.fromDegrees(5.48505, 51.44623, 400),
            orientation: {
                heading: Cesium.Math.toRadians(0.0),
                pitch: Cesium.Math.toRadians(-15.0),
            }
        });
```

### Step 9
Let's take a look at the ifcviewer now. This repository incorporates the implementation of ifcjs-viewer of [Gangula2.](https://github.com/Gangula2/ifcjs-viewer-101) If you want to learn more about developing IFC viewers from scratch, make sure to check his tutorial. BIM-GIS is built on top of his implementation, but adds the following functionalities:

First, a function inside
`BIM-GIS/ifcviewer/bundle.js`
that determines the IFC file to load based on the building that was clicked on the cesium viewer, instead of a file that was uploaded with a button:

```javascript
// Load IFC from URL
async function loadIfcFromUrl() {
    const urlParams = new URLSearchParams(window.location.search);
    const ifcUrl = urlParams.get('ifc_url');
    if (ifcUrl) {
        await loadIfc(ifcUrl);
    } else {
        console.log('No IFC URL provided');
    }
}
loadIfcFromUrl();
```

Additionally, the necessary changes inside
`BIM-GIS/ifcviewer/index.html`
to make queries powered by IfcOpenShell and download the IFC file.

```html
       <!-- Form for the IFC query -->
       <form id="ifc-query-form" method="post" action="http://127.0.0.1:8000/get_ifc_attributes/">
        <div id="query-container">
            <span>Generate an inventory of all entities of class</span>
            <select name="entity_type">
                <!-- List of classes. These classes are a subclass of IfcBuildngElement -->
                <option value="IfcBeam">IfcBeam</option>
                <option value="IfcBuildingElementProxy">IfcBuildingElementProxy</option>
                .
                .
                .
```

### Step  10
You are ready to run the server. In the right bottom corner of Visual Studio Code, click on **Go Live.** You can ignore and close the browser tab that will pop up.

Now, update the directory of the project. Copy the path of the folder named "django" inside "BIM-GIS":

<img width="446" alt="image" src="https://github.com/abaronbo/BIM-GIS/assets/124626975/7df4b056-94e9-4eb0-b4d5-b29e7b837c25">

Then, go to the terminal and type "cd" followed by a space, and paste the path you just copied. Execute the command.

`cd Users/.../NewFolder/BIM-GIS/dango`

Your terminal should now be pointing to the django folder.

Now, execute the following command to run the server:

`python manage.py runserver`

**Congratulations!!! Your server is now running**

You should be able to see the following lines in the terminal, which include the local address of your server: `http://127.0.0.1:8000/`.

<img width="384" alt="image" src="https://github.com/abaronbo/BIM-GIS/assets/124626975/575e2110-b988-462e-b0dd-3f6642c35900">

### Step 11
Now that the server is running, let's go through the platform and validate its functionality. Open a browser (Firefox is recommended) and navigate to the local address displayed in the terminal:

<img width="1440" alt="image" src="https://github.com/abaronbo/BIM-GIS/assets/124626975/2efba09b-bd9c-4ef4-8656-3043ff71adef">

Select the option "Upload Dataset (CSV)". In this demo, we will be uploading the SampleDataset.csv provided in the repository. 

<img width="1440" alt="image" src="https://github.com/abaronbo/BIM-GIS/assets/124626975/882661ee-f1ff-4778-aca5-2957700fe59f">

This file establishes a relationship between two IFC files and the BAG ID of two buildings, highlighted in the picture below:

<img width="1221" alt="image" src="https://github.com/abaronbo/BIM-GIS/assets/124626975/4ea42c06-f367-4e23-aee5-f1c43de9f6c9">


**IMPORTANT:*  The IFC files referenced in the dataset are stored in the path `BIM-GIS/django/media`. In principle, it could be possible to host the files in the web. This was not done in this academic demo (but you are encouraged to try it out and share your results!).

It is also possible to establish the relationship between an IFC file and the BAG ID of the building manually. Simply click on a building and you will be prompted to upload its IFC if the association does not exist yet:

<img width="1440" alt="image" src="https://github.com/abaronbo/BIM-GIS/assets/124626975/9fc28629-6d63-44d8-9c1b-6c8b0e402403">

### Step 12
At this point we have covered how to upload datasets and files. Let's check the added functionaly explained in Step 9. Go to the Cesium viewer and select one of the buildings associacted with an IFC file. The browser will load its associated IFC file in a second tab:

<img width="1440" alt="image" src="https://github.com/abaronbo/BIM-GIS/assets/124626975/5ab2d061-7d6e-48be-bc8b-cfa27c584bc5">

You can download the IFC file and query it using the web interface to obtain an inventory list of the selected class, including all the available property sets and properties.

<img width="1439" alt="image" src="https://github.com/abaronbo/BIM-GIS/assets/124626975/6eaa03af-a014-48d3-8f1b-faa406a43de0">

### Step 13
Did you make a mistake? Would you like to reset the database? Execute the following command to clear the database:

`python manage.py cleardb`

## Congratulations!!!
Great job on completing the BIM-GIS Tutorial! I hope you have gained some insights in the world of Django and IFC viewers. Now you're all set to dive deeper and further develop the platform. Way to go! 🚀🌟 Feel free to reach out [a.g.baron.botero@student.tue.nl](mailto:a.g.baron.botero@student.tue.nl) in case of questions or collaboration opportunities.

























