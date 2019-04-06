a1=0x55
a2=0x55

id=0x01
ll=0x07
cmd1=0x01
par1=0xb2
par2=0x00
par3=0x00
par4=0x00
print(id)
print(ll)
print(cmd1)
print(par1)
print(par2)
print((int(id+ll+cmd1+par1+par2+par3+par4)))
print(hex(~(id+ll+cmd1+par1+par2+par3+par4)&0xff))


a=0x01
print(~a&0xff)