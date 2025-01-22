package br.com.demagistro.demagistro.service;

import br.com.demagistro.demagistro.entity.Livro;
import br.com.demagistro.demagistro.repository.LivroRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class LivroService {
    @Autowired
    private LivroRepository livroRepository;

    public List<Livro> getAllLivros(){

        return livroRepository.findAll();
    }

    public Livro getBookByTitulo(String titulo) {
        return livroRepository.findByTitulo(titulo);
    }

    public Livro addLivro(Livro livro) {
        return livroRepository.save(livro);
    }

    public Livro updateLivro(Livro livro) {
        return livroRepository.save(livro);
    }

    public void deleteBook(Integer id) {
        livroRepository.deleteById(id);
    }
}
