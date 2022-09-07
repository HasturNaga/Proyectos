
package cicloWhile;


public class ejercicioWhile01 {
    public static void main(String[] arg) {
        int conteo = 0;
        while(conteo < 7){
            System.out.println("conteo = " + conteo);
            conteo++;
        }
        int contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while (contador <= 7);
    }
}
