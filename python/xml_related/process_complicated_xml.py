# ------------------------------------------------------------
# --  Title: process_complicated_xml.py
# --  Description: Basic processing to a little complicated xml file.
# --  Author: Dong Haxia
# --  Date: 07-08-2020
# ------------------------------------------------------------

# Search the namespaced XML file
import xml.etree.ElementTree as ET


tree = ET.parse("sample_complicated.xml")
root = tree.getroot()


ns = {'real_person': 'http://people.example.com',
'role': 'http://characters.example.com'}
for actor in root.findall('real_person:actor', ns):
    name = actor.find('real_person:name', ns)
    print(name.text)
    for char in actor.findall('role:character', ns):
        print('   |-->', char.text)

