package org.tfg.orsy.controller;

import org.tfg.orsy.model.Usuario;
import org.tfg.orsy.repository.UsuarioRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/usuarios")
@CrossOrigin
public class UsuarioController {

    @Autowired
    private UsuarioRepository repo;

    @GetMapping
    public List<Usuario> getAll() {
        return repo.findAll();
    }

    @PostMapping
    public Usuario crear(@RequestBody Usuario u) {
        return repo.save(u);
    }

    @PutMapping("/{id}")
    public Usuario actualizar(@PathVariable Long id, @RequestBody Usuario u) {
        Usuario existente = repo.findById(id).orElse(null);

        if (existente != null) {
            existente.setNombre(u.getNombre());
            existente.setEmail(u.getEmail());
            existente.setPassword(u.getPassword());
            existente.setRol(u.getRol());
            return repo.save(existente);
        }

        return null;
    }

    @DeleteMapping("/{id}")
    public void borrar(@PathVariable Long id) {
        repo.deleteById(id);
    }
}
