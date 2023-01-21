from rc5 import RC5
rc5_1=RC5(16,12,4)
rc5_2=RC5(32,12,16)
rc5_3=RC5(64,12,16)
def test_const():
    assert (rc5_1.P,rc5_1.Q)==(0xB7E1,0x9E37)
    assert (rc5_2.P,rc5_2.Q)==(0xB7E15163,0x9E3779B9)
    assert (rc5_3.P,rc5_3.Q)==(0xB7E151628AED2A6B,0x9E3779B97F4A7C15)

def test_split():
    assert rc5_1.split(b'\0'*4)==[0]*2
    assert rc5_1.split(b'\x01\x23\x45\x67')==[8961, 26437]

def test_encode():
    plaintext=0x00000000000000000000000000000000
    key=0x000000000000000000000000
    assert rc5.encode(w=32,r=12,b=16,plaintext=plaintext,key=key)==0x21A5DBEE154B8F6D