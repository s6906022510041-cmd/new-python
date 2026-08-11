heroes = ['Ironman', 'thor','hulk','superman','spiderman']
h2 = ['Dr. Strange', 'Cpt. America', 'Black Panther','Anr Man']

heroes.insert(0, h2[0])
print(heroes.index('thor'))
heroes.insert(heroes.index('thor') + 1, h2[1])
print(heroes)
heroes.remove('superman')
heroes.append('Ant Man')
print(heroes)
heroes.sort()
print(heroes)
heroes.reverse()
print(heroes)
newheroes = heroes
newheroes[0] ='wonder woman'
print(heroes)
copyheroes = [] + heroes
print(copyheroes)
copyheroes[0] = 'hanuman'
print(heroes)
print(copyheroes)