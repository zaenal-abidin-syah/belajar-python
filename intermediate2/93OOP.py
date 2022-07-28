# stack
# import stack as st
# reverse words 

# def reverseW(w):
#     stack=st.stack()
#     str=''
#     for i in w:
#         st.push(stack,i)
#     for i in range(st.size(stack)):
#         str+=st.pop(stack)
#     return str

# print(reverseW("kasur rusak"))



#  meggunakna class
from stack import Stack as st

def reverseW(w):
    stack=st()
    str=''
    for i in w:
        stack.push(i)
    print(stack)
    for i in range(stack.size()):
        str+=stack.pop()
    return " ".join(str)


# print(reverseW('nawawi'))
print(dir(st))