/*
Ejercicio 3: leer numeros hasta que se introduca un cero.
Para cada una indicar si es par o impar.
Primro lo haremos con la clase Scanner.
Luego con la clase JOptionPane
*/
package clasesYObjetosN3;

import java.util.Scanner;

public class CiclosN3Sc {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;
        
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero != 0){
            if(numero % 2 == 0){
                System.out.println("El numero ingresado " + numero + " es PAR");
            }else{
                System.out.println("El numero ingresado " + numero + " es IMPAR");
            }
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El numero ingresado es " + numero + " finaliza el progrema.");
    }
}
