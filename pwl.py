
from itertools import product
import pyfiglet

H = '\033[1;31m'
L = '\033[1;37m'
X = '\033[1;33m' 

sfsf = pyfiglet.figlet_format('P w L')

print(H+sfsf)

print('# pass word list')
print(H+'''
                                                  INSTA:@__so1dier
''')

print((((((((((((H+'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ '))))))))))))

print ()
l_m = int ( input (( H+'[+]' ) + (((( L+' ENTER THE MINI LENGTH : ' ))))))

print((((((((((((H+'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ '))))))))))))

print()


l_x= int ( input (( H+'[+]' ) + ((((L+' ENTER THE MAX LENGTH : ' ))))))

print((((((((((((H+'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ '))))))))))))

print()


counter = 0

ch = str ( input (( H+'[+] ') + (((( L+' ENTER THE CHARTER : ' ))))))

print((((((((((((H+'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ '))))))))))))

print()


filename = str ( input (( H+'[+]' ) + (((( L+' ENTER FILE NAME : ' ))))))


file_open = open(filename,'w')

for i in range(l_m,l_x+1):
    
    for x in product(ch,repeat=i):
        
        word = ""''.join( x )
        
        file_open.write( word )
        
        file_open.write('\n')
        
        counter += 1
        

print((((((((((((H+'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ '))))))))))))

print()

print((L+"Your Wordlist Of | Passwords Ready✓✓ ".format(counter)))