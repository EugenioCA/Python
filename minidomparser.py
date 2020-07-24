from xml.dom import minidom

# parse an xml file by name
mydoc = minidom.parse('items.xml')

items = mydoc.getElementsByTagName('item')

# total amount of items
print(len(items))

# one specific item attribute
print(items[1].attributes['name'].value)

# all item attributes
for elem in items:
    print(elem.attributes['name'].value)

# one specific item's data
print(items[1].firstChild.data)
print(items[1].childNodes[0].data)

# all items data
for elem in items:
    print(elem.firstChild.data)