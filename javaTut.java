//package ok;

import java.util.Scanner;

public class javaTut {

	public static void main(String[] args) {
	
		System.out.println("I am a boy");
		
		
		Integer name= 3;
		System.out.println(name.equals(10));
		System.out.println(name--);
		
		String x="water";
		String y="Juice";
		
		System.out.println("before swap,\tx= "+x+"\ty= "+y);
		
		System.out.println(x + y);
		String z=x;
		x=y;
		y=z;
		System.out.println("After swap,\tx= "+x+"\ty= "+y);

		System.out.println("What is your name?\t");
		Scanner scan = new Scanner(System.in);
		x=scan.nextLine();
		System.out.println("Your name is "+x);
		scan.close();
	}

}
