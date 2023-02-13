package com.remake.friends.model;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.hibernate.annotations.ColumnDefault;
import org.hibernate.annotations.CreationTimestamp;

import javax.persistence.*;
import java.sql.Timestamp;
import java.util.List;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
@Entity
public class Board {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @ManyToOne
    @JoinColumn(name = "userId")
    private User user;

    @Column(nullable = false, length = 50)
    private String title;

    @Lob
    private String Content;

    @ColumnDefault("0")
    private int count;

    @Column(nullable = false, length = 4)
    private String category;

    @OneToMany(mappedBy = "board")
    private List<Reply> replys;

    @CreationTimestamp
    private Timestamp createDate;
}
