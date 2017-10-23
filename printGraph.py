from javax.swing import *
from java.awt import BorderLayout
fro mjava.awt import *
import java.awt.event.ActionListener   
import java.awt.event.ActionEvent 	

frame = JFrame("Electripy-Circuit Solver and Simulator")
btnPnl = JPanel(FlowLayout(FlowLayout.CENTER))
components = []
temp_res = {}
pane=JPanel()
    
class Example:

    def add_res(self,event):
        pane.removeAll()
        self.disp1=JLabel("Enter Value of Resistance")
        self.val1 = JTextField(15)
        self.node1 = JLabel("Enter node 1")
        self.val2=JTextField(15)
        self.node2=JLabel("Enter node 2")
        self.val3= JTextField(15)
        self.submit=JButton('Submit',actionPerformed=self.removing)
        self.comp='r'
        self.freq=0
        self.phase=0
        pane.add(self.disp1)
        pane.add(self.val1)
        pane.add(self.node1)
        pane.add(self.val2)
        pane.add(self.node2)
        pane.add(self.val3)
        pane.add(self.submit)
        SwingUtilities.updateComponentTreeUI(frame)
        frame.add(pane)
        SwingUtilities.updateComponentTreeUI(frame)
        frame.setVisible(True)

    def add_capac(self,event):
        pane.removeAll()
        self.disp1=JLabel("Enter value of Capacitance")
        self.val1 = JTextField(15)
        self.node1 = JLabel("Enter node 1")
        self.val2=JTextField(15)
        self.node2=JLabel("Enter node 2")
        self.val3= JTextField(15)
        self.submit=JButton('Submit',actionPerformed=self.removing)
        self.comp='c'
        self.freq=0
        self.phase=0
        pane.add(self.disp1)
        pane.add(self.val1)
        pane.add(self.node1)
        pane.add(self.val2)
        pane.add(self.node2)
        pane.add(self.val3)
        pane.add(self.submit)
        frame.add(pane)
        SwingUtilities.updateComponentTreeUI(frame)
        frame.setVisible(True)

    def add_ind(self,event):
        pane.removeAll()
        self.disp1=JLabel("Enter value of inductor")
        self.val1=JTextField(15)
        self.node1=JLabel("Enter node 1")
        self.val2=JTextField(15)
        self.node2=JLabel("Enter node 2")
        self.val3=JTextField(15)
        self.submit=JButton('Submit',actionPerformed=self.removing)
        self.comp='i'
        self.freq=0
        self.phase=0
        pane.add(self.disp1)	
        pane.add(self.val1)
        pane.add(self.node1)
        pane.add(self.val2)
        pane.add(self.node2)
        pane.add(self.val3)
        pane.add(self.submit)
        frame.add(pane)
        SwingUtilities.updateComponentTreeUI(frame)
        frame.setVisible(True)

    def v_dc(self,event):
        pane.removeAll()
        self.disp1=JLabel("Enter Magnitude of DC Voltage")
        self.val1=JTextField(15)
        self.node1=JLabel("Enter node 1")
        self.val2=JTextField(15)
        self.node2=JLabel("Enter node 2")
        self.val3=JTextField(15)
        self.submit=JButton('Submit',actionPerformed=self.removing)
        self.comp='vdc'
        self.freq=0
        self.phase=0
        pane.add(self.disp1)	
        pane.add(self.val1)
        pane.add(self.node1)
        pane.add(self.val2)
        pane.add(self.node2)
        pane.add(self.val3)
        pane.add(self.submit)
        frame.add(pane)
        SwingUtilities.updateComponentTreeUI(frame)
        frame.setVisible(True)

    def v_ac(self,event):
        pane.removeAll()
        self.disp1=JLabel("Enter Magnitude of AC Voltage")
        self.val1=JTextField(15)
        self.node1=JLabel("Enter node 1")
        self.val2=JTextField(15)
        self.node2=JLabel("Enter node 2")
        self.val3=JTextField(15)
        self.frequency=JLabel("Enter Frequency")
        self.a=JTextField(15)
        self.theta1=JLabel("Enter Phase Value")
        self.b=JTextField(15)
        self.submit=JButton('Submit',actionPerformed=self.removing)
        self.comp='vac'
        pane.add(self.disp1)	
        pane.add(self.val1)
        pane.add(self.node1)
        pane.add(self.val2)
        pane.add(self.node2)
        pane.add(self.val3)
        pane.add(self.frequency)
        pane.add(self.a)
        pane.add(self.theta1)
        pane.add(self.b)
        pane.add(self.submit)
        frame.add(pane)
        SwingUtilities.updateComponentTreeUI(frame)
        frame.setVisible(True)

    def __init__(self):
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH)
        frame.setLayout(BorderLayout())
        res = JButton('resisitor',actionPerformed=self.add_res)
        capac = JButton('capacitor',actionPerformed=self.add_capac)
        button = JButton('Create Circuit')
        ind = JButton('inductor',actionPerformed=self.add_ind)
        source1 = JButton('DC source',actionPerformed=self.v_dc)
        source2 = JButton('AC source',actionPerformed=self.v_ac)
        btnPnl.add(source1);
        btnPnl.add(source2);	
        btnPnl.add(res);
        btnPnl.add(capac);
        btnPnl.add(ind);
        btnPnl.add(button)
        frame.add(btnPnl, BorderLayout.SOUTH);
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
        frame.setVisible(True)

    def removing(self,event):
        if self.comp=='vac':
            r=[self.comp,float(self.val1.getText()),str(self.val2.getText()),str(self.val3.getText()),float(self.a.getText()),float(self.b.getText())]
        else:
            r=[self.comp,float(self.val1.getText()),str(self.val2.getText()),str(self.val3.getText()),self.freq,self.phase]
        components.append(r)
        pane.removeAll()
        frame.remove(pane)
        SwingUtilities.updateComponentTreeUI(frame)
        frame.setVisible(True)
       
if __name__ == '__main__':
    Example()