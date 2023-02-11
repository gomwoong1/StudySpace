package com.remake.friends.model;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.hibernate.annotations.CreationTimestamp;

import javax.persistence.*;
import java.sql.Timestamp;

@Builder
@NoArgsConstructor
@AllArgsConstructor
@Data
@Entity
public class User {
    // 어노테이션 공부중
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(nullable = false, unique = true, length = 20)
    private String username;

    @Column(nullable = false, length = 100)
    private String password;

    @Column(nullable = false, length = 50)
    private String email;

    @Column(nullable = false, length = 2)
    private String sex;

    @Enumerated(EnumType.STRING)
    private RoleType role;

    @Column(nullable = false, length = 13)
    private String phone;

    @CreationTimestamp
    private Timestamp createDate;

//    @OneToMany(mappedBy = "board", fetch = FetchType.EAGER)
//    private Board board;
//
//    @OneToMany(mappedBy = "reply", fetch = FetchType.EAGER)
//    private Reply reply;
}
