import random

print('Colour of ion in aqueous solution: 1')
print('Solubility: 2')

ion_colour = {'Cr3+': 'green', 'Mn2+': 'colourless', 'Fe2+': 'pale green', 
    'Co2+': 'pink', 'Ni2+': 'green', 'Cu2+': 'blue', 
    'Cr2O7 2-': 'orange', 'MnO4 -': 'purple', 'Fe3+': 'pale yellow',
    'CrO4 2-': 'yellow'
}

cation = ['Na+', 'K+', 'NH4 +', 'Ag+', 'Ba2+', 'Pb2+',
'Mg2+', 'Al3+', 'Zn2+', 'Fe2+', 'Fe3+', 'Cu2+']

anion = ['NO3-', 'HCO3 -', 'Cl-', 'Br-', 'I-', 'SO4 2-', 'CO3 2-', 'OH-']

test = input('Which test (enter if no): ')
while test:
    if test == '1': 
        con = True
        while con:
            ion = random.choice(list(ion_colour.keys()))
            colour = ion_colour[ion]
            print(ion)
            ans = input('corresponding colour: ')
            ans = ans.lower().strip()
            
            if ans == '':
                con = False
            elif ans != colour:
                print('correct answer is', colour)
            else: 
                print('Correct')
            print()
    
    if test == '2':
        con = True
        while con:
            catq = random.choice(cation)
            anq = random.choice(anion)
            
            print(catq,' + ', anq)
            
            if catq == 'Na+' or catq == 'K+' or catq == 'NH4 +' or anq == 'NO3-' or anq == 'HCO3 -':
                solubility = True
            
            elif anq == 'CO3 2-' or anq == 'OH-':
                solubility = False
                
            elif anq == 'Cl-' or anq == 'Br-' or anq == 'I-':
                if catq == 'Ag+' or catq == 'Pb2+':
                    solubility = False
                else: 
                    solubility = True
                    
            elif anq == 'SO4 2-':
                if catq == 'Ba2+' or catq == 'Pb2+' or catq == 'Ca2+':
                    solubility == False
                else:
                    solubility == True
                     
            ans = input('Soluble - 1, insoluble - 2: ')
            if ans == '':
                con = False
            elif (ans == '1' and solubility) or (ans == '2' and not solubility):
                print('Correct')
            else:
                if solubility: 
                    print('It is soluble')
                else:
                    print('It is insoluble')
            print()
            
    test = input('Which test (enter if no): ')
            

