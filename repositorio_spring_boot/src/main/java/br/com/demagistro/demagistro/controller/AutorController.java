package br.com.demagistro.demagistro.controller;

import br.com.demagistro.demagistro.entity.Autor;
import br.com.demagistro.demagistro.service.AutorService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/Autor/V1")
public class AutorController {

    private final AutorService autorService;
    @Autowired
    public AutorController(AutorService autorService) {
        this.autorService = autorService;
    }

    @PostMapping("/AddAutor")
    public ResponseEntity<Autor> addAutor(Autor autor){
        Autor autorSalvo = autorService.AddAutor(autor);
        return ResponseEntity.ok(autorSalvo);

    }

    @GetMapping("/GetAutor/{AutorName}")
    public ResponseEntity<Autor> getAutor(@PathVariable String autorNome){
        final Autor autorByName = autorService.getAutorByNome(autorNome);
        if(autorByName == null){
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(autorByName);
    }

    @PutMapping("/updateAutor")
    public ResponseEntity<Autor> updateAutor(Autor autor){
        Autor autorSalvo = autorService.UpdateAutor(autor);
        return ResponseEntity.ok(autorSalvo);
    }

    @DeleteMapping("/deleteAutor/{id}")
    public ResponseEntity<Autor> deleteAutor(@PathVariable("id") Integer id){
        autorService.DeleteAutor(id);
        return ResponseEntity.ok().build();
    }
}
