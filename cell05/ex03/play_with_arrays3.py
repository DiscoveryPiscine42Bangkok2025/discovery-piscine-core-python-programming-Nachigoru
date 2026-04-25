original_array =  [2, 8, 9, 48, 8, 22, -12, 2]
result_array = []

for num in original_array:
    if num > 5:
        result_array.append(num + 2)

unqiue_array = list(set(result_array))

print(original_array)
print(result_array)