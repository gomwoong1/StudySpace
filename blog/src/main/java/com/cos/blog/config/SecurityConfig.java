package com.cos.blog.config;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.method.configuration.EnableGlobalMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;

import com.cos.blog.config.auth.PrincipalDetailService;

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
public class SecurityConfig {
	
	@Autowired
	private PrincipalDetailService principalDetailService;
	/*
	 	request가 요청될 때 경로가 /auth/하위라면 접근을 허용
	 	나머지 경로는 접근 거부
	 	그리고 로그인은 폼 로그인 방식이며 인증이 필요하다면 /auth/loginForm 으로 화면을 이동시킴
	 */
	
	/*
	@Override
	protected void configure(HttpSecurity http) throws Exception {
		http
			.authorizeRequests()
				.antMatchers("/", "/auth/**", "/js/**", "/css/**", "/image/**")
				.permitAll()
				.anyRequest()
				.authenticated()
			.and()
				.formLogin()
				.loginPage("/auth/loginForm");
	} */
	
	// 시큐리티가 대신 로그인 해줄 때 password를 가로채기 하는데,
	// 입력한 평문 password와 DB에 저장된 암호문 password를 비교하려면 평문을 해시 암호화 해야함.
	protected void configure(AuthenticationManagerBuilder auth) throws Exception {
		auth.userDetailsService(principalDetailService).passwordEncoder(encodePWD());
	}
	
	@Bean
	public SecurityFilterChain filterChain(HttpSecurity http) throws Exception{
		http
		  .csrf().disable()  // csrf 토큰 비활성화 (테스트시 걸어두는게 좋음)
		  .authorizeHttpRequests()
		    .antMatchers("/", "/auth/**", "/js/**", "/css/**", "/image/**")
			.permitAll()
			.anyRequest()
			.authenticated()
		  .and()
		    .formLogin()
		    .loginPage("/auth/loginForm")
		    .loginProcessingUrl("/auth/loginProc")  // 시큐리티가 해당 주소로 요청오는 로그인을 가로채 대신 로그인 (form방식, name= username, password)
		    .defaultSuccessUrl("/");   // 요청 성공시 리다이렉트 url
//		    .failureUrl("/auth/joinForm");   //요청 실새피 리다이렉트 url
		
		return http.build();
	}
	
	// return 하는 해시 암호값을 IoC하게 됨 -> 스프링이 관리하게 된다는 뜻.
	@Bean
	public BCryptPasswordEncoder encodePWD() {
		return new BCryptPasswordEncoder();
	}
}
