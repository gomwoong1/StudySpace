package winter_study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class std_5 {

	public static void main(String[] args) throws IOException {
		
		// 문제 풀이 중지
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] num = new int[10];
		int[] result = new int[10];
		
		for (int i = 0; i < num.length; i++ ) {
			num[i] = br.read() % 42;
		}
		
		for (int i = 0; i < num.length; i++ ) {
			System.out.println(i + ": " + num[i]);
		}
		
		br.close();
	}

}
