// 13~14강 실습 (HTTP 4대 요청)
package com.cos.blog.test;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.RestController;

// 사용자가 요청하면 Data(데이터)를 응답하게 하려면? @RestController
// 만일 사용자가 요청했을 때 HTML을 응답하게 하려면? @Controller

@RestController
public class HttpControllerTest {
	
	// select
	@GetMapping("/http/get")
	public String getTest() {
		return "get 요청";
	}
	
	// insert
	@PostMapping("/http/post")
	public String postTest() {
		return "post 요청";
	}
	
	// update
	@PutMapping("/http/put")
	public String putTest() {
		return "put 요청";
	}
	
	// delete
	@DeleteMapping("/http/delete")
	public String deleteTest() {
		return "delete 요청";
	}
	
}
