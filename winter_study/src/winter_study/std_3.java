package winter_study;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class std_3 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int cnt = Integer.parseInt(br.readLine());
		String[] str = new String[cnt];
		
		for(int i = 0; i < cnt; i++) {
			str[i] = br.readLine();
		}
		
		String result = wordCompare(str);
		System.out.println(result);
	}
	
	private static String wordCompare(String[] target) {
		String temp = "";
		char[] alpha = new char[2];
		
		for(int i = 0; i < target[0].length(); i++) {
			int cnt = 0;
			
			for (String s : target) {
				alpha[cnt] = s.charAt(i);
				cnt++;
			}
			
			if (alpha[0] == alpha[1])
				temp += alpha[0];
			else
				temp += '?';
		}
		
		return temp;
	}
}
