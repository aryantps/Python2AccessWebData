import xml.etree.ElementTree as ET
data = '''
<person>
    <name>Chuck</name> 
    <phone type="intl">+1 734 303 4456</phone>
        <mobile>12345857</mobile>
        <landline>427727</landline>
    <email hide="yes" /> 
</person>
'''
tree = ET.fromstring(data)
print(tree.find('person/phone/'))