package winter_study;

public class test {
	public static void main(String[] args) {
		mouse jerry = new mouse();
		
		jerry.countTail = 10;
		jerry.name = "제리";
		jerry.age = 81;
		
		jerry = null;
	}
}

class mouse {
	int age, countTail;
	String name;
	
	public void sing() {
		System.out.println("찍찍!");
	}
}