
a = hex(85)
b=b'xq180.0'
#b=b'xq1.0'
print(str(b))
print(str(b)[2],str(b)[3])
if str(b)[2]=="x" and str(b)[3]=="q":
    print("1")
    print(int(float(str(b)[4:-1])))