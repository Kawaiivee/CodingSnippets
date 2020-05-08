public class Tests{
	public static void main(String[] args){
		LinkedListTest();
	}

	public static void LinkedListTest(){
		MyLinkedList LL = new MyLinkedList();
		LL.insert(2);
		LL.insert(4);
		LL.insert(6);
		LL.print();
	}
}
