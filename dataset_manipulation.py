import csv

# color matching to normalize colors of the given dataset
colors_matching = {'Red': 'Red', 'Blue': 'Blue', 'Blue-White': 'Blue-White',
                   'Blue-white': 'Blue-White', 'Blue White': 'Blue-White',
                   'White': 'White', 'white': 'White', 'Whitish': 'White',
                   'yellow-white': 'White', 'Yellowish White': 'Yellowish', 'Orange': 'Orange',
                   'yellowish': 'Yellowish', 'Yellowish': 'Yellowish', 'White-Yellow': 'White',
                   'Orange-Red': 'Orange', 'Pale yellow orange': 'Orange', 'Color': 'Color',
                   'Blue white': 'Blue-White'}

type_matching = {'0': 'Red Dwarf', '1': 'Brown Dwarf', '2': 'White Dwarf',
                 '3': 'Main Sequence', '4': 'Super Giants', '5': 'Hyper Giants', 'Type': 'Type'}

file = csv.reader(open('Stars.csv'))
lines = list(file)

for line in lines:
    line[6] = type_matching[line[6]]
    line[4] = colors_matching[line[4]]

# write lines back in a csv file
writer = csv.writer(open('Stars_manipulated.csv', 'w'))
writer.writerows(lines)
