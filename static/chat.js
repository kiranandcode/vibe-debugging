const socket = io();
const input = document.getElementById("input");
const chat = document.getElementById("chat");

function send() {
    const msg = input.value;
    socket.emit("user_message", { message: msg });
    chat.innerHTML += `<div><b>You:</b> ${msg}</div>`;
    input.value = "";
}

socket.on("bot_message", function(data) {
    chat.innerHTML += `<div><b>LLM:</b> ${data.message}</div>`;
});
