/*
Ejercicio 5: realiar un juego para adivinar un numero,
para elo generar un numero aleatorio entre 0-100, y
luego ir pidiendo numeros indicando "es mayor" o "es menor"
segun sea mayor o menor con respecto a N
El proceso termina cuando el usuario acierta y mostramos
el numero de intentos hechos.
 */
package clasesYObjetosN5;

import java.util.Scanner;

public class CiclosN5Sc {
    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, aleatorio, contador = 0;
        
        aleatorio = (int)(Math.random()*100);
        do{
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(entrada.nextLine());
            if(numero < aleatorio){
                System.out.println("Dgite un numero mayor.");
            }
            else if(numero > aleatorio){
                System.out.println("Digite un numero menor.");
            }
            else{
                System.out.println("¬°¬°¬°FELICITACIONES!!! Has adivinado el numero.");
            }
            contador++;        
        }while(numero != aleatorio);
        System.out.println("Adivinaste al numero en: " + contador + " intentos.");
    }
    
}
