package operaciones;

public class aritmetica {

    int a;
    int b;

    public aritmetica() {
        System.out.println("Es esta ejecutando este constructor numero uno.");
    }

    public aritmetica(int a, int b) {
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando este constructor numero dos.");
    }

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
