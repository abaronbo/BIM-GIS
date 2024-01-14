import { Color } from 'three';
import { IfcViewerAPI } from 'web-ifc-viewer';

function CreateViewer(container) {
    let viewer = new IfcViewerAPI({ container, backgroundColor: new Color(0xffffff) });
    viewer.axes.setAxes();
    viewer.grid.setGrid();
    return viewer;
}

const container = document.getElementById('viewer-container');
let viewer = CreateViewer(container);
//const input = document.getElementById("file-input");

window.onmousemove = () => viewer.IFC.selector.prePickIfcItem();

// Select items and log properties
window.ondblclick = async () => {
    const item = await viewer.IFC.selector.pickIfcItem(true);
    if (item.modelID === undefined || item.id === undefined) return;
    console.log(await viewer.IFC.getProperties(item.modelID, item.id, true));
}

viewer.clipper.active = true;

//input.addEventListener("change", async (changed) => {
//    const file = changed.target.files[0];
//    const ifcURL = URL.createObjectURL(file);
//    loadIfc(ifcURL, true); 
//}, false);

async function loadIfc(url, isLocalFile = false) {
    await viewer.dispose();
    viewer = CreateViewer(container);

    let model;
    if (isLocalFile) {
        model = await viewer.IFC.loadIfcUrl(url);
    } else {
        const fullUrl = `${url}`; //http://127.0.0.1:8000
        model = await viewer.IFC.loadIfcUrl(fullUrl);
    }

    viewer.shadowDropper.renderShadow(model.modelID);
}

window.onkeydown = (event) => {
    if (event.code === 'KeyP') {
        viewer.clipper.createPlane();
    }
    else if (event.code === 'KeyO') {
        viewer.clipper.deletePlane();
    }
    else if (event.code === 'Escape') {
        viewer.IFC.selector.unpickIfcItems();
    }
}

// Load IFC from URL
async function loadIfcFromUrl() {
    const urlParams = new URLSearchParams(window.location.search);
    const ifcUrl = urlParams.get('ifc_url');
    console.log("ifc_url = " + ifcUrl)
    if (ifcUrl) {
        await loadIfc(ifcUrl); 
    } else {
        console.log('No IFC URL provided');
    }
}

loadIfcFromUrl();