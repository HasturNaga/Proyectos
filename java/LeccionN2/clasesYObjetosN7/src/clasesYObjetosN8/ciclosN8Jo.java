/*
Ejercicio 8: pedir un numero N, y mostrar todos lo numeros del 1 al N.
 */
package clasesYObjetosN8;

import javax.swing.JOptionPane;

public class ciclosN8Jo {
    public static void main(String[] args) {
        
        System.out.println("Digite un numero = ");
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        int i = 1;
        while(i <= numero) {
            JOptionPane.showMessageDialog(null, i);
            i++;
        }    
    } 
}
