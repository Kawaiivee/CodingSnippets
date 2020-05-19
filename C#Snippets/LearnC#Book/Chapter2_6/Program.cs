using System;
using System.Collections.Generic;
using System.Xml;

namespace Chapter2_6
{
    class Program
    {
        static void Main(string[] args) //command line arguments
        {
            //myByte is declared
            byte myByte;

            //byte is 0 to 255 -- initialized
            myByte = 7;

            //int is -2147483648 to 2147483647
            int myInt = 2000000;

            //float is 8 bytes of storage for decimal point values  -- approximately 7 digits accuracy --- use suffix F
            float myFloat = 123.4567F;

            //double is more exact -- values between +-5.0x10^(-324) to +-1.7x10^(308) --- values get set to double if there is a floating point by default
            double myDouble = 123.456789101112131415;

            //decimal is even more exact -- 28 to 29 digits --- use suffix M ---- notice how the last '20' digits get cut off
            decimal myDecimal = 123.4567891011121314151617181920M;

            //single character --- use '
            char myChar = 'A';

            //string is multiple characters --- use "
            string myString = "Ramir";

            //bool is true or false
            bool myBool = true;

            //Just a conditiona
            Console.WriteLine(
                myByte.ToString() + "\n" +
                myInt.ToString() + "\n" +
                myFloat.ToString() + "\n" +
                myDouble.ToString() + "\n" +
                myDecimal.ToString() + "\n" +
                myChar + "\n" +
                myString + "\n" +
                myBool.ToString() + "\n"
            );

            //typecasting is the same (<datatype>)

            //OPERATORS!
            //int sum = 1 + 1;                //2
            //int dif = 1 - 1;                //0
            //int product = 2 * 3;            //6
            //int quotient_1 = 7 / 2;         //3
            //double quotient_2 = 7 / 2;      //3.0
            //double quotient_3 = 7.0 / 2;    //3.5
            //double quotient_4 = 7 / 2.0;    //3.5
            //double quotient_5 = 7.0 / 2.0;  //3.5
            //int mod = 7 % 2;                //1
            //sum++;                          //3 --- sum = sum + 1
            //dif--;                          //-1 -- dif = dif + 1

            //ARRAY TIME!

            //init and declare
            int[] integers = { 1, 2, 3, 5, 8 };

            //init and declare separately
            char[] chars;
            chars = new[] { 'R', 'A', 'M', 'I', 'R' };

            //arrays come with cool properties like arr.length for the number of elements or arr.copy() to return a copy of the array (so we dont have to iterate ourselves)
            int[] source = { 12, 1, 5, -2, 16, 14 };
            int[] dest = { 1, 2, 3, 4 };

            //static usage -- Array.Copy(source, dest, 3); --- first 4 items ----- source, dest, 3 picks elements indexed at 0, 1, 2, 3 in source to dest
            Array.Copy(source, dest, 3);

            //static usage -- Array.Sort(arr) sorts the elements in arr
            Array.Sort(source);
            Array.Sort(dest);

            Console.WriteLine(
                source.ToString() + "\n" +
                dest.ToString() + "\n"
            );

            //static usage -- Array.IndexOf(dest, 21); --- returns first index of element if found, if not returns -1
            int pos_1 = Array.IndexOf(integers, 5);     //3
            int pos_2 = Array.IndexOf(integers, 13);    //-1
            int pos_3 = Array.IndexOf(chars, 'R');      //0

            Console.WriteLine(
                pos_1.ToString() + "\n" + pos_2.ToString() + "\n" + pos_3.ToString() + "\n"
            );

            //string methods -- properties (like Length) and methods like Substring()
            string str_1 = "Ramir";
            string str_2 = "Agu";

            Console.WriteLine((str_1.Length).ToString());
            Console.WriteLine((str_2.Length).ToString());

            string str_3 = str_1.Substring(1, 3);       //"ami"
            string str_4 = "ami";

            Console.WriteLine(str_3);
            Console.WriteLine(str_4);

            bool b = str_3.Equals(str_4);
            if (b)
            {
                Console.WriteLine("Strings Are Equal");
            }
            else
            {
                Console.WriteLine("Strings Are Inequal");
            }

            //split method is cool for parsing through strings
            string names = "Peter, John; Andy, , David";
            string[] separator = { ", ", "; "};             //literal comma-space and semicolon-space separators -- could have more custom ones
            string[] substrings = names.Split(separator, StringSplitOptions.None);      //There are more string split options like ~.RemoveEmpty Entries (like between Andy and David there is an extra value)

            Console.WriteLine("Note how the literal SPACE value from names array gets its own line");
            Console.WriteLine("-----------");

            for (int i = 0; i < substrings.Length; i++)
            {
                Console.Write(substrings[i] + "\n");
            }

            Console.WriteLine("-----------");
            Console.WriteLine("\n");

            //First Data Structure --- List
            List<int> newEmptyListOfInts = new List<int>();         //list of numbers initialized as empty
            List<int> numList = new List<int> { 11, 21, 31, 41 };   //list of numbers inited and declared with starting values

            numList.Add(51);    //appends 51 to the end of the numList
            int numListCount = numList.Count;       //Count property for number of elements in numList
            numList.Insert(2, 51);      //Inserts 51 as the new element at index 2 (31 and so on get shifted right)
            numList.Remove(51);         //Removes the FIRST instance of 51 that is seen
            numList.RemoveAt(0);        //Removes the element at the GIVEN index -- index 0 is 11
            numList.Contains(21);       //Returns true if numList contains the element 21, false if it doesnt
            numList.Clear();           //removes all elements from the list

            // value vs reference types -- examples: strings are reference data types, ints are value data types

            // Output -- Could write in the beginning with 'using static System.Console' <- then we could just used WriteLine() or Write()  without Console object
            Console.Write("Hello, ");                 //Does not move the cursor to the next line while printing
            Console.WriteLine("How Are You");       //New line for cursor

            //Could also do really cool string formatted things like this with {n}
            string name = "Ramir";              //string format string
            int score = 87;                     //int score
            float acc_score = 87.123456F;       //really cool usage in the string format == F3 makes it 3 after the decimal
            float money = 17.3777777F;          //use C to make this one into money
            Console.WriteLine(
                "Hello {0}!!! You scored {1} on your exam! It was exactly {2:F3}. That's worth {3:C}!",
                name, score, acc_score, money
            );

            // Escape sequences \n , \t , \ for literal, etc
            Console.WriteLine("I\tam \n 5'10\" tall. \n");

            // Input -- Console.Read() Stuff -- PARSING with Convert.ToInt32(). Convert.ToDecimal(), Convert.ToSingle(), Convert.ToDouble()
            Console.WriteLine("Enter an integer: ");
            int numUserInput = Convert.ToInt32(Console.ReadLine());
            numUserInput++;
            Console.WriteLine(numUserInput.ToString() + " + 1 = " + numUserInput.ToString());

            //Control Flow
            Console.WriteLine("Enter an integer for age: ");
            int ageInput = Convert.ToInt32(Console.ReadLine());
            if ( ageInput < 21 || ageInput > 100)
            {
                Console.WriteLine("Invalid Age");
                Console.WriteLine("Age must be between 0 and 100");
            }
            else if (ageInput < 21)
            {
                Console.WriteLine("Sorry, you are under-age.");
            }
            else if (ageInput > 100)
            {
                Console.WriteLine("Sorry, you are over-age.");
            }
            else
            {
                Console.WriteLine("You are the correct age.");
            }

            //ternary expression also exists
            //int result = x > y ? 1 : 0;       result is 1 if true and 0 if false

            //switch case
            Console.WriteLine("Pick a number from 1-100: ");
            int val = Convert.ToInt32(Console.ReadLine());
            char grade;
            switch (val)
            {
                case int n when (n >= 90):
                    grade = 'A';
                    break;
                case int n when (n >= 80):
                    grade = 'B';
                    break;
                case int n when (n >= 70):
                    grade = 'C';
                    break;
                case int n when (n >= 60):
                    grade = 'D';
                    break;
                case int n when (n < 60 ):
                    grade = 'E';
                    break;
                default:
                    grade = '?';
                    break;
            }
            Console.WriteLine("Grade is: " + grade + "\n");

            //forloop
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine("Line: " + i.ToString());
            }

