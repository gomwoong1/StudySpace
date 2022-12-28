package winter_study;

import java.util.Scanner;

public class std_2 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int val = sc.nextInt(); //반복 횟수 입력받기
		sc.nextLine(); //개행문자 제거
		
		for(int i=0; val > i; i++) {
			String cmd = sc.nextLine();
			
			System.out.println(cntChar(cmd, 'a'));
		}
		
		sc.close();
	}
	
	public static int cntChar(String cmd, char target) {
		int cnt = 0;
		
		for(int i=0; i < cmd.length(); i++) {
			if(cmd.charAt(i) == target)
				cnt++;
		}
		return cnt;
	}
}

