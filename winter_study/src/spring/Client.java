package spring;

public class Client {

	public static void main(String[] args) {
		Animal baduck = new Dog();
		Animal nabi = new Cat();
		
		baduck.playWithOwner();

		System.out.println();
		System.out.println();
		
		nabi.playWithOwner();
	}
}
