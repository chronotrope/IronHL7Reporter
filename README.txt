IronHL7Reporter -  Iron HL7 Reporter
This is a work in progress.
Building an IronPython based GUI wrapper which uses John Paulett's python-hl7 python class.
https://github.com/chronotrope/python-hl7

The current requirements are:

1.  Analyze a sample HL7 message from a HL7 extract (many HL7 files extracted to a text file).
2.  This analyzed message will be parsed(using John Paulett's Python-HL7 class). and displayed as a TreeView.
3.  The user would then be able to click (or double-click...haven't nailed that down yet) and select the HL7 fields they want to report on.
4.  The user would then click the "Parse" button and the desired fields would be parsed and a tab-delimited file would then be generated (may be excel in the future...we'll see).

http://integrationdojo.blogspot.com/2013/09/started-working-on-ironhl7reporter.html