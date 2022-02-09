#Input from user

leg = input("Te rugam introdu legea functiei:\n")
valoriel_calcul = input("Te rugam introdu numere folosind ca separator \",\":\n").split(',')
values = []
if len(valoriel_calcul) < 3:
    print("Te rugam sa introduci minim 3 valori!")
    exit()
for x in valoriel_calcul:
    values.append(int(x))

letters_for_points = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
for x in range(2):
    print()

def leg_separator():
    if '+' in leg:
        ax = leg.split('+')[0]
        ax = str(ax).replace("x", '')
        sign = "+"
    elif '-' in leg:
        ax = leg.split('-')[0]
        ax = str(ax).replace("x", '')
        sign = "-"
    b = leg.split(sign)[1]
    list = [ax, sign, b]
    return list
x_d = []
y_d = []
def get_points():
    list = leg_separator()
    done_values = []
    for x in values:
        if '+' in list[1]:
            done = int(list[0])*int(x)+int(list[2])
            done_values.append(done)
        elif '-' in list[1]:
            done = int(list[0])*int(x)-int(list[2])
            done_values.append(done)
    count = 0
    return_values = []
    for x in letters_for_points:
        if count == len(values):
            return_values = str(return_values).replace("['", '').replace("']", '').replace("', '", ' ')
            return return_values
        else:
            text = f"{x}({values[int(count)]}, {done_values[int(count)]})"
            x_d.append(int(values[int(count)]))
            y_d.append(int(done_values[int(count)]))
            count += 1
            return_values.append(text)
try:
    test = get_points()
    print(test)
except:
    print("Legea functiei trebuie sa arate ceva de genu \"2x+3\"")
    exit()

# Graphic 

import matplotlib.pyplot as plt

plt.plot(x_d, y_d)
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Graficul fuctiei \"{leg}\"!')
plt.show()