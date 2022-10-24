package operaciones;

public class principal {

    public static void main(String[] args) {
        int a = 10;
        int b = 7;
        miMetodo();
        aritmetica aritmetica1 = new aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumar();

        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);

        resultado = aritmetica1.sumarConArgumento(12, 26);
        System.out.println("Resultados con argumentos: " + resultado);

        aritmetica aritmetica2 = new aritmetica(5, 8);
        System.out.println("aritmetica2 = " + aritmetica2.a);
        System.out.println("aritmetica2 = " + aritmetica2.b);

        Persona persona = new Persona("Ariel", "Betancud");
        System.out.print("persona = " + persona);
        System.out.println("Persona nombre: " + persona.nombre);
        System.out.println("Persona apellido: " + persona.apellido);
    }

    public static void miMetodo() {
        int a = 10;
        System.out.println("Aqui hay otro metodo");
    }

}

class Persona {

    String nombre;
    String apellido;

    Persona(String nombre, String apellido) {
        super();
        //Imprimir imprimir = new Imprimir();
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        
    }

    class Imprimir {

        public Imprimir() {
            super();
        }
        public void imprimir(Persona persona){
            System.out.println("Persona dede la clase imprimir: " + persona);
            System.out.println("Impresion del objeto actual (this): " + this);
        }
    }
}