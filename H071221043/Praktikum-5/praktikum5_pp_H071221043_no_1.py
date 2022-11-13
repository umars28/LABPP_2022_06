mat1 = []
mat2 = []

mat1_0 = mat1.append(int(input('input nilai matrix pertama index 1,1:')))
mat1_1 = mat1.append(int(input('input nilai matrix pertama index 1,2:')))
mat1_2 = mat1.append(int(input('input nilai matrix pertama index 2,1:')))
mat1_3 = mat1.append(int(input('input nilai matrix pertama index 2,2:')))

mat2_0 = mat2.append(int(input('input nilai matrix kedua index 1,1:')))
mat2_1 = mat2.append(int(input('input nilai matrix kedua index 1,2:')))
mat2_2 = mat2.append(int(input('input nilai matrix kedua index 2,1:')))
mat2_3 = mat2.append(int(input('input nilai matrix kedua index 2,2:')))

print('|', mat1[0], mat1[1], '|', 'X', '|', mat2[0], mat2[1], '|', '=', '|', mat1[0]*mat1[1]+mat2[0]*mat2[2], mat1[0]*mat1[1]+mat2[1]*mat2[3], '|')
print('|', mat1[2], mat1[3], '|', ' ', '|', mat2[2], mat2[3], '|', ' ', '|', mat1[2]*mat1[3]+mat2[0]*mat2[2], mat1[2]*mat1[3]+mat2[1]*mat2[3], '|')
