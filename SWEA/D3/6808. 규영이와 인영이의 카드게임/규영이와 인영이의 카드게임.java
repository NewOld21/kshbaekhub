import java.util.*;
import java.io.*;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
class Solution
{
    static int win;
    static int lose;
    static int[] order;
    static int[] cardI0;
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
		int T = Integer.parseInt(br.readLine());

		for(int test_case = 1; test_case <= T; test_case++)
		{
            int[] card = new int[19];
            order = new int[9];
            win = 0;
            lose = 0;
            

			st = new StringTokenizer(br.readLine());
            for(int i=0; i<9; i++) {
                int num = Integer.parseInt(st.nextToken());
                card[num] = 1;
                order[i] = num;
            }

            cardI0 = new int[9];
            int cnt = 0;
            for(int i=1; i<19; i++){
                if(card[i]==0)
                    cardI0[cnt++] = i;
            }

            boolean[] visited = new boolean[9];
            cardGame(0, 0, 0, visited);

            System.out.println("#" + test_case + " " + win + " " + lose);
		}
	}

    private static void cardGame(int sumG0, int sumI0, int cnt, boolean[] visited){
        if(cnt==9){
            if(sumG0 > sumI0)
                win++;
            else if(sumG0 < sumI0)
                lose++;
            return ;
        }

        for(int i=0; i<9; i++){
            if(!visited[i]){
                visited[i] = true;
                if(order[cnt] > cardI0[i]){
                    cardGame(sumG0+order[cnt] + cardI0[i], sumI0,cnt+1, visited);
                }
                else{
                    cardGame(sumG0, order[cnt] + cardI0[i] + sumI0,cnt+1, visited);
                }
                
                visited[i] = false;
            }
        }
    }
}