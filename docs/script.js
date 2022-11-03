"use strict";
let button1 = document.getElementById("button");
button1.addEventListener("click", buttonpressed);
let para1 = document.getElementById("inputfield");
function buttonpressed(event) {
    console.log(event.target);
    para1.textContent = "input= button";
}
let gamepad;
window.addEventListener("gamepadconnected", (e) => {
    console.log("Gamepad connected at index %d: %s. %d buttons, %d axes.", e.gamepad.index, e.gamepad.id, e.gamepad.buttons.length, e.gamepad.axes.length);
    para1.textContent = "gamepad connected: " + e.gamepad.id;
    gamepad = e.gamepad;
    console.log(gamepad.buttons);
    setInterval(update, 20);
});
let buttons = [
    'A', 'B', 'X', 'Y',
    'Start', 'Back', 'Axis-Left', 'Axis-Right',
    'LB', 'RB', 'Power', 'A', 'B', 'X', 'Y',
];
let buttonsCache = [];
let pressed = [];
function update() {
    pressed = [];
    let b = 0;
    if (gamepad.buttons) {
        for (b; b < gamepad.buttons.length; b++) {
            if (gamepad.buttons[b].pressed) {
                pressed.push(buttons[b]);
                break;
            }
        }
    }
    if (gamepad.axes) {
        if (gamepad.axes[0] >= 0.5) {
            pressed.push("L-right");
        }
        if (gamepad.axes[1] >= 0.5) {
            pressed.push("L-down");
        }
        if (gamepad.axes[0] <= -0.5) {
            pressed.push("L-left");
        }
        if (gamepad.axes[1] <= -0.5) {
            pressed.push("L-up");
        }
    }
    para1.textContent = pressed.toString();
}
//# sourceMappingURL=script.js.map