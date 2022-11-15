package CiclosN3;

import javax.swing.JOptionPane;

public class numerosImpares {

    public static void main(String[] args) {
        long producto = 1;

        for (int i = 1; i <= 20; i += 2) {
            producto *= i;
        }
        JOptionPane.showMessageDialog(null, "El produto de los numeros impares es: " + producto);
        
    }

}
