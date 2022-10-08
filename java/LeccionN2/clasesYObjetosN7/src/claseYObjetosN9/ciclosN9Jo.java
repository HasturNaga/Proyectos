/*
Ejercicio 9: pedir el dia, mes y año de una fecha e indicar si la fecha es correcta.
Suponiendo que todos los meses son de 30 dias.
 */
package claseYObjetosN9;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class ciclosN9Jo {

    public static void main(String[] args) {
        System.out.println("Digite un dia: ");
        int dia = Integer.parseInt(JOptionPane.showInputDialog("Digite un dia: "));
        System.out.println("Digite un mes: ");
        int mes = Integer.parseInt(JOptionPane.showInputDialog("Digite un mes: "));
        System.out.println("Digite un anio: ");
        int anio = Integer.parseInt(JOptionPane.showInputDialog("Digite un año: "));
        if ((dia != 0) && (dia <= 30)) {
            if ((mes != 0) && (mes <= 12)) {
                if ((anio != 0) && (anio <= 2022)) {
                    JOptionPane.showMessageDialog(null, "La fecha ingresada es: " + dia + "/" + mes + "/" + anio);
                } else {
                    JOptionPane.showMessageDialog(null, "Fecha incorrecta, año incorrecto.");
                }
            } else {
                JOptionPane.showMessageDialog(null, "Fecha incorrecta, mes incorrecto.");
            }
        } else {
            JOptionPane.showMessageDialog(null, "Fecha incorrecta, dia incorrecto.");
        }
    }

}