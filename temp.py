import xml.etree.ElementTree as et

tree = et.parse('Client-Tutorial.xml')
root = tree.getroot()

def print_value(tree):
    for child in tree.iter():
        print(child.tag, child.attrib)
        if(child.tag=='group'):
            for child1 in child.iter():
                print(child1.tag, child1.attrib)


def find_rec(node, element):
    for item in node.findall(element):
        yield item
        for child in find_rec(item, element):
            yield child

def print_rec(children, j):
    i=0
    for child in children:
        print(('child', j, child.keys(), child.tag, child.attrib))
        if (child.tag=="source"):
            i = i+1
            texts = child.findall('g')
            if len(texts) == 0 :
                print(("source_g",j,i,child.attrib, child.tag, child.text))
            for text in texts:
                i = i+1
                print(("source",j,i,child.attrib, child.tag, text.text))

        else:
            #print(("NOT source",child.attrib, child.tag))
            for child1 in child.iter():
                print_rec(child1, j+1)

print_rec(tree.iter('xliff'),0)