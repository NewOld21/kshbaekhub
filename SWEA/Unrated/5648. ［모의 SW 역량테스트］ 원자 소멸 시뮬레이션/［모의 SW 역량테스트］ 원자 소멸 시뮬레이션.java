import java.util.*;
import java.io.*;

class Solution
{
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {1, -1, 0, 0};

    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());

        for(int test_case = 1; test_case <= T; test_case++)
        {
            int N = Integer.parseInt(br.readLine());
            int cnt = 0;

            Node[] atom = new Node[N];

            for(int i = 0; i < N; i++){
                st = new StringTokenizer(br.readLine());

                int x = Integer.parseInt(st.nextToken()) * 2;
                int y = Integer.parseInt(st.nextToken()) * 2;
                int d = Integer.parseInt(st.nextToken());
                int k = Integer.parseInt(st.nextToken());

                atom[i] = new Node(x, y, d, k);
            }

            boolean[] dead = new boolean[N];
            int alive = N;

            // HashMap 한 번만 생성
            HashMap<Integer, Integer> map = new HashMap<>(2048);

            while(alive > 0){

                // 기존 데이터만 제거
                map.clear();

                // 1. 모든 살아있는 원자 이동
                for(int i = 0; i < N; i++){

                    if(dead[i])
                        continue;

                    Node node = atom[i];

                    node.x += dx[node.dir];
                    node.y += dy[node.dir];

                    // 범위 밖
                    if(node.x < -2000 || node.x > 2000 ||
                       node.y < -2000 || node.y > 2000){

                        dead[i] = true;
                        alive--;

                        continue;
                    }

                    int key =
                        (node.x + 2000) * 4001
                        + (node.y + 2000);

                    map.put(
                        key,
                        map.getOrDefault(key, 0) + 1
                    );
                }

                // 2. 충돌 확인
                for(int i = 0; i < N; i++){

                    if(dead[i])
                        continue;

                    Node node = atom[i];

                    int key =
                        (node.x + 2000) * 4001
                        + (node.y + 2000);

                    if(map.get(key) >= 2){

                        cnt += node.energy;

                        dead[i] = true;
                        alive--;
                    }
                }
            }

            System.out.println(
                "#" + test_case + " " + cnt
            );
        }
    }
}

class Node{

    int x;
    int y;
    int dir;
    int energy;

    Node(int x, int y, int dir, int energy){

        this.x = x;
        this.y = y;
        this.dir = dir;
        this.energy = energy;
    }
}