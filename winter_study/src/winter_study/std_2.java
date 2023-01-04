package winter_study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class std_2 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		//Scanner sc = new Scanner(System.in) 대체
		int val = Integer.parseInt(br.readLine());
		String[] result = new String[val]; //결과를 저장할 문자열 배열
		Stack<Character> stack = new Stack<>();
		
		for(int i=0; i < val; i++) {
			stack.clear();
			String cmd = br.readLine();
			for(int j = 0; j < cmd.length(); j++) {
				if(cmd.charAt(j) == ')') {
					if(stack.size() == 0) {
						stack.push(cmd.charAt(j));
						break;
					}
					else
						stack.pop();
				}
				else if(cmd.charAt(j) == '(') {
					stack.push(cmd.charAt(j));
				}
			}
			
			if(stack.size() == 0)
				result[i] = "YES";
			else
				result[i] = "NO";
		}
		
		for(String i : result)
			System.out.println(i);
		br.close();
	}
}