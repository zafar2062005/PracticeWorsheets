def median(x):
    x = sorted(x)
    if len(x)%2 != 0:
        middle = len(x)//2
        a = x[middle]
        return a
    else:
        middle = len(x)//2
        a = (x[middle] + x[middle-1])/2
        return a             
# print(median([4,1,2,6,3,5]))

def mode(x):
    counter = {}
    a = sorted(list(set(x)))
    for i in a:
        counter.update({i : x.count(i)})
    max_key = max(counter, key=counter.get) 
    return max_key
# print(mode([1,2,2,2,3,3,3,3,4,3]))

clues = [0, 1, 2, 3, 4]
pos = 3

def visit(clues, pos):
    if clues[pos] == None:
       pass
    else:              
       i = clues[pos]
       clues[pos] = None
       visit(clues, i)       

print(visit(clues, pos))

s1 = input().strip()
s2 = input().strip()

def edit_distance(s1, s2):
    distance = abs(len(s1) - len(s2))
    s1 = s1.lower()
    s2 = s2.lower()
    
    if len(s1) == len(s2):
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
        return count
    else:
        count = 0
        count += abs(len(s1)-len(s2))
        longest = s1 if len(s1) > len(s2) else s2 
        shortest = s1 if len(s1) < len(s2) else s2 
        lst = []
        for i in range(abs(len(s1) - len(s2))+1):
               lst.append(edit_distance(shortest, longest[i : len(shortest)+i]))
    
        return count + min(lst)    
print(edit_distance(s1, s2))