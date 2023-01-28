// 24강 insert 테스트 클래스
// 26강 select 테스트
// 27강 다중 select 테스트
package com.cos.blog.test;

import java.util.List;
import java.util.function.Supplier;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.data.web.PageableDefault;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

import com.cos.blog.model.RoleType;
import com.cos.blog.model.User;
import com.cos.blog.repository.UserRepository;

/*
 	MEMO
 	
 	@Autowired
 	해당 어노테이션이 붙은 객체는 UserRepository 타입을 스프링이 관리하고 있다면
 	자동으로 값을 넣어준다. 
 	해당 어노테이션이 생략된다면 null이 된다. 가져올 값이 없기 때문이다.
 	
 	@ {id}
 	매핑 어노테이션의 경로에서 중괄호로 변수명을 지정하면 주소로 값을 받을 수 있다.
 	
 	@PathVariable 자료형 변수명
 	위의 매핑에서 중괄호로 받은 변수명을 그대로 메서드의 매개변수로 매핑받는 것
 	변수명은 중괄호에 적어넣은 문자를 똑같이 입력해야 한다.
 */

@RestController
public class DummyControllerTest {
	
	// 의존성 주입(DI)
	@Autowired
	private UserRepository userRepository;
	
	@PostMapping("/dummy/join")
	public String join(User user) {
		
		user.setRole(RoleType.USER);
		userRepository.save(user);
		return "회원가입이 완료되었습니다.";
	}
	
	// {id} 는 파라미터로 전달 받을 수 있음.
	@GetMapping("/dummy/user/{id}")
	public User detail(@PathVariable int id) {
		
		/*
			 findById 메서드의 리턴값은 Optional<T> 이다.
			 값을 전달받아서 DB에서 찾아오려고 했는데 값이 없다면 user가 null이 될 것.
			 이러면 return 값이 null이 될텐데 프로그램에 문제가 생길 수 있으므로 Optional에 감싸서 돌려줌
			 사용자가 감싸진걸 풀어서 null인지 아닌지를 판단
		 
		 	 1. findById(id).get(); 
		 	 절대 null이 반환될 수 없는 구조에서 사용함.
		 	 
		 	 2. findById(id).orElseGet();
		 	 잘 찾아왔다면 그 값을 반환, 없다면 Supplier 인터페이스 이용해 새로운
		 	 user 객체를 만들고 이를 반환. (빈 객체) 
		 	 
		 	 User user = userRepository.findById(id).orElseGet(new Supplier<User>() {
				@Override
				public User get() {
					return new User();
				}
			});
			
			3. findById(id).orElseThrow(new Supplier<IllegalArgumentException>() {
				@Override
				public IllegalArgumentException get() {
					
					return new IllegalArgumentException("해당 유저는 없습니다.  id: " + id);
				}
			});
			
			있다면 값 반환, 없다면 에러 처리를 통해 메시지 출력.
		 */
		
		User user = userRepository.findById(id).orElseThrow(new Supplier<IllegalArgumentException>() {
			@Override
			public IllegalArgumentException get() {
				return new IllegalArgumentException("해당 유저는 없습니다.  id: " + id);
			}
		});
		
		// user 객체를 웹 브라우저는 이해할 수 없음.
		// 때문에 스프링부트의 Message Converter가 json 라이브러리 호출해 자동으로 json으로 변환후 전달
		return user;
		/*
		 	람다식
		 	
		 	User user = userRepository.findById(id).orElseThrow(()->{
		 		return new IllegalArgumentException("해당 사용자는 없습니다.");
		 	});
		 */
	}
	
	@GetMapping("/dummy/user")
	public List<User> list(){
		return userRepository.findAll();
	}
	
	// 한 페이지 당 2건의 데이터를 리턴하는 메서드
	// dummy/user/page/page?page=0  <-- 식으로 웹 브라우저에서 다음 페이지로 접근가능
	@GetMapping("dummy/user/page")
	public Page<User> pageList(@PageableDefault(size=2, sort="id", direction = Sort.Direction.DESC) Pageable pageable) {
		Page<User> users = userRepository.findAll(pageable);
		return users;
	}
}
