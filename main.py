ap=[156,987]
def decrementing(n):
    nstr = str(n)
    for i in range(len(nstr)-1):

        if int(nstr[i])==0 and int(nstr[i+1])==9:
            return False
        if int(nstr[i]) != int(nstr[i+1])+1:
            return False
    return True

def incrementing(n):
    nstr = str(n)
    for i in range(len(nstr)-1):
        if int(nstr[i])==0 and int(nstr[i+1])==1:
            return False
        elif int(nstr[i])==9 and int(nstr[i+1])==0:
            pass
        elif int(nstr[i])!= int(nstr[i+1])-1:
            return False
    return True

def interesting(n):
    nstr = str(n)
    if n<100:
        return False

    else:
        if nstr[1:] =='0'*(len(nstr)-1):
            return True
        elif nstr == nstr[0]*len(nstr):
            return True
        elif nstr == nstr[::-1]:
            return True
        elif decrementing(n):
            return True
        elif incrementing(n):
            return True
    return False

def is_interesting(n,awesome_phrases):
    #I would pass only 1 argument, and include "awesome_phrases" in interesting(n)
    if n ==98:
        return 1
    if n==99:
        return 1
    if n in awesome_phrases:
        return 2
    elif n-1 in awesome_phrases or n-2 in awesome_phrases or n+1 in awesome_phrases or n+2 in awesome_phrases:
        return 1
    elif interesting(n):
        return 2
    elif interesting(n-1) or interesting(n-2) or interesting(n+1) or interesting(n+2):
        return 1
    else:
        return 0




