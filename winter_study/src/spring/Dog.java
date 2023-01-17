package spring;

public class Dog extends Animal {

	@Override
	void play() {
		System.out.println("멍멍");
	}
	
	@Override
	void runSomething() {
		System.out.println("훅 메서드 오버라이딩");
	}

}
