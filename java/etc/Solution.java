import java.util.ArrayList;

class Solution {
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

  public static class Pair {
    public final int x;
    public final int y;
    public Pair(int x, int y) {
      this.x = x; this.y = y;
    }
  }

  // grid an m x n rect (height x width)

  public static void flowAtlantic(Point[][] points) {
    int height = points.length;
    int width = points[0].length;
    // Move the north edge south, then move the west edge east
    int furthestEdge = 0;
    // move north edge to the bottom
    // opt: stop early when perimeter doesn't move
    while (furthestEdge < height) {
      Point[] rowAbove = null;
      if (furthestEdge > 0) {
        rowAbove = points[furthestEdge - 1];
      }

      Point[] row = points[furthestEdge];
      for (int pt_in_row_index = 0; pt_in_row_index < width; pt_in_row_index++) {
        Point current_point = row[pt_in_row_index];
        // perimeter always touches
        if (furthestEdge == 0) {
          current_point.reachesAtl = true;
          continue;
        }
        if (rowAbove != null) {
          Point point_above = rowAbove[pt_in_row_index];
          if (point_above.reachesAtl && point_above.value < current_point.value) {
            current_point.reachesAtl = true;
          }
        }
      }

      // Move west edge to the east
      for (int pt_in_col_index = furthestEdge; pt_in_col_index < height; pt_in_col_index++) {
        Point current_point = points[pt_in_col_index][furthestEdge];
        // perimeter touches
        if (furthestEdge == 0) {
          current_point.reachesAtl = true;
          continue;
        }
        Point point_left = points[pt_in_col_index][furthestEdge - 1];
        if (point_left.reachesAtl && point_left.value < current_point.value) {
          current_point.reachesAtl = true;
        }
      }
      furthestEdge++;
    }
  }

  public static void flowPacific(Point[][] points) {
    int height = points.length;
    int width = points[0].length;
    // Move the south edge north, then move the east edge west
    int furthestEdge = height - 1;
    // move south edge to the top
    // opt: stop early when perimeter doesn't move
    while (furthestEdge >= 0) {
      Point[] rowBelow = null;
      if (furthestEdge < height - 1) {
        rowBelow = points[furthestEdge + 1];
      }

      Point[] row = points[furthestEdge];
      for (int pt_in_row_index = 0; pt_in_row_index < width; pt_in_row_index++) {
        Point current_point = row[pt_in_row_index];
        // perimeter always touches
        if (furthestEdge == height - 1) {
          current_point.reachesPac = true;
          continue;
        }
        if (rowBelow != null) {
          Point point_below = rowBelow[pt_in_row_index];
          if (point_below.reachesPac && point_below.value < current_point.value) {
            current_point.reachesPac = true;
          }
        }
      }

      // Move east edge to the west
      for (int pt_in_col_index = furthestEdge; pt_in_col_index >= 0; pt_in_col_index--) {
        Point current_point = points[pt_in_col_index][furthestEdge];
        // perimeter touches
        if (furthestEdge == height - 1) {
          current_point.reachesPac = true;
          continue;
        }
        Point point_right = points[pt_in_col_index][furthestEdge + 1];
        if (point_right.reachesPac && point_right.value < current_point.value) {
          current_point.reachesPac = true;
        }
      }
      furthestEdge--;
    }
  }

  public static ArrayList<Pair> getSolutions(Point[][] points) {
    ArrayList<Pair> solutions = new ArrayList<>();
    for (int row = 0; row < points.length; row++) {
      for (int col = 0; col < points[0].length; col++) {
        if (points[row][col].reachesAtl && points[row][col].reachesPac) {
          solutions.add(new Pair(row, col));
        }
      }
    }
    return solutions;
  }

  public static ArrayList<Pair> div(int[][] grid) {
    if (grid.length <= 0) {
      return new ArrayList<Pair>();
    }

    int m = grid.length;
    int n = grid[0].length;
    Point[][] points = new Point[m][n];

    for (int row = 0; row < m; row++) {
      for (int col = 0; col < n; col++) {
        points[row][col] = new Point(grid[row][col]);
      }
    }

    flowAtlantic(points);
    flowPacific(points);

    // for (int row = 0; row < m; row++) {
    //   for (int col = 0; col < n; col++) {
    //     flow(points, row, col, m, n);
    //   }
    // }
    ArrayList<Pair> solutions = getSolutions(points);
    printPts(points);
    return solutions;
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

  public static void printSolutions(ArrayList<Pair> solutions) {
    for (Pair p : solutions) {
      System.out.print("(" + p.x + ", " + p.y + ")");
    }
    System.out.println();
  }

  public static void main(String[] args) {
    // int[][] grid = new int[][]{
    //   {1,2,2,3,5},
    //   {3,2,3,4,4},
    //   {2,4,5,3,1},
    //   {6,7,1,4,5},
    //   {5,1,1,2,4}
    // };
    // int[][] grid = new int[][]{
    //   {4, 3},
    //   {2, 1}
    // };
    int[][] grid = new int[][]{
      {5, 7, 12},
      {0, 1, 8},
      {2, 9, 3}
    };
    printGrid(grid);
    ArrayList<Pair> solutions = div(grid);
    printSolutions(solutions);
  }
}