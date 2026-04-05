package org.tfg.orsy.controller;

import org.tfg.orsy.model.Producto;
import org.tfg.orsy.repository.ProductoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/productos")
@CrossOrigin
public class ProductoController {

    @Autowired
    private ProductoRepository repo;

    @GetMapping
    public List<Producto> obtenerTodos() {
        return repo.findAll();
    }

    @PostMapping
    public Producto crear(@RequestBody Producto producto) {
        return repo.save(producto);
    }

    @PutMapping("/{id}")
    public Producto actualizar(@PathVariable Long id, @RequestBody Producto p) {
        Producto existente = repo.findById(id).orElse(null);

        if (existente != null) {
            existente.setNombre(p.getNombre());
            existente.setPrecio(p.getPrecio());
            return repo.save(existente);
        }

        return null;
    }

    @DeleteMapping("/{id}")
    public void borrar(@PathVariable Long id) {
        repo.deleteById(id);
    }
}


