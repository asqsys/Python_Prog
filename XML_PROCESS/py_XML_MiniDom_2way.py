import xml.dom.minidom

xml = xml.dom.minidom.parse(result) # or xml.dom.minidom.parseString(xml_string)

itemList = xml.getElementsByTagName('item')
for item in itemList [1:]:

    summaryList = item.getElementsByTagName('summary')
    statusList = item.getElementsByTagName('status')
    keyList = item.getElementsByTagName('key')

    lineText = (summaryList[0].nodeValue + " " + statusList[0].nodeValue  + " " + keyList[0].nodeValue)

    p = Paragraph(lineText, style)
    Story.append(p)
	
	
# doc = parse('C:\\eve.xml')
# my_node_list = doc.getElementsByTagName("name")
# my_n_node = my_node_list[0]
# my_child = my_n_node.firstChild
# my_text = my_child.data 
# print my_text
