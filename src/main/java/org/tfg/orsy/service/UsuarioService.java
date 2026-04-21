package org.tfg.orsy.service;

import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.tfg.orsy.model.RolUsuario;
import org.tfg.orsy.model.Usuario;
import org.tfg.orsy.repository.UsuarioRepository;

import java.util.List;

@Service
public class UsuarioService {

    private final UsuarioRepository usuarioRepository;
    private final PasswordEncoder passwordEncoder;

    public UsuarioService(UsuarioRepository usuarioRepository, PasswordEncoder passwordEncoder) {
        this.usuarioRepository = usuarioRepository;
        this.passwordEncoder = passwordEncoder;
    }

    public List<Usuario> listar() {
        return usuarioRepository.findAll();
    }

    public Usuario crear(Usuario usuario) {
        usuario.setEmail(normalizarEmail(usuario.getEmail()));
        String pin = validarPin(usuario.getPassword());
        validarPinUnico(pin, null);
        usuario.setPassword(passwordEncoder.encode(pin));
        if (usuario.getRol() == null) {
            usuario.setRol(RolUsuario.EMPLEADO);
        }
        return usuarioRepository.save(usuario);
    }

    public Usuario actualizar(Long id, Usuario usuarioActualizado) {
        Usuario existente = usuarioRepository.findById(id).orElse(null);
        if (existente == null) {
            return null;
        }

        existente.setNombre(usuarioActualizado.getNombre());
        existente.setEmail(normalizarEmail(usuarioActualizado.getEmail()));
        if (usuarioActualizado.getPassword() != null && !usuarioActualizado.getPassword().isBlank()) {
            String pin = validarPin(usuarioActualizado.getPassword());
            validarPinUnico(pin, existente.getId());
            existente.setPassword(passwordEncoder.encode(pin));
        }
        if (usuarioActualizado.getRol() != null) {
            existente.setRol(usuarioActualizado.getRol());
        }

        return usuarioRepository.save(existente);
    }

    public void borrar(Long id) {
        usuarioRepository.deleteById(id);
    }

    public String normalizarEmail(String email) {
        return email == null ? null : email.trim().toLowerCase();
    }

    public String validarPin(String pin) {
        if (pin == null || !pin.trim().matches("\\d{4}")) {
            throw new IllegalArgumentException("El PIN debe tener 4 dígitos");
        }
        return pin.trim();
    }

    public void validarPinUnico(String pin, Long usuarioIdActual) {
        boolean enUso = usuarioRepository.findAll().stream()
                .anyMatch(usuario ->
                        usuario.getPassword() != null &&
                        passwordEncoder.matches(pin, usuario.getPassword()) &&
                        (usuarioIdActual == null || !usuario.getId().equals(usuarioIdActual)));

        if (enUso) {
            throw new IllegalArgumentException("Ese PIN ya está en uso");
        }
    }

    public Usuario buscarPorPin(String pin) {
        String pinNormalizado = validarPin(pin);

        return usuarioRepository.findAll().stream()
                .filter(usuario -> usuario.getPassword() != null && passwordEncoder.matches(pinNormalizado, usuario.getPassword()))
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("PIN incorrecto"));
    }
}
