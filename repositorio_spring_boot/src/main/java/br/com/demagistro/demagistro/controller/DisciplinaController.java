package br.com.demagistro.demagistro.controller;

import br.com.demagistro.demagistro.entity.Disciplina;
import br.com.demagistro.demagistro.service.DisciplinaService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/Disciplina/v1")
public class DisciplinaController {
    private final DisciplinaService disciplinaService;
    @Autowired
    public DisciplinaController(DisciplinaService disciplinaService) {
        this.disciplinaService = disciplinaService;
    }
    @GetMapping
    public ResponseEntity<List<Disciplina>> listDisciplinas() {
        List<Disciplina> disciplinas = disciplinaService.getAllDisciplinas();
        return ResponseEntity.ok(disciplinas);
    }
    @PostMapping("/Add disciplina")
    public ResponseEntity<Disciplina> addDisciplina(Disciplina disciplina) {

        Disciplina disciplinaSalva = disciplinaService.addDisciplina(disciplina);
        return ResponseEntity.ok(disciplinaSalva);
    }

    @GetMapping("/getDisciplina/{DisciplinaName}")
    public ResponseEntity<Disciplina> getDisciplina(@PathVariable String disciplinaNome) {
        final Disciplina disciplinaByName = disciplinaService.getDisciplinaByNome(disciplinaNome);
        if (disciplinaByName == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(disciplinaByName);
    }

    @PutMapping("/updateDisciplina")
    public ResponseEntity<Disciplina> updateDisciplina(Disciplina disciplina) {
        Disciplina disciplinaSalva = disciplinaService.updateDisciplina(disciplina);
        return ResponseEntity.ok(disciplinaSalva);
    }

    @DeleteMapping("/DeleteDisciplina/{id}")
    public ResponseEntity<Disciplina> deleteDisciplina(@PathVariable("id") Integer id) {
        disciplinaService.deleteDisciplina(id);
        return ResponseEntity.ok().build();
    }
}
