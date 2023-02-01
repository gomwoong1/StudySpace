package com.cos.blog.config.auth;

import java.util.ArrayList;
import java.util.Collection;

import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import com.cos.blog.model.User;

import lombok.Getter;

// 스프링 시큐리티가 로그인 요청 가로채서 로그인을 진행하고 완료가 되면 UserDetails 타입의 오브젝트를
// 스프링 시큐리티의 고유한 세션 저장소에 저장을 해준다.  ( 여기선 UserDetails 타입의 PrincipalDetail )

//@Getter -> user의 getter를 사용하기 위함.

@Getter
public class PrincipalDetail implements UserDetails {
	private User user;  // 컴포지션 ( 객체를 품고 있는 것. 상속과는 다름 )

	public PrincipalDetail(User user) {
		this.user = user;
	}
	
	@Override
	public String getPassword() {
		return user.getPassword();
	}

	@Override
	public String getUsername() {
		return user.getUsername();
	}

	// 계정이 만료되지 않았는지 리턴 (true: 만료되지 않음)
	@Override
	public boolean isAccountNonExpired() {
		return true;
	}

	// 계정이 잠기지 않았는지 리턴 (true: 잠기지 않음)
	@Override
	public boolean isAccountNonLocked() {
		return true;
	}

	// 비밀번호가 만료되지 않았는지 리턴 (true: 만료되지 않음)
	@Override
	public boolean isCredentialsNonExpired() {
		return true;
	}

	// 계정이 활성화(사용가능)인지 리턴 (true: 활성화)
	@Override
	public boolean isEnabled() {
		return true;
	}
	
	// 계정이 어떤 권한을 가졌는지를 리턴
	@Override
	public Collection<? extends GrantedAuthority> getAuthorities() {
		
		Collection<GrantedAuthority> collectros = new ArrayList<>();
		collectros.add( () -> { return "ROLE_"+user.getRole(); });
		
//		collectros.add(new GrantedAuthority() {
//			
//			@Override
//			public String getAuthority() {
//				// 스프링에서 ROLE 앞에 "ROLE_"가 꼭 붙어야 함. 규칙임.  --> ROEL_USER / ROLE_ADMIN
//				return "ROLE_"+user.getRole();
//			}
//		});
		return collectros;
	}
	
}
