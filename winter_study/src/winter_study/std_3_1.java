package winter_study;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class std_3_1 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		char[] str = br.readLine().toUpperCase().toCharArray();
		int count = 0, max = 0;
		char result = '?';
		
		for(int i = 65; i <= 91; i++) {
			count = 0;
			for (int j : str) {
				if (i == j) {
					count += 1;
					if (count > max) {
						result = (char) i;
						max = count;
					}
					else if (count == max)
						result = '?';
				}
			}
		}
		
		System.out.println(result);
	}

}
