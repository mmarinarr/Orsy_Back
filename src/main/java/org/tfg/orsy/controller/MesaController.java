package org.tfg.orsy.controller;

import org.tfg.orsy.model.Mesa;
import org.tfg.orsy.model.MesaEstadoDTO;
import org.tfg.orsy.repository.MesaRepository;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/mesas")
@CrossOrigin
public class MesaController {

    private final MesaRepository repo;

    public MesaController(MesaRepository repo) {
        this.repo = repo;
    }

    @GetMapping
    @PreAuthorize("hasAnyRole('ADMIN', 'EMPLEADO')")
    public List<Mesa> getAll() {
        return repo.findAll();
    }

    @GetMapping("/{id}")
    @PreAuthorize("hasAnyRole('ADMIN', 'EMPLEADO')")
    public ResponseEntity<Mesa> getById(@PathVariable Long id) {
        return repo.findById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    @PreAuthorize("hasRole('ADMIN')")
    public Mesa crear(@RequestBody Mesa m) {
        return repo.save(m);
    }

    @PutMapping("/{id}")
    @PreAuthorize("hasRole('ADMIN')")
    public ResponseEntity<Mesa> actualizar(@PathVariable Long id, @RequestBody Mesa m) {

        return repo.findById(id).map(existente -> {

            existente.setNumero(m.getNumero());
            existente.setCapacidad(m.getCapacidad());
            existente.setX(m.getX());
            existente.setY(m.getY());
            existente.setEstado(m.getEstado());

            return ResponseEntity.ok(repo.save(existente));

        }).orElse(ResponseEntity.notFound().build());
    }

    @PutMapping("/{id}/estado")
    @PreAuthorize("hasAnyRole('ADMIN', 'EMPLEADO')")
    public ResponseEntity<Mesa> cambiarEstado(@PathVariable Long id, @RequestBody MesaEstadoDTO dto) {

        return repo.findById(id).map(mesa -> {

            mesa.setEstado(dto.estado());

            return ResponseEntity.ok(repo.save(mesa));

        }).orElse(ResponseEntity.notFound().build());
    }

    @DeleteMapping("/{id}")
    @PreAuthorize("hasRole('ADMIN')")
    public ResponseEntity<Void> borrar(@PathVariable Long id) {

        if (!repo.existsById(id)) {
            return ResponseEntity.notFound().build();
        }

        repo.deleteById(id);
        return ResponseEntity.noContent().build();
    }
}
