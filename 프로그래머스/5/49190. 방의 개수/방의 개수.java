import java.util.*;

class Solution {

    public int solution(int[] arrows) {
        int answer = 0;

        int[] dy = {1, 1, 0, -1, -1, -1, 0, 1};
        int[] dx = {0, 1, 1, 1, 0, -1, -1, -1};

        HashSet<Long> nodes = new HashSet<>();
        HashSet<Long> lines = new HashSet<>();

        int y = 0;
        int x = 0;

        nodes.add(0L);

        for (int dir : arrows) {

            for (int k = 0; k < 2; k++) {

                int ny = y + dy[dir];
                int nx = x + dx[dir];

                long now = x + (long)y * 100000000;
                long next = nx + (long)ny * 100000000;

                long line = now * 10 + dir;

                if (nodes.contains(next) && !lines.contains(line)) {
                    answer++;
                }

                nodes.add(next);

                lines.add(now * 10 + dir);
                lines.add(next * 10 + (dir + 4) % 8);

                y = ny;
                x = nx;
            }
        }

        return answer;
    }
}