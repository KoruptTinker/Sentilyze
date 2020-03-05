package GUI;
import java.awt.*;
import javax.naming.spi.DirStateFactory.Result;
import javax.swing.*;
import java.sql.*;

public class ex3 {
	public static Connection con;
	public static Statement st;
	public static ResultSet rs;
	public static double percent; 
	public static double percentminus;
	
	
	
   public static void main(String args[]) {
	   new ex3();
   }
   public ex3() {
  //    frame.getContentPane().add(new MyComponent());
      try{
    	 JLabel rsLabel = new JLabel("");
    	JFrame frame = new JFrame();
  		con = DriverManager.getConnection("jdbc:mysql://localhost:3306/sentilyzer","root","password");
  		String query = "SELECT result FROM results ORDER BY ID DESC LIMIT 1";
  		st = con.createStatement();
  		rs = st.executeQuery(query);
  		
  		while(rs.next()) {
  			
  			String s = rs.getString("result");
  			double d=Double.parseDouble(s);
  			System.out.println(d);
  			rsLabel.setText(rs.getString("result"));
  			percent = d;
  			percentminus = 100-percent;
  			frame.getContentPane().add(new MyComponent());
  			frame.setSize(400, 400);
  	        frame.setVisible(true);
  	        rsLabel.setText("Positivity % - " +percent);
  	        frame.add(rsLabel);
  			System.out.println(percent);
  			System.out.println(percentminus);
  		}
  	}catch(Exception ex){
  		System.out.println("Error:" + ex);
  	}
 
      
   }


   

}

class Slice {
	public Connection con;
	public Statement st;
	public ResultSet rs;
	
   double value;
   Color color;
   public Slice(double value, Color color) {  
      this.value = value;
      this.color = color;
   }
}

class MyComponent extends JComponent {
	


Slice[] slices = {new Slice(ex3.percent, Color.red), new Slice(ex3.percentminus, Color.black)};
//Slice[] slices = {new Slice(58, Color.red), new Slice(42, Color.black)};
   MyComponent() {}
   public void paint(Graphics g) {
      drawPie((Graphics2D) g, getBounds(), slices);
      super.paint(g);
      g.setColor(Color.red);
      g.drawString("Positive - Red", 250, 50);
      g.setColor(Color.black);
      g.drawString("Negative - Black", 250, 100);
   }
   void drawPie(Graphics2D g, Rectangle area, Slice[] slices) {
      double total = 0.0D;
      
      for (int i = 0; i < slices.length; i++) {
         total += slices[i].value;
      }
      double curValue = 0.0D;
      int startAngle = 0;
      for (int i = 0; i < slices.length; i++) {
         startAngle = (int) (curValue * 360 / total);
         int arcAngle = (int) (slices[i].value * 360 / total);
         g.setColor(slices[i].color);
         g.fillArc(0, 0, 150, 150, startAngle, arcAngle);
         curValue += slices[i].value;
      }
     
   

   } 
}
