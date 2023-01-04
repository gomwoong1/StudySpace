package winter_study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class std_3 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int cnt = Integer.parseInt(br.readLine());
		
		String str = br.readLine();
		String str2 = br.readLine();
		String str3 = br.readLine();
		String result = "";
		
		for(int i = 0; i < str.length(); i++) {
			char a = str.charAt(i), b = str2.charAt(i), c = str3.charAt(i);
			if (a == b && a == c)
				result += a;
			else
				result += '?';
		}
		
		System.out.println(result);
	}

}
