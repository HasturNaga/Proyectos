/*
Ejercicio 2: leer 5 numeros, gurdarlos en un arreglo y
mostrarlos en el orden inverso al introducido.
 */
package arreglos_ejercicio_2;

import java.util.Scanner;

public class Arreglos_Ejercicio_2 {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        float numeros[] = new float[5];

        System.out.println("Guardando los elementos del arreglos.");
        for (int i = 0; i < 5; i++) {
            System.out.println((i + 1) + ". Digite un numero: ");
            numeros[i] = entrada.nextFloat();
        }

        for (int i = 4; i >= 0; i--) {
            System.out.println(" "+numeros[i]);
        }
        System.out.println("\n");
    }
}
