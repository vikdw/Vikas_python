from lxml import etree as et
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

et.register_namespace("h","http://www.w3.org/TR/html4/")
# et.register_namespace('f',"https://www.w3schools.com/furniture")
ns= {'h':"http://www.w3.org/TR/html4/",'f':"https://www.w3schools.com/furniture"}
r = et.fromstring(s2)
print(r[0][0])
sr= r.find('.//{http://www.w3.org/TR/html4/}td')
print(sr)
sr= r.findall('.//{*}td')
print(sr)
sr= r.findall(".//h:td", ns)
print(sr[0].text, sr[1].text)
# sr= r.findall(".//*:td[contains(text()='Apples')]", ns)
print(et.dump(r))

sx= r.xpath('.//h:table', namespace={'h':"http://www.w3.org/TR/html4/",'f':"https://www.w3schools.com/furniture"})



# r = et.fromstring(s)
# print(r.tag)
# et.SubElement(r,'subject')
# sb=r.xpath('.//subject')
# print(sb)
# sb[0].set('xml_Math',"XML_with_Math")
# sb[0].text="Maths"
# print(et.tostring(r, pretty_print=True).decode('UTF-8'))

# t=r.xpath(".//*[text()='Maths']")
# print(t)


sb1= r.findall('subject')
print(sb1)





# ns= {'h':"http://www.w3.org/TR/html4/",'f':"https://www.w3schools.com/furniture"}
# root=etree.fromstring(s2)
# etree.register_namespace('h',"http://www.w3.org/TR/html4/")
# etree.register_namespace('f',"https://www.w3schools.com/furniture")
# # print(etree.dump(root))
# # for x in root:
# #     print(x.tag)
# l = root.findall('.//{https://www.w3schools.com/furniture}table')
# for x in l:
#     for y in x:
#         print(y.text)





















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


          


# root = et.Element('xml', version="x.x")

# # Pass the parent node, name of the child node,
# # and any number of optional attributes
# et.SubElement(root, 'head')
# et.SubElement(root, 'title', bgcolor="red", fontsize='22')
# et.SubElement(root, 'body', fontsize="15")

# print (et.tostring(root, pretty_print=True).decode("utf-8"))
# for x in root:
#     if x.tag == "head":
#         x.set('headCount', '1')
#         et.SubElement(x ,'body', eyes='black')

# print (et.tostring(root, pretty_print=True).decode("utf-8"))