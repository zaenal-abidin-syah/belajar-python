"""
mengecek apakah parenthesis checking

operator = +-&/
operand = abc
kurung = ()

1. cek 

"""



import stack as st
import os

def parenthesisChecking(strMath:str)->bool:
	print(f"Mengecek string math {strMath}".center(50, "="))
	stack = st.stack()
	operator = "+-*/"
	kurung = {"(":")","{":"}","[":"]"}
	for i in strMath:
		if i in kurung.keys():
			st.push(stack, i)
		elif i in kurung.values():
			if st.isEmpty(stack):
				return False
			elif i == kurung[st.peek(stack)]:
				st.pop(stack)
			elif i != kurung[st.peek(stack)]:
				print(f"kurung {i} tidak sama dengan {st.peek(stack)}")
				return False
	
	else:
		return True		













