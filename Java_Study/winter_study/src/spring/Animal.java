package spring;

public abstract class Animal {
	public void playWithOwner() {  //템플릿 메서드 (견본 메서드)
		System.out.println("귀염둥이 이리온");
		play();
		runSomething();
		System.out.println("잘했어");
	} 

	abstract void play();    //추상 메서드
	void runSomething() {    //훅 메서드 (선택적으로 오버라이딩)
		System.out.println("꼬리 살랑살랑");
	}
}
