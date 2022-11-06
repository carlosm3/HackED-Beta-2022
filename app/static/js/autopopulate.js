// Element selector
// const colorInput = document.getElementById("color-picker");
const red = document.getElementById("red");
const green = document.getElementById("green");
const blue = document.getElementById("blue");
const outputPreview = document.getElementById("color-preview");
const brightness = document.getElementById("bright");
const play = document.getElementById("play");

// Auto-populate inputs
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);

// if (urlParams.get("color")) {
//     colorInput.value = urlParams.get("color");
//     outputPreview.style.backgroundColor = urlParams.get("color");
// }
if (urlParams.get("bright")) {
    document.getElementById("bright").value = urlParams.get("bright");
}
if (urlParams.get("r") && urlParams.get("g") && urlParams.get("b") && urlParams.get("a")) {
    updateColorPreview();
}
if (urlParams.get("cold")) {
    document.getElementById("cold").value = urlParams.get("cold");
}
if (urlParams.get("warmth")) {
    document.getElementById("warmth").value = urlParams.get("warmth");
}
if (urlParams.get("r")) {
    red.value = urlParams.get("r");
}
if (urlParams.get("g")) {
    green.value = urlParams.get("g");
}
if (urlParams.get("b")) {
    blue.value = urlParams.get("b");
}

// Color preview
function updateColorPreview() {
    // var color = colorInput.value;
    // const r = parseInt(color.substr(1, 2), 16);
    // const g = parseInt(color.substr(3, 2), 16);
    // const b = parseInt(color.substr(5, 2), 16);
    const r = red.value;
    const g = green.value;
    const b = blue.value;
    const a = brightness.value;
    color = "rgba(" + r + "," + g + "," + b + "," + a + ")";
    console.log(color);
    outputPreview.style.backgroundColor = color;
}

// colorInput.addEventListener("input", updateColorPreview, false);
brightness.addEventListener("input", updateColorPreview, false);
red.addEventListener("input", updateColorPreview, false);
green.addEventListener("input", updateColorPreview, false);
blue.addEventListener("input", updateColorPreview, false);
