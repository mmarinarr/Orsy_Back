package org.tfg.orsy.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.tfg.orsy.model.Comanda;
import org.tfg.orsy.model.EstadoComanda;

import java.util.Optional;

public interface ComandaRepository extends JpaRepository<Comanda, Long> {

    Optional<Comanda> findFirstByMesaIdAndEstado(Long mesaId, EstadoComanda estado);
}
