package MyPackage;

public class Person{
    String firstName;
    String lastName;
    static int currentid = 0;
    int id;
    public Person(){
        firstName = "";
        lastName = "";
        id = currentid;
        currentid++;
    }

    public Person(String fn, String ln){
        firstName = fn;
        lastName = ln;
        id = currentid;
        currentid++;
    }

/*--------------------------------*/
    public String getFirstName(){
        return firstName;
    }

    public String getLastName(){
        return lastName;
    }

    public int getId(){
        return id;
    }

/*--------------------------------*/
    public void setFirstName(String fn){
        firstName = fn;
    }

    public void setLastName(String ln){
        lastName = ln;
    }

    public void setId(int i){
        id = i;
    }

/*--------------------------------*/
    public String toString(){
        String str = "First Name is: " + this.getFirstName() + "\nLast Name is: " + this.getLastName() + "\nID is: " + this.getId();
        return str;
    }
}
