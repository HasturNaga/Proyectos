package operaciones;

public class principal {

    public static void main(String[] args) {
        aritmetica aritmetica1 = new aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumar();
        
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumento(12, 26);
        System.out.println("Resultados con argumentos: " + resultado);
    }

}
