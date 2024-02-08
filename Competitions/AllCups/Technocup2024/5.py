roman = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}
roman_ = new_dict = { value: key for key, value in roman.items() }

# 5 = V: IV (1 * 5) and VIII (5 * 1 * 1 * 1)
# 15 = XV: 


# Q = int(input())
# for i in range(Q):

x = int(input())
for dec_num in list(roman.values())[1:]:
    if x % dec_num:
        pass