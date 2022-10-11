
package caja;

public class Principal {

    public static void main(String[] args) {
    
        int medidaAncho = 3;
        int medidaAlto = 2;
        int medidaProf = 6;
        
        Caja caja1 = new Caja();
        caja1.ancho = medidaAncho;
        caja1.alto = medidaAlto;
        caja1.profundidad = medidaProf;
        int resultado = caja1.calcularVolumen();
        System.out.println("El resultado del volumen de la caja 1 es: " + resultado);
        Caja caja2 = new Caja(2, 4, 6);
        System.out.println("El resultado del volumen de la caja 1 es: " + caja2.calcularVolumen());
    }
    
}
