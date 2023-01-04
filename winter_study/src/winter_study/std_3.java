package winter_study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class std_3 {

	public static void main(String[] args) throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int val = Integer.parseInt(bf.readLine());
		String[] temp = bf.readLine().split(" ");
		int max = -999;
		
		int[] value = new int[val];
		
		for(int i = 0; i < val; i++) {
			value[i] = Integer.parseInt(temp[i]);
		}
		
		for(int i = 0; i < val; i++) {
			for(int j = i+1; j < val; j++) {
				int sum = value[i]+value[j];
				System.out.println(value[i] + " + " + value[j] + " = " + sum);
				if( value[i]+value[j] > max )
					max = value[i]+value[j];
			}
		}
		System.out.println(max);
	}
}
