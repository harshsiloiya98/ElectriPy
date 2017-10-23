from java.awt import BorderLayout, Color, Dimension, Graphics, Graphics2D, Point, Polygon, RenderingHints, Shape
from javax.swing import JButton, JFrame, JPanel, JLabel, SwingConstants
from java.awt.event import ActionEvent, ActionListener, MouseAdapter, MouseEvent, MouseListener, MouseMotionListener
from javax.swing.border import LineBorder

showInputs = True
showOutputs = True

def overrides(interface):
	def overrider(method):
		assert(method.__name__ in dir(interface))
		return method
	return overrider

class Component(JLabel):
	__inputs = []
	__outputs = []
	def __init__(self, text, x, y):
		super().__init__(text)
		addMouseListener.__init__(self)
		self.addMouseListener(self)
		self.addMouseMotionListener(self)
	def addOutput(o):
		__outputs.append(o)
	def addInput(i):
		__inputs.append(i)
	@overrides(JLabel)
	def paintComponent(g):
		super().paintConnector(g)
		g2D = Graphics2D(g)
		if (showInputs):
			for x in __inputs:
				x.paintConnector(g2D)
		if (showOutputs):
			for y in __outputs:
				if (y.isAvailable()):
					y.paintConnector(g2D)
	inDrag = False
	startDragX = 0
	startDragY = 0
	@overrides(MouseListener)
	def mousePressed(e):
		startDragX = e.getX()
		startDragY = e.getY()
	@overrides(MouseListener)	
	def mouseReleased(e):
		if (inDrag):
			print("\"", getText().strip(), "\"", "gets dragged to", getX(), ",", getY())
			inDrag = False
	