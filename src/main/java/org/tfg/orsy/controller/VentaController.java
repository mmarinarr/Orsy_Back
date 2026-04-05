package org.tfg.orsy.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.tfg.orsy.model.Venta;
import org.tfg.orsy.repository.VentaRepository;

import java.util.List;

@RestController
@RequestMapping("/ventas")
@CrossOrigin
public class VentaController {

    @Autowired
    private VentaRepository repo;

    // GET /ventas → devuelve todas las ventas con lineas
    @GetMapping
    public List<Venta> getAll() {
        return repo.findAll();
    }

    // POST /ventas → crear nueva venta (opcional si quieres registrar al pagar comanda)
    @PostMapping
    public Venta crear(@RequestBody Venta venta) {
        return repo.save(venta);
    }
}
