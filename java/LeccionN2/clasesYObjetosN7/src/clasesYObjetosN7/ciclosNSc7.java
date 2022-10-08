/*
Ejercicio 7: pedir numeros hasta que se introca uno negativo
y calcular la media
 */
package clasesYObjetosN7;

import java.util.Scanner;

public class ciclosNSc7 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero = 0, contador = 0, suma = 0;
        float promedio = 0;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0) {
            suma += numero;
            contador ++;
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        if(contador == 0){
            System.out.println("\nError, la division entre cero no existe.");
        }
        else
            promedio = (float)suma/contador;
            System.out.println("\nEl promedio es: " + promedio);
    }
}
