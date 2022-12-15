from hewan import ular, tokek
ular = ular("hitam")
tokek = tokek("tutul")

print("-"*30)
print("--- Cara ular bergerak ---")
ular.bergerak()
print("-"*30)
print("--- Cara tokek bergerak ---")
print("-"*30)
tokek.bergerak()

print("-"*30)
print("--- Cara ular bertarung ---")
ular.bertarung()
print("-"*30)

print("--- Cara tokek bertarung ---")
tokek.bertarung()
print("-"*30)

print("ular serang tokek")
print("--- Darah tokek sebelum diserang ---")
tokek.cekDarah()
ular.serang(tokek)
print("--- Darah tokek setelah diserang ---")
tokek.cekDarah()
