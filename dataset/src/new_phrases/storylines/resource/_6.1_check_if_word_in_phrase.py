import time
import _6_sentences as _6
import re

if __name__ == "__main__":
    print('start')
    start = time.time()
    count = 0
    bad_phrases = []
    for item in _6.sentences:
        w = item['word']
        phrase = item['phrase']        
        if not w.lower() in phrase.lower():
            print(f'{w} NOT IN {phrase}')
            bad_phrases.append(item)            
            count += 1
    with open('./_6.2_sentences_to_fix.py','w') as f:
        f.write(f'bad_phrases = [\n')
        for item in bad_phrases:
            f.write(f'{item},\n')
        f.write('\n]')
    print('END')
    print(f'count: {count}')
    print(f'Time ellapsed: {time.time()-start} seconds.')
        