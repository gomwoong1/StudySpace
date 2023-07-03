package winter_study;

public class study_self {
		static String txt; //클래스 == 정적 변수
		String txt2; //인스턴스 변수
		
	public static void main(String[] args) {
		String text = "hello world!"; //지역 변수
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

