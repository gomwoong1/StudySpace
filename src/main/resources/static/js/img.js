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
        $("#input").val('');

        $.ajax({
            type: "POST",
            url: "/gpt/image/create",
            data: JSON.stringify(req),
            contentType: "application/json; charset=utf-8",
            dataType: "json"
        }).done(function(resp) {
            $('#show-img').attr('src', `data:image/png;base64,${resp.data}`);
            console.log(resp.data);
        }).fail(function(error) {
            console.log(JSON.stringify(error));
        });
    }
}

index.init();