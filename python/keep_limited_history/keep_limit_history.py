# ------------------------------------------------------------
# --  Title: keep_limit_history.py
# --  Description: keep limited history when reading a file.
# --  Author: Dong Haxia
# --  Date: 2020-7-14
# ------------------------------------------------------------


from collections import deque

# Generator function
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)

    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# Example use on a file
with open(r'C:\HPE-file\frequent-use\Scripts-personal\python\limited_history.txt') as f: 
    for line, prevlines in search(f, "python", 3):
        for pline in prevlines:
            print(pline, end='')
        print(line, end='')
        print('_'*20)    
        print('\n\n\n')        