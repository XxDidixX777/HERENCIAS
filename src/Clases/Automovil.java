/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Clases;

/**
 *
 * @author Didier
 */
public class Automovil extends Vehiculo {
     private String marca;
    private String modelo;
    private double precio;

    public Automovil(String fechaFabricacion, String vinChasis, String vinMotor, String marca, String modelo, double precio) {
        super(fechaFabricacion, vinChasis, vinMotor);
        this.marca = marca;
        this.modelo = modelo;
        this.precio = precio;
        
    }

    /**
     * @return the marca
     */
    public String getMarca() {
        return marca;
    }

    public String getModelo() {
        return modelo;
    }

    public double getPrecio() {
        return precio;
    }

   
    
        public void mostrarDatos() {
        System.out.println("Informacion del Automoovil ");
        System.out.println("Fecha de Fabricacion: " + getFechaFabricacion());
        System.out.println("VIN del Chasis: " + getVinChasis());
        System.out.println("VIN del Motor: " + getVinMotor());
        System.out.println("Marca: " + getMarca());
        System.out.println("Modelo: " + getModelo());
        System.out.printf("Precio: $%,.2f%n", getPrecio()); 
        System.out.println("Disfruta de tu " + getMarca() + " " + getModelo() + "");
        
        
    }
    
    
}
