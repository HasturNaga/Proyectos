package ejercicion7;

import java.util.Scanner;

public class EjercicioN7 {

    public static void main(String[] args) {

        final int salario = 1000, comision = 150;
        float varUno, varValor = 0;
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Sistema de calculo de sueldo");
        varUno = sc.nextFloat();
        
        for (int i = 0; i < varUno; i++) {
            System.out.println("Ingrese el valor del auto numero " + (i + 1));
            varValor = (float) (salario + comision + (varValor * 0.05));
        }
        System.out.println("El sueldo del empldo es de: " + varUno);
    }

}
