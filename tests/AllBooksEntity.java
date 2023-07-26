package com.oldhammer.fantasylistbuilder.entities;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Setter
@Getter
@NoArgsConstructor
@AllArgsConstructor
@Table(name = "allbooks")
public class AllBooksEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "book_id", unique = true, nullable = false)
    Long id;

    @Column(name = "name", unique = true, nullable = false)
    String name;

    @Column(name = "version", unique = true, nullable = false)
    String version;

    @Column(name = "linkPath", unique = true, nullable = false)
    String linkPath;
}
