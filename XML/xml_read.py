from lxml import etree
import numpy as np


s='''<book category="web" cover="paperback">
     <title lang="en">Learning XML 2</title>
     <author>Erik Ray</author>
     <year>2006</year>
     <price>49.95</price>
     </book>'''

s2='''
<root>
<h:table xmlns:h="http://www.w3.org/TR/html4/">
  <h:tr>
    <h:td>Apples</h:td>
    <h:td>Bananas</h:td>
  </h:tr>
</h:table>
<f:table xmlns:f="https://www.w3schools.com/furniture">
  <f:name>African Coffee Table</f:name>
  <f:width>80</f:width>
  <f:length>120</f:length>
</f:table>
</root> '''
ns= {'h':"http://www.w3.org/TR/html4/",'f':"https://www.w3schools.com/furniture"}
root=etree.fromstring(s2)
etree.register_namespace('h',"http://www.w3.org/TR/html4/")
etree.register_namespace('f',"https://www.w3schools.com/furniture")
# print(etree.dump(root))
# for x in root:
#     print(x.tag)
l = root.findall('.//{https://www.w3schools.com/furniture}table')
for x in l:
    for y in x:
        print(y.text)





















# data=np.loadtxt('XML/data.csv',delimiter=',',dtype=str)

# tree = etree.parse('XML/input.xml')
# r = tree.getroot()
# print(r)

# root = etree.fromstring(s)
# print(root)

# l= root.xpath('.//title[@lang="en"]')
# print(l)
# for x in l:
#     print(x.tag)
#     print(x.attrib['lang'])
#     print((x.text).split())

# p = root.findall('./title')
# for x in p:
#     print(x.tag)








# for c in r:
#     if c.tag=='author':
#         c.text=str(data[0][0])
# f=etree.tostring(root, encoding='UTF-8', xml_declaration=True)
# with open('XML/output.xml','wb') as file:
#     file.write(f)


          



