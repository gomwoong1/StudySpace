package study;

public class Test {
	public static void main(String args[]) {
		Car car1 = new Car();
		Car car2 = null;
		Fire f1 = new Fire();
		Fire f2 = null;
		
		car1 = f1;
		f2 = (Fire)car1;
	}
}

class Car {
	String name;
	int door;
}

class Fire extends Car {
	public void water() {System.out.println("물");}
}

class Ambul extends Car {
	public void move() {System.out.println("삐용");}
}