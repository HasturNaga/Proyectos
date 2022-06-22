package ejercicion9;
//Como hago una rama 
//funciona....

import java.util.Scanner;


public class ejercicioN9 {

    public static void main(String[] args) {

        int num1 = 4, num2 = 5;
        int solucion = num1 + num2;
        System.out.println("La suma es = " + solucion);

        solucion = num1 - num2;
        System.out.println("La resta es: " + solucion);

        solucion = num1 * num2;
        System.out.println("La multiplicacion es: " + solucion);

        double division = 3.4 / num2;
        System.out.println("division = " + division);

        division = num1 % num2;
        System.out.println("El resto de la division es = " + division);

        //if (num1 % == 0) Prguntar al profesor
        //    System.out.println("El numero ingresado es par");
        //else
        //System.out.println("El numero ingresadoes inmpar");
        int varNum1 = 1, varNum2 = 4;
        int varNum3 = varNum1 + 6 - varNum2;
        System.out.println("Variable numero 3 = " + varNum3);
        /*
        varNum1 +=;
        System.out.println("varNum1 = " + varNum1);
        varNum1 -=;
        System.out.println("varNum1 = " + varNum1);
        varNum1 *=;
        System.out.println("varNum1 = " + varNum1);
        varNum1 /=;
        System.out.println("varNum1 = " + varNum1);
        varNum1 %=;
        System.out.println("varNum1 = " + varNum1);*/

        int varA = 7;
        int varB = -varA;
        System.out.println("varA" + varA);
        System.out.println("varB = " + varB);

        boolean varC = true;
        boolean varD = !varC;
        System.out.println("varD = " + varD);

        int varE = 9;
        int varF = ++varE;
        System.out.println("varE = " + varE);
        System.out.println("varF = " + varF);

        int varG = 3;
        int varH = varG++;
        System.out.println("varG = " + varG);
        System.out.println("varH = " + varH);

        int varI = 4;
        //int varH = --varI;
        System.out.println("varI = " + varI);
        //System.out.println("varH = " + varH);

        int varK = 8;
        int varL = varK--;
        System.out.println("varK = " + varK);
        System.out.println("varL = " + varL);

        int aNum = 5;
        int bNum = 4;
        boolean cNum = (aNum == bNum);
        System.out.println("cNum = " + cNum);

        boolean dNum = aNum != bNum;
        System.out.println("dNum = " + dNum);

        String cadenaA = "Hrllo";
        String cadenaB = "bye bye";
        boolean cVar = !cadenaA.equals(cadenaB);
        System.out.println("cVar = " + !cVar);
        if (cadenaA.equals(cadenaB)) {
            System.out.println("cVar = " + cVar);
        }

        boolean gVar = aNum == bNum;
        System.out.println("gVar = " + gVar);

        gVar = aNum != bNum;
        System.out.println("gVar = " + gVar);

        gVar = aNum >= bNum;
        System.out.println("gVar = " + gVar);

        gVar = aNum <= bNum;
        System.out.println("gVar = " + gVar);

        gVar = aNum < bNum;
        System.out.println("gVar = " + gVar);

        gVar = aNum > bNum;
        System.out.println("gVar = " + gVar);

        if (aNum % 2 == 0) {
            System.out.println("El numero es par.");
        } else {
            System.out.println("El numero es impar.");
        }

        if (aNum >= bNum) {
            System.out.println("La persona A el mayor que la B");
        } else {
            System.out.println("La persona A el menor que la B");
        }

        int valorA = 7;
        int valorMinimo = 0;
        int valorMaximo = 10;
        boolean respuesta = valorA >= 0 && valorA <= 10;

        if (respuesta) {
            System.out.println("Esta dentro del rango establecido.");
        } else {
            System.out.println("No esta dentro del rango estalecido.");
        }
        
        boolean vacaciones = false;
        boolean diaLibre = false;
        
        if(vacaciones || diaLibre) {
            System.out.println("Puede asistir al partido.");            
        }else {
            System.out.println("No pude asistir al partido.");
        }
        
        boolean respuestaT = (5 < 8) ? true : false;
        //no funcina var, para tipo de variable;
        int x = 5;
        int y = 10;
        int z = ++x + y--;
        
        System.out.println("x = " + x);
        System.out.println("y = " + y);
        System.out.println("z = " + z);
        
        double varNumero = 4 + 5 * 6 / 3;
        System.out.println("varNumero = " + varNumero);
        
        varNumero = (4 + 5) * 6 / 3;
        System.out.println("varNumero = " + varNumero);
        
        Scanner sc = new Scanner(System.in);
        float nota1, nota2, nota3, suma;
        
        System.out.println("Digite las tres calificaciones");
        nota1 = Float.parseFloat(sc.nextLine());
        nota2 = Float.parseFloat(sc.nextLine());
        nota3 = Float.parseFloat(sc.nextLine());
        
        suma = nota1 + nota2 + nota3;
        
        System.out.println("La suma es: " + suma);
        
        float guillermo, luis, juan, total;
        Scanner sc1 = new Scanner(System.in);
        
        System.out.println("Digite la cantidad de dinero de guillermo: ");
        guillermo = Float.parseFloat(sc1.nextLine());
        
        luis = guillermo / 2;
        juan = (luis + guillermo) / 2;
        total = luis + guillermo + juan;
        System.out.println("luis = " + luis);
        System.out.println("juan = " + juan);
        System.out.println("guillermo = " + guillermo);
        
        final int salario = 1000;
        int comision = 150, venta;
        float salarioMensual, ventaCarro, porcVenta, totalPrecio;
        Scanner sc3 = new Scanner(System.in);
        
        System.out.println("Digite la cantidad de carros vendidos: ");
        venta = Integer.parseInt(sc3.nextLine());
        System.out.println("Digite el precio de un carro: ");
        ventaCarro = Float.parseFloat(sc3.nextLine());
        
        comision *= venta;
        totalPrecio = ventaCarro * venta;
        porcVenta = totalPrecio * 0.05F;
        salarioMensual = salario + comision + porcVenta;
        System.out.println("El salario es:");
        
        
        
        
        
        
        
        
    }
    

}
