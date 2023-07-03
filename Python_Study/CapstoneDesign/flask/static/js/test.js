let index = {
    init: function() {
        $('#send_btn').on("click", () => {
            this.send();
        }),

        $('#send_btn2').on("click", () => {
            this.send_pre();
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
    },

    send_pre: function() {
        let hour = $("#hour").val()

        $.ajax( {
            type: "POST",
            url: "/predictTest",
            data: JSON.stringify(hour),
            contentType: "application/json; charset=utf-8",
            dataType: "json"
        }).done(function(resp) {
            $('#pre_res').text(resp.predict)
        }).fail(function(error) {
            alert(JSON.stringify(error));
        });
    }
}

index.init()