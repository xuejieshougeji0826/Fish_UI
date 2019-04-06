 
import serial  
import time  
# 打开串口  
ser = serial.Serial('/dev/ttyAMA0', 115200)  


if ser.isOpen == False:
    ser.open()
print("chuankouyidakai")# 打开串口
qianzhui=0x55
id=0x01
lengh=0x07
cmd=0x01
par_di=0x02
par_gao=0xee
t_di=0x00
t_gao=0x00
message=hex(~(id+lengh+cmd+par_gao+par_di+t_di+t_gao)&0xff)
#a=hex（85）
final=b"UU\x01\x07\x01\x24\x01\x00\x00\xd1"
#final =str(a)+final
print(final)
ser.write(final)