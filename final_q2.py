
# coding: utf-8

# In[5]:


#第二題
import math
import numpy
def iexp(n):
    return complex(math.cos(n), math.sin(n))
 
def is_pow2(n):
    return False if n == 0 else (n == 1 or is_pow2(n >> 1))
 
def dft(xs):
    "naive dft"
    n = len(xs)
    return [sum((xs[k] * iexp(-2 * math.pi * i * k / n) for k in range(n)))
            for i in range(n)]
if __name__ == "__main__":
    x = [1,1,1,1]
    w = [1,1]
    y = numpy.convolve(w, x, mode='full')
    print(y)
    dfreqx = dft(x)
    dfreqw = dft(w)
    dfreqy = dft(y)
    print(dfreqx)
    print(dfreqw)
    print(dfreqy)
    pass


# In[3]:


#第一題
import math
def iexp(n):
    return complex(math.cos(n), math.sin(n))

def is_pow2(n):
    return False if n == 0 else (n == 1 or is_pow2(n >> 1))
 
def dft(xs):
    "naive dft"
    n = len(xs)
    return [sum((xs[k] * iexp(-2 * math.pi * i * k / n) for k in range(n)))
            for i in range(n)]
 
def dftinv(xs):
    "naive dft"
    n = len(xs)
    return [sum((xs[k] * iexp(2 * math.pi * i * k / n) for k in range(n))) / n
            for i in range(n)]
 
if __name__ == "__main__":
    wave1 = [1,0,0,0,0,0,0,0]
    wave2 = [1,1,1,1,1,1,1,1]
    wave3 = [1,-1,1,-1,1,-1,1,-1]
    wave4 = [3,0,2,0,2,0,2,0]
    dfreq5 = [1,1,0,0,0,0,1,1]
    dfreq6 = [1,1,0,0,0,0,0,1]
    wave7 = [1,1,0,0]
    wave8 = [1,1,0,0,0,0,0,0]
    dfreq1 = dft(wave1)
    dfreq2 = dft(wave2)
    dfreq3 = dft(wave3)
    dfreq4 = dft(wave4)
    wave5 = dftinv(dfreq5)
    wave6 = dftinv(dfreq6)
    dfreq7 = dft(wave7)
    dfreq8 = dft(wave8)
    print(dfreq1)
    print(dfreq2)
    print(dfreq3)
    print(dfreq4)
    print(wave5)
    print(wave6)
    print(dfreq7)
    print(dfreq8)
    pass

