package com.oldhammer.fantasylistbuilder.entities;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.util.List;

@Entity
@Setter
@Getter
@NoArgsConstructor
@AllArgsConstructor
@Table(name = "equipments")
public class EquipmentEntity {


    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "equipment_id", unique = true, nullable = false)
    Long id;

    @Column(name = "name", unique = true, nullable = false)
    String name;

    @Column(name = "type", unique = true, nullable = false)
    String type;

    @Column(name = "effects", unique = true, nullable = false)
    String effects;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "book_id")
    AllBooksEntity book;

    @OneToMany(fetch = FetchType.LAZY)
    @JoinColumn(name = "rule_id")
    List<SpecialRuleEntity> specialRules;
}
