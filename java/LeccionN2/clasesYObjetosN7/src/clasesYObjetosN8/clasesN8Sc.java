/*
Ejercicio 8: pedir un numero N, y mostrar todos lo numeros del 1 al N.
 */
package clasesYObjetosN8;

import java.util.Scanner;

public class clasesN8Sc {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero = ");
        int numero = Integer.parseInt(entrada.nextLine());
        int i = 1;
        while (i <= numero) {
            System.out.println(i);
            i++;
        }

    }
}
