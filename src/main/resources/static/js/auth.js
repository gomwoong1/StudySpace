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
            username: $('#_username').val(),
            password: $('#_pwd').val(),
            name: $('#_name').val(),
            sex: $('#_sex').val(),
            department: $('#_dept').val(),
            studentNumber: $('#_stdNumber').val(),
            phone: $('#_tel').val()
        }

        $.ajax( {
            type: "POST",
            url: "/auth/joinProc",
            data: JSON.stringify(data),
            contentType: "application/json; charset=utf-8",
            dataType: "json"
        }).done(function(resp) {
            if (resp.status == 500) {
                alert("회원가입에 실패하였습니다.");
            }
            else {
                alert("회원가입 되었습니다.");
                location.href="/";
            }
        }).fail(function(error) {
                alert(JSON.stringify(error));
        });
    },

    login: function() {

    }
}

index.init();