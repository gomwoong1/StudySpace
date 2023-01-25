// 24강 - insert 테스트 인터페이스
package com.cos.blog.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.cos.blog.model.User;


/*
 	MEMO
 	
 	DAO 역할을 수행할 수 있다.
 	또한 @Repositori 어노테이션 없이도 Bean에 자동으로 등록이 된다. 따라서 생략 가능하다.
 	
 	이제 하위 인터페이스는 자동으로 메모리에 뜬다.
 */
public interface UserRepository extends JpaRepository<User, Integer>{

}
