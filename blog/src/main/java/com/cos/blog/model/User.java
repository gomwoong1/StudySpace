// 18강

package com.cos.blog.model;

import java.sql.Timestamp;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

import org.hibernate.annotations.ColumnDefault;
import org.hibernate.annotations.CreationTimestamp;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

/*
 	ORM: Object -> table로 매핑해주는 기술.
 
 	@Entiy
	프로젝트 실행시, User 클래스가 MySQL에 테이블이 자동 생성됨.
	
	@Id
	PK (Primary Key, 기본키) 지정 어노테이션
	
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	오토 인크리먼트 넘버링 전략을 해당 프로젝에 연결된 DB의 연결된 전략을 따라간다는 것.
	오라클 사용 -> 시퀀스, MySQL 사용 -> 오토 인크리먼트 따라 간다는 의미
	오토 인크리먼트 설정도 겸하는 듯?
	
	@Column(nullable = false, length=n)
	널값 허용하지 않고, 길이는 n까지만.
	
	@ColumnDefault("'user'")
	문자인 경우 쌍따옴표 내부에 따옴표를 삽입해야 함.
	문자가 아니라면 따옴표 필요 없음.
	디폴트값을 설정
	
	@CreationTimestamp
	현재 시스템시간 자동 insert
 */

@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
@Entity
public class User {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int id;  // 오토 인크리먼트 적용
	
	@Column(nullable = false, length= 30)
	private String username;
	
	@Column(nullable = false, length=100)
	private String password;
	
	@Column(nullable = false, length= 50)
	private String email;
	
	//enum을 쓰는게 좋음. enum은 도메인 설정이 가능하기 때문. (범위지정, 즉 오타낼 수 없음)
	@ColumnDefault("'user'")
	private String role;  
	
	@CreationTimestamp
	private Timestamp createDate;
}
