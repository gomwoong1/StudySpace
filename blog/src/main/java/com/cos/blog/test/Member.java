// DB 대신 모델 만들어서 활용하는 것

// (1) 14강
// (2) 16강 final을 쓰는 이유를 잠시 예시로 들었을 때.
// (3) 16강 - 실질적으로 사용했던 코드

package com.cos.blog.test;

import lombok.AllArgsConstructor;
import lombok.Data;
// import lombok.NoArgsConstructor;
// import lombok.RequiredArgsConstructor;
// import lombok.Getter;
// import lombok.Setter;

// @Getter
// lombok이 지원하는 getter

// @Setter
// lombok이 지원하는 setter

// @Data -> getter/setter

// @AllArgsConstructor
// 모든 필드를 파라미터로 갖는 생성자
// 강의 Say -> 요즘 잘 안쓴다?

// @RequiredArgsConstructor
// final 키워드가 붙은 모든 필드를 파라미터로 갖는 생성자

// @NoArgsConstructor
// 기본 생성자

@Data
@AllArgsConstructor
public class Member {

	private int id;
	private String username;
	private String password;
	private String email;
	
// (2)
// 상수시키는 이유 -> 어차피 DB에서 데이터 들고 올거니까 불변성 유지를 위해서.
//	private final int id;
//	private final String username;
//	private final String password;
//	private final String email;
	
// (1)
//	private int id;
//	private String username;
//	private String password;
//	private String email;
	
//	public Member(int id, String username, String password, String email) {
//		this.id = id;
//		this.username = username;
//		this.password = password;
//		this.email = email;
//	}
//	
//	public int getId() {
//		return id;
//	}
//	public void setId(int id) {
//		this.id = id;
//	}
//	public String getUsername() {
//		return username;
//	}
//	public void setUsername(String username) {
//		this.username = username;
//	}
//	public String getPassword() {
//		return password;
//	}
//	public void setPassword(String password) {
//		this.password = password;
//	}
//	public String getEmail() {
//		return email;
//	}
//	public void setEmail(String email) {
//		this.email = email;
//	}
}
