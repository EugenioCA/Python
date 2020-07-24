from xml.dom import minidom

# Parse an xml file by name
mydoc = minidom.parse('items.xml')

items = mydoc.getElementsByTagName('item')

# Calculate the total amount of items
print(len(items))

# Obtain one specific item attribute
print(items[1].attributes['name'].value)

# Obtain all item attributes
for elem in items:
    print(elem.attributes['name'].value)

# Obtain one specific item's data
print(items[1].firstChild.data)
print(items[1].childNodes[0].data)

# Obtain all items data
for elem in items:
    print(elem.firstChild.data)
