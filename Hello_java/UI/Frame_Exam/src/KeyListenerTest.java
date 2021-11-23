
import java.awt.List;
import java.awt.Panel;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
 
import javax.swing.*;
 
public class KeyListenerTest extends JFrame {
 
    public KeyListenerTest() {
 
        setTitle("눌린 키 확인");
        setSize(200, 200);
        setVisible(true);
 
        Panel p = new Panel();
        List l = new List(5); // List에 focus를 주기위함.
        p.add(l);
        add(p);
 
        l.addKeyListener(new KeyListener() { // List에 액션리스너를 달음.
 
            public void keyTyped(KeyEvent e) {
                System.out.println(e.getKeyChar()+" keyTyped key");
                
            }
 
            @Override
            public void keyReleased(KeyEvent e) {
                //System.out.println(e.getKeyCode()+" keyReleased key2");
                System.out.println(e.getKeyChar()+" keyReleased key");
            }
 
            // 모든 키에 반응하지만 대소문자 구분을 못한다.
            public void keyPressed(KeyEvent e) {
                //System.out.println(e.getKeyCode()+" preesed key2");
                System.out.println(e.getKeyChar()+" preesed key");
            }
        });
 
    }
 
    public static void main(String[] args) {
        new KeyListenerTest();
    }
 
}
 