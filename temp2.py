import xml.etree.ElementTree as et

tree = et.parse('Client-Tutorial.xml')
root = tree.getroot()

for node in root.iter('source'):
    node.text = "This is a node text"
    for url in node.iterfind('g'):
        #print(('g:',url.text))
        url.text = "This is a URL"

tree.write('output.xml')
