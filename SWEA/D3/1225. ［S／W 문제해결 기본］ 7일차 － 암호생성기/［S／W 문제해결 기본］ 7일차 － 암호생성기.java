/////////////////////////////////////////////////////////////////////////////////////////////
// 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
// 아래 표준 입출력 예제 필요시 참고하세요.
// 표준 입력 예제
// int a;
// double b;
// char g;
// String var;
// long AB;
// a = sc.nextInt();                           // int 변수 1개 입력받는 예제
// b = sc.nextDouble();                        // double 변수 1개 입력받는 예제
// g = sc.nextByte();                          // char 변수 1개 입력받는 예제
// var = sc.next();                            // 문자열 1개 입력받는 예제
// AB = sc.nextLong();                         // long 변수 1개 입력받는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
// 표준 출력 예제
// int a = 0;                            
// double b = 1.0;               
// char g = 'b';
// String var = "ABCDEFG";
// long AB = 12345678901234567L;
//System.out.println(a);                       // int 변수 1개 출력하는 예제
//System.out.println(b); 		       						 // double 변수 1개 출력하는 예제
//System.out.println(g);		       						 // char 변수 1개 출력하는 예제
//System.out.println(var);		       				   // 문자열 1개 출력하는 예제
//System.out.println(AB);		       				     // long 변수 1개 출력하는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
import java.util.*;
import java.io.*;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    StringTokenizer st;
		for(int test_case = 1; test_case <= 10; test_case++)
		{
			int N = Integer.parseInt(br.readLine());
	        String s = br.readLine();
	            
			Queue<Integer> q = new LinkedList<>();
	        st = new StringTokenizer(s);
				
	        while(st.hasMoreTokens()) {
	            q.add(Integer.parseInt(st.nextToken()));
	        }
	            
	        int pre_num = 100;
	        int cnt = 1;
	        while(pre_num > 0) {
	        	pre_num = q.poll();
	            	
	            if(pre_num - cnt <= 0) {
	            	pre_num = 0;
	            	cnt = 0;
	            }
	            q.add(pre_num-cnt);
                cnt = cnt%5 + 1;
	       }
	            
	      StringBuilder sb = new StringBuilder();
           sb.append("#").append(N);

            while (!q.isEmpty()) {
                sb.append(" ").append(q.poll());
            }

            System.out.println(sb);
		}
	}
}