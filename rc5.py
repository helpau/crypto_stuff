from typing import Tuple
import numpy as np

class RC5():
    def __init__(self,W,R,b):
        self.W=W
        self.R=R
        self.b=b
        self.u=self.W//8
        self.t=2*(self.R+1)
        self.c=max(self.b,1)//(self.u)
        self.L=[0]*self.c
        self.S=[]
        self.mod = 2 ** self.W
        self.mask = self.mod - 1
        if self.W == 16:
            self.P,self.Q=(0xB7E1, 0x9E37)
        elif self.W == 32:
            self.P,self.Q= (0xB7E15163, 0x9E3779B9)
        elif self.W == 64:
            self.P,self.Q= (0xB7E151628AED2A6B, 0x9E3779B97F4A7C15)
        self.A=0
        self.B=0

    def uint(self,n:int):
        if self.W==16:
            return np.uint16(n)
        if self.W==32:
            return np.uint32(n)
        return np.uint64(n)
    def split(self,key:bytes):
        key+=b'\x00'*min(self.b%self.u,(self.u-self.b%(self.u)))
        for i in range(self.b-1,-1,-1):
            self.L[i//(self.u)]=(self.L[i//(self.u)]<<8)+key[i]

        return self.L

    def extend(self):
        self.S=[self.P]
        for i in range(1,self.t):
            self.S.append((self.S[i-1]+self.Q)%self.mod)
        return self.S

    def mixing(self):
        i=j=0
        A=B=0
        for counter in range(3*max(self.t,self.c)):
            A=self.S[i]=np.left_shift(self.uint(self.S[i]+A+B),3)
            B=self.L[j]=np.left_shift(self.uint(self.L[j]+A+B),self.uint(A+B))
            i=(i+1)%self.t
            j=(j+1)%self.c
        self.A,self.B=A,B
        return (A,B)
    def encrypt_block(self,plaintext,key):
        self.split(key)
        self.extend()
        self.mixing()
        self.A=self.A+self.S[0]
        self.B=self.B+self.S[1]
        for i in range(1,self.R+1):
            self.A=(self.__lshift(self.A^self.B,self.B)+self.S[2*i])%self.mod
            self.B=(self.__lshift(self.B^self.A,self.A)+self.S[2*i+1])%self.mod

        return (self.A.to_bytes(self.u, byteorder='big')
                + self.B.to_bytes(self.u, byteorder='big')) 
        
    def decrypt_block():
        for i in range(r,0,-1):
            B=((B-S[2*i+1])>>A)^A
            A=((A-S[2*i])>>B)^B
        B=B-S[1]
        A=A-S[0]
if __name__=="__main__":
    pass