package org.tfg.orsy.controller;

import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;
import org.tfg.orsy.model.Venta;
import org.tfg.orsy.repository.VentaRepository;

import java.util.List;

@RestController
@RequestMapping("/ventas")
@CrossOrigin
public class VentaController {

    private final VentaRepository repo;

    public VentaController(VentaRepository repo) {
        this.repo = repo;
    }

    @GetMapping
    @PreAuthorize("hasRole('ADMIN')")
    public List<Venta> getAll() {
        return repo.findAll();
    }

    @PostMapping
    @PreAuthorize("hasAnyRole('ADMIN', 'EMPLEADO')")
    public Venta crear(@RequestBody Venta v) {
        return repo.save(v);
    }
}
