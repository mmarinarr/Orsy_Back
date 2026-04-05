package org.tfg.orsy.controller;

import org.tfg.orsy.model.Comanda;
import org.tfg.orsy.repository.ComandaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/comandas")
@CrossOrigin
public class ComandaController {

    @Autowired
    private ComandaRepository repo;

    @GetMapping
    public List<Comanda> getAll() {
        return repo.findAll();
    }

    @GetMapping("/abiertas")
    public List<Comanda> getAbiertas() {
        return repo.findByEstado("ABIERTA");
    }

    @GetMapping("/mesa/{mesaId}")
    public List<Comanda> getByMesa(@PathVariable Long mesaId) {
        return repo.findByMesaIdAndEstado(mesaId, "ABIERTA");
    }

    @PostMapping
    public Comanda crear(@RequestBody Comanda c) {
        return repo.save(c);
    }

    @PutMapping("/{id}")
    public Comanda actualizar(@PathVariable Long id, @RequestBody Comanda c) {
        Comanda existente = repo.findById(id).orElse(null);
        if (existente != null) {
            existente.setEstado(c.getEstado());
            existente.setMesa(c.getMesa());
            existente.setProductos(c.getProductos());
            return repo.save(existente);
        }
        return null;
    }

    @DeleteMapping("/{id}")
    public void borrar(@PathVariable Long id) {
        repo.deleteById(id);
    }
}