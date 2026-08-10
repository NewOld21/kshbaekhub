import java.util.PriorityQueue;

class Solution {
    public int solution(int[][] board) {
        int answer = 0;
        int N = board[0].length;

        PriorityQueue<Node> pq =
                new PriorityQueue<>((o1, o2) -> Integer.compare(o1.cnt, o2.cnt));

        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};

        
        boolean[][][] visited = new boolean[N][N][2];
        pq.offer(new Node(0, 0, 0, 0));

        while (!pq.isEmpty()) {
            Node node = pq.poll();

            if (visited[node.x][node.y][node.way]) {
                continue;
            }

            visited[node.x][node.y][node.way] = true;

            if (node.x == N - 1 && node.y == N - 1) {
                answer = node.cnt;
                break;
            }

            for (int i = 0; i < 4; i++) {
                int nx = node.x + dx[i];
                int ny = node.y + dy[i];

                if (0 <= nx && nx < N && 0 <= ny && ny < N && board[nx][ny] == 0) {
                    int nextWay = (i == 0 || i == 1) ? 0 : 1;

                    if (visited[nx][ny][nextWay]) {
                        continue;
                    }

                    if (node.way == nextWay) {
                        pq.offer(new Node(node.cnt + 1, nx, ny, nextWay));
                    } 
                    else {
                        pq.offer(new Node(node.cnt + 6, nx, ny, nextWay));
                    }
                }
            }
        }


        pq.clear();
        visited = new boolean[N][N][2];

        pq.offer(new Node(0, 0, 0, 1));

        while (!pq.isEmpty()) {
            Node node = pq.poll();

            if (visited[node.x][node.y][node.way]) {
                continue;
            }

            visited[node.x][node.y][node.way] = true;

            if (node.x == N - 1 && node.y == N - 1) {
                if (answer == 0) {
                    answer = node.cnt;
                } else {
                    answer = Math.min(answer, node.cnt);
                }

                break;
            }

            for (int i = 0; i < 4; i++) {
                int nx = node.x + dx[i];
                int ny = node.y + dy[i];

                if (0 <= nx && nx < N && 0 <= ny && ny < N && board[nx][ny] == 0) {
                    int nextWay = (i == 0 || i == 1) ? 0 : 1;

                    if (visited[nx][ny][nextWay]) {
                        continue;
                    }

                    if (node.way == nextWay) {
                        pq.offer(new Node(node.cnt + 1, nx, ny, nextWay));
                    } 
                    else {
                        pq.offer(new Node(node.cnt + 6, nx, ny, nextWay));
                    }
                }
            }
        }

        return answer * 100;
    }
}

class Node {
    int cnt;
    int x;
    int y;
    int way;

    Node(int cnt, int x, int y, int way) {
        this.cnt = cnt;
        this.x = x;
        this.y = y;
        this.way = way;
    }
}