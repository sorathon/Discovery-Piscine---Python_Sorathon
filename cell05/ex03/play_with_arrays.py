original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []

for num in original_array :
    if num > 5 :
        new_array.append(num+2)

unique_array = set(new_array)

print(original_array) 
print(unique_array)