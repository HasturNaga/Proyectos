/*
Ejercicio 3: leer numeros hasta que se introduca un cero.
Para cada una indicar si es par o impar.
Primro lo haremos con la clase Scanner.
Luego con la clase JOptionPane
*/
package claseYOjetosN02;

import javax.swing.JOptionPane;

public class ciclosN04 {

    public static void main(String[] args) {
        int numero;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero != 0){
            if(numero % 2 == 0){
                JOptionPane.showMessageDialog(null, "El numero ingresado " + numero + " es PAR");
            }else{
                JOptionPane.showMessageDialog(null, "El numero ingresado " + numero + " es IMPAR");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        JOptionPane.showMessageDialog(null, "El numero ingresado es " + numero + " finaliza el programa.");  
    }
    
}
