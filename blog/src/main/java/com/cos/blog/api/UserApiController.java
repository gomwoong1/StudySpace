package com.cos.blog.api;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.cos.blog.dto.ResponseDto;
import com.cos.blog.model.RoleType;
import com.cos.blog.model.User;
import com.cos.blog.service.UserService;

@RestController
public class UserApiController {
	
	@Autowired
	private UserService userService;
	
	/*
		해당 방식도 가능하고, 파라미터에 넣어서 호출하는 것도 가능.
		스프링 컨테이너에 session도 bean으로 등록되어 있다는 뜻.
		
		@Autowired
		private HttpSession session;
	 */
	
	@PostMapping("/api/user")
	public ResponseDto<Integer> save(@RequestBody User user) {
		
		System.out.println("UserApiController: save 호출됨.");
		
		user.setRole(RoleType.USER);
		userService.회원가입(user);
		
		return new ResponseDto<Integer>(HttpStatus.OK.value(), 1);
	}
	
	/*  시큐리티 사용에 따른 미사용
	@PostMapping("/api/user/login")
	public ResponseDto<Integer> login(@RequestBody User user, HttpSession session) {
		System.out.println("UserApiController: login 호출됨.");

		User principal = userService.로그인(user);
		
		if (principal != null) {
			session.setAttribute("principal", principal);
		}
		return new ResponseDto<Integer>(HttpStatus.OK.value(), 1);
	}
	*/
}
