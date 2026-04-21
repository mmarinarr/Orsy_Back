package org.tfg.orsy.controller;

import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.*;
import org.tfg.orsy.dto.AuthResponse;
import org.tfg.orsy.dto.LoginRequest;
import org.tfg.orsy.model.Usuario;
import org.tfg.orsy.repository.UsuarioRepository;
import org.tfg.orsy.service.UsuarioService;

@RestController
@RequestMapping("/auth")
@CrossOrigin
public class AuthController {

    private final AuthenticationManager authenticationManager;
    private final UsuarioRepository usuarioRepository;
    private final UsuarioService usuarioService;

    public AuthController(AuthenticationManager authenticationManager,
                          UsuarioRepository usuarioRepository,
                          UsuarioService usuarioService) {
        this.authenticationManager = authenticationManager;
        this.usuarioRepository = usuarioRepository;
        this.usuarioService = usuarioService;
    }

    @PostMapping("/login")
    public AuthResponse login(@RequestBody LoginRequest request) {
        String email = usuarioService.normalizarEmail(request.email());

        Authentication authentication = authenticationManager.authenticate(
                new UsernamePasswordAuthenticationToken(email, request.password())
        );

        Usuario usuario = usuarioRepository.findByEmail(authentication.getName())
                .orElseThrow(() -> new RuntimeException("Usuario no encontrado"));

        return new AuthResponse(
                usuario.getId(),
                usuario.getNombre(),
                usuario.getEmail(),
                usuario.getRol()
        );
    }

    @PostMapping("/pin-login")
    public AuthResponse loginConPin(@RequestBody LoginRequest request) {
        Usuario usuario = usuarioService.buscarPorPin(request.password());

        return new AuthResponse(
                usuario.getId(),
                usuario.getNombre(),
                usuario.getEmail(),
                usuario.getRol()
        );
    }
}
