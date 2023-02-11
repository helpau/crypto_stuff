from rc5 import RC5
rc5_1=RC5(16,12,4)
rc5_2=RC5(32,12,16)
rc5_3=RC5(64,12,16)
rc5_4=RC5(32,12,16)
def test_const():
    assert (rc5_1.P,rc5_1.Q)==(0xB7E1,0x9E37)
    assert (rc5_2.P,rc5_2.Q)==(0xB7E15163,0x9E3779B9)
    assert (rc5_3.P,rc5_3.Q)==(0xB7E151628AED2A6B,0x9E3779B97F4A7C15)

def test_split():
    assert rc5_1.split(b'\0'*4)==[0]*2
    assert rc5_1.split(b'\x01\x23\x45\x67')==[8961, 26437]

def test_extend():
    assert rc5_1.extend()==[47073, 22040, 62543, 37510, 12477, 52980, 27947, 2914, 43417, 18384, 58887, 33854, 8821, 49324, 24291, 64794, 39761, 14728, 55231, 30198, 5165, 45668, 20635, 61138, 36105, 11072]

def test_mixing():
    assert rc5_1.mixing()==(55154,14826)

def test_encrypt_block():
    assert False

def test_decrypt_block():
    assert False