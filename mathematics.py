
'''EXPONENT MATH FUNCTIONS - VERSION 2.1

Copyright 2019 Jieruei Chang
Licensed under the MIT License

BASIC MATH FUNCTIONS.
'''

import math, pygame
try:
    import wolframalpha
    client = wolframalpha.Client('key') #Put wolframalpha key here to use the Wolfram|Alpha function.
    wolframOn = True
except:
    wolframOn = False
  
'''Initial expression handling and basic computation'''
def compute(expression):
    try:
        expression = expression.replace('^','**')
        return [eval(expression)]
    except:
        try:
            parsed = parse(expression)
            return determine(parsed)
        except:
            if wolframOn:    return wolfram(expression)   

'''First decompose the expression'''
def parse(expression):
    termlist=[]
    precede = ''
    for char in expression:
        if char == '+' or char == '-' or char == '=' or char == ';' or char == ':' or char == ',':
            termlist.append(precede)
            termlist.append(char)
            precede = ''
            #print termlist
        elif char == '(':
            termlist.append(precede)
            precede = '('
        elif char == ')':
            precede += ')'
            termlist.append(precede)
            precede = ''
        elif char != ' ':
            precede += char
    termlist.append(precede)
    #print termlist
    l=len(termlist)
    for item in range(l-1):
        if termlist[item] == '':
            termlist.pop(item)
            #print termlist
    #print '---------'
    #print termlist
    return termlist

'''Determine the type of the expression'''
def determine(terms):
    if terms[0] == 'quad' and terms[1] == ':' and terms[2] != 'show':
        a = float(terms[2])
        b = float(terms[4])
        c = float(terms[6])
        return quadratic(a,b,c)
    elif terms[0] == 'quad' and terms[2] == 'show':
        a = float(terms[4])
        b = float(terms[6])
        c = float(terms[8])
        return showquadratic(a,b,c)        
    elif 'x^2' in terms[0]:
        a = float(terms[0].replace('x^2',''))
        if 'x' in terms[2]:
            b = float(terms[2].replace('x',''))
        else:
            b = 0.0
        if len(terms) == 7:
            c = float(terms[4])-float(terms[7])
            return quadratic(a,b,c)
        elif len(terms) == 5:
            print a
            print b
            print terms[4]
            return quadratic(a,b,float(terms[4]))
    elif terms[0] == 'linear' and terms[1] == ':':
        return linear(terms[2],terms[4],terms[6],terms[8])        
    elif '(' in terms[0] and terms[1] == ';':
        print "linear"
        return linear(terms[0][1],terms[0][3],terms[2][1],terms[2][3])
    else:
        print "kill"
        kill = 1/0

'''Linear functions'''
def linear(x1,y1,x2,y2,form='si'):
    #print "linear"
    '''try:
        print x1
        print y1
        print x2
        print y2
    except:
        print "oops"'''
    x1=float(x1)
    y1=float(y1)
    x2=float(x2)
    y2=float(y2)
    #print 'passed float test'
    slope = (y1-y2)/(x1-x2)
    b = y1-slope*x1
    #print 'passed slope'
    #str(slope)
    #str(b)
    #print 'passed final'   
    return ['y = '+str(slope)+'x + '+str(b)]

'''Factor quadratics'''
def factor(a,b,c):
    return 'FACTORING'

'''Use quadratic equation to solve'''    
def quadratic(a,b,c):
    print "quadratic"
    #print 'x = '+str((b*(-1)+(sqrt(b*b-4*a*c)))/2*a)+' , '+str((b*(-1)-(sqrt(b*b-4*a*c)))/2*a)
    return ['x = '+str((b*(-1)+(math.sqrt(b*b-4*a*c)))/(2*a))+' , '+str((b*(-1)-(math.sqrt(b*b-4*a*c)))/(2*a))]

'''Combinations and factorials'''
def choose(n,r):
    return (math.factorial(n))/(math.factorial(r)*math.factorial(n-r))

'''Graphing
def graph(surface, equation, xvalues, w=320, h=300):
    yvalues = []
    for i in xvalues:
        try:
            x = i
            yvalues.append(eval(equation))
        except:    pass
    pygame.draw.rect(surface,(255,255,255),(0,0,w,h))
    for i in range(len(xvalues)):
        pygame.draw.rect(surface,(0,0,0),(i*(len(xvalues)/w,h-yvalues[i],3,3)))'''

'''Use functions from the Math library'''
def cos(x):
    return math.cos(x)

def sin(x):
    return math.sin(x)

def tan(x):
    return math.tan(x)

def log(x):
    return math.log(x)

def sqrt(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)
pi = math.pi
e = math.e

'''Variables for use'''
totalvar = []
for x in range(26):
    totalvar.append(0)
A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z=totalvar

'''Simplify the expression, if possible'''    
def simplify(terms):
    return 'something'

'''Send query to Wolfram Alpha as last resort'''

def wolfram(expression):
    global client
    res = client.query(expression).results
    for result in res:
        for key in result.keys():
            #print key
            key = str(key)
            if key == 'subpod':
                return [result['subpod'][u'plaintext']]

'''Basic interface'''
def main():
    print 'EXPONENT Mathematics Unit'
    while True:
        print '-------------------------'
        query = raw_input('> ')
        if query == 'exit':
            break
        for x in compute(query):
            print x

if __name__ == '__main__':
    main()
