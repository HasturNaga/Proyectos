/*
Ejercicio 4: pedir numeros hasta que se teclee uno negartivo,
y mostrar cuantos numeros se han introducido.
Lo hacemos primero con la clave Scanner.
Luego la hacemos con la clase JOptionPane.
*/
package clasesYObjetosN3;

import java.util.Scanner;


public class CiclosN4Sc {

    public static void main(String[] args) {
       int numero, contador = 0;
       Scanner entrada = new Scanner(System.in);
       
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0){
            System.out.println("El numero es " + numero + " es POSITIVO");
            contador++;
            System.out.println("Digite otro numero.");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("A ingresado " + contador + " numeros no negativos.");
    }
    
}
