/*
Ejercicio 9: pedir el dia, me y año de una fecha e
indicar si la fecha es correcta. Suponiendo que
todos los meses son de 30 dias.
 */
package Ejercicio09;

import javax.swing.JOptionPane;

public class Ejercicio09 {

    public static void main(String[] args) {
        int dia = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el dia: "));
        int mes = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el mes: "));
        int anio = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el anio: "));
        if ((dia != 0) && (dia <= 30)) {
            if ((mes != 0) && (mes <= 12)) {
                if ((anio != 0) && (anio <= 2022)) {
                    JOptionPane.showMessageDialog(null, "La fecha igresada es: " + dia + "/" + mes + "/" + anio);
                } else {
                    JOptionPane.showMessageDialog(null, "La fecha es incorrecta, año incorrecto.");
                }
            } else {
                JOptionPane.showMessageDialog(null, "La fecha es incorrecta, mes incorrecto.");
            }
        } else {
            JOptionPane.showMessageDialog(null, "La fecha es incorrecta, dia incorrecto.");
        }
    }
}
