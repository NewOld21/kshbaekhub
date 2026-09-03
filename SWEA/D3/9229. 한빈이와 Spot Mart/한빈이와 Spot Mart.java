import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringTokenizer st;

        for(int test_case = 1; test_case <= T; test_case++)
        {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());

            int[] snacks = new int[N];

            for(int i = 0; i < N; i++){
                snacks[i] = Integer.parseInt(st.nextToken());
            }

            int mx = -1;

            for(int i = 0; i < N - 1; i++){
                for(int j = i + 1; j < N; j++){

                    int sum = snacks[i] + snacks[j];

                    if(sum <= M){
                        mx = Math.max(mx, sum);
                    }
                }
            }

            System.out.println("#" + test_case + " " + mx);
        }
    }
}