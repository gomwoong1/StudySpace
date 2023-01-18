package winter_study;

public class test {
	public static void main(String[] args) {
		int i = 10;
		
		if (i == 10) {
			int m = i + 5;
			i = m;
		}
		
		else {
			int j = i + 10;
			i = j;
		}
		
		System.out.println(i);
	}
}
