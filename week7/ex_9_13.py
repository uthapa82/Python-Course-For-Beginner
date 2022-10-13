from collections import OrderedDict

glossary_0 = OrderedDict()

glossary_0['append'] = " to add something."
glossary_0['pop'] = " to remove last element"
glossary_0['del'] = " to delete."
glossary_0['lower()'] = " to change element into lower."
glossary_0['insert'] = " to insert some element anywhere ina list."
glossary_0['remove'] = " to remove elements from list"
glossary_0['sort'] = " to sort something"
glossary_0['reverse'] = " to reverse something"

for name, meaning in glossary_0.items():
    print(name.title() + ": " + meaning)