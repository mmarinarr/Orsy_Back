package org.tfg.orsy.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;
import org.tfg.orsy.model.*;
import org.tfg.orsy.repository.*;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/comandas")
@CrossOrigin
public class ComandaController {

    private final ComandaRepository comandaRepo;
    private final MesaRepository mesaRepo;
    private final ProductoRepository productoRepo;

    public ComandaController(ComandaRepository comandaRepo,
                             MesaRepository mesaRepo,
                             ProductoRepository productoRepo) {
        this.comandaRepo = comandaRepo;
        this.mesaRepo = mesaRepo;
        this.productoRepo = productoRepo;
    }

    // =========================
    // CREAR COMANDA (CORREGIDO)
    // =========================
    @PostMapping
    @PreAuthorize("hasAnyRole('ADMIN', 'EMPLEADO')")
    public ResponseEntity<Comanda> crear(@RequestBody ComandaDTO dto) {

        // 1. Buscar mesa
        Mesa mesa = mesaRepo.findById(dto.mesaId())
                .orElseThrow(() -> new RuntimeException("Mesa no encontrada"));

        // 2. Crear comanda
        Comanda comanda = new Comanda();
        comanda.setMesa(mesa);
        comanda.setEstado(dto.estado() != null ? dto.estado() : EstadoComanda.ABIERTA);
        comanda.setFecha(LocalDateTime.now());

        // 3. Crear líneas
        List<LineaComanda> lineas = new ArrayList<>();

        for (LineaDTO l : dto.lineas()) {

            Producto producto = productoRepo.findById(l.productoId())
                    .orElseThrow(() -> new RuntimeException("Producto no encontrado"));

            LineaComanda linea = new LineaComanda();
            linea.setProducto(producto);
            linea.setNombre(producto.getNombre());
            linea.setPrecio(producto.getPrecio());
            linea.setCategoria(producto.getCategoria() != null ? producto.getCategoria().getNombre() : null);
            linea.setCantidad(l.cantidad());
            linea.setComanda(comanda); // 🔥 CLAVE (evita el 500)

            lineas.add(linea);
        }

        comanda.setLineas(lineas);

        // 4. Guardar todo en cascada
        return ResponseEntity.ok(comandaRepo.save(comanda));
    }

    // =========================
    // COMANDA ACTIVA POR MESA
    // =========================
    @GetMapping("/mesa/{mesaId}")
    @PreAuthorize("hasAnyRole('ADMIN', 'EMPLEADO')")
    public ResponseEntity<Comanda> getActiva(@PathVariable Long mesaId) {

        return comandaRepo.findFirstByMesaIdAndEstado(mesaId, EstadoComanda.ABIERTA)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.ok(null));
    }

    // =========================
    // TODAS LAS COMANDAS
    // =========================
    @GetMapping
    @PreAuthorize("hasAnyRole('ADMIN', 'EMPLEADO')")
    public List<Comanda> getAll() {
        return comandaRepo.findAll();
    }

    // =========================
    // ACTUALIZAR COMANDA
    // =========================
    @PutMapping("/{id}")
    @PreAuthorize("hasAnyRole('ADMIN', 'EMPLEADO')")
    public ResponseEntity<Comanda> actualizar(@PathVariable Long id,
                                              @RequestBody ComandaDTO dto) {

        Comanda comanda = comandaRepo.findById(id)
                .orElseThrow(() -> new RuntimeException("Comanda no encontrada"));

        if (dto.estado() != null) {
            comanda.setEstado(dto.estado());
        }

        return ResponseEntity.ok(comandaRepo.save(comanda));
    }

    // =========================
    // BORRAR
    // =========================
    @DeleteMapping("/{id}")
    @PreAuthorize("hasRole('ADMIN')")
    public void borrar(@PathVariable Long id) {
        comandaRepo.deleteById(id);
    }
}
