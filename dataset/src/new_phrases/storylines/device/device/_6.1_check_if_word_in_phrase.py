import time
import _6_sentences_formatted as _6
import re

# Program to check if for every phrase in _6_ the "word" appears in the "phrase".
# The tuples where the "word" does no appear in the "phase" are written to _6.2_ .
# Fix the sentences that need fixing manually in _6_ and run _6.3_ to generate the final product in result.npy.
if __name__ == "__main__":
    print("start")
    start = time.time()
    count = 0
    bad_phrases = []
    for item in _6.sentences_formatted:
        w = item["word"]
        phrase = item["phrase"]
        if not w.lower() in phrase.lower():
            print(f"{w} NOT IN {phrase}")
            bad_phrases.append(item)
            count += 1
    with open("./_6.2_sentences_to_fix.py", "w") as f:
        f.write(f"sentences_to_fix = [\n")
        for item in bad_phrases:
            f.write(f"{item},\n")
        f.write("\n]")
    print("END")
    print(f"count: {count}")
    print(f"Time ellapsed: {time.time()-start} seconds.")
