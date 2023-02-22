let index = {
    init: function() {
        $('#btn_join').on("click", () => {
            this.join();
        });

        $('#btn_login').on("click", () => {
            this.login();
        });
    },

    join: function() {
        let data = {
            username: $('#_id').val(),
            password: $('#_pwd').val(),
            name: $('#_name').val(),
            sex: $('#_sex').val(),
            department: $('#_dept').val(),
            studentNumber: $('#_stdNumber').val(),
            phone: $('#_tel').val()
        }

        console.log(JSON.stringify(data));
        // $.ajax( {
        //     type: "POST",
        //     data: JSON
        // })
    },

    login: function() {

    }
}

index.init();