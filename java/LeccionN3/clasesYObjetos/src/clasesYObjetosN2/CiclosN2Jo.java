/*
Ejercicio 2: leer un numero e indicar si es positivo o 
negativo. El proceso se repite hasta que se introduzca un cero.
*/
package clasesYObjetosN2;

import javax.swing.JOptionPane;

public class CiclosN2Jo {

    public static void main(String[] args) {
        System.out.println("Digite un numero: ");
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while (numero != 0) {
            if (numero > 0) {
                JOptionPane.showMessageDialog(null, "El numero " + numero + " es POSITIVO.");
            } else {
                System.out.println("El numero " + numero + " es NEGOTIVO.");
            }
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        }
        JOptionPane.showMessageDialog(null, "El numero " + numero + " es NEGATIVO.");
    }

}
