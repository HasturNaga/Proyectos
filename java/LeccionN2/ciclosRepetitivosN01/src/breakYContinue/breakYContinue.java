
package breakYContinue;


public class breakYContinue {


    public static void main(String[] args) {
        
        inicio:
        for(int contador = 0; contador < 7; contador++){
            if(contador % 2 == 0){
                System.out.println("contador = " + contador);
                break inicio;
            }
        }
    
        for(int contador = 0; contador < 7; contador++){
            if(contador % 2 != 0){
                continue;
            }
            System.out.println("contador = " + contador);
        }
                        
    }
}