import _2_commercial_examples_list as im;
import time

start = time.time()

full_list = []

for k in im.lists_dic:     
    full_list.extend(im.lists_dic[k])    

with open("./_3_full_commecrial_examples_list.py","w") as f3:
    f3.write(f'full_list = [\n')
    for i in full_list:
        f3.write(f"""'{i}',\n""")
    f3.write(']')
print('fin')
print("Elapsed: %s seconds" % round((time.time()-start),2))
