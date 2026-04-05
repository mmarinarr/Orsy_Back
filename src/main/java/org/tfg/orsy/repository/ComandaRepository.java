package org.tfg.orsy.repository;

import org.tfg.orsy.model.Comanda;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface ComandaRepository extends JpaRepository<Comanda, Long> {
    List<Comanda> findByMesaIdAndEstado(Long mesaId, String estado);
    List<Comanda> findByEstado(String abierta);
}
