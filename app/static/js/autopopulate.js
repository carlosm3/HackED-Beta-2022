console.log("Autopopulate script loaded");

// Element selector
const colorInput = document.getElementById("color-picker");
const outputPreview = document.getElementById("color-preview");

// Auto-populate inputs
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
if (urlParams.has("address")) {
    document.getElementById("ip-address").value = urlParams.get("address");
}
if (urlParams.get("color")) {
    colorInput.value = urlParams.get("color");
    outputPreview.style.backgroundColor = urlParams.get("color");
}
if (urlParams.get("bright")) {
    document.getElementById("bright").value = urlParams.get("bright");
}
if (urlParams.get("cold")) {
    document.getElementById("cold").value = urlParams.get("cold");
}
if (urlParams.get("warmth")) {
    document.getElementById("warmth").value = urlParams.get("warmth");
}

// Color preview
colorInput.addEventListener(
    "input",
    function () {
        var color = colorInput.value;
        const r = parseInt(color.substr(1, 2), 16);
        const g = parseInt(color.substr(3, 2), 16);
        const b = parseInt(color.substr(5, 2), 16);
        // console.log(`red: ${r}, green: ${g}, blue: ${b}`)
        console.log(color);

        outputPreview.style.backgroundColor = color;
    },
    false
);
