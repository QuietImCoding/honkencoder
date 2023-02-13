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

def printwrapped(text, banner, pure):
    if not pure:
        print(banner)
    print(text)

ustring = "USAGE: python honkencoder.py [honkify/dehonkify]"
PURE_MODE = len(sys.argv) > 2
try: 
    if sys.argv[1] == 'honkify':
        printwrapped(honkify(intext.strip()),
                     " ~~~ HONKIFYING ~~~ ", PURE_MODE)
    elif sys.argv[1] == 'dehonkify':
        try:
            printwrapped(dehonkify(intext.strip()),
                     " ~~~ ATTEMPTING TO DE-HONKIFY ~~~ ", PURE_MODE)
        except:
            exit("de-honkification failed...")
    else:
        print(ustring)
except Exception as h:
    print(h)
