package ejercicion8;

import java.util.Scanner;

public class ejercicioN8 {

    public static void main(String[] args) {
        
        byte numEnteroByte = 127;
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("Valor minimo del Byte: " + Byte.MIN_VALUE);
        System.out.println("Valor maximo del Byte: " + Byte.MAX_VALUE);
        
        short numEnteroShort = 32767;
        System.out.println("numEnteroShort = " + numEnteroByte);
        System.out.println("Valor minimo del Short: " + Short.MIN_VALUE);
        System.out.println("Valor maximo del Short: " + Short.MAX_VALUE);
        
        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt = " + numEnteroByte);
        System.out.println("Valor minimo del int: " + Integer.MIN_VALUE);
        System.out.println("Valor maximo del int: " + Integer.MAX_VALUE);

        long numEnteroLong = 2147483647;
        System.out.println("numEnteroShort = " + numEnteroByte);
        System.out.println("Valor minimo del Long: " + Long.MIN_VALUE);
        System.out.println("Valor maximo del Long: " + Long.MAX_VALUE); 
        
        float numFloat = 3.4028235E38F;
        System.out.println("numFloat = " + numFloat);
        System.out.println("Valor minimo del Float: " + Float.MIN_VALUE);
        System.out.println("Valor maximo del Float: " + Float.MAX_VALUE);
        
        double numDouble = 1.7976931348623157E308;
        System.out.println("numFloat = " + numDouble);
        System.out.println("Valor minimo del numDouble: " + Double.MIN_VALUE);
        System.out.println("Valor maximo del numDouble: " + Double.MAX_VALUE);
        
        char varCaracter = 'a';
        System.out.println("varCaracter = " + varCaracter);
        
        boolean varBool = true;
        System.out.println("varBool = " + varBool);
        
        if(varBool) {
            System.out.println("La banera es verde.");
        }
        else {
            System.out.println("La bandera es roja.");
        }
        
        int edad = 15;
        //boolean adulto = edad >= 18;
        
        if(edad >= 18) {
            System.out.println("Eres mayor de edad.");
        }
        else { 
            System.out.println("Eres menor de edad.");
        }
        
        int varEdad = Integer.parseInt("20");
        System.out.println("varEdad = " + (varEdad + 1));
        double varPi = Double.parseDouble("3.343441416");
        System.out.println("varPi = " + varPi);
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite se edad: ");
        varEdad = Integer.parseInt(sc.nextLine());
        System.out.println("varEdad = " + varEdad);
        
        String edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
        char varChar = 'a';
        char fraseChar = "programdores".charAt(0);
        
        Scanner sc1 = new Scanner(System.in);
        System.out.println("Digite el nombre del libro: ");
        String nombreLibro = sc1.nextLine();
        System.out.println("Digite el id del libro: ");
        int idLibro = Integer.parseInt(sc1.nextLine());
        System.out.println("Digite el precio del libro: ");
        double precioLibro = Double.parseDouble(sc1.nextLine());
    }
    
}
