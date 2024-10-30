import _2_commercial_examples_lists as im;
import time

start = time.time()

full_list = []

for k in im.lists_dic:     
    full_list.extend(im.lists_dic[k])
    print(f'Key: {k}')
    print(f'LenFL: {len(full_list)}')

with open("./_3_full_commecrial_examples_list.py","w") as f3:
    f3.write(f'full_list = {full_list}')
print('fin')
print("Elapsed: %s seconds" % round((time.time()-start),2))
