from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['Anu'] = 'python'
favorite_languages['Anup'] = 'C'
favorite_languages['Anusha'] = 'C++'
favorite_languages['Abhi'] = 'Go'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")