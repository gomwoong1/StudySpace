package winter_study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class std_4 {
	static int count = 0;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int sum = 0;
		String origin = br.readLine(), val = "";
		
		if( origin.length() == 1 ) {
			origin = "0" + origin;
			val = origin;
		}
		else
			val = origin;
		
		do {
			if ( val.length() == 1)
				val = "0" + val;
			
			sum = Character.getNumericValue(val.charAt(0)) + Character.getNumericValue(val.charAt(1));
			val = String.valueOf(val.charAt(1)) + String.valueOf(sum%10);
			
			count++;
		} while(!val.equals(origin));
		
		System.out.println(count);
		br.close();
	}

}
