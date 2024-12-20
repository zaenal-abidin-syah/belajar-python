"""
belajar dict

"""


data_dict = {}
# data_dict = dict()

data_dict.update({"a":"zaenal"})
data_dict.update({"b":"rizki"})
data_dict.update({"c":"alamsyah"})
print(data_dict)

data_dict.pop("b")
print(data_dict)
data_dict.popitem()
print(data_dict)

print(data_dict.keys())
print(data_dict.values())

print(data_dict["a"])
# print(data_dict["b"]) # error
print(data_dict.get("a")) 
print(data_dict.get("b"))  # none


template_dict = {
	"nama":None,
	"nim":None,
	"email":None
}

mhs = dict.fromkeys(template_dict.keys())
print(mhs)