package com.cos.blog.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.method.configuration.EnableGlobalMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

/*
 	빈 등록: 스프링 컨테이너에서 객체를 관리할 수 있게 하는 것
 	
 	@Configuration
 	설정 파일 빈 등록 어노테이션
 	
 	@EnableWebSecurity
 	시큐리티의 필터가 등록이 된다. 필터의 설정은 어노테이션이 붙은 클래스에서 한다.
 	
 	@EnableGlobalMethodSecurity(prePostEnabled = true)
 	특정 주소로 접근할 경우 권한 및 인증을 미리 확인하는 것
 	
 	위의 세개 어노테이션은 세트로 보면 된다.
 */

@Configuration 
@EnableWebSecurity
@EnableGlobalMethodSecurity(prePostEnabled = true)
public class SecurityConfig extends WebSecurityConfigurerAdapter{
	
	/*
	 	request가 요청될 때 경로가 /auth/하위라면 접근을 허용
	 	나머지 경로는 접근 거부
	 	그리고 로그인은 폼 로그인 방식이며 인증이 필요하다면 /auth/loginForm 으로 화면을 이동시킴
	 */
	
	@Override
	protected void configure(HttpSecurity http) throws Exception {
		http
			.authorizeRequests()
			.antMatchers("/auth/**")
			.permitAll()
			.anyRequest()
			.authenticated()
		.and()
			.formLogin()
			.loginPage("/auth/loginForm");
	}
}
