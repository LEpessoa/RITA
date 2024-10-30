# List of sentences representing slices of storylines for each commercially available item in the full_list.py
import time
sentences = {

}

if __name__ == "__main__":
    start = time.time()
    phrases = []
    with open("./_6_sentences.py", 'w') as f:
        phrase_count = 0
        for phrase_dic in all_sentences:
            for key in phrase_dic:
                for phrase in phrase_dic[key]:
                    phrases.append(
                        {'type': 'DEVICE', 'word': key, 'phrase': phrase})
        print(f'phrase count: {len(phrases)}')
        print(f'This operation took {time.time()-start} seconds to complete.')
        f.write(f'{phrases}')
    # for l in all_sentences:
    #     for k in l.keys():
    #         if len(l[k]) != 5:
    #             print(f'Key: {k}')
