package org.tfg.orsy.model;

import jakarta.persistence.*;
import org.tfg.orsy.model.EstadoMesa;

@Entity
public class Mesa {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private int numero;
    private int capacidad;

    @Enumerated(EnumType.STRING)
    private EstadoMesa estado;

    private int x;
    private int y;

    public Mesa() {}

    public Mesa(int numero, int capacidad, EstadoMesa estado, int x, int y) {
        this.numero = numero;
        this.capacidad = capacidad;
        this.estado = estado;
        this.x = x;
        this.y = y;
    }

    // getters y setters

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public int getCapacidad() {
        return capacidad;
    }

    public void setCapacidad(int capacidad) {
        this.capacidad = capacidad;
    }

    public EstadoMesa getEstado() {
        return estado;
    }

    public void setEstado(EstadoMesa estado) {
        this.estado = estado;
    }

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
}
