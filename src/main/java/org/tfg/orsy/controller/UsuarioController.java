package org.tfg.orsy.controller;

import org.springframework.security.access.prepost.PreAuthorize;
import org.tfg.orsy.model.Usuario;
import org.tfg.orsy.service.UsuarioService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/usuarios")
@CrossOrigin
public class UsuarioController {

    private final UsuarioService usuarioService;

    public UsuarioController(UsuarioService usuarioService) {
        this.usuarioService = usuarioService;
    }

    @GetMapping
    @PreAuthorize("hasRole('ADMIN')")
    public List<Usuario> getAll() {
        return usuarioService.listar();
    }

    @PostMapping
    @PreAuthorize("hasRole('ADMIN')")
    public Usuario crear(@RequestBody Usuario u) {
        return usuarioService.crear(u);
    }

    @PutMapping("/{id}")
    @PreAuthorize("hasRole('ADMIN')")
    public Usuario actualizar(@PathVariable Long id, @RequestBody Usuario u) {
        return usuarioService.actualizar(id, u);
    }

    @DeleteMapping("/{id}")
    @PreAuthorize("hasRole('ADMIN')")
    public void borrar(@PathVariable Long id) {
        usuarioService.borrar(id);
    }
}
