import sys, random

intext = sys.stdin.read()
if len(intext) == 0:
    exit('Pipe some text into stdin')

def byte2honk(bytein):
    v = ord(bytein)
    ostr = ""
    honk_l = "honk"
    honk_u = "HONK"
    ind = 0
    for i in range(8):
        pbit = v % 2
        ostr += honk_l[ind] if pbit else honk_u[ind]
        v >>= 1
        ind = (ind + 1) % 4
    return(ostr)

def honk2byte(honkin):
    obyte = 0
    for i in range(8):
        obyte += 2 ** i if honkin[i].islower() else 0 
    return(chr(obyte))
    
def honkify(intext):
    ostr = ""
    spice = " .!?-"
    honks = [byte2honk(a) for a in intext]
    for h in honks:
        i_1 = random.choice(spice) * random.randint(0,3)
        i_2 = random.choice(spice) * random.randint(0,3)        
        ostr += h[:4] + i_1 + h[4:] + i_2
    return(ostr)

def dehonkify(intext):
    honkies = ''.join(l for l in intext if l in "honkHONK")
    ostr = ''
    for honk in range(0,len(honkies), 8):
        ostr += honk2byte(honkies[honk:honk+8])
    return(ostr)

ustring = "USAGE: python honkencoder.py [honkify/dehonkify]"
try: 
    if sys.argv[1] == 'honkify':
        print(" ~~~ HONKIFYING ~~~ ")
        print(honkify(intext.strip()))
    elif sys.argv[1] == 'dehonkify':
        print(" ~~~ ATTEMPTING TO DE-HONKIFY ~~~ ")
        try:
            print(dehonkify(intext.strip()))
        except Exception as e:
            exit("Unable to de-honk input text")
    else:
        print(ustring)
except:
    print(ustring)
