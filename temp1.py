txt = """<?xml version="1.0"?>
<pages>
    <page>
        <url>http://example.com/Labs</url>
        <title>Labs</title>
        <subpages>
            <page>
                <url>http://example.com/Labs/Email</url>
                <title>Email</title>
                <subpages>
                    <page/>
                    <url>http://example.com/Labs/Email/How_to</url>
                    <title>How-To</title>
                </subpages>
            </page>
            <page>
                <url>http://example.com/Labs/Social</url>
                <title>Social</title>
            </page>
        </subpages>
    </page>
    <page>
        <url>http://example.com/Tests</url>
        <title>Tests</title>
        <subpages>
            <page>
                <url>http://example.com/Tests/Email</url>
                <title>Email</title>
                <subpages>
                    <page/>
                    <url>http://example.com/Tests/Email/How_to</url>
                    <title>How-To</title>
                </subpages>
            </page>
            <page>
                <url>http://example.com/Tests/Social</url>
                <title>Social</title>
            </page>
        </subpages>
    </page>
</pages>"""

import xml.etree.ElementTree as et

tree1 = et.fromstring(txt)
print(type(tree1))

tree = et.parse('Client-Tutorial.xml')
root = tree.getroot()
print(type(root))

for node in root.iter('source'):
    print(('source:',node.text))
    for url in node.iterfind('g'):
        print(('g:',url.text))
