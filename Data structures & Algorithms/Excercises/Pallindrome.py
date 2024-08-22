def pallindromeChecker(n):
    for i in range(0,int(len(n)/2),1):
        if n[i] != n[len(n)-i-1]:
            return False
        else:
            return True
        
    
ans = pallindromeChecker("LOL")

if (ans):
    print("Yes pallindrome")

else:
    print("Not pallindrome")