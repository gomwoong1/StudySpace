// HTML 요소 찾기
const chatMessages = document.querySelector(".chat-messages");
const chatForm = document.querySelector(".chat-input form");
const chatInput = document.querySelector(".chat-input input[type='text']");

function addSystemChatMessage(message) {
    const messageEl = document.createElement("li");
    messageEl.classList.add("message");
    messageEl.textContent = message;
    chatMessages.appendChild(messageEl);
}

function addChatMessage(message) {
    const messageEl = document.createElement("li");
    messageEl.classList.add("message-right");
    messageEl.textContent = message;

    chatMessages.appendChild(messageEl);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// submit 이벤트 핸들러
chatForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const message = chatInput.value;
    if (message.trim() !== "") {
        addChatMessage(message);
        chatInput.value = "";
    }
});