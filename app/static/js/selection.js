var overlay = document.getElementById("overlay");
var toggleSelection = document.getElementById("set-area");
var coordinateX1 = document.getElementById("x1");
var coordinateY1 = document.getElementById("y1");
var coordinateX2 = document.getElementById("x2");
var coordinateY2 = document.getElementById("y2");
// var ipAddress = document.getElementById("ip-address");
const streamForm = document.getElementById("stream-form");
var elem = document.documentElement;
var div = document.getElementById("div"),
    x1 = 0,
    y1 = 0,
    x2 = 0,
    y2 = 0;

function openFullscreen() {
    if (elem.requestFullscreen) {
        elem.requestFullscreen();
    } else if (elem.webkitRequestFullscreen) {
        elem.webkitRequestFullscreen();
    } else if (elem.msRequestFullscreen) {
        elem.msRequestFullscreen();
    }
}

function closeFullscreen() {
    if (document.exitFullscreen) {
        document.exitFullscreen();
    } else if (document.webkitExitFullscreen) {
        document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) {
        document.msExitFullscreen();
    }
}

function reCalc() {
    var x3 = Math.min(x1, x2);
    var x4 = Math.max(x1, x2);
    var y3 = Math.min(y1, y2);
    var y4 = Math.max(y1, y2);
    div.style.left = x3 + "px";
    div.style.top = y3 + "px";
    div.style.width = x4 - x3 + "px";
    div.style.height = y4 - y3 + "px";
}

function mouseDown(e) {
    div.hidden = 0;
    x1 = e.clientX;
    y1 = e.clientY;
    reCalc();
}

function mouseUp(e) {
    div.hidden = 1;
    coordinateX1.value = x1;
    coordinateY1.value = y1;
    coordinateX2.value = x2;
    coordinateY2.value = y2;
    overlay.style.display = "none";
    closeFullscreen();
    elem.removeEventListener("mousemove", mouseMove);
    document.getElementById("stream-form").submit();
}

function mouseMove(e) {
    x2 = e.clientX;
    y2 = e.clientY;
    reCalc();
}

toggleSelection.addEventListener("click", function () {
    elem.addEventListener("mousedown", mouseDown, { once: true });
    elem.addEventListener("mouseup", mouseUp, { once: true });
    elem.addEventListener("mousemove", mouseMove);
    openFullscreen();
    overlay.style.display = "block";
});

const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);

var x = 0;

if (urlParams.get("x1")) {
    coordinateX1.value = urlParams.get("x1");
    x += 1;
}
if (urlParams.get("y1")) {
    coordinateY1.value = urlParams.get("y1");
    x += 1;
}
if (urlParams.get("x2")) {
    coordinateX2.value = urlParams.get("x2");
    x += 1;
}
if (urlParams.get("y2")) {
    coordinateY2.value = urlParams.get("y2");
    x += 1;
}

const successMsg = document.getElementById("success-msg");

const stopBtn = document.getElementById("stop-btn");

if (x == 4 && urlParams.get("stop") == null) {
    successMsg.style.display = "inline";
    stopBtn.disabled = false;
    toggleSelection.disabled = true;
} else {
    successMsg.style.display = "none";
    stopBtn.disabled = true;
    toggleSelection.disabled = false;
}
