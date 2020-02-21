# Using Pretty Tables
# First you need to install library of PTable using pip 

from prettytable import PrettyTable as PT

t = PT(['Name','Family','Avg'])

t.add_row(['Ali','Rizvi','03.73'])
t.add_row(['Rubab','Qizilbash','02.03'])

print(t)
