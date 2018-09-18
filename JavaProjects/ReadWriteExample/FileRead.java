import java.util.*;
import java.io.*;

public class FileRead{
    public static void main(String[] args){
        String fileName = "data.txt";
        String line = null;

        try{
            FileReader FR = new FileReader(fileName);
            BufferedReader BR = new BufferedReader(FR);
            while((line = BR.readLine()) != null){
                System.out.println(line);
            }
            BR.close();
        }
        catch(FileNotFoundException E){
            String msg = "Unable To Open File: " + fileName;
            print(msg);
        }
        catch(IOException E){
            String msg = "Error Reading File: " + fileName;
            print(msg);
            E.printStackTrace();
        }
    }

    public static String input(){
        Scanner scan = new Scanner(System.in);
        String currentInput = scan.nextLine();
        return currentInput;
    }

    public static void print(String S){
        System.out.println(S);
    }
}
