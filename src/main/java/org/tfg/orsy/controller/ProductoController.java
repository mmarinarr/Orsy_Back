package org.tfg.orsy.controller;

import org.springframework.security.access.prepost.PreAuthorize;
import org.tfg.orsy.model.Categoria;
import org.tfg.orsy.model.Producto;
import org.tfg.orsy.model.ProductoDTO;
import org.tfg.orsy.repository.CategoriaRepository;
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
    @PreAuthorize("hasAnyRole('ADMIN', 'EMPLEADO')")
    public List<ProductoDTO> obtenerTodos() {
        return repo.findAll().stream()
                .map(p -> new ProductoDTO(
                        p.getId(),
                        p.getNombre(),
                        p.getPrecio(),
                        p.getCategoria() != null ? p.getCategoria().getId() : null,
                        p.getCategoria() != null ? p.getCategoria().getNombre() : null
                ))
                .toList();
    }

    @Autowired
    private CategoriaRepository categoriaRepo;

    @PostMapping
    @PreAuthorize("hasRole('ADMIN')")
    public Producto crear(@RequestBody Producto p) {

        Long catId = p.getCategoria().getId();

        Categoria categoria = categoriaRepo.findById(catId)
                .orElseThrow(() -> new RuntimeException("Categoría no encontrada"));

        p.setCategoria(categoria);

        return repo.save(p);
    }

    @PutMapping("/{id}")
    @PreAuthorize("hasRole('ADMIN')")
    public Producto actualizar(@PathVariable Long id, @RequestBody Producto p) {

        Producto existente = repo.findById(id)
                .orElseThrow(() -> new RuntimeException("Producto no encontrado"));

        Categoria categoria = categoriaRepo.findById(p.getCategoria().getId())
                .orElseThrow(() -> new RuntimeException("Categoría no encontrada"));

        existente.setNombre(p.getNombre());
        existente.setPrecio(p.getPrecio());
        existente.setCategoria(categoria);

        return repo.save(existente);
    }

    @DeleteMapping("/{id}")
    @PreAuthorize("hasRole('ADMIN')")
    public void borrar(@PathVariable Long id) {
        repo.deleteById(id);
    }
}

