package br.com.demagistro.demagistro.service;


import br.com.demagistro.demagistro.entity.Autor;
import br.com.demagistro.demagistro.repository.AutorRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class AutorService {
    @Autowired
    private AutorRepository autorRepository;
    public Autor getAutorByNome(String nome){
        return autorRepository.findByNome(nome);
    }
    public Autor AddAutor(Autor autor){
        return autorRepository.save(autor);
    }
    public Autor UpdateAutor(Autor autor){
        return autorRepository.save(autor);
    }
    public void DeleteAutor(Integer id){
        autorRepository.deleteById(id);
    }
}
