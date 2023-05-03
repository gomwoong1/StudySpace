let index = {
    init: function() {
        $('#send_btn').on("click", () => {
            this.send();
        })
    },

    send: function() {
        let text = $("#text").val()

        $.ajax( {
            type: "POST",
            url: "/jsonData",
            data: JSON.stringify(text),
            contentType: "application/json; charset=utf-8",
            dataType: "json"
        }).done(function(resp) {
            $('#res').text(resp.PData)
        }).fail(function(error) {
            alert(JSON.stringify(error));
        });
    }
}

index.init()