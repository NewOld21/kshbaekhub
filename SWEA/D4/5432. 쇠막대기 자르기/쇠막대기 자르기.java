import java.util.*;
import java.io.*;


class Solution
{
	public static void main(String args[]) throws Exception
	{
	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		Stack<Character> stack = new Stack<>();
		for(int test_case = 1; test_case <= T; test_case++)
		{
			String list = br.readLine();

			int bar = 0;
			int cnt = 0;
			int ans = 0;
			for(int i=0; i<list.length(); i++) {
				char c = list.charAt(i);
				if(c=='(') {
					if(list.charAt(i+1) == ')') {
						ans += bar; // 3 + 3 
						i++;
						continue;
					}else {
						stack.push('(');
						bar += 1;
					}
					
				}
				else if(c==')') {
					stack.pop();
					bar--;
					cnt += 1;
				}
				
			}
            ans += cnt;
			System.out.println("#" + test_case + " " + ans);
		}
	}
}