# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
s = "hello python"
print("length:", s.upper())
print("lower case:",s.lower())
print("character at index 6:",s[6])
print("position of python:",s.find("python"))
print("slice:",s[6:])
print("replace:",s.replace("python","world"))
print("contains python:","python" in s)
print("concatenation:", s + " programming")
s2 = "hello                 world"
print("trim:",s2.strip())