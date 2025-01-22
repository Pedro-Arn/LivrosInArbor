package br.com.demagistro.demagistro.entity;

import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.ArrayList;
import java.util.List;

@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
public class Autor {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    private String nome;
    private int anoDeNascimento;
    private String sexo;

    @ManyToMany(mappedBy = "autores")
    @JsonIgnore
    private List<Livro> livros = new ArrayList<>();
}
