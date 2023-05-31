def find_duplicates(data):
    hash_table = {}
    duplicates = []

    for item in data:
        if item in hash_table:
            duplicates.append(item)
        else:
            hash_table[item] = True

    return duplicates

# Contoh penggunaan
data = [2, 4, 6, 8, 2, 10, 4, 12, 14, 6, 16, 18, 20, 8, 12]
duplicate_items = find_duplicates(data)
print("Data duplikat:", duplicate_items)
