// var container = document.getElementById("container");
// var selection = document.createElement("div");
// selection.classList.add("selection-box");

// container.addEventListener("mousedown", function (e) {
//     var click_y = e.pageY;
//     var click_x = e.pageX;

//     selection.style.top = click_y + "px";
//     selection.style.left = click_x + "px";
//     selection.style.width = 0;
//     selection.style.height = 0;
//     selection.appendChild(container);

//     container.addEventListener("mousemove", function (e) {
//         var move_x = e.pageX,
//             move_y = e.pageY,
//             width = Math.abs(move_x - click_x),
//             height = Math.abs(move_y - click_y),
//             new_x,
//             new_y;

//         new_x = move_x < click_x ? click_x - width : click_x;
//         new_y = move_y < click_y ? click_y - height : click_y;

//         selection.style.width = width + "px";
//         selection.style.height = height + "px";
//         selection.style.top = new_y + "px";
//         selection.style.left = new_x + "px";
//     });

//     container.addEventListener("mouseup", function (e) {
//         container.removeEventListener("mousemove");
//         selection.remove();
//     });
// });

const overlay = document.getElementById("overlay");
const area = document.getElementById("selection-area");

var elem = document.documentElement;
var startPoint = [0, 0];
var endPoint = [0, 0];

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

function actionOne(e) {
    area.style.display = "block";
    startPoint = [e.clientX, e.clientY];
    document.addEventListener("mousemove", drag);
    document.addEventListener("mouseup", actionTwo);
}

function actionTwo(e) {
    document.removeEventListener("mousedown");
    document.removeEventListener("mousemove");
    document.removeEventListener("mouseup");
    endPoint = [e.clientX, e.clientY];
}

function drag(e) {
    endPoint = [e.clientX, e.clientY];
    area.style.left = startPoint[0] + "px";
    area.style.top = startPoint[1] + "px";
    area.style.width = endPoint[0] - startPoint[0] + "px";
    area.style.height = endPoint[1] - startPoint[1] + "px";
}

document.addEventListener("mousedown", function (e) {
    // startPoint = [event.clientX, event.clientY];
    // area.style.left = startPoint[0] + "px";
    // area.style.top = startPoint[1] + "px";
    // area.style.width = "0px";
    // area.style.height = "0px";
    // area.style.display = "block";
    // overlay.style.display = "block";
    // startPoint = [event.clientX, event.clientY];
    // overlay.style.display = "block";
    // area.style.display = "block";
    // area.style.left = startPoint[0] + "px";
    // area.style.top = startPoint[1] + "px";
    // console.log("Mouse down: " + startPoint);
});

document.addEventListener("mouseup", function (e) {
    // if (document.fullscreenElement) {
    //     closeFullscreen();
    // }
    // overlay.style.display = "none";
    // endPoint = [event.clientX, event.clientY];
    // area.style.display = "none";
    // console.log("Mouse up: " + endPoint);
    // x1.value = startPoint[0];
    // y1.value = startPoint[1];
    // x2.value = endPoint[0];
    // y2.value = endPoint[1];
});

document.addEventListener("mousemove", function (e) {
    // area.style.width = e.clientX - startPoint[0] + "px";
    // area.style.height = e.clientY - startPoint[1] + "px";
    // console.log("Mouse move: " + [e.clientX, e.clientY]);
});

document.getElementById("area").addEventListener("click", function () {
    // openFullscreen();
    overlay.style.display = "block";
    document.addEventListener("mousedown", actionOne);
    console.log("clicked");
});

// var mousedownID = -1;  //Global ID of mouse down interval
// function mousedown(event) {
//     if (mousedownID == -1)  //Prevent multimple loops!
//         mousedownID = setInterval(whilemousedown, 100 /*execute every 100ms*/);

// }
// function mouseup(event) {
//     if (mousedownID != -1) {  //Only stop if exists
//         clearInterval(mousedownID);
//         mousedownID = -1;
//     }

// }
// function whilemousedown() {
//     /*here put your code*/
// }
// //Assign events
// document.addEventListener("mousedown", mousedown);
// document.addEventListener("mouseup", mouseup);
// //Also clear the interval when user leaves the window with mouse
// document.addEventListener("mouseout", mouseup);
