// 24강 insert 테스트 클래스
package com.cos.blog.test;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

import com.cos.blog.model.RoleType;
import com.cos.blog.model.User;
import com.cos.blog.repository.UserRepository;

/*
 	MEMO
 	
 	@Autowired
 	해당 어노테이션이 붙은 객체는 UserRepository 타입을 스프링이 관리하고 있다면
 	자동으로 값을 넣어준다. 
 	해당 어노테이션이 생략된다면 null이 된다. 가져올 값이 없기 때문이다.
 	
 	
 */

@RestController
public class DummyControllerTest {
	
	// 의존성 주입(DI)
	@Autowired
	private UserRepository userRepository;
	
	@PostMapping("/dummy/join")
	public String join(User user) {
		
		user.setRole(RoleType.USER);
		userRepository.save(user);
		return "회원가입이 완료되었습니다.";
	}
}
