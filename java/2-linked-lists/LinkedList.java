public class LinkedList {
  public int item;
  public LinkedList next;
  LinkedList(int item) {
    this.item = item;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    LinkedList current = this;
    while (current != null) {
      s.append(current.item).append(", ");
      current = current.next;
    }
    return s.substring(0, s.length() - 2).toString();
  }

  public static void main(String[] args) {
    LinkedList t = new LinkedList(5);
    t.next = new LinkedList(55);
    System.out.println(t.toString());
  }
}