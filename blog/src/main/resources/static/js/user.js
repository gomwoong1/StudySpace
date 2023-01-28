let index = {
	init: function() {
		$("#btn_save").on("click", () => {
			this.save();
		});
	},
	
	save: function() {
		let data = {
			username: $("#username").val(),
			password: $("#password").val(),
			email: $("#email").val()
		}
		
		// ajax 통신을 이용해서 3개의 데이터를 json으로 변경 후 insert 요청할 것
		$.ajax().done().fail();  
	}
}

index.init();