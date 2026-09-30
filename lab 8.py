# Simple hash functions: division, mid-square, folding
def division_hash(key, table_size):
    return key %  table_size
def mid_square_hash(key, table_size):
    square = key * key
    square_text = str(square)
    middle_digits = square_text[2:4]
    return int (middle_digits) % table_size
def folding_hash(key, table_size):
    parts = str(key)
    total = 0
    while len(parts) > 0:
        total = total + int(parts[:2])
        parts = parts[:2]
    return total % table_size
keys = [1234, 5678, 9012]
size = 10
for k in keys:
    print("key:", k)
    print(" Division method:", division_hash(k, size))
    print(" Mid-square method:", mid_square_hash(k, size))
    print(" Folding method:", folding_hash(k, size))
 
