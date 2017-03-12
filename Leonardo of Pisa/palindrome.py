#Manil Bastola

import sys

def PalindromeDetectorCore(myStr, mark,acc):
    
    if mark <= acc:
        return True
    else:
        if myStr[mark].lower() == myStr[acc].lower():
            return PalindromeDetectorCore(myStr, mark-1,acc+1)
        else:
            return False

def PalindromeDetector(myStr):
    Alphanumerics = 'abcdefghijklmnopqrstuvwxyz0123456789'
    newStr = ''
    for ch in myStr.lower():
        if ch in Alphanumerics:
            newStr = newStr+ch
    return PalindromeDetectorCore(newStr, len(newStr)-1,0)

def main():
    if PalindromeDetector(sys.argv[1])==True:
        print('This is a Palindrome')
    else:
        print('This is not a Palindrome')

main()
            
        
            
            
            
        
    
    
