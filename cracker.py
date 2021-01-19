def inverse(totient,e):
    a=[totient,e]

    while a[-1]!=1:
        #print(a[-1])
        a.append(a[-2]%a[-1])

        # Define a sequence b
    b=[]
    for i in range(len(a)-2):
        b.append(a[i]//a[i+1])

        # Define a sequence c
    c=[0,1]
    for i in range(len(b)):
        c.append(c[-1]*b[i]+c[-2])

        # Mod if necessary
    if len(c)%2==0:
        return c[-1]
    else:
        return totient-c[-1]

def binaryExpo(a,b,mod):
    binarystring = bin(b)[2:]
    product = 1
    #print(binarystring)
    for char in binarystring[::-1]:

        if char == "1":
            product*=a
            product%=mod
        a*=a
        a%=mod
    return product

def texttoint(text):
    result = 0
    for char in text:
        result*=256
        result+=ord(char)
    return result

def intotext(num):
    result = ""
    while num > 0:
        result = chr(num%256)+result
        num //= 256
    return result

N = 699941932777
e = 131071

p = "prime1"
q = "prime2"

d = inverse((p-1)*(q-1),e)

interceptedmsg = 80316608948

print(intotext(binaryExpo(interceptedmsg,d,p*q)))
