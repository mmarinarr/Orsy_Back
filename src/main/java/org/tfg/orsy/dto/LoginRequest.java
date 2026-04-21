package org.tfg.orsy.dto;

public record LoginRequest(
        String email,
        String password
) {}
