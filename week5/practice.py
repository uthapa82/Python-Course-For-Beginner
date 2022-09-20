             #revising  DICTONARY's lessons.
#accessing values practice.
aliens_colors = {'color': 'blue', 'name': 'jhadoo', 'city': 'pokhara',}
print(aliens_colors['color'])
print(aliens_colors['name'])

ram_0 = aliens_colors['name']
print("your name is " + ram_0)
print(ram_0 + " lives in " + aliens_colors['city'] + " with his family.")
#adding in dictonary.
aliens_colors['x-position'] = 5
aliens_colors['Abhi'] = 2
print(aliens_colors)

#poll
fav_lang = {
    'abhishek': 'python',
    'anu': 'c',
    'anup': 'c++',
}
print("abhisheck's favorite language is " + fav_lang['abhishek'])
print("anu's favorite language is " + fav_lang['anu'])
#to find keys only. / values only.
for names in fav_lang.keys(): #remember at last .keys(): not .items():.
    print(names)
for programs in fav_lang.values():
    print("\n" + programs)

favo_lang = {
    'anup': 'c++',
    'anu': 'c',
    'abhi': 'python'
}
siblings_0 = ['anu', 'anup']
for names in favo_lang.keys():
    print(names)
if names in  siblings_0:
    print("Hi," + names + "I see your favorite language is" + favo_lang[names] ) 



