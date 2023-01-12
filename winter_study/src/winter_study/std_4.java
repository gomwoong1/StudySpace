package winter_study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class std_4 {
	static int count = 0;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int sum = 0;
		String nextVal = "", origin = br.readLine(), val = "";
		
		if( origin.length() == 1 ) 
			val = "0" + origin;
		else
			val = origin;
		
		while(true) {
			if ( val.length() == 1)
				val = "0" + val;
			
			System.out.println("???"+val.charAt(0));
			
			sum = Character.getNumericValue(val.charAt(0)) + Character.getNumericValue(val.charAt(1));
//			nextVal = String.valueOf(val.charAt(1)) + String.valueOf(sum%10);
			val = String.valueOf(val.charAt(1)) + String.valueOf(sum%10);
			
//			System.out.println("!!!"+nextVal);
//			val = nextVal;
			System.out.println("~~~"+val);
//			val = String.valueOf(val.charAt(1)) + String.valueOf(sum%10);
//			val = nextVal;
			count++;
			
			if(val.equals(origin))
				break;
		}
		
		System.out.println(count);
		br.close();
	}

}
