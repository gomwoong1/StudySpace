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
		
		while(val.equals(origin)) {
			sum = Character.getNumericValue(val.charAt(0)) + Character.getNumericValue(val.charAt(1));
			val = (val.charAt(1) + String.valueOf(sum));
			count++;
			
			System.out.println("val값: " + val.charAt(1) + ", sum값: " + Integer.toString(sum).substring(1) + "/... " +sum);
//			System.out.println("origin: " + origin + ", val값: " + nextVal + ", sum값: " + sum + ", count: " + count);
		}
		
		System.out.println(count);
		br.close();
	}

}
