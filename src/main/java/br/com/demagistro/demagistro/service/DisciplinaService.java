package br.com.demagistro.demagistro.service;

import br.com.demagistro.demagistro.entity.Disciplina;
import br.com.demagistro.demagistro.repository.DisciplinaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class DisciplinaService {
    @Autowired
    private DisciplinaRepository disciplinaRepository;

    public List<Disciplina> getAllDisciplinas() {
        return disciplinaRepository.findAll();
    }
    public Disciplina getDisciplinaByNome(String nome) {
        return disciplinaRepository.findByNome(nome);
    }
    public Disciplina addDisciplina(Disciplina disciplina) {
        return disciplinaRepository.save(disciplina);
    }
    public Disciplina updateDisciplina(Disciplina disciplina) {
        return disciplinaRepository.save(disciplina);
    }
    public void deleteDisciplina(Integer id) {
        disciplinaRepository.deleteById(id);
    }
}
