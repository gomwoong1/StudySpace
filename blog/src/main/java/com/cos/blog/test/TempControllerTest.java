// 17강 - yml설정하기

package com.cos.blog.test;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class TempControllerTest {
	
	@GetMapping("/temp/home")
	public String tempHome() {
		System.out.println("tempHome");
		return "/home.html";
	}
	
	@GetMapping("temp/img")
	public String tempImg() {
		return "/a.png";
	}
	
	// static 이하에 놓은 jsp 파일은 브라우저가 찾을 수 없음
	// jsp가 동적인 파일이기 때문. 따라서 에러 발생 (404)
	// 에러를 해결하려면 경로를 변경해야 함.
	@GetMapping("temp/jsp")
	public String tempJsp() {
		// prefix: /WEB-INF/views/test
		// suffix: test.jsp
		
		return "test";
	}
}
