public class MyLinkedList{
    class Node{
        Node prev;
        Node next;
        int data;
        public Node(int d){
            data = d;
        }
    }

    public Node head;
    public Node tail;
    private int size = 0;

    public int size(){
        return size;
    }

    public void insert(int d){
        Node newNode = new Node(d);
        if(this.head == null){
            this.head = newNode;
            this.head.next = this.tail;
        }
        else{
            if(this.head.next == null){
                newNode.prev = this.head;
                this.head.next = newNode;
                this.tail = newNode;
            }
            else{
                this.tail.next = newNode;
                newNode.prev = this.tail;
                this.tail = newNode;
            }
        }
        this.size++;
    }

    public void print(){
        Node currNode = this.head;
        while(currNode != null){
            System.out.println(currNode.data);
            currNode = currNode.next;
        }
    }
}
