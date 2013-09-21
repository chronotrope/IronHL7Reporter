import re
import sys

global messageString
global foundMSH


class MessageFunctions:
	def __init__(self, messageFile, outFile):
		self.messageFile = messageFile
		self.outFile = outFile
	
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