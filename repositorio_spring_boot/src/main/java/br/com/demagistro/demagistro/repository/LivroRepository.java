package br.com.demagistro.demagistro.repository;

import br.com.demagistro.demagistro.entity.Livro;
import org.springframework.data.jpa.repository.JpaRepository;

public interface LivroRepository extends JpaRepository<Livro, Integer> {
    public Livro findByTitulo(String titulo);
}
