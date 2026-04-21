package org.tfg.orsy.dto;

import org.tfg.orsy.model.RolUsuario;

public record AuthResponse(
        Long id,
        String nombre,
        String email,
        RolUsuario rol
) {}
