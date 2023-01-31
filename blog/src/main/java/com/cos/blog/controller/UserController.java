package com.cos.blog.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class UserController {

	// 인증 안된 사용자가 출입할 수 있는 경로 -> /auth/**
	// 그냥 주소가 /이면 index.jsp도 허용
	// static 이하 정적 파일들 허용
	
	@GetMapping("/auth/joinForm")
	public String joinForm() {
		
		return "user/joinForm";
	}
	
	@GetMapping("/auth/loginForm")
	public String loginForm() {
		
		return "user/loginForm";
	}
}
