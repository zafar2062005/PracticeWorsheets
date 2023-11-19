arr1 = [[1,2,3], [4,5,6], [9,8,9]]
def diagonalDifference(arr):
    n = len(arr)
    l1 = []
    l2 = []
    for i in range(n):
        l1.append(arr[i][i])
        l2.append(arr[i][-(i+1)])
    return abs(sum(l1) - sum(l2))
# print(diagonalDifference(arr1))

narray  = [
    [0,0,0,0],
    [0,0,0,1],
    [0,0,0,0],
    [0,0,0,0],
    [0,1,0,0],
    [0,0,0,0]
]
def rec_distance(narray):
    col = []
    row = []
    for i in narray:
        if 1 in i:
            row.append(i.index(1))

    for i in range(len(narray)):        
        if 1 in narray[i]:
            col.append(i)    
    print(abs(abs(row[0]-row[1])+abs(col[0]-col[1])))
rec_distance(narray)
print(rec_distance(narray)) 

multid = ["stri", 3.0, 4.0, [5, 6, ["li", 2, [67]], False]]

def flat(x):
    flatlist = []
    output = []
    for i in x:
        if isinstance(i, list):
            flatlist.append("list")  # Append "list" to flatlist
            flatlist.extend(flat(i))
        else:
            flatlist.append(type(i).__name__)
    for i in flatlist:
        if not i in output:
            output.append(i)
    
    return output

print(flat(multid))


nested_list = [['Sarwan', 'EE', '2021'], ['Lulowalokand Wala', 'CND', '2021'], ['Hamza Junaid', 'EE', '2021'], ['Ahsan Qadeer', 'CS', '2020'], ['Muhammad Ali Bhutto', 'EE', '2020'], ['Marium Habiby', 'SDP', '2021'], ['Adil Ali Khan', 'EE', '2021']]
sorted_list = sorted(nested_list, key=lambda x : (x[2] , x[1], x[0]))
print(sorted_list)


def rec_distance(grid):
    col = []
    row = []
    for i in grid:
        if "1" in i:
            if i.count("1")>1:
                x = i.find("1")
                y = x + 1 + i.find("1", x)
                row.append(x)
                row.append(y)
            else:
                row.append(i.index("1"))
    for i in range(len(grid)):
        if "1" in grid[i]:
            if grid[i].count("1")>1:
                col.append(i)
            col.append(i)
    return abs(row[0]-row[1]) + abs(col[0]-col[1])
      


