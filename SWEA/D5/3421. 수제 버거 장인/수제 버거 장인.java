import java.util.*;
import java.io.*;


class Solution
{
    static int N;
    static int M;
    static int[][] arr;
    static int ans;
	public static void main(String args[]) throws Exception
	{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		
		for(int test_case = 1; test_case <= T; test_case++)
		{
		
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            
            arr = new int[M][2];
            ans = 0;

            for(int i=0; i<M; i++){
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                arr[i][0] = a;
                arr[i][1] = b;
            }

            makeHum();
            System.out.println("#" + test_case + " " + ans);
			
		}
	}

    private static void makeHum(){
        for (int mask = 0; mask < (1 << N); mask++) {

            boolean possible = true;

            for (int i = 0; i < M; i++) {
                int a = arr[i][0]-1;
                int b = arr[i][1]-1;
                // a = 1 [001], b = 2 [010]
                // (1 << a) = 001,  (1 << b) = 010
                // mask = 6 [110]
                // mask & a,    mask & b
                //  110              110
                //  001              010
                //  => 000           => 010
                if ((mask & (1 << a)) != 0 && (mask & (1 << b)) != 0) {
                    possible = false;
                    break;
                }
            }

            if (possible) {
                ans++;
            }
        }
    }
}