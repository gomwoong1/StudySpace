// 20강

package com.cos.blog.model;

import java.sql.Timestamp;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.Lob;
import javax.persistence.ManyToOne;

import org.hibernate.annotations.ColumnDefault;
import org.hibernate.annotations.CreationTimestamp;

/*
 	NOTE
 	
 	@Lob
 	대용량 데이터를 처리하는데 사용함
 	
 	@JoinColumn(name="userId")
 	필드 생성시 userId라는 이름으로 생성되도록 지정함
 	
 	@ManyToOne
 	연관관계를 지정하는 어노테이션.
 	Many = Board 클래스,  One = user 필드
 	한 명의 유저는 여러 개의 게시글을 쓸 수 있다.  /  여러 개의 게시글은 한 명의 유저에게 쓰일 수 있다.
 	
 	DB는 오브젝트 타입을 저장할 수 없기 때문에 FK (Foreign Key, 외래키)를 사용한다
 	자바는 오브젝트를 저장할 수 있다. 이러한 차이점으로부터 충돌이 발생한다.
 	때문에 자바에서 데이터베이스의 자료형에 맞춰서 테이블을 생성하게 된다.
 	
 */

@Entity
public class Board {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int id;
	
	@Column(nullable = false, length = 100)
	private String title;
	
	@Lob
	private String content;
	
	@ColumnDefault("0")
	private int count;
	
	@ManyToOne
	@JoinColumn(name="userId")
	private User user;
	
	@CreationTimestamp
	private Timestamp creatDate;
}
