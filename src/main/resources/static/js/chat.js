// document.querySelector('#send').addEventListener('click', function () {
//     let template = `<div class="line">
//           <span class=" mine"> ${document.querySelector('#input').value}</span>
//         </div>`
//
//     // document.getElementById('input').innerText = ''
//     document.querySelector('.chat-content').insertAdjacentHTML('beforeend', template)
// })

// HTML 요소 찾기
const chatMessages = document.querySelector(".chat-messages");
const chatForm = document.querySelector(".chat-input form");
const chatInput = document.querySelector(".chat-input input[type='text']");

// 채팅 메시지 추가 함수
function addChatMessage(message) {
    const messageEl = document.createElement("li");
    messageEl.classList.add("message");
    messageEl.textContent = message;
    chatMessages.appendChild(messageEl);
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