            //foreach loop
            char[] letters = {'A', 'B', 'C'};
            foreach (char c in letters)
            {
                Console.WriteLine(c);
            }

            //while loop -- do while also exists
            bool flag = true;
            while (flag)
            {
                Console.WriteLine("\nFlag is initially " + flag + "\nNow flipping it to break from while loop\n");
                flag = !flag;
            }

            int[] arr = { 1, 2, 3, 4, 5};
            foreach (int i in arr)
            {
                Console.WriteLine("Gonna skip if i == 2");
                if (i == 2) continue;
                if (i == 4) break;
                Console.WriteLine("i is {0}", i);
            }

            //exception handling -- try catch finally ----divide by zero example
            int numerator, denominator;

            Console.WriteLine("Please enter the numerator: ");
            numerator = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Please enter the denominator: ");
            denominator = Convert.ToInt32(Console.ReadLine());

            try
            {
                double quo = numerator / denominator ;
                Console.WriteLine("The result is: " + quo.ToString());
            }
            catch (Exception e)     //generic exception, you can make custom ones too -----Could do array example IndexOutOfRangeException specific object
            {
                Console.WriteLine(e.Message);       //message property of the thrown exception --- zero division
            }
            finally
            {
                Console.WriteLine("End of Error Handling Example");
            }
        }
    }
}
