// 가장 먼저 실습한 것. [3~4강]

package com.cos.blog.test;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

// 스프링 실행시, 기준 패키지 이하의 모든 것들을 스캔해서 메모리에 로드(new)하는 게 아님
// 특정 어노테이션 (@)이 붙어있는 클래스 파일들을 로드(new) 해서 스프링 컨테이너에서 관리

@RestController
public class BlogControllerTest {
	
	@GetMapping("/test/hello")
	public String hello() {
		return "<h1>Hello Springboot</h1>";
	}
}
