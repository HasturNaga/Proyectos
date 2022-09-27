/*
Ejercicio1: leer y mostrar el cuadrado,
repetir el proceso hasta que se ingrese un numero negativo.
*/
package potenciaCuadradaJO;

import javax.swing.JOptionPane;

public class potenciaCuadradaN02 {

    public static void main(String[] args) {
        int numero, cuadrado;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while (numero >= 0){
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El numero " + numero + " elevado al cuadrado es: " + cuadrado);
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }     
        System.out.println("El programa a finalizado por un numero negativo");
    }
    
}
