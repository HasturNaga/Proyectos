/*
Ejercicio 2: leer un numero e indicar si es positivo o 
negativo. El proceso se repite hasta que se introduzca un cero.
*/
package clasesYObjetosN2;

import java.util.Scanner;

public class CiclosN2Sc {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero: ");
        int numero = Integer.parseInt(entrada.nextLine());
        while (numero != 0) {
            if (numero > 0) {
                System.out.println("El numero " + numero + " es POSITIVO.");
            } else {
                System.out.println("El numero " + numero + " es NEGOTIVO.");
            }
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El numero " + numero + " finaliza el programa.");
    }

}
