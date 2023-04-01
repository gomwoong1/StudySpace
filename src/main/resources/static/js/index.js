const toggleButton = document.querySelector(".dark-light");

toggleButton.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");
});

let index = {
    init: function() {
        $("#btn_qeustion").on("click", () => {
            this.question();
        });
    },

    question: function() {
        let data = {
            question: $("#qeustion").val()
        };

        $.ajax( {
            type: "POST",
            // url: "/gpt/question",
            url: "/gpt/chat/question",
            data: JSON.stringify(data),
            contentType: "application/json; charset=utf-8",
            dataType: "text"
        }).done(function(resp) {
            $('#answer').val(resp);
        }).fail(function(error) {
            alert(JSON.stringify(error));
        });
    }
}

index.init();