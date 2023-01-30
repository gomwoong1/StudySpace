package com.cos.blog.service;

import javax.transaction.Transactional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.cos.blog.model.User;
import com.cos.blog.repository.UserRepository;

/*
 	MEMO
 	
 	@Service
 	스프링이 컴포넌트 스캔을 통해 자동으로 Bean에 등록해줌. (IoC)
 	
 	
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
	
	@Transactional
	public void 회원가입(User user) {
			userRepository.save(user);
	}
	
	
}
