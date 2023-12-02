with open("input.txt") as f:
    lines = f.read().splitlines()

res = 0

for line in lines:
    num = ""
    for char in line:
        if char.isdigit():
            num += char
            break
        
    for char in line[::-1]:
        if char.isdigit():
            num += char
            break
    
    res += int(num) 
    
print(res)