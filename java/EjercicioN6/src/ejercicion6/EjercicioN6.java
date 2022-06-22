/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ejercicion6;

import java.util.Scanner;

/**
 * c
 
 */
public class EjercicioN6 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int varGuillermo, varLuis, varJuan;
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese los N dolares que posee Guilermo: ");
        varGuillermo = sc.nextInt();
        varLuis = varGuillermo / 2;
        varJuan = (varLuis + varGuillermo) / 2;
        
        System.out.println("Guillermo tiene: " + varGuillermo + " dolares");
        System.out.println("Luis tiene: " + varLuis + " dolares");
        System.out.println("Juan tiene: " + varJuan + " dolares");
    }
    
}
