import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class BasicGUI{
    public static void main(String[] args){
        GUI();
    }

    public static void GUI(){
        //Creating the Frame
        JFrame frame = new JFrame("ECHOBOT GUI");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(360, 480);

        //Creating the menuBar and adding components with menuItems as 'options'
        //NORTH contentPane
        //-----------------------------
        //Still kind of want to find a way to store the menu items in a data structure
        //so that I don't have to hard code each option
        JMenuBar menuBar = new JMenuBar();
        JMenu fileMenu = new JMenu("File");
        JMenu editMenu = new JMenu("Edit");
        JMenu viewMenu = new JMenu("View");
        JMenu preferencesMenu = new JMenu("Preferences");
        JMenu helpMenu = new JMenu("Help");
        JMenu aboutMenu = new JMenu("About");

        menuBar.add(fileMenu);
        menuBar.add(editMenu);
        menuBar.add(viewMenu);
        menuBar.add(preferencesMenu);
        menuBar.add(helpMenu);
        menuBar.add(aboutMenu);

        String[] fileOptions = {"Open", "Save As"};
        String[] editOptions = {"Cut","Copy","Paste"};
        String[] viewOptions = {"Up", "Down"};
        String[] preferencesOptions = {"Configuration", "Style"};

        for(String str : fileOptions){
            fileMenu.add(new JMenuItem(str));
        }
        for(String str : editOptions){
            editMenu.add(new JMenuItem(str));
        }
        for(String str : viewOptions){
            viewMenu.add(new JMenuItem(str));
        }
        for(String str : preferencesOptions){
            preferencesMenu.add(new JMenuItem(str));
        }

        //Text Area
        JTextArea messageBox = new JTextArea();
        messageBox.setEditable(false);        //no adding your own

        //Creating the panel at bottom and adding components
        //SOUTH contentPane
        JPanel msgPanel = new JPanel(); // the panel is not visible in output
        JLabel prompt = new JLabel("Enter Text");
        JTextField inputMsg = new JTextField(10); // accepts up to 10 characters...really just kind of setting length of box here
        JButton sendButton = new JButton("Send");
        JButton resetButton = new JButton("Reset");
        msgPanel.add(prompt);
        msgPanel.add(inputMsg);
        msgPanel.add(sendButton);
        msgPanel.add(resetButton);

        sendButton.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent ae){
                System.out.print(inputMsg.getText() + "\n"); //Testing to see if I actually get the string
                messageBox.append("YOU: " +inputMsg.getText() + "\n");
                System.out.print(inputMsg.getText() + "\n"); //Testing to see if I actually get the string
                messageBox.append("ECHOBOT: " +inputMsg.getText() + "\n");
                prompt.setText("Msg Sent!");
            }
        });

        resetButton.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent ae){
                inputMsg.setText("");
                prompt.setText("Msg Reset!");
            }
        });

        //Placing the components (menuBar, panel, and messageBox on frame)
        frame.getContentPane().add(BorderLayout.NORTH, menuBar);
        frame.getContentPane().add(BorderLayout.SOUTH, msgPanel);
        frame.getContentPane().add(BorderLayout.CENTER, messageBox);
        frame.setVisible(true);
    }
}
