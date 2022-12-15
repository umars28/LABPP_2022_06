m1 = []
m2 = []

m1_a = m1.append(int(input("Input nilai matrix pertama index 1,1 : ")))
m1_b = m1.append(int(input("Input nilai matrix pertama index 1,2 : ")))
m1_c = m1.append(int(input("Input nilai matrix pertama index 2,1 : ")))
m1_d = m1.append(int(input("Input nilai matrix pertama index 2,2 : ")))

m2_a = m2.append(int(input("Input nilai matrix pertama index 1,1 : ")))
m2_b = m2.append(int(input("Input nilai matrix pertama index 1,2 : ")))
m2_c = m2.append(int(input("Input nilai matrix pertama index 2,1 : ")))
m2_d = m2.append(int(input("Input nilai matrix pertama index 2,2 : ")))

print('|', m1[0], m1[1], '|', 'X', '|', m2[0], m2[1], '|', '=', '|', m1[0]*m2[0]+m1[0]*m2[2], m1[1]*m2[1]+m1[1]*m2[3], '|')
print('|', m1[2], m1[3], '|', ' ', '|', m2[2], m2[3], '|', ' ', '|', m1[2]*m2[0]+m1[2]*m2[2], m1[3]*m2[1]+m1[3]*m2[3], '|')