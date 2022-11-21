/*
Ejercicio 3: ler 5 numero por teclado, almacenrlos en 
un arreglo y a continuacion realizae la media de los
numero positivos, la media de los negativos y contar el
numero de ceros.
 */
package arreglos_ejercicio_3;

import java.util.Scanner;

public class Arreglos_Ejercicio_3 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float numeros[] = new float[5];
        float negativos = 0, positivos = 0, mediaNeg, mediaPos;
        int conteo0 = 0, conteo_Neg = 0, conteo_Pos = 0;

        System.out.println("Guardamos los elementos del arreglo: ");
        for (int i = 0; i < 5; i++) {
            System.out.println((i + 1) + ". Digite un numero: ");
            numeros[i] = entrada.nextFloat();
            if (numeros[i] > 0) {
                positivos += numeros[i];
                conteo_Pos++;
            } else if (numeros[i] < 0) {
                negativos += numeros[i];
                conteo_Neg++;
            } else {
                conteo0++;
            }
        }

        if (conteo_Pos == 0) {
            System.out.println("\nNo se puede sacar la media de los numeros positivos");
        } else {
            mediaPos = positivos / conteo_Pos;
            System.out.println("\nLa media de los numeros positivos es: " + mediaPos);
        }

        if (conteo_Neg == 0) {
            System.out.println("\nNo se puede sacar la media de los numeros negativos.");
        } else {
            mediaNeg = negativos / conteo_Neg;
            System.out.println("La media de los numeros negativos es: " + mediaNeg);
        }
        System.out.println("La cantidad de ceros es: " + conteo0);
    }
}