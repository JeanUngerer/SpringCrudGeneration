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
@Table(name = "specialRules")
public class SpecialRuleEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "rule_id", unique = true, nullable = false)
    Long id;

    @Column(name = "name", unique = true, nullable = false)
    String name;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "book_id")
    AllBooksEntity book;

    @Column(name = "phaseOfApplication", unique = true, nullable = false)
    String phaseOfApplication;

    @Column(name = "ruleText", unique = true, nullable = false)
    String ruleText;
}
