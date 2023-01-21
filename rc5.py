from typing import Tuple

class RC5():
    def __init__(self,W,R,b):
        self.W=W
        self.R=R
        self.b=b
        self.u=self.W//8
        self.t=2*(self.R+1)
        self.c=max(self.b,1)//(self.u)
        self.L=[0]*self.c
        if self.W == 16:
            self.P,self.Q=(0xB7E1, 0x9E37)
        elif self.W == 32:
            self.P,self.Q= (0xB7E15163, 0x9E3779B9)
        elif self.W == 64:
            self.P,self.Q= (0xB7E151628AED2A6B, 0x9E3779B97F4A7C15)

    def __lshift(self, val, n):
        n %= self.w
        return ((val << n) & self.mask) | ((val & self.mask) >> (self.w - n))

    def __rshift(self, val, n):
        n %= self.w
        return ((val & self.mask) >> n) | (val << (self.w - n) & self.mask)


    def split(self,key:bytes):
        key+=b'\x00'*min(self.b%self.u,(self.u-self.b%(self.u)))
        for i in range(self.b-1,-1,-1):
            self.L[i//(self.u)]=(self.L[i//(self.u)]<<8)+key[i]

        return self.L

    def expansion(self):
        P,Q=self.const_gen()
        S=[P]
        for i in range(1,t):
            S.append(S[-1]+Q)

    def mixing(self):
        i=j=0
        A=B=0
        c=0
        for i in range(3*max(self.t,c)):
            A=S[i]=(S[i]+A+B)<<3
            B=L[j]=(L[j]+A+B)<<(A+B)
            i=(i+1)%self.t
            j=(j+1)%c
    def encrypt(plaintext,key):
        A=A+S[0]
        B=B+S[1]
        for i in range(1,self.r+1):
            A=((A^B)<<B)+S[2*i]
            B=((B^A)<<A)+S[2*i+1]
        
    def decrypt():
        for i in range(r,0,-1):
            B=((B-S[2*i+1])>>A)^A
            A=((A-S[2*i])>>B)^B
        B=B-S[1]
        A=A-S[0]
if __name__=="__main__":
    pass