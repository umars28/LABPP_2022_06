array1 = set (map(int,input ('array 1:').split()))
array2 = set (map(int, input ('array 2 :').split()))

duplikat = tuple(array1 & array2)
print(f"Terdapat {len(duplikat)} duplikasi, yaitu", duplikat)