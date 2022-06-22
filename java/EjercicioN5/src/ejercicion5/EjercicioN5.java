
package ejercicion5;

import java.util.Scanner;

public class EjercicioN5 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int primera, segunda, tercera, resultado;
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Ingrese la primer variable: ");
        primera = sc.nextInt();
        System.out.println("Ingrese la segunda variable: ");
        segunda = sc.nextInt();
        System.out.println("Ingrese la tercera variable: ");
        tercera = sc.nextInt();
        
        resultado = primera + segunda + tercera;
        
        System.out.println("La suma de las tres variables es: " + resultado);
       
    }
    
}
