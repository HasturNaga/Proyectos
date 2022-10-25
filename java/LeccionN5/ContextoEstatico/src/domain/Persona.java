
package domain;

public class Persona {
    private int idPersona;
    private static int contadorDePersonas;
    private String nombre;
    
    
    public Persona(String nombre){
        this.nombre = nombre;
        // Incrementa el contador por cada objto nuevo
        Persona.contadorDePersonas++;
        //Vamos a asignar un nuevo valor a la variaable idPersona
        this.idPersona = Persona.contadorDePersonas;
        
    }

    public int getIdPersona() {
        return this.idPersona;
    }

    public void setIdPersona(int idPersona) {
        this.idPersona = idPersona;
    }

    public static int getContadorDePersonas() {
        return contadorDePersonas;
    }

    public static void setContadorDePersonas(int contadorDePersonas) {
        Persona.contadorDePersonas = contadorDePersonas;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + ", nombre=" + nombre + '}';
    }
}
