const overlay = document.getElementById("overlay");
const toggleSelection = document.getElementById("area");

var elem = document.documentElement;

/* View in fullscreen */
function openFullscreen() {
    if (elem.requestFullscreen) {
        elem.requestFullscreen();
    } else if (elem.webkitRequestFullscreen) {
        /* Safari */
        elem.webkitRequestFullscreen();
    } else if (elem.msRequestFullscreen) {
        /* IE11 */
        elem.msRequestFullscreen();
    }
}

/* Close fullscreen */
function closeFullscreen() {
    if (document.exitFullscreen) {
        document.exitFullscreen();
    } else if (document.webkitExitFullscreen) {
        /* Safari */
        document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) {
        /* IE11 */
        document.msExitFullscreen();
    }
}

var div = document.getElementById("div"),
    x1 = 0,
    y1 = 0,
    x2 = 0,
    y2 = 0;

var coordinateX1 = document.getElementById("x1");
var coordinateY1 = document.getElementById("y1");
var coordinateX2 = document.getElementById("x2");
var coordinateY2 = document.getElementById("y2");

function reCalc() {
    //This will restyle the div
    var x3 = Math.min(x1, x2); //Smaller X
    var x4 = Math.max(x1, x2); //Larger X
    var y3 = Math.min(y1, y2); //Smaller Y
    var y4 = Math.max(y1, y2); //Larger Y
    div.style.left = x3 + "px";
    div.style.top = y3 + "px";
    div.style.width = x4 - x3 + "px";
    div.style.height = y4 - y3 + "px";
}

// onmousedown = function (e) {
//     div.hidden = 0; //Unhide the div
//     x1 = e.clientX; //Set the initial X
//     y1 = e.clientY; //Set the initial Y
//     reCalc();
// };

// onmousemove = function (e) {
//     x2 = e.clientX; //Update the current position X
//     y2 = e.clientY; //Update the current position Y
//     // console.log(x2, y2);
//     reCalc();
// };

// onmouseup = function (e) {
//     div.hidden = 1; //Hide the div
//     coordinateX1.value = x1;
//     coordinateY1.value = y1;
//     coordinateX2.value = x2;
//     coordinateY2.value = y2;
// };

// elem.addEventListener("mousedown", function (e) {
//     div.hidden = 0; //Unhide the div
//     x1 = e.clientX; //Set the initial X
//     y1 = e.clientY; //Set the initial Y
//     reCalc();
// });

function mouseDown(e) {
    div.hidden = 0; //Unhide the div
    x1 = e.clientX; //Set the initial X
    y1 = e.clientY; //Set the initial Y
    reCalc();
}

// elem.addEventListener("mouseup", function (e) {
//     div.hidden = 1; //Hide the div
//     coordinateX1.value = x1;
//     coordinateY1.value = y1;
//     coordinateX2.value = x2;
//     coordinateY2.value = y2;
//     overlay.style.display = "none";
//     closeFullscreen();
// });

function mouseUp (e) {
    div.hidden = 1; //Hide the div
    coordinateX1.value = x1;
    coordinateY1.value = y1;
    coordinateX2.value = x2;
    coordinateY2.value = y2;
    overlay.style.display = "none";
    closeFullscreen();
    elem.removeEventListener("mousemove");
}

// elem.addEventListener("mousemove", function (e) {
//     x2 = e.clientX; //Update the current position X
//     y2 = e.clientY; //Update the current position Y
//     reCalc();
// });

function mouseMove(e) {
    x2 = e.clientX; //Update the current position X
    y2 = e.clientY; //Update the current position Y
    reCalc();
}

toggleSelection.addEventListener("click", function () {
    elem.addEventListener("mousedown", mouseDown, { once: true });
    elem.addEventListener("mouseup", mouseUp, { once: true });
    elem.addEventListener("mousemove", mouseMove);
    openFullscreen();
    overlay.style.display = "block";
    console.log("clicked");
});
