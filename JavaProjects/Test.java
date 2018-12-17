import java.util.*;

public class Test{
	public static void main(String[] args){
		System.out.println("Hello World!");
		printf("Hello World!\n");
		int numArgs = args.length;
		for(int i = args.length; i > 0; i--){
			System.out.println(args[args.length-i]);
		}
		
		Scanner numberScanner = new Scanner(System.in);
		printf("Please provide an int: ");
		int i = numberScanner.nextInt();
		Test T = new Test();
		i = T.plus2(i);
		System.out.print("Your number plus 2 is: " + i);
		System.out.print("Changes");
	}
	
	public static void printf(String s){
		System.out.print(s);
	}

	public int plus2(int x){
		int z = x + 2;
		return z;
	}
}