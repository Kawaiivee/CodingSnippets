package MyPackage;
import MyPackage.Person;
import java.util.*;

public class Student extends Person{
    String major;
    float gpa;
    char grade;
/*--------------------------------*/
    public Student(String firstName, String lastName, String maj, float g, char gr){
        super(firstName, lastName);
        major = maj;
        gpa = g;
        grade = gr;
    }
/*--------------------------------*/
    public String getMajor(){
        return major;
    }

    public float getGpa(){
        return gpa;
    }

    public char getGrade(){
        return grade;
    }
/*--------------------------------*/
    public void setMajor(String m){
        major = m;
    }

    public void setGpa(float g){
        gpa = g;
    }

//    public void setGrade(char g){
//        grade = g;
//    } Not using this because I wanted to make the letter grade calculated off of the gpa
/*--------------------------------*/
    public String toString(){
        String str = super.toString() + "\nMajor is: " + this.getMajor() + "\nGPA is: " + this.getGpa() + "\nGrade is: " + this.getGrade();
        return str;
    }
}
