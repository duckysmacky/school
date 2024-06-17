line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))
m_out_hrs, m_out_min = line1[0], line1[1]
n_in_hrs, n_in_min = line1[2], line1[3]

n_out_hrs, n_out_min = line2[0], line2[1]
m_in_hrs, m_in_min = line2[2], line2[3]

total_hrs = 0

# Out Hours
if n_in_hrs > m_out_hrs:
    out_hrs = n_in_hrs - m_out_hrs
else:
    out_hrs = (n_in_hrs + 24) - m_out_hrs

# Out Minutes
if n_in_min > m_out_min:
    out_min = n_in_min - m_out_min
else:
    out_min = (n_in_min + 60) - m_out_min
    total_hrs += 1
    
# In Hours
if m_in_hrs > n_out_hrs:
    in_hrs = m_in_hrs - n_out_hrs
else:
    in_hrs = (m_in_hrs + 24) - n_out_hrs

# In Minutes
if m_in_min > n_out_min:
    in_min = m_in_min - n_out_min
else:
    in_min = (m_in_min + 60) - n_out_min
    total_hrs += 1
    
print(out_hrs, out_min)
print(in_hrs, in_min)

total_hrs = int((out_hrs / in_hrs) / 2)

print(total_hrs, out_min)
print(total_hrs, in_min)