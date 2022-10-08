package operaciones;

public class aritmetica {

    int a;
    int b;

    public void sumar() {
        int resultado = a + b;
        System.out.println("Resultado = " + resultado);
    }

    public int sumarConRetorno() {
        //int resultado = a + b;
        return a + b;
    }
    
    public int sumarConArgumento(int a, int b) {
    
        this.a = a;
        this.b = b;
        return this.sumarConRetorno();
    }
}
