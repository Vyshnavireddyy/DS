def hd(str1,str2):
    if len(str1)!=len(str2):
        raise ValueError("The length of str1 and str2 must be the same")
    return sum(ch1!=ch2 for ch1,ch2 in zip(str1,str2))
s1="caroline is a bitch"
s2="katherin is so cunt"
h=hd(s1,s2)
print(f"Hamming Distance between '{s1}' and '{s2}' is :{h}")