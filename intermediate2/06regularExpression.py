# core modules reguler expression is re

import re

# if re.match('^a...s$', "abyss"):
#     print("successful")
# else:
#     print("unsuccessful")

# metacharacter
# [] . ^ $ * + ? {} () \ |

# [] di dalamnya berisi beberapa karakter yang jika salah satu karakter itu muncul maka hasilnya true atau match

# print(re.match(r'[abc]', "the titanic"))
#  result none or not match 
# re.match hanya mencocokan di kata pertama dari string

#  use re.search untuk mencari ke seluruhan karakter string

# print(re.search(r"[abc]", "the titanic"))

# pada re.search hanya mencari 1 karakter saja untuk mencari ke selluruhan gunakan re.findall

# print(re.findall(r"[abc]", "the titanic"))


# . dot titik artinya boleh berisi karkter apapun dan sesuai dengn jumlah titik

# print(re.search(r"..","abc"))
# print(re.findall(r"..","abcd"))



# ^ => start karakter

# print(re.findall(r"^h..","halo nama saya rizki"))

# $ => end karakter
# print(re.findall(r"i$","halo nama saya rizki"))

# * star => kosong atau lebih karakter yang sama
# print(re.search(r"ab*c","ac"))
# print(re.search(r"ab*c","abc"))
# print(re.search(r"ab*c","abbbbc"))
# print(re.search(r"ab*c","abbbbfc")) # not match karena b harus diikuti dengan c

# + => satu atau lebih karakter yang sama tidak boleh kosong
# print(re.search(r"ab+c","ac")) # not match
# print(re.search(r"ab+c","abc"))
# print(re.search(r"ab+c","abbbbc"))
# print(re.search(r"ab+c","abbbbfc")) # not match karena b harus diikuti dengan c


# ? => karakter hanya muncul satu kali atau tidak sama sekali
# print(re.search(r"ab?c","ac"))
# print(re.search(r"ab?c","abc"))
# print(re.search(r"ab?c","abbc")) # karakter tidak boleh muncul lebih dari satu kali



# {} => mengatur minimal dan maksimal muncul karakter yang sama
# d{3,7} => minimal 3 karakter dan maksimal 7 karakter


# print(re.search(r"ab{3, 8}c","abc"))# minimal 3
# print(re.search(r"ab{3,8}c","abbbc"))
# print(re.search(r"ab{3,8}c","abbbbbbbbbbbc"))# maksimal 8


# {m} artinya karakter hannya boleh  muncul sebanyak m karakter

# print(re.search(r"ab{4}c","abbbc")) # karakter b kurang 
# print(re.search(r"ab{4}c","abbbbc"))
# print(re.search(r"ab{4}c","abbbbbc"))# karakter b berlebihana


# | => dimana boleh memilih satu antara karakter

# print(re.search(r"a|b","a"))
# print(re.search(r"a|b","b"))
# print(re.search(r"a|b","c")) # tidak ada pilihan c


# () => for grouping
# print(re.search(r"(a|b)c","ac"))
# print(re.search(r"(a|b)c","bc"))
# print(re.search(r"(a|b)c","a"))# harus ada c




# \ => digunakan untuk beberapa metacharacter
# seperti "\$ daku \."
# special sequences
#  \A => akan match jika spesifik karakter start dari string
# seperti "\Athe" match dengan "the sun" tapi tidak match dengan "in the sun"

# \b => jika spesifik karakter berada di awalan atau diakhir kata
# contoh
# print(re.search(r"\bfoo","football"))
# print(re.search(r"\bfoo","a football")) # match karena foo berada di awal kata
# print(re.search(r"\bfoo","afootball"))# tidak match karena foo berada  di tengah kata
# print(re.search(r"\bfoo","the foo"))
# print(re.search(r"foo\b","the afoo test"))
# print(re.search(r"foo\b","the afootest")) # tidak match karena foo berada di tengah kata

# \B => lawan dari \b
# tidak boleh berada diawal atau di akhir kata
# print(re.search(r"\Bfoo","a football")) # tidak match karena foo tidak boleh di awal kata
# print(re.search(r"foo\B","the afoo test")) # tidak match karena foo tidak boleh di akhir kata


# \d => digit atau angka , ekuivalent dengan [0-9]
# \D => lawan dari \d, ekuivalent dengn [^0-9]
# \s => match jika mengandung space
# \S => jika tidak mengandung space
# \w => match jika ada alfanumerik (digit dan alfabet), ekuivalent [a-zA-Z0-9_] underscore termasuk di dalamnya
# \W => kebalikan dari \w
# \Z => match jika sepesifik karakter berada di akhir kalimat





