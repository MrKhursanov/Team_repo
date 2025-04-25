from collections import Counter

def modes(a):
    dict = Counter(a)
    mode = [key for key, value in dict.items() if value==max(dict.values()) ]
    if len(mode)==1:
        return mode
    else:
        return -1