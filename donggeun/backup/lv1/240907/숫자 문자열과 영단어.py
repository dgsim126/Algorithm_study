def solution(s):
    result=""

    i= 0
    while(i<len(s)):
        if(s[i]=="z"):
            i+=4
            result+="0"
        elif(s[i]=="o"):
            i+=3
            result+="1"
        elif(s[i]=="t"):
            if(s[i+1]=="w"):
                i+=3
                result+="2"
            elif(s[i+1]=="h"):
                i+=5
                result+="3"
        elif(s[i]=="f"):
            if(s[i+1]=="o"):
                i+=4
                result+="4"
            elif(s[i+1]=="i"):
                i+=4
                result+="5"
        elif(s[i]=="s"):
            if(s[i+1]=="i"):
                i+=3
                result+="6"
            elif(s[i+1]=="e"):
                i+=5
                result+="7"
        elif(s[i]=="e"):
            i+=5
            result+="8"
        elif(s[i]=="n"):
            i+=4
            result+="9"
        else:
            result+=str(s[i])
            i+=1

    return int(result)

## main ##
s= "23four5six7"
print(solution(s))