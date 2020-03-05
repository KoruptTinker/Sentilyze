package GUI;
import java.sql.*;
import java.sql.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.WindowAdapter;
import java.io.IOException;
import java.awt.event.WindowEvent;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.naming.spi.DirStateFactory.Result;
import javax.swing.*;
import java.sql.*;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import javax.swing.Timer;
public class menu {
	JFrame mainFrame ;
	static String searches;
	public Connection con;
	public Statement st;
	public ResultSet rs;
	public menu() {
		gui();
	}
	
		
	
	public static void main(String args[]) {
		new menu();
		
	}
	
	public void gui() {
		JFrame mainFrame = new JFrame("Menu");
		mainFrame.setSize(400, 400);
		mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		JPanel controlPanel = new JPanel(new GridBagLayout());
		GridBagConstraints gbc  = new GridBagConstraints();
		controlPanel.setSize(400,400);
		
		//
		//Frame colours from here
		//
		controlPanel.setBackground(Color.white);
		mainFrame.addWindowListener(new WindowAdapter() {
			public void windowClosing() {
				System.exit(0);
			}
		});
		mainFrame.setLocationRelativeTo(null);
		
		JMenuBar menu = new JMenuBar();
		
		JMenu file = new JMenu("File");
		menu.add(file);
		JMenuItem clear =  new JMenuItem("Clear");
		file.add(clear);
		
		clear.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				try{
			  		con = DriverManager.getConnection("jdbc:mysql://localhost:3306/sentilyzer","root","password");
			  		String cls = "truncate table searches";
			  		st = con.createStatement();
			  		int rs = st.executeUpdate(cls);
			  		
			  	}catch(Exception ex){
			  		System.out.println("Error:" + ex);
				  }
				  try{
					con = DriverManager.getConnection("jdbc:mysql://localhost:3306/sentilyzer","root","password");
					String cls = "truncate table results";
					st = con.createStatement();
					int rs = st.executeUpdate(cls);
					
				}catch(Exception ex){
					System.out.println("Error:" + ex);
				}
			}
		});
		
		JMenuItem exit = new JMenuItem("Exit");
		file.add(exit);
		
		mainFrame.setJMenuBar(menu);
		exit.addActionListener(new ActionListener() {
			
			public void actionPerformed(ActionEvent e) {
				System.exit(0);
			}
			
		});
				
		gbc.insets = new Insets(10,10,10,10);
		JLabel userLabel = new JLabel("Enter your search query: ");
		final JTextField userText = new JTextField(6); 
		
		
		
		JButton searchbyhash = new JButton("Search by hashtag");
		
		
		
		JButton searchbyuser = new JButton("Search by user");
		
		//search by hash function
		searchbyhash.addActionListener(new ActionListener() {
		
			public void actionPerformed(ActionEvent e) {
				
				JOptionPane.showMessageDialog(null, "Please wait while your request completes. It may take upto 35 seconds.");
				
				//query input stored in variable "x"
				String x = userText.getText();
				searches = x;
				
				
				//storing queries in a table
				try {
					con = DriverManager.getConnection("jdbc:mysql://localhost:3306/sentilyzer","root","password");
					String query = "Insert into searches (search) values(?)";
					PreparedStatement  prepst = con.prepareStatement(query);
					prepst.setString(1, userText.getText());
					
					prepst.execute();
					con.close();
						
				}catch(Exception ex){
					System.out.println("Error:" + ex);
				}
				
				
				//calling twitter_api.py
				try{
					Process p= Runtime.getRuntime().exec("python M:\\Project\\hashRunner.py");
			}
			catch(IOException except){
				System.out.println("Error in loading twitter_api"+e);
			}
				
				//
				//Change delay here
				//
				try {
	                   Thread.sleep(35000);
	              } catch(InterruptedException ex) {
	                   Thread.currentThread().interrupt();
	              }
				
				new ex3();
				
		}
		});
		
				
		
		//search by user function
		searchbyuser.addActionListener(new ActionListener() {
			
			public void actionPerformed (ActionEvent e) {
				
				JOptionPane.showMessageDialog(null, "Please wait while your request completes. It may take upto 25 seconds.");
				
				//query input stored in variable "query"
				String x = userText.getText();
				searches = x;
				
				try {
					con = DriverManager.getConnection("jdbc:mysql://localhost:3306/sentilyzer","root","password");
					String query = "Insert into searches (search) values(?)";
					PreparedStatement  prepst = con.prepareStatement(query);
					prepst.setString(1, userText.getText());
					
					prepst.execute();
					con.close();
						
				}catch(Exception ex){
					System.out.println("Error:" + ex);
				}
				try{
					Process p= Runtime.getRuntime().exec("python M:\\Project\\userRunner.py");
					
			}
			catch(IOException except){
				System.out.println(e);
				
			}
				
				//
				//Change delay here
				//
				try {
	                   Thread.sleep(25000);
	              } catch(InterruptedException ex) {
	                   Thread.currentThread().interrupt();
	              }
				new ex3();
				
			}
		
			
		});
		//
		//Change button colours here
		//
		searchbyhash.setBackground(Color.MAGENTA);
		searchbyuser.setBackground(Color.MAGENTA);
		gbc.gridx = 0;
		gbc.gridy = 0;
		controlPanel.add(userLabel);
		controlPanel.add(userText);
		gbc.gridx = 0;
		gbc.gridy = 5;
		controlPanel.add(searchbyhash,gbc);
		gbc.gridx = 1;
		gbc.gridy = 5;
		controlPanel.add(searchbyuser,gbc);
		
		
		mainFrame.add(controlPanel);
//		mainFrame.pack();
		mainFrame.setVisible(true);
				
	}
}
