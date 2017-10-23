from java.awt import BorderLayout, Color, Dimension, Graphics, Graphics2D, Point, Polygon, Shape, RenderingHints
from java.awt.event import ActionEvent, ActionListener, MouseAdapter, MouseEvent, MouseListener, MouseMotionListener
from javax.swing import JButton, JFrame, JLabel, JPanel, SwingConstants
from javax.swing.border import LineBorder

frame = JFrame("ElectriPy")
prompt = JLabel("Add a component")
components = []
lines = []
drawpanel = DrawPanel()
showInputs = True
showOutputs = True
addingComponent = False
selectingOutput = False
selectingInput = False

