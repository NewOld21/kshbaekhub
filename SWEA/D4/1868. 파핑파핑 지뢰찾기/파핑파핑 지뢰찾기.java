import java.util.*;
import java.io.*;

class Solution
{
    static int[] dx = {0,0,1,-1,1,1,-1,-1};
    static int[] dy = {1,-1,0,0,1,-1,1,-1};
    static int[][] graph;
    static int N;
    static int ans;
	public static void main(String args[]) throws Exception
	{
	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

		for(int test_case = 1; test_case <= T; test_case++)
		{
            N = Integer.parseInt(br.readLine());
            graph = new int[N][N]; 


            for(int i=0; i<N; i++){
                String str = br.readLine();
                for(int j=0;j<N;j++){
                    if(str.charAt(j) == '*'){
                        graph[i][j] = -1;
                        for(int idx=0; idx<8; idx++){
                            int nx = i + dx[idx];
                            int ny = j + dy[idx];
                            if(nx>=0 && nx<N && ny>=0 && ny<N && graph[nx][ny] != -1){
                                graph[nx][ny] += 1;
                            }
                        }
                    }
                }
            }
            
            ans = 0;
            for(int x=0; x<N;x++){
                for(int y=0; y<N; y++){
                    if(graph[x][y] == 0){
                        bfs(x,y);
                    }
                }
            }
            for(int x=0; x<N;x++){
                for(int y=0; y<N; y++){
                    if(graph[x][y] >0){
                        ans++;
                    }
                }
            }

            System.out.println("#" + test_case + " " + ans);
		}
	}


    private static void bfs(int x, int y){
        Queue<Node> q = new ArrayDeque<>();
        q.offer(new Node(x,y));
        graph[x][y] = -1;
        while(!q.isEmpty()){
            Node node = q.poll();

            for(int idx=0; idx<8; idx++){
                int nx = node.x + dx[idx];
                int ny = node.y + dy[idx];
                if(nx>=0 && nx<N && ny>=0 && ny<N && graph[nx][ny] != -1){
                    if(graph[nx][ny]==0){
                        q.offer(new Node(nx,ny));
                    }
                    graph[nx][ny] = -1;
                }
           }
        }
        ans++;
    }
}

class Node{
    int x;
    int y;

    Node(int x, int y){
        this.x = x;
        this.y = y;
    }
}
