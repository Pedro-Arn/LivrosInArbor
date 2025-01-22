package br.com.demagistro.demagistro.repository;

import br.com.demagistro.demagistro.entity.Disciplina;
import org.springframework.data.jpa.repository.JpaRepository;

public interface DisciplinaRepository extends JpaRepository<Disciplina, Integer> {
    public Disciplina findByNome(String nome);
}
