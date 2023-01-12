package winter_study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class std_4 {
	static int count = 0;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int sum = 0;
		String nextVal = "", origin = br.readLine(), val;
		
		if( origin.length() == 1 ) 
			val = "0" + origin;
		else
			val = origin;
		
		System.out.println("길이: " + val.length() + ", 값: " + val);
		System.out.println(val.charAt(0) + ", " + val.charAt(1));
		
		while(true) {
			sum = Character.getNumericValue(val.charAt(0)) + Character.getNumericValue(val.charAt(1));
//			val = (val.charAt(1) + String.valueOf(sum).substring(1));
			val = (val.charAt(1) + String.valueOf(sum).substring(0, (int)((Math.log10(sum)+1)-1)));
			count++;
			
			if(val.equals(nextVal))
				break;
//			System.out.println("val값: " + val.charAt(1) + ", sum값: " + String.valueOf(sum) + "/... " +val);
//			System.out.println("origin: " + origin + ", val값: " + nextVal + ", sum값: " + sum + ", count: " + count);
		}
		
		System.out.println(count);
		br.close();
	}

}
