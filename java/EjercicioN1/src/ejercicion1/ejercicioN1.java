package ejercicion1;

import java.util.Scanner;

public class ejercicioN1 {

    public static void main(String[] args) {
        System.out.println("Hola mundo desde Java.");

        int miVariale = 10;
        System.out.println("miVariale = " + miVariale);
        miVariale = 5;
        System.out.println("miVariale = " + miVariale);
        String miVarialeCadena = "Bienvenidos";
        System.out.println("miVarialeCadena = " + miVarialeCadena);
        miVarialeCadena = "Sigamos creciendo";
        System.out.println(miVarialeCadena);

        /*var miVariableEntera2 = 10; //No reconoce la palabra var
        var miVariableEntera2 = "Seguimos estudiando";
        var opcion = 45;
        
        //En cambio usamos String en su lugar
        String usuario = "Osvaldo";
        String titulo = "Ingeniero";
        String union = titulo + " " + usuario;
        System.out.println("union = " + union);
        
        var a = 8;
        var b = 4;
        System.out.println(usuario + a + b + );*/
        String nombre = "Natalia";
        System.out.println("\nNuva linea: \n" + nombre);
        System.out.println("Tabulador: \t" + nombre);
        System.out.println("\t\t.:MENU:.");
        System.out.println("Retroseso: \b\b");
        System.out.println("Comilas simple: \'" + nombre + "\'");
        System.out.println("Comillas Dobles: \"" + nombre + "\"");
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite su nombre: ");
        String usuario1 = sc.nextLine();
        System.out.println("usuario1 = " + usuario1);
        System.out.println("Escriba el titulo: ");
        String titulo = sc.nextLine();
        System.out.println("Resultado: " + titulo + " " + usuario1);
    }

}
