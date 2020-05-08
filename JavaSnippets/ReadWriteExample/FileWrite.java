import java.util.*;
import java.io.*;

public class FileWrite{
    public static void main(String[] args){
        String fileName = "data.txt";
        print("Start writing lines!\n<Enter> for next line\n<exit> to exit\n<abort> to abort");
        try{
            FileWriter FW = new FileWriter(fileName);
            BufferedWriter BW = new BufferedWriter(FW);

            String currentLine = null;
            while(!(currentLine = input()).equals("exit")){
                if(currentLine.equals("abort")){
                    print("Discarding Data(Erased Past Data)...");
                    System.exit(0);
                }
                currentLine = currentLine + "\n";
                BW.write(currentLine);
            }
            print("Saving Data...");
            BW.close();
        }
        catch(IOException E){
            E.printStackTrace();
        }
    }

    static Scanner scan = new Scanner(System.in);
    public static String input(){
        String str;
        str = scan.nextLine();
        //str = str + "\n";
        return str;
    }

    public static void print(String str){
        System.out.println(str);
    }
}
