package com.cos.blog.service;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.cos.blog.model.RoleType;
import com.cos.blog.model.User;
import com.cos.blog.repository.UserRepository;

/*
 	MEMO
 	
 	@Service
 	스프링이 컴포넌트 스캔을 통해 자동으로 Bean에 등록해줌. (IoC)
 	
 	@Transactional(readOnly = true)
 	select 할 때 트랜잭션 시작, 서비스 종료시에 트랜잭션 종료. 정합성을 지킴
 */

/*
 	폐기 코드
 	
 	@Transactional
	public int 회원가입(User user) {
		try {
			userRepository.save(user);
			return 1;
		} catch (Exception e) {
			e.getStackTrace();
			System.out.println("UserSerivce: 회원가입() : " + e.getMessage());
		}
		return -1;
	}
 */

@Service
public class UserService {
	
	@Autowired
	private UserRepository userRepository;
	
	@Autowired
	private BCryptPasswordEncoder encoder;
	
	@Transactional
	public void 회원가입(User user) {
		String	rawPassword = user.getPassword();
		String encPassword = encoder.encode(rawPassword);
		user.setRole(RoleType.USER);
		user.setPassword(encPassword);
		userRepository.save(user);
	}
	
	@Transactional
	public void 회원수정(User user) {
		User persistance = userRepository.findById(user.getId())
				.orElseThrow(() -> {
					return new IllegalArgumentException("회원찾기 실패");
				});
		
		String rawPassword = user.getPassword();
		String encPassword = encoder.encode(rawPassword);
		persistance.setPassword(encPassword);
		
		persistance.setEmail(user.getEmail());
	}
	/*
	@Transactional(readOnly = true)
	public User 로그인(User user) {
			return userRepository.findByUsernameAndPassword(user.getUsername(), user.getPassword());
	}
	*/
}
