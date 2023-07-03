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
            url: "/lr/value",
            data: JSON.stringify(text),
            contentType: "application/json; charset=utf-8",
            dataType: "json"
        }).done(function(resp) {
            $('#normal').text(`보통:${resp.normal}`)
            $('#danger').text(`위험:${resp.danger}`)
            $('#high_danger').text(`고위험:${resp.high_danger}`)
        }).fail(function(error) {
            alert(JSON.stringify(error));
        });
    }
}

index.init()