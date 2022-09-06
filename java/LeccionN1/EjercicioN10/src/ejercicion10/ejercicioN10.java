
package ejercicion10;

import java.util.Scanner;

public class ejercicioN10 {

    public static void main(String[] args) {
        boolean condicion = false;
        
        if(condicion) {
            System.out.println("Condicion Verdadera.");
        }else {
            System.out.println("Condicion Falsa.");
        }
        
        int numero = 2;
        String numeroTexto = "Número desconocido";
        
        if(numero == 1) {
            numeroTexto = "Numero uno";
        }else if (numero == 2) {
            numeroTexto = "Numero dos";
        }else if (numero == 3) {
            numeroTexto = "Numero tres";
        }else if (numero == 4) {
            numeroTexto = "Numero cuatro";
        }else {
            System.out.println("Numro no encntrado.");
        }
        System.out.println("El numero es: " + numero);
        
        Scanner sc4 = new Scanner(System.in);
        System.out.println("Digite un mes del año: ");
        int mes = Integer.parseInt(sc4.nextLine());
        String estacion = "Estacion desconocida";
        
        if(mes == 1 || mes == 2 || mes == 3){
            estacion = "Invierno";
        }else if(mes == 4 || mes == 5 || mes == 6){
            estacion = "otoño";
        }else if(mes == 7 || mes == 8 || mes == 9){
            estacion = "primavera";
        }else if(mes == 10 || mes == 11 || mes == 12){
            estacion = "verano";
        }
        System.out.println("estacion = " + estacion);
        
        Scanner sc5 = new Scanner(System.in);
        System.out.println("Digite un numero: ");
        int varNumero = Integer.parseInt(sc4.nextLine());
        String varTexto = "Valor desconocido";
        
        switch(varNumero){
            case 1:
                varTexto = "Numero uno";
                break;
            case 2:
                varTexto = "Numero dos";
                break;
            case 3:
                varTexto = "Numero tres";
                break;
            case 4:
                varTexto = "Numero cuatro";
                break;
            default:
                System.out.println("Numero no encontrado");    
        }
        
        Scanner sc6 = new Scanner(System.in);
        System.out.println("Digite un mes del año: ");
        mes = Integer.parseInt(sc6.nextLine());
        
        switch(mes) {
            case 1: case 2: case 3:
                estacion = "Invierno";
                break;
            case 4: case 5: case 6:
                estacion = "Otoño";
                break;
            case 7: case 8: case 9:
                estacion = "Primavera";
                break;
            case 10: case 11: case 12:
                estacion = "Verano";
                break;            
        }
        System.out.println("estacion = " + estacion);
        
        Scanner sc7 = new Scanner(System.in);
        System.out.println("Digite un numero entre 0 y 10: ");
        int nota = Integer.parseInt(sc6.nextLine());
        
        if(nota >= 9 && nota <= 10){
            System.out.println("A");
        }else if(nota >= 8 && nota < 9){
            System.out.println("B");
        }else if(nota >= 7 && nota < 8){
            System.out.println("C");
        }else if(nota >= 6 && nota < 7){
            System.out.println("D");
        }else if(nota >= 0 && nota < 6){
            System.out.println("F");
        }else {
            System.out.println("La nota ingresada no es valida");
        }
    }
    
}