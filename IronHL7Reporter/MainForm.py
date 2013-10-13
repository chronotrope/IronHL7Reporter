import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *
import MessageFunctions as mf

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._treeView1 = System.Windows.Forms.TreeView()
		self._treeNode1 = System.Windows.Forms.TreeNode()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# treeView1
		# 
		self._treeView1.Location = System.Drawing.Point(55, 63)
		self._treeView1.Name = "treeView1"
		self._treeView1.Size = System.Drawing.Size(616, 235)
		self._treeView1.TabIndex = 0
		# 
		#treeNode1
		
		
		# button2
		# 
		self._button2.Enabled = False
		self._button2.Location = System.Drawing.Point(876, 126)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(158, 34)
		self._button2.TabIndex = 5
		self._button2.Text = "Analyze Message"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(876, 63)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(158, 34)
		self._button1.TabIndex = 4
		self._button1.Text = "Select HL7 fle..."
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.onSelectFile
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(14, 552)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(942, 38)
		self._label1.TabIndex = 6
		self._label1.Text = "Waiting for HL7 message file..."
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Black
		self._textBox1.ForeColor = System.Drawing.Color.Lime
		self._textBox1.Location = System.Drawing.Point(58, 337)
		self._textBox1.Multiline = True
		self._textBox1.Name = "textBox1"
		self._textBox1.ReadOnly = True
		self._textBox1.ScrollBars = System.Windows.Forms.ScrollBars.Both
		self._textBox1.Size = System.Drawing.Size(612, 182)
		self._textBox1.TabIndex = 7
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(55, 22)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(162, 23)
		self._label2.TabIndex = 12
		self._label2.Text = "Message Tree View:"
		self._label2.Click += self.Label2Click
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(58, 311)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(217, 23)
		self._label3.TabIndex = 9
		self._label3.Text = "Message Parsing Output:"
		# 
		# button3
		# 
		self._button3.Enabled = False
		self._button3.Location = System.Drawing.Point(876, 203)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(158, 34)
		self._button3.TabIndex = 13
		self._button3.Text = "Choose Output Directory"
		self._button3.UseVisualStyleBackColor = True
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(876, 264)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(158, 20)
		self._textBox2.TabIndex = 14
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(760, 264)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 15
		self._label4.Text = "File Name Prefix:"
		self._label4.Click += self.Label4Click
		# 
		# MainForm
		# 
		self.AutoScroll = True
		self.ClientSize = System.Drawing.Size(1097, 595)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._treeView1)
		self.Name = "MainForm"
		self.Text = "IronHL7Reporter"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label2Click(self, sender, e):
		pass

	def Label4Click(self, sender, e):
		pass

	def onSelectFile(self, sender, e):
		self._label1.Text = 'select your hl7 file'
		dialog = OpenFileDialog()
		##dialog.Filter = "HL7 text files (*.txt)|All Files (*.*)|*.* "
		dialog.Filter = "HL7 Text files (*.txt)|*.txt|All files (*.*)|*.*"
		dialog.FilterIndex = 1
		
		
		if dialog.ShowDialog(self) == DialogResult.OK:
			f = open(dialog.FileName)
			self._label1.Text = 'i opened the file - status'
			print 'i opened the file'
			longFileName = str(f)
			h = longFileName.split(",")
			h1 = h[0]
			h2 = h1.split("'")
			inputFileName = h2[1]
			print longFileName
			print inputFileName
			getMessage = mf.MessageFunctions(inputFileName, 'outfile.txt', self._treeView1, self._treeNode1)
			myMessage = getMessage.findMessage()
			parseTree = getMessage.buildParseTree(myMessage)
			
			
 
