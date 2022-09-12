suri = {'cat': 'Abhijeet'}
kali = {'rat': 'Anishma'}
khaire = {'dog': 'Anup'}

pets_list = [suri, kali, khaire]
#loppint throught the list.
for animals in pets_list:
    print(animals)

for k, v in suri.items():
    print(k + " owner is " + v)

for k, v in kali.items():
    print(k + " owner is " + v)

for k, v in khaire.items():
    print(k + " owner is " + v)