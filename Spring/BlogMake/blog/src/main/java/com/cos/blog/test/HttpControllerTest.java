// 13~14강 실습 (HTTP 4대 요청)
// 16강 실습

package com.cos.blog.test;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
//import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

// 사용자가 요청하면 Data(데이터)를 응답하게 하려면? @RestController
// 만일 사용자가 요청했을 때 HTML을 응답하게 하려면? @Controller

// browser에서 get 요청은 가능하지만 그 외에 요청은 불가능 -> http 405 Error
// 따라서 별도의 툴이 필요함.

// 전송받은 값과 객체(오브젝트) 간 자동 매핑해주는 건 MessageConverter가 담당(스프링)
// Body에 데이터를 보내면 오브젝트에 간편하게 매핑 가능. (@RequestBody 어노테이션 통해서)

@RestController
public class HttpControllerTest {
	
	// 16강 사용 코드
	private final static String TAG = "HttpControllerTest";
	
	/*
	(1) 16강 사용 메서드 - 빌더 어노테이션 사용 전 
	
	public String lombokTest() {
		Member m = new Member(1, "gomwoong", "1234", "gomwoong@naver.com");
		System.out.println(TAG+" getter: " + m.getId());
		m.setId(5000);
		System.out.println(TAG+" getter: " + m.getId());
		
		return "lombok 테스트 완료";
	}
	
	*/
	
	// (2) 16강 사용 메서드 - 빌더 어노테이션 사용
	@GetMapping("/http/lombok")
	public String lombokTest() {
		Member m = Member.builder().username("gomwoong").password("1234")
				.email("gomwoong@naver.com").build();
		System.out.println(TAG+" getter: " + m.getId());
		m.setId(5000);
		System.out.println(TAG+" getter: " + m.getId());
		
		return "lombok 테스트 완료";
	}
	
	
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
	
	// (3)
	@GetMapping("/http/get")
	public String getTest(Member m) {
		return "get 요청: " + m.getId() + ", " + m.getUsername() +", "+ m.getPassword() +", "+ m.getEmail();
	}
	
	/*
	    (1)
		public String getTest() {
			return "get 요청";
		}
	
	    (2)
		public String getTest(@RequestParam int id, @RequestParam String username) {	
			return "get 요청: " + id + ", " + username;
		}
		
	 ------------------------------------------------------------------
	*/ 
	
	// insert
	
	/*
		NOTE
		
		(1) 원형이다.
			원형에서 파라미터에 어노테이션과 자료형의 타입, 이름을 붙여서 받는 것도 된다.
			단, post방식은 어노테이션이 @RequestBody 이다.
			또한 @RequestBody 자료형 text <- text일 필요가 없다. GET과는 다른 점.
			
		(2) HTML에서 <Form> 태그를 이용하여 데이터를 던질 때. 
		    (postman) x-www-form-urlencoded
		
		(3) (postman) row-text / (MIME): text/plain
		    파라미터는 @RequestBody String text 
		
		(4) (postman) row-json / (MIME): application/json
			파라미터는 @RequestBody Member m 
			파라미터에 오브젝트를 입력하면 스프링이 그대로 json과 매핑해줌.
			JSON이 아니라 일반 문자열을 전송하면 매핑 불가로 인해 오류 발생
	*/
	
	// (4)
	@PostMapping("/http/post")
	public String postTest(@RequestBody Member m) {
		return "post 요청: " + m.getId() + ", " + m.getUsername() +", "+ m.getPassword() +", "+ m.getEmail();
	}
	
	/*
	    (1) 원형
		public String postTest() {
			return "post 요청";
		}
	
	    (2)
		public String postTest(Member m) {
			return "post 요청: " + m.getId() + ", " + m.getUsername() +", "+ m.getPassword() +", "+ m.getEmail();
		}
	
	    (3)
		public String postTest(@RequestBody String text) {
			return "post 요청: " + text;
		}
	 -------------------------------------------------------------------
	*/
	 
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
