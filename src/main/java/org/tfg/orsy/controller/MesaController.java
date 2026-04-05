package org.tfg.orsy.controller;

import org.tfg.orsy.model.Mesa;
import org.tfg.orsy.repository.MesaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/mesas")
@CrossOrigin
public class MesaController {

    @Autowired
    private MesaRepository repo;

    @GetMapping
    public List<Mesa> getAll() {
        return repo.findAll();
    }

    @PostMapping
    public Mesa crear(@RequestBody Mesa m) {
        return repo.save(m);
    }

    @PutMapping("/{id}")
    public Mesa actualizar(@PathVariable Long id, @RequestBody Mesa m) {
        Mesa existente = repo.findById(id).orElse(null);

        if (existente != null) {
            existente.setNumero(m.getNumero());
            existente.setCapacidad(m.getCapacidad());
            existente.setX(m.getX());
            existente.setY(m.getY());
            existente.setEstado(m.getEstado());
            return repo.save(existente);
        }

        return null;
    }

    @DeleteMapping("/{id}")
    public void borrar(@PathVariable Long id) {
        repo.deleteById(id);
    }
}
