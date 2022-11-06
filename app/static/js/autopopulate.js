// Element selector
const colorInput = document.getElementById("color-picker");
const outputPreview = document.getElementById("color-preview");
const brightness = document.getElementById("bright");

// Auto-populate inputs
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);

if (urlParams.get("color")) {
    colorInput.value = urlParams.get("color");
    outputPreview.style.backgroundColor = urlParams.get("color");
}
if (urlParams.get("bright")) {
    document.getElementById("bright").value = urlParams.get("bright");
}
if (urlParams.get("color") && urlParams.get("bright")) {
    updateColorPreview();
}
if (urlParams.get("cold")) {
    document.getElementById("cold").value = urlParams.get("cold");
}
if (urlParams.get("warmth")) {
    document.getElementById("warmth").value = urlParams.get("warmth");
}

// Color preview
function updateColorPreview() {
    var color = colorInput.value;
    const r = parseInt(color.substr(1, 2), 16);
    const g = parseInt(color.substr(3, 2), 16);
    const b = parseInt(color.substr(5, 2), 16);
    const a = brightness.value;
    color = "rgba(" + r + "," + g + "," + b + "," + a + ")";
    console.log(color);
    outputPreview.style.backgroundColor = color;
}

colorInput.addEventListener("input", updateColorPreview, false);
brightness.addEventListener("input", updateColorPreview, false);
