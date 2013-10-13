import re
import sys
from System.Windows.Forms import *
import hl7
from System.Drawing import Color

global messageString
global foundMSH
global mshFound



class MessageFunctions:
	def __init__(self, messageFile, outFile, treeView, nodeRoot):
		self.messageFile = messageFile
		self.outFile = outFile
		self.treeView = treeView
		self.nodeRoot = nodeRoot
		
	
	def findMessage(self):
		workingFile = open(self.messageFile, "r")
		fileHandle = open(self.outFile, 'w')
		messageString = ''
		message = ''
		foundMSH = 0
		pattern = re.compile('^(?!MSH)')
		while workingFile:
			
			for line in workingFile:
				line.rstrip("\n")
				splitSegment = line.split("|")
			
				if (re.search("MSH", splitSegment[0])):
					foundMSH += 1
					if foundMSH ==1:
						messageString = line +'\r'
						## beginning of first message found
						foundMSH =+1
				elif foundMSH > 0 and pattern.match(splitSegment[0]):
					## searching for non-MSH segments following first MSH segment
					messageString = messageString + line +'\r' 
				
				
				if (foundMSH > 1) and (re.search("MSH", splitSegment[0])):
					## found the 2nd message.  Now save off the first message for analysis.
				
					message = messageString
				
					##fileHandle.write(message)
					return message
					## to be used when finding many messages
					'''messageString = ''
					message = ''  '''
					break
			return messageString
				
			
		fileHandle.close()
		
	def buildParseTree(self, myMessage):
		comp2 = ''
		mshFound = False
		myColor = Color.White
		self.myMessage = myMessage
		h = hl7.parse(self.myMessage)
		print str(len(h))+ ' segments found'
		self.nodeRoot.Text = 'HL7 Message'
		for field in range(0, len(h)):
			print 'field = ' + str(field)
			nodeName = (h[field][0][0])
			nodeName = TreeNode()
			nodeName.Text = str(h[field][0][0])
			self.nodeRoot.Nodes.Add(nodeName)
			print 'field length for ' + str(h[field][0][0]) + ' = '+ str(len(h[field])-1) + ' field = ' + str(h[field])
			i=0
			for value in(h[field]):
				print '2nd field = ', field
				print 'value  = ' + str(value)
				for comp in value:
					childNode = str(h[field][0][0])+ "-"+ str(i) +"." + str(value.index(comp)+1)
					childNode = TreeNode()
					print 'childnode = ' + str(childNode)
					if i > 0 and i < len(h[field])-1:
						if not comp:
							comp2 = str(h[field][0][0])+ "-"+ str(i+1) +"." + str(value.index(comp)+1) + '""'
							myColor = Color.Yellow
						else:
							comp2 = comp
							myColor = Color.White
					if str(h[field][0][0]) == 'MSH':
						print 'i found msh!' + str(i)
						print 'msh comp2 = ' + comp2
						print 'comp2 string = ' + str(h[field][0][0])+ "-"+ str(i+1) +"." + str(value.index(comp)+2) + '""'
						if i == 1 and comp2 == str(h[field][0][0])+ "-"+ str(i+1) +"." + str(value.index(comp)+1) + '""':
									comp3 = str(h[field][0][0])+ "-"+ str(i) +"." + str(value.index(comp)+1) +' = '+ '|'
									childNode.Tag = str(h[field][0][0])+ "-"+ str(i+1) +"." + str(value.index(comp)+1) 
									myColor = Color.White
									mshFound = True
						elif mshFound == True and i==1:
								print 'i = ' + str(i)
								comp2 = comp
								comp3 = str(h[field][0][0])+ "-"+ str(i+1) +"." + str(value.index(comp)) +' = ^'+ comp2
								childNode.Tag = str(h[field][0][0])+ "-"+ str(i+1) +"." + str(value.index(comp))
						else:
							comp2 = comp
							comp3 = str(h[field][0][0])+ "-"+ str(i) +"." + str(value.index(comp)+1) +' = '+ comp2
							childNode.Tag = str(h[field][0][0])+ "-"+ str(i) +"." + str(value.index(comp)+1)
					else:
						comp2 = comp       						       					
						childNode.Tag = str(h[field][0][0])+ "-"+ str(i) +"." + str(value.index(comp)+1)
						comp3 = str(h[field][0][0])+ "-"+ str(i) +"." + str(value.index(comp)+1) + ' = ' + comp2
							
						
						
					print 'comp2 = ' + comp
					print 'msh found = ' + str(mshFound)
					childNode.Text =  comp3
					childNode.BackColor = myColor
					nodeName.Nodes.Add(childNode)
					myColor = Color.White
				i+=1
				comp2 = ''
				comp = ''
		self.treeView.Nodes.Add(self.nodeRoot)