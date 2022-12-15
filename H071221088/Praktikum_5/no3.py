array1 = input("Input array ke-1 : ").split()
array2 = input("Input array ke-2 : ").split()
set_a= set(array1)
set_b= set (array2)

tup_a= tuple(set_a & set_b)

print(f"terdapat {len(set_a & set_b)} duplikat yaitu : {tup_a}")