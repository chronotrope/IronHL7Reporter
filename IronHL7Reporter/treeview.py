#!/usr/bin/ipy

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
from System import Array
from System.Drawing import Color
from System.Windows.Forms import Application, Form, StatusBar
from System.Windows.Forms import TreeView, TreeNode, DockStyle
from System.Drawing import Size
import MessageFunctions as mf
import hl7


class IForm(Form):

    def __init__(self):
    	
    	self.sb = StatusBar()
        self.sb.Parent = self
        
   	
    	
    	getMessage = mf.MessageFunctions('C:/Users/ruben/Downloads/897301.txt', 'outfile.txt')
    	myMessage = getMessage.findMessage()
    	h = hl7.parse(myMessage)
    	
    	for m in range(0,len(h)):
    		i=0 
    		for value in(h[m]):
       	 		'''print "length1 = " + str(len(value))
        		##if "\n" not in value:
        		for comp in value:
        			if i > 0:
        				print "position = " +str(h[m][0][0])+ "-"+ str(i) +"." + str(value.index(comp)+1) + " value = " + comp
        		i+=1'''
    	
        self.Text = 'HL7 Message Analyzer'
        
        
        tv = TreeView()
        

        root = TreeNode()
        ##System.Array[int]([1, 2, 3])
        root.Text = 'HL7 Message'
       
        
        j=0
        
      	##fieldArray = Array[TreeNode]([20])
      	
      	
        for field in range(0, len(h)):
        
        	nodeName = (h[field][0][0])
        	nodeName = TreeNode()
        	nodeName.Text = str(h[field][0][0])
        	
        	root.Nodes.Add(nodeName)
        	##print str(nodeName.__class__)
        	msh1Found = 0
        	
        	print 'field length = ' + str(len(h[field]))
        	i=0
        	for value in(h[field]):
        		print 'value  = ' + str(value)
        		k = 0
        		for comp in value:
        			##print value.index(0)
        			childNode = str(h[field][0][0])+ "-"+ str(i) +"." + str(value.index(comp)+1)
        			childNode = TreeNode()
        			##childNode.Tag = str(h[field][0][0])+ "mno -"+ str(i) +"." + str(value.index(comp)+1)
        			print 'childnode = ' + str(childNode)
        			if i > 0 and i < len(h[field])-1:
        				if not comp:
        					comp2 = str(h[field][0][0])+ "-"+ str(i+1) +"." + str(value.index(comp)+1) + '""'
        					
        					myColor = Color.Yellow 
        				else:
        					comp2 = comp
        					myColor = Color.White
        					       					
        				##print "position = " +str(h[field][0][0])+ "-"+ str(i) +"." + str(value.index(comp)+1) + " value = " + comp2
        				
        				
        				
        				if str(h[field][0][0]) == 'MSH':
        					print 'i found msh!' + str(i)
        					print 'msh comp2 = ' + comp2
        					print 'comp2 string = ' + str(h[field][0][0])+ "-"+ str(i+1) +"." + str(value.index(comp)+2) + '""'
        					if i == 1 and comp2 == str(h[field][0][0])+ "-"+ str(i+1) +"." + str(value.index(comp)+1) + '""':
        						comp3 = str(h[field][0][0])+ "-"+ str(i) +"." + str(value.index(comp)+1) +' = '+ '|'
        						childNode.Tag = str(h[field][0][0])+ "-"+ str(i+1) +"." + str(value.index(comp)+1) 
        						myColor = Color.White
        						j=1
        						
        					elif j==1 and i==1:
        						print 'i = ' + str(i)
        						comp2 = comp
        						comp3 = str(h[field][0][0])+ "-"+ str(i+1) +"." + str(value.index(comp)) +' = ^'+ comp2
        						childNode.Tag = str(h[field][0][0])+ "-"+ str(i+1) +"." + str(value.index(comp))  
        						j+=1        						
        					else:
        						comp2 = comp
        						comp3 = str(h[field][0][0])+ "-"+ str(i) +"." + str(value.index(comp)+1) +' = '+ comp2
        						childNode.Tag = str(h[field][0][0])+ "-"+ str(i) +"." + str(value.index(comp)+1)     	
        				else:
        					comp2 = comp
        					       						       					
        					childNode.Tag = str(h[field][0][0])+ "-"+ str(i) +"." + str(value.index(comp)+1)
        					comp3 = str(h[field][0][0])+ "-"+ str(i) +"." + str(value.index(comp)+1) + ' = ' + comp2
        						
        					
        					
        				print 'comp2 = ' + comp
        				print 'j = ' + str(j)
        				childNode.Text =  comp3
        				childNode.BackColor = myColor
        				nodeName.Nodes.Add(childNode)
        					
        					
        		i+=1
        		comp2 = ''
        		comp = ''
        		
		
			
        
        ##child3.Nodes.AddRange((gchild2, gchild2))
       	tv.CheckBoxes = False
       	
        tv.Parent = self
        tv.SuspendLayout
        tv.Nodes.Add(root)
        tv.Dock = DockStyle.Fill
        tv.Scrollable
        tv.ResumeLayout
        tv.AfterSelect += self.AfterSelect

        
        
        
        self.Size = Size(400, 500)
        self.CenterToScreen()
        
    	
    	
    def AfterSelect(self, sender, event):    
        self.sb.Text = event.Node.Tag
    

Application.Run(IForm())
