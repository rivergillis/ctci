class ContinentalDivide {
  public static final int PACIFIC = 10;
  public static final int ATLANTIC = 20;
  public static final int NONE = 0;

  public static class Point {
    public boolean reachesPac;
    public boolean reachesAtl;
    public boolean found;
    public int value;
    public Point(int value) {
      reachesAtl = false; reachesPac = false; found = false;
      this.value = value;
    }
  }

  // grid an m x n rect

  public static void flow(Point[][] points, int row, int col, int m, int n) {
    if (points[row][col].found) {
      return;
    }
    points[row][col].found = true;
    
    System.out.println(row + " " + col);
    int currentVal = points[row][col].value;

    if (row <= 0 || col <= 0) {
      points[row][col].reachesPac = true;
    }
    if (row >= m - 1 || col >= n - 1) {
      points[row][col].reachesAtl = true;
    }

    if (row+1 < m) {
      if (points[row + 1][col].value <= currentVal) {
        flow(points, row + 1, col, m, n);
      }
    }
    if (row-1 >= 0) {
      if (points[row - 1][col].value <= currentVal) {
        flow(points, row - 1, col, m, n);
      }
    }
    if (col+1 < n) {
      if (points[row][col+1].value <= currentVal) {
        flow(points, row, col + 1, m, n);
      }
    }
    if (col-1 >= 0) {
      if (points[row][col-1].value <= currentVal) {
        flow(points, row, col - 1, m, n);
      }
    }

    return;
  }

  public static void div(int[][] grid) {
    if (grid.length <= 0) {
      return;
    }

    int m = grid.length;
    int n = grid[0].length;
    Point[][] points = new Point[m][n];

    for (int row = 0; row < m; row++) {
      for (int col = 0; col < n; col++) {
        points[row][col] = new Point(grid[row][col]);
      }
    }

    for (int row = 0; row < m; row++) {
      for (int col = 0; col < n; col++) {
        flow(points, row, col, m, n);
      }
    }
    printPts(points);
  }

  public static void printPts(Point[][] pts) {
    for (Point[] row : pts) {
      for (Point item : row) {
        if (item.reachesAtl) {
          System.out.print("A");
        }
        if (item.reachesPac) {
          System.out.print("P");
        }
        System.out.print(", ");
      }
      System.out.println();
    }
  }

  public static void printGrid(int[][] grid) {
    for (int[] row : grid) {
      for (int item : row) {
        System.out.print(item + ", ");
      }
      System.out.println();
    }
  }

  public static void main(String[] args) {
    int[][] grid = new int[][]{
      {1,2,2,3,5},
      {3,2,3,4,4},
      {2,4,5,3,1},
      {6,7,1,4,5},
      {5,1,1,2,4}
    };
    printGrid(grid);
    div(grid);
  }
}