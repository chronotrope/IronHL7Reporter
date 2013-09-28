import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._treeView1 = System.Windows.Forms.TreeView()
		self.SuspendLayout()
		# 
		# treeView1
		# 
		self._treeView1.Location = System.Drawing.Point(75, 63)
		self._treeView1.Name = "treeView1"
		self._treeView1.Size = System.Drawing.Size(441, 202)
		self._treeView1.TabIndex = 0
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(605, 397)
		self.Controls.Add(self._treeView1)
		self.Name = "MainForm"
		self.Text = "IronHL7Reporter"
		self.ResumeLayout(False)

