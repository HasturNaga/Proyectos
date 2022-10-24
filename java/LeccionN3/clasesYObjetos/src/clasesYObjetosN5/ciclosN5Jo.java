/*
Ejercicio 5: realiar un juego para adivinar un numero,
para elo generar un numero aleatorio entre 0-100, y
luego ir pidiendo numeros indicando "es mayor" o "es menor"
segun sea mayor o menor con respecto a N
El proceso termina cuando el usuario acierta y mostramos
el numero de intentos hechos.
 */
package clasesYObjetosN6;

import javax.swing.JOptionPane;

public class CiclosN5Jo {

    public static void main(String[] args) {
        int numero, aleatorio, contador = 0;
        aleatorio = (int)(Math.random()*100);
        
        do{
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            if(numero < aleatorio){
                JOptionPane.showMessageDialog(null, "Digite un numero mayor.");
            }
            else if(numero > aleatorio){
                JOptionPane.showMessageDialog(null, "Digite un numero menor.");
            }
            else{
                JOptionPane.showMessageDialog(null, "¡¡¡FELICITACIONES!!! Has adivinado el numero.");
            }
            contador++;        
        }while(numero != aleatorio);
        JOptionPane.showMessageDialog(null,"Adivinaste al numero en: " + contador + " intentos.");
    }
    
}