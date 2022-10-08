/*

 */
package clasesYObjetosN6;

import javax.swing.JOptionPane;

public class ciclosN6Jo {


    public static void main(String[] args) {
        int numero, suma = 0;
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            suma += numero;
        }while(numero != 0);
        JOptionPane.showMessageDialog(null, "La suma de los numeros ingrsados es: " + suma);
    }
    
}
