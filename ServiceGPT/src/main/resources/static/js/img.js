let index = {
    init: function() {
        $("#send").on("click", ()=> {
            this.sendRequirement();
        });

        $("#input").on("keydown", (event) => {
            if (event.keyCode === 13) {
                event.preventDefault();
                this.sendRequirement();
            }
        });
    },

    sendRequirement: function() {
        let req = $("#input").val();
        $("#input").val('답변 중입니다.');

        $("#input").prop("disabled", true);
        $("#send").prop("disabled", true);

        $.ajax({
            type: "POST",
            url: "/gpt/image/create",
            data: JSON.stringify(req),
            contentType: "application/json; charset=utf-8",
            dataType: "json"
        }).done(function(resp) {
            $('#show-img').attr('src', `data:image/png;base64,${resp.data}`);

            $("#input").val('');
            $("#input").prop("disabled", false);
            $("#send").prop("disabled", false);
        }).fail(function(error) {
            console.log(JSON.stringify(error));
        });
    }
}

index.init();