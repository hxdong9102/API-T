# ------------------------------------------------------------
# --  Title: process_simple_xml.py
# --  Description: Basic processing to a simple xml file.
# --  Author: Dong Haxia
# --  Date: 07-08-2020
# ------------------------------------------------------------

import xml.etree.ElementTree as ET


tree = ET.parse("sample.xml")
root = tree.getroot()
#print(root.tag, root.attrib)
#print(root[0][1].text)


# Iterate direct children
for child in root:
    print(child.tag, child.attrib)


# Iterate recursively over all the sub-tree
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)


# find a specified node
for country in root.findall("country"):
    rank = country.find("rank").text
    name = country.get('name')
    print(name, rank)


# Modifying an XML File
for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')

tree.write('updated_sample.xml')


# Remove elements
for country in root.iter('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write("del_sample.xml")
