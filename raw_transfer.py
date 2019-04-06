import binascii
def tran(raw):
    qianzhui=0x55
    id = 0x01
    ll = 0x07
    cmd1 = 0x01
    print(qianzhui)
    print(str(id))
    print(ll)
    print(cmd1)
    q = (raw)
    r10 = (round(q * 1000 / 240))
    print((q * 1000 / 240))
    r16 = (int(q * 1000 / 240))
    raw_gao = (int(r10 / 0xff))
    raw_di = (r10 & 0xff)
    print(hex(raw_gao))
    print('0'+str(raw_gao))
    print(hex(raw_di))
    t_1 = 0x00
    t_2 = 0x00
    #t = 0x0000
    biaozhi=~(id + ll + cmd1 + raw_gao + raw_di + t_1 + t_2) & 0xff
    print(biaozhi)
    print(hex(biaozhi))
    #message=hex(qianzhui)+hex(qianzhui)+hex(id)+hex(ll)+hex(cmd1)+hex(raw_di)+hex(raw_gao)+hex(0)+hex(0)+hex(biaozhi)
    #message=(hex(id))
    #print(str(message).encode())
    final = b"\x55\x55\x01\x07\x01\x24\x01\x00\x00\xd1"
    print(final)
    print(binascii.a2b_hex("5555010701"+panduan(raw_di)+panduan(raw_gao)+"0000"+
                           panduan(int(biaozhi))))
    #a =chr(0x01)
    #print(a)
def panduan(a):
    if 0<=a<10:
        a="0"+str(a)
    elif a<0:
        a=hex(abs(a))[-2]+hex(a)[-1]
    else: a=hex(a)[-2]+hex(a)[-1]
    return a
tran(77)
