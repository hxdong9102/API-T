# -----------------------------------------------------------------
# --  Title: del_dup_line.py
# --  Description: Eliminate duplicate lines when reading a file.
# --  Author: Dong Haixia
# --  Date: 2020-7-15
# ------------------------------------------------------------------

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


# Read a file
with open(r"C:\HPE-file\frequent-use\Scripts-personal\python\del_duplicate\duplicate.txt", 'r') as f:
    for line in dedupe(f):
        print(line)