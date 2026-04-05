package org.tfg.orsy.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.tfg.orsy.model.Venta;

public interface VentaRepository extends JpaRepository<Venta, Long> {
}
