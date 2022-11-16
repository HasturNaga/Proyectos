/*
Esu de la palabra Final.
Esta palabra tiene diferente significados dependiendo donde
se aplique:
    variables: evita cambiar el valor que almacena la variable.
    metodos: evita que se modifique la definicion o el comportamiento
        de un metodo desde una subclase (hija).
    class: evita que se creen clases hijas.
Otra carateristica es qu normalmente, cuando trabajamos con variables
se comina con el modificador de acceso estatico para convertir una
variable en una constante, es decir que no se puede modificar su valor,
el ejemplo de esto es la clase Math en la cual todos sus atributos
son de tipo static y final, es por esto que la variable pi* se conoce
como constante.

*/
package test;

import domain.Persona;

public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 28412847;
        System.out.println("miDni = " + miDni);
        //miDni = 00000000;
        //Persona.CONSTANTE_AQUI = 9;
        System.out.println("Mi atributo constante es: " + Persona.CONSTANTE_AQUI);
        
        final Persona persona1 = new Persona();
        //persona1 = new Persona(); no se puede asignar una nueva referencia.
        persona1.setNombre("Ricardo Modon");
        System.out.println("persona nombre: " + persona1.getNombre());
        persona1.setNombre("Alfonso Modon");
        System.out.println("persona nombre: " + persona1.getNombre());
    }
}