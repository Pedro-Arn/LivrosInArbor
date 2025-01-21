package br.com.demagistro.demagistro.controller;

import br.com.demagistro.demagistro.entity.Livro;
import br.com.demagistro.demagistro.service.LivroService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/Book/v1")
public class LivroController {

    private final LivroService livroService;
    @Autowired
    public LivroController(LivroService livroService) {
        this.livroService = livroService;
    }

    @GetMapping
    public ResponseEntity<List<Livro>> listBooks(){
        List<Livro> livro = livroService.getAllLivros();
        return ResponseEntity.ok(livro);
    }
    @PostMapping("/addbook")
    public ResponseEntity<Livro> addLivro(Livro livro) {
        Livro livroSalvo = livroService.addLivro(livro);
        return ResponseEntity.ok(livroSalvo);
    }
    @GetMapping("/getBook/{Booktitulo}")
    public ResponseEntity<Livro> getLivroByTitulo(@PathVariable("Booktitulo") String titulo) {
        final Livro livroByTitulo = livroService.getBookByTitulo(titulo);
        if(livroByTitulo == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(livroByTitulo);
    }
    @PutMapping("/updatebook")
    public ResponseEntity<Livro> updateLivro(Livro livro) {
        Livro livroSalvo = livroService.updateLivro(livro);
        return ResponseEntity.ok(livroSalvo);
    }
    @DeleteMapping("/deleteBook/{id}")
    public ResponseEntity<Livro> deleteBook(@PathVariable("id") Integer id) {
        livroService.deleteBook(id);
        return ResponseEntity.ok().build();
    }
}
