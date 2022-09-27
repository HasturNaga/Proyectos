
package ciclosDeJava;

public class ciclos {
    public static void main(String[] args) {
        int contador = 0;
// Ciclo while
        while (contador < 7) {
            System.out.println("Contador = " + contador);
            contador++;
        }
        contador = 0;
// Ciclo do while
        do {
            System.out.println("Contador = " + contador);
            contador++;
        } while (contador < 7);
// Ciclo for
        for (int i = 0; i < 7; i++) {
            System.out.println("Contador = " + i);
        }

        inicio:
        for (int i = 0; i < 7; i++) {
            if (contador % 2 == 0) {
                System.out.println("Contador = " + i);
                break inicio;
            }
        }

        for (int i = 0; i < 7; i++) {
            if (i % 2 != 0) {
                continue;
            }
            System.out.println("Contador = " + i);
        }
        
        
        
    }
}
