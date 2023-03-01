
class PlusMethon {
    public void plus(){
        System.out.println("PlusMethon");
    }
}

class IntPlus extends PlusMethon {
    public int plus(int a, int b){
        return a + b;
    }

    public void plus(){
        System.out.println("IntPlus");
    }

}

class DoublePlus extends PlusMethon {
    public double plus(double a, double b){
        return a + b;
    }

    public void plus(){
        System.out.println("DoublePlus");
    }
}

class FloatPlus extends PlusMethon {
    public float plus(float a, float b){
        return a + b;
    }

    public void plus(){
        System.out.println("FloatPlus");
    }
}

public class Main {
    public static void main(String[] args) {
        IntPlus intPlus = new IntPlus();
        DoublePlus doublePlus = new DoublePlus();
        FloatPlus floatPlus = new FloatPlus();

        intPlus.plus();
        doublePlus.plus();
        floatPlus.plus();

        System.out.println(intPlus.plus(1, 2));
        System.out.println(doublePlus.plus(1.1, 2.2));
        System.out.println(floatPlus.plus(1.1, 2.2));
    }
}