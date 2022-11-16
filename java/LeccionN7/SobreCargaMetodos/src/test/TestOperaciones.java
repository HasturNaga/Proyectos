package test;

import operaciones.Operaciones;

public class TestOperaciones {
    public static void main(String[] args) {
        int resultado = Operaciones.sumar(7, 9);
        System.out.println("resultado = " + resultado);
        
        double resultado1 = Operaciones.sumar(5.0, 9);
        System.out.println("resultado = " + resultado1);
        
        double resultado2 = Operaciones.sumar(7, 9L);
        System.out.println("resultado = " + resultado2);
    }
   
}
