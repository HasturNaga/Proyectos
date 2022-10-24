/*
Ejercicio1: leer y mostrar el cuadrado,
repetir el proceso hasta que se ingrese un numero negativo.
 */
package CiclosN2;

import javax.swing.JOptionPane;


public class PositivoNegativo2 {


    public static void main(String[] args) {
       
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero != 0){
            if(numero > 0){
                JOptionPane.showMessageDialog(null, "El numero " + numero + " es POSITIVO.");
            }else{
                JOptionPane.showMessageDialog(null, "El numero " + numero + " es NEGATIVO.");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        JOptionPane.showMessageDialog(null, "El numero " + numero + " finaliza el programa.");
    }
    
}
