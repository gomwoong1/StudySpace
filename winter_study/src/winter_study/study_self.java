package winter_study;

public class study_self {
	public static void main(String[] args) {
		String text = "hello world!";
		System.out.println("호출전: " + text);
		
		changeTxt(text);
		System.out.println("호출후: " + text);
		//String값은 Call By Value.
	}

	public static void changeTxt(String txt) {
		txt = "bye world!";
		System.out.println("method: " + txt);
	}
}

