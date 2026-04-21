package org.tfg.orsy.config;

import org.springframework.boot.CommandLineRunner;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;
import org.tfg.orsy.model.RolUsuario;
import org.tfg.orsy.model.Usuario;
import org.tfg.orsy.repository.UsuarioRepository;

@Component
public class UsuarioInitializer implements CommandLineRunner {

    private final UsuarioRepository usuarioRepository;
    private final PasswordEncoder passwordEncoder;

    public UsuarioInitializer(UsuarioRepository usuarioRepository, PasswordEncoder passwordEncoder) {
        this.usuarioRepository = usuarioRepository;
        this.passwordEncoder = passwordEncoder;
    }

    @Override
    public void run(String... args) {
        migrarPasswordsAntiguas();
        crearAdminPorDefectoSiNoExiste();
    }

    private void migrarPasswordsAntiguas() {
        java.util.List<Usuario> usuariosActualizados = new java.util.ArrayList<>();

        for (Usuario usuario : usuarioRepository.findAll()) {
            if (usuario.getEmail() == null || usuario.getEmail().isBlank()) {
                continue;
            }

            boolean actualizado = false;
            String password = usuario.getPassword();
            if (password != null && !password.startsWith("$2")) {
                usuario.setPassword(passwordEncoder.encode(password));
                actualizado = true;
            }
            if (usuario.getRol() == null) {
                usuario.setRol(RolUsuario.EMPLEADO);
                actualizado = true;
            }
            if (actualizado) {
                usuariosActualizados.add(usuario);
            }
        }

        if (!usuariosActualizados.isEmpty()) {
            usuarioRepository.saveAll(usuariosActualizados);
        }
    }

    private void crearAdminPorDefectoSiNoExiste() {
        Usuario admin = usuarioRepository.findByEmail("admin@orsy.local")
                .orElseGet(Usuario::new);

        admin.setNombre("Administrador");
        admin.setEmail("admin@orsy.local");
        admin.setPassword(passwordEncoder.encode("4321"));
        admin.setRol(RolUsuario.ADMIN);
        usuarioRepository.save(admin);
    }
}
