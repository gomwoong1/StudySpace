let index = {
	init: function() {
		$("#btn_save").on("click", () => {
			this.save();
		});
	},
	
	save: function() {
		alert("user의 save 메서드 호출됨.");
	}
}

index.init();