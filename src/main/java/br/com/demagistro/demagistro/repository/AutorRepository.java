package br.com.demagistro.demagistro.repository;

import br.com.demagistro.demagistro.entity.Autor;
import org.springframework.data.jpa.repository.JpaRepository;

public interface AutorRepository extends JpaRepository<Autor, Integer> {
    public Autor findByNome(String nome);
}
