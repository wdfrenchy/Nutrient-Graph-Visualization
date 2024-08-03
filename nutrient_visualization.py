import matplotlib.pyplot as plt
import numpy as np
import csv

# Thinking about making highest protein to calorie ratio foods in the food list
# Protein/Calories=PCRatio

full_list = []

with open("/Users/frenwd24/Desktop/AIPython/nutrients (1).csv", 'r') as file:
 csvreader = csv.reader(file)
 xx = 0
 for row in csvreader:
    if(xx<50):
       full_list.append(row)
    xx += 1

result = np.array(full_list)

tr = result.T
food = tr[0]

macros = np.zeros([len(result), 3])
cals = np.zeros([len(result), 3])

for i in range(len(result)):
  cals[i][0] = 4
  cals[i][1] = 4
  cals[i][2] = 9

for i in range(len(result)):
  for j in range(1, len(result[i])):
        k = result[i][j]
        if not k.isnumeric():
           result[i][j] = 0

for i in range(len(result)):
   macros[i][0] = result[i][3]
   macros[i][1] = result[i][7]
   macros[i][2] = result[i][4]

total_cals = macros * cals
f_cals = []
for i in range(len(total_cals)):
   f_cals.append((total_cals[i][0] + total_cals[i][1] + total_cals[i][2]))
print(f_cals)

# request = input("Enter a food item: ")
# item_index = np.where(food == request)

# if item_index[0].size == 0:
#    print("Item not in the list")
# else:
#    calories = sum(total_cals[item_index][0])
#    print("The total calories is " + str(calories) + ".")
#    protein = result[item_index[0][0]][3]
#    print("The total protein is " + str(protein) + ".")
#    #total = total_cals[item_index[0][0]][0] + total_cals[item_index[0][0]][1] + total_cals[item_index[0][0]][2]
#    ratio = float(protein) / float(calories)
#    print("The protein to calorie ratio is " + str(ratio) + ".")
   
# print(food)

all_ratios = []

for i in range(len(food)):
    calories = f_cals[i]
    protein = result[i][3]
    if calories == 0:
       ratio = 0
    else:
       ratio = float(protein) / float(calories)
    all_ratios.append(ratio)
# # ratio = protein / total

x = food
y = all_ratios
#print(all_ratios)

y_pos = range(len(y))
plt.figure(figsize=(100,8))
plt.bar(y_pos, y)

plt.xticks(y_pos, x, rotation=90)

plt.text(3, 7, 'Protein to Calorie Ratios', 
         fontsize = 18, color = 'g')

plt.xlabel('Foods', fontsize = 15)

plt.ylabel('Protein per Calorie (g/cal)', fontsize = 15)

plt.annotate('Highest Protein per Calorie Ratio', xy = (2.4, 8), 
             fontsize = 16, xytext = (3, 9), 
             arrowprops = dict(facecolor = 'red'),
             color = 'g')

plt.tight_layout() 

plt.show()
