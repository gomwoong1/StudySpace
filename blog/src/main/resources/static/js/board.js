let index = {
	init: function() {
		$("#btn_save").on("click", () => {
			this.save();
		});
	},
	
	save: function() {
		let data = {
			title: $("#title").val(),
			content: $("#content").val(),
		};
		
		// ajax 통신을 이용해서 3개의 데이터를 json으로 변경 후 insert 요청할 것
		// ajax는 비동기 호출이기 때문에 ajax 하단의 코드를 실행하다가 done 혹은 fail 수행
		$.ajax({
			type: "POST",
			url: "/api/board",
			data: JSON.stringify(data),   // json으로 파싱했기 때문에 BODY에 삽입 후 전송
			contentType: "application/json; charset=utf-8",   // BODY 데이터가 어떤 타입인지 기술(MIME 타입)
			dataType: "json"   // 서버에게 요청 후 응답이 왔을 때, 반환된 데이터의 형식을 json으로 지정함.
		}).done(function(resp) {
			alert("글쓰기가 완료되었습니다.");
			location.href="/";
		}).fail(function(error) {
			alert(JSON.stringify(error));
		});  
	}
}

index.init();