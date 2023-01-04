package winter_study;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class std_3 {

	private static String result;

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int cnt = Integer.parseInt(br.readLine());
		String[] str = new String[cnt];
		
		for(int i = 0; i < cnt; i++) {
			str[i] = br.readLine();
		}
		
		result = "";
		
		wordCompare(str[0], str[1]);
		wordCompare(str[2], result);
		System.out.println(result);
	}
	
	private static void wordCompare(String target, String target2) {
		for(int i = 0; i < target.length(); i++) {
			if (target.charAt(i) == target2.charAt(i))
				result += target.charAt(i);
			else
				result += '?';
		}
	}
}
