class Solution {
    public boolean exist(char[][] board, String word) {
        boolean visited[][] = new boolean[board.length][board[0].length];
        for (int i = 0; i < board.length; i++) {
            Arrays.fill(visited[i], false);
        }
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == word.charAt(0)) {
                    if (solve(board, i, j, word, 0, visited))
                        return true;
                }
            }
        }
        return false;
    }

    public boolean solve(char[][] board, int row, int col, String word, int idx, boolean[][] visited) {
        if (row < 0 || col < 0 || row >= board.length || col >= board[0].length) return false;
        if (visited[row][col]) return false;
        if (board[row][col] != word.charAt(idx)) return false;
        if (idx == word.length() - 1) return true;

        visited[row][col] = true;
        int[] r = {0, 1, 0, -1};
        int[] c = {1, 0, -1, 0};

        for (int i = 0; i < 4; i++) {
            if (solve(board, row + r[i], col + c[i], word, idx + 1, visited)) {
                return true;
            }
        }

        visited[row][col] = false;
        return false;
    }
}
