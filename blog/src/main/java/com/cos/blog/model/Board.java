// 20강

package com.cos.blog.model;

import java.sql.Timestamp;
import java.util.List;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.Lob;
import javax.persistence.ManyToOne;
import javax.persistence.OneToMany;

import org.hibernate.annotations.ColumnDefault;
import org.hibernate.annotations.CreationTimestamp;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

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
 	
 	전자는 항상 클래스,  후자는 항상 연관관계를 맺는 필드를 뜻함.
 	
 	DB는 오브젝트 타입을 저장할 수 없기 때문에 FK (Foreign Key, 외래키)를 사용한다
 	자바는 오브젝트를 저장할 수 있다. 이러한 차이점으로부터 충돌이 발생한다.
 	때문에 자바에서 데이터베이스의 자료형에 맞춰서 테이블을 생성하게 된다.
 	
 	Reply는 @JoinColumn이 필요 없다.
 	하나의 게시글에 여러 개의 댓글이 달릴 경우, FK가 존재하면
 	FK는 여러 개가 된다. 이는 1정규화가 위배된 것으로, @JoinColumn이 필요없는 이유가 된다.
 	
 	단, @OneToMany 뒤 (mappedBy = "board")가 붙어야 한다.  (인자값은 필드값을 적어야 한다.)
 	mappedBy는 연관관계의 주인이 아님을 나타낸다. (FK가 아니라는 뜻)
 	따라서 DB에 컬럼을 만들지 말라는 의미가 되며, 인자값으로 입력된 Reply.board가 FK가 된다.
 	단지 join을 통해 값을 얻기 위함을 뜻하기도 한다.
 	
 	@ManyToOne은 join을 통해 들고올게 하나밖에 없다는 뜻이다. 
 	때문에 기본 fetch 전략은 EAGER이다. 무조건 하나 join해 오라는 뜻이다.
 	
 	@OneToMany는 무작정 join을 수행하면 데이터가 1개가 될 수도, 1만개 될 수도 있다.
 	때문에 필요에 따라 join할지 말지를 정하기 때문에 기본 fetch 전략은 LAZY다. 
 	여기선 UI가 무조건 댓글이 보이는 구조이기 때문에 fetch를 EAGER로 설정한다.
 */

@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
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
	
	@OneToMany(mappedBy = "board",  fetch = FetchType.EAGER)
	private List<Reply> reply;
	
	@CreationTimestamp
	private Timestamp createDate;
}
