def jaccard(str1,str2):
    set1,set2=set(str1.split()),set(str2.split())
    intersection=set1.intersection(set2)
    union=set1.union(set2)
    return len(intersection)/len(union)
s1="data sci is fun"
s2="xyz"
print("jaccard index is :",jaccard(s1,s2))