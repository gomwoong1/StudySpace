// 13~14강 실습 (HTTP 4대 요청)
package com.cos.blog.test;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
//import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

// 사용자가 요청하면 Data(데이터)를 응답하게 하려면? @RestController
// 만일 사용자가 요청했을 때 HTML을 응답하게 하려면? @Controller

// browser에서 get 요청은 가능하지만 그 외에 요청은 불가능 -> http 405 Error
// 따라서 별도의 툴이 필요함.

@RestController
public class HttpControllerTest {
	
	// select
	
	/*
	 NOTE
	 
	 (1) 쿼리스트링에서 지정한 변수의 이름과 매개변수의 이름이 일치한다면 대응
	 	 파라미터는 있는데 일치하지 않는다면 에러. 
	           
     (2) 파라미터는 여러 개 받을 수도 있다.
	       
     (3) 파라미터가 오브젝트(객체)라면 인스턴스 변수를 자동으로 매핑하기 때문에
         @RequestParam type name 을 여러 개 적지 않아도 된다.
         단, 입력받지 않은 인스턴스 변수는 String -> null, int는 Error 400을 출력한다.
	*/
	
	@GetMapping("/http/get")
	public String getTest(Member m) {
		return "get 요청: " + m.getId() + ", " + m.getUsername() +", "+ m.getPassword() +", "+ m.getEmail();
	}
	
	// (1)
	//	public String getTest() {
	//		return "get 요청";
	//	}
	
	//  (2)
	//	public String getTest(@RequestParam int id, @RequestParam String username) {	
	//		return "get 요청: " + id + ", " + username;
	//	}
	
	// insert
	
	/*
		NOTE
		
		(1) 원형이다.
			원형에서 파라미터에 @RequestParam type name도 당연히 된다.
			
		(2) 
	*/
	
	@PostMapping("/http/post")
	public String postTest(Member m) {
		return "post 요청";
	}
	
	// (1) 원형
	//	public String postTest() {
	//		return "post 요청";
	//	}
	
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
