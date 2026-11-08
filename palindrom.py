word = input("vnesite besedo: ").lower()
if word == word[::-1]:
    print("beseda je palindrom.")
else:
    print("beseda ni palindrom.")