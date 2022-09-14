/*
Ejercicio 4: pedir numeros hasta que se teclee uno negartivo,
y mostrar cuantos numeros se han introducido.
Lo hacemos primero con la clave Scanner.
Luego la hacemos con la clase JOptionPane.
*/
package ciclosN06;

import javax.swing.JOptionPane;

public class ciclosN06 {

    public static void main(String[] args) {
        int numero, contador = 0;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero >= 0){
            JOptionPane.showMessageDialog(null, "El numero " + numero + " es POSITIVO");
            contador++;
            numero = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite otro numero: "));
        }
        JOptionPane.showMessageDialog(null, "A ingresado " + contador + " numeros que no son negativos.");
    }
    
}
