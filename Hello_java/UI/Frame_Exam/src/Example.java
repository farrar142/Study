import javax.swing.*;
import java.awt.*;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
public class Example extends JFrame {

    public static void main(String[] args)
    {
        Dimension res = Toolkit.getDefaultToolkit().getScreenSize(); //
        //윈도우 설정
        JFrame frame = new JFrame("KeyListener Test");
        frame.setLocation(500,400);
        frame.setSize(res.width/4,res.height/4);
        //구성물 1
        JTextField textfield1 = new JTextField();
        textfield1.setText("Key log");
        textfield1.setToolTipText("show keys");
        //구성물 2
        JLabel label1 = new JLabel();
        label1.setText("this is label");

        //입력 이벤트
        KeyListener klObj = new KeyListener() {
            public void keyTyped(KeyEvent e){
                System.out.println(e.getKeyChar()+" keyTyped key");
            }
            public void keyReleased(KeyEvent e){
                System.out.println(e.getKeyChar()+" keyReleased key");
            }
            public void keyPressed(KeyEvent e){
                System.out.println(e.getKeyChar()+" preesed key");
            }
        };

        textfield1.addKeyListener(klObj);

        //레이아웃 설정
        frame.add(textfield1, BorderLayout.CENTER);
        frame.pack();
        frame.setVisible(true);
    }
}
 