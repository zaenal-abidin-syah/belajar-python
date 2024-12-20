a = "heLlO WoRLd"

aLower = a.lower()
print(aLower)
print(aLower.islower())

aTitle = a.title()
print(aTitle)
print(aTitle.istitle())

aUpper = a.upper()
print(aUpper)
print(aUpper.isupper())

b = "abc123"
print(b.isalnum())
b = "abc"
print(b.isalpha())
b = "123"
print(b.isdecimal())
b = "   "
print(b.isspace())


print("abc".startswith("a"))
print("abc".endswith("c"))


print("-".join(["1","2","3"]))
print("h-a-l-o".split("-"))

print("align kanan".rjust(50, "="))
print("align kiri".ljust(50, "="))
print("align tengah".center(50, "="))

# format string
a="abc"
print(f"halo nama saya {a:>35}")
print(f"halo nama saya {a:<35}")
print(f"halo nama saya {a:^35}")

a=2
b=-5
print(f"angka = {a:+d} dan {b:+d}")

a = 3.143432645
print(f"decimal ={a:10.2f}")
print(f"decimal ={a:010.2f}")

a=1000000
print(f"Rp {a:,}")


a = 0.0045
print(f"{a:.2%}")




