/*
Ejercicio 7: pedir numeros hasta que se introca uno negativo
y calcular la media
 */
package clasesYObjetosN7;

import javax.swing.JOptionPane;

public class ciclosN7Jo {

    public static void main(String[] args) {
        int numero = 0, contador = 0, suma = 0;
        float promedio = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while (numero >= 0) {
            suma += numero;
            contador++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        if (contador == 0) {
            JOptionPane.showMessageDialog(null, "\nError, la division entre cero no existe.");
        } else {
            promedio = (float) suma / contador;
        }
        JOptionPane.showMessageDialog(null, "\nEl promedio es: " + promedio);
    }
}
