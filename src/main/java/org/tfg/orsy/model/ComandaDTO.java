package org.tfg.orsy.model;

import java.util.List;

public record ComandaDTO(
        Long mesaId,
        EstadoComanda estado,
        List<LineaDTO> lineas
) {}
