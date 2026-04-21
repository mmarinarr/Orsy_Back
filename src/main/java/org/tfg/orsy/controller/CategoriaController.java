package org.tfg.orsy.controller;

import org.springframework.security.access.prepost.PreAuthorize;
import org.tfg.orsy.model.Categoria;
import org.tfg.orsy.repository.CategoriaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/categorias")
@CrossOrigin
public class CategoriaController {

    @Autowired
    private CategoriaRepository repo;

    @GetMapping
    @PreAuthorize("hasAnyRole('ADMIN', 'EMPLEADO')")
    public List<Categoria> obtenerTodas() {
        return repo.findAll();
    }

    @PostMapping
    @PreAuthorize("hasRole('ADMIN')")
    public Categoria crear(@RequestBody Categoria categoria) {
        return repo.save(categoria);
    }

    @PutMapping("/{id}")
    @PreAuthorize("hasRole('ADMIN')")
    public Categoria actualizar(@PathVariable Long id, @RequestBody Categoria c) {
        Categoria existente = repo.findById(id).orElse(null);

        if (existente != null) {
            existente.setNombre(c.getNombre());
            return repo.save(existente);
        }

        return null;
    }

    @DeleteMapping("/{id}")
    @PreAuthorize("hasRole('ADMIN')")
    public void borrar(@PathVariable Long id) {
        repo.deleteById(id);
    }
}
