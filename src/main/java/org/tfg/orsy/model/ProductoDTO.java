package org.tfg.orsy.model;

public class ProductoDTO {

    private Long id;
    private String nombre;
    private double precio;
    private Long categoriaId;
    private String categoriaNombre;
    private Categoria categoria;

    public ProductoDTO(Long id, String nombre, double precio, Long categoriaId, String categoriaNombre) {
        this.id = id;
        this.nombre = nombre;
        this.precio = precio;
        this.categoriaId = categoriaId;
        this.categoriaNombre = categoriaNombre;
        if (categoriaId != null) {
            Categoria categoria = new Categoria();
            categoria.setId(categoriaId);
            categoria.setNombre(categoriaNombre);
            this.categoria = categoria;
        }
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    public Long getCategoriaId() {
        return categoriaId;
    }

    public void setCategoriaId(Long categoriaId) {
        this.categoriaId = categoriaId;
    }

    public String getCategoriaNombre() {
        return categoriaNombre;
    }

    public void setCategoriaNombre(String categoriaNombre) {
        this.categoriaNombre = categoriaNombre;
    }

    public Categoria getCategoria() {
        return categoria;
    }

    public void setCategoria(Categoria categoria) {
        this.categoria = categoria;
    }
}
