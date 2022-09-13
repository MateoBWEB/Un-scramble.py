#UNSCRAMBLE.PY








jumbled_flag = 'ocip{FTC0l_I4_t5m_ll0m_y_y3nbc7ceac6ÿ°}'

# break up into 4 char blocks 

blocks = []
for i in range(0, len(jumbled_flag),4):
    chunk = jumbled_flag[i:]
    if len(chunk) > 4:
        chunk = chunk[0:4]

    blocks.append(''.join(chunk))


#reverse the blocks and put together
flag = ''
for block in blocks:
    flag = flag + block[::-1]

print(flag)