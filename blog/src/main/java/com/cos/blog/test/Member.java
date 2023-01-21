// DB 대신 모델 만들어서 활용하는 것

// (1) 14강
// (2) 16강 - lombok 셋팅

package com.cos.blog.test;

import lombok.Data;
// import lombok.Getter;
// import lombok.Setter;

// @Getter
// lombok이 지원하는 getter

// @Setter
// lombok이 지원하는 setter

// @Data -> getter/setter
@Data
public class Member {
	private int id;
	private String username;
	private String password;
	private String email;
	
// (1)
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
