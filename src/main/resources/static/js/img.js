let index = {
    init: function() {
        $("#input").on("keydown", (event) => {
            if (event.keyCode === 13) {
                event.preventDefault();
                this.sendRequirement();
            }
        });
    },

    sendRequirement: function() {
        let req = $("#input").val();

        $.ajxa({
            type: "POST",
            url: "/gpt/image/create",
            data: JSON.stringify(req),
            contentType: "application/json; charset=utf-8",
            dataType: "json"
        }).done(function(resp) {

        }).fail(function(error) {

        });
    }
}