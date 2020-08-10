# ------------------------------------------------------------
# --  Title: xpath_support.py
# --  Description: several xpath support examples.
# --  Author: Dong Haxia
# --  Date: 07-08-2020
# ------------------------------------------------------------


import xml.etree.ElementTree as ET

contents = '''
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
'''
root = ET.fromstring(contents)

# Top-level element
top_element = root.findall(".")

# All 'neighbor' grand-children of 'country' children of the top-level
neighbor = root.findall("./country/neighbor")

# Nodes with name='Singapore' that have a 'year' child
spec_node = root.findall(".//year/..[@name='Singapore']")

# 'year' nodes that are children of nodes with name='Singapore'
root.findall(".//*[@name='Singapore']/year")

# All 'neighbor' nodes that are the second child of their parent
root.findall(".//neighbor[2]")
