// 채팅 로그를 담는 배열 생성
let chatLog = [];

let index = {
    init: function () {
        // 전송 버튼을 누르면 이벤트 발생
        $("#send").on("click", ()=> {
            this.addChatLog();
        });
        
        // 채팅 입력창에서 엔터를 누르면 이벤트 발생
        $("#input").on("keydown", (event) => {
            if (event.keyCode === 13) {
                event.preventDefault();
                this.addChatLog();
            }
        });
    },

    addChatLog: function() {
        let text = $("#input").val();

        // 채팅 입력창이 빈칸이 아니라면 이벤트 실행
        if (text !== '') {
            // 채팅 입력창 공백으로 만들기
            $('#input').val('');

            // 서버로부터 응답이 오기 전까지 채팅 입력창 비활성화 및 안내메시지 출력
            $("#input").prop("disabled", true);
            $("#send").prop("disabled", true);
            $("#input").prop("placeholder", "답변하는 중입니다.");

            // 말풍선 추가하기
            $('.chat_content').append(`
                <div class="line">
                    <span class="chat-box mine">${text}</span>
                </div>
            `);

            // 채팅 로그에 role, content 담기
            chatLog.push({
                role: "user",
                content: text,
            });

            // 스크롤 아래로 내려주기
            $('.chat_content').scrollTop($('.chat_content').prop('scrollHeight'));

            $.ajax({
                type: "POST",
                url: "/gpt/chat/question",
                data: JSON.stringify(chatLog),
                contentType: "application/json; charset=utf-8",
                dataType: "json"
            }).done(function(resp) {
                let temp = Object.create(index);
                temp.addSysChatLog(resp.data)
                $("#input").prop("disabled", false);
                $("#send").prop("disabled", false);
                $("#input").prop("placeholder", "채팅을 입력하세요");
            }).fail(function(error) {
                console.log("송수신에러");
                console.log(JSON.stringify(error));
            });
        }
    },

    // 답변이 돌아오면 Model의 답을 추가해주는 이벤트
    addSysChatLog: function(answer) {
        // 채팅 로그에 role, content 담기
        chatLog.push(answer);

        // 말풍선 추가하기
        $('.chat_content').append(`
                <div class="line">
                    <span class="chat-box">${answer.content}</span>
                </div>
        `);

        // 스크롤 아래로 내려주기
        $('.chat_content').scrollTop($('.chat_content').prop('scrollHeight'));
    }
}

index.init();