import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;

public class Magic8Ball{
    public static void main(String[] args){
        GUI();
    }

    public static void GUI(){
        //Creating the Frame
        JFrame frame = new JFrame("Magic8Ball");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(256,80);

        //Text Area
        JTextArea messageBox = new JTextArea();
        messageBox.setEditable(false);        //no adding your own

        //Creating the panel at bottom and adding components
        //SOUTH contentPane
        JPanel msgPanel = new JPanel(); // the panel is not visible in output // accepts up to 10 characters...really just kind of setting length of box here
        JButton shakeButton = new JButton("Shake");
        msgPanel.add(shakeButton);

        shakeButton.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent ae){
                messageBox.setText("Answer: " + shakeBall() + "\n");
            }
        });

        //Placing the components (menuBar, panel, and messageBox on frame)
        frame.getContentPane().add(BorderLayout.SOUTH, msgPanel);
        frame.getContentPane().add(BorderLayout.CENTER, messageBox);
        frame.setVisible(true);
    }

    public static String shakeBall(){
        String[] answerList = {
            "It is certain",
            "It is decidedly so",
            "Without a doubt",
            "Yes - definitely",
            "You may rely on it",
            "As I see it, yes",
            "Most Likely",
            "Outlook Good",
            "Yes",
            "Signs point to yes",
            "Reply hazy, try again",
            "Ask again later",
            "Better not tell you now",
            "Cannot predict now",
            "Concentrate and ask again",
            "Don't count on it",
            "My reply is no",
            "My sources say no",
            "Outlook not so good",
            "Very doubtful"
        };

        String answer = answerList[(int)(Math.random() * answerList.length)];
        return answer;
    }
}
