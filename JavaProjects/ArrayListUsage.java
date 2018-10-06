import MyPackage.Person;
import MyPackage.Student;

import java.util.*;

public class ArrayListUsage{
    public static void main(String[] args){
        Person P1 = new Person("Kurt", "Vonnegut");
        Person P2 = new Person("Ray", "Bradbury");
        Person P3 = new Person("Haruki", "Murakami");
        Person P4 = new Person("George", "Orwell");
        Student P5 = new Student("Ender", "Wiggins", "Battle School", 4.0f, 'A');
        Student P6 = new Student("Gregory", "Heffley", "Elementary School", 2.0f, 'C');

        ArrayList<Person> list = new ArrayList();
        Person[] array = {P1, P2, P3, P4, P5, P5, P6};
        String[] fullName = new String[7];
        int count = 0;

        for(Person p : array){
            fullName[count] = p.getFirstName();
            list.add(p);
            count++;
        }

        for(int i = 0; i < 5; i++){
            fullName[i] = fullName[i] + " " + array[i].getLastName();
            display(fullName[i]);
        }

        for(Person p : array){
            display(p.toString());
        }
    }

    public static void display(String s){
        System.out.println(s);
    }
}
