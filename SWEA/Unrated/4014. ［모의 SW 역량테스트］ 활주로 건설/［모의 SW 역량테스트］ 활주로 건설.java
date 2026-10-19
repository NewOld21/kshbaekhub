
import java.io.*;
import java.util.*;

class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int N = Integer.parseInt(st.nextToken());
            int X = Integer.parseInt(st.nextToken());

            int[][] map = new int[N][N];

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());

                for (int j = 0; j < N; j++) {
                    map[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int answer = 0;

            for (int i = 0; i < N; i++) {
                boolean[] used = new boolean[N];
                boolean check = true;

                for (int j = 0; j < N - 1; j++) {
                    int diff = map[i][j] - map[i][j + 1];

                    if (diff == 0) continue;

                    if (Math.abs(diff) > 1) {
                        check = false;
                        break;
                    }

                    if (diff == 1) {
                        for (int k = j + 1; k <= j + X; k++) {
                            if (k >= N || map[i][k] != map[i][j + 1] || used[k]) {
                                check = false;
                                break;
                            }
                            used[k] = true;
                        }
                    } else {
                        for (int k = j; k > j - X; k--) {
                            if (k < 0 || map[i][k] != map[i][j] || used[k]) {
                                check = false;
                                break;
                            }
                            used[k] = true;
                        }
                    }

                    if (!check) break;
                }

                if (check) answer++;
            }

            for (int j = 0; j < N; j++) {
                boolean[] used = new boolean[N];
                boolean check = true;

                for (int i = 0; i < N - 1; i++) {
                    int diff = map[i][j] - map[i + 1][j];

                    if (diff == 0) continue;

                    if (Math.abs(diff) > 1) {
                        check = false;
                        break;
                    }

                    if (diff == 1) {
                        for (int k = i + 1; k <= i + X; k++) {
                            if (k >= N || map[k][j] != map[i + 1][j] || used[k]) {
                                check = false;
                                break;
                            }
                            used[k] = true;
                        }
                    } else {
                        for (int k = i; k > i - X; k--) {
                            if (k < 0 || map[k][j] != map[i][j] || used[k]) {
                                check = false;
                                break;
                            }
                            used[k] = true;
                        }
                    }

                    if (!check) break;
                }

                if (check) answer++;
            }

            System.out.println("#" + test_case + " " + answer);
        }
    }
}
