import _2_commercial_examples_lists as im
import time

# Program to read the dictionaries in _2_ and create a list of tuples in _3_ with only the names of the commercial objects.
start = time.time()

full_list = []

for k in im.lists_dic:
    full_list.extend(im.lists_dic[k])
    print(f"Key: {k}")
    print(f"LenFL: {len(full_list)}")

with open("./_3_full_commecrial_examples_list.py", "w") as f3:
    f3.write(f"full_list = {full_list}")
print("fin")
print("Elapsed: %s seconds" % round((time.time() - start), 2))
