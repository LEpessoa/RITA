import time
import _5_sentences_divided as sd

if __name__ == "__main__":
    start = time.time()
    phrases = []
    with open("./_6_sentences.py", "w") as f:
        phrase_count = 0
        f.write("sentences = [\n")
        for key in sd.sentences:
            for phrase in sd.sentences[key]:
                p = {"type": "Device", "word": key, "phrase": phrase}
                phrases.append(p)
                f.write(f"{p},\n")
        print(f"phrase count: {len(phrases)}")
        print(f"This operation took {time.time()-start} seconds to complete.")
        f.write("]")
    # for l in all_sentences:
    #     for k in l.keys():
    #         if len(l[k]) != 5:
    #             print(f'Key: {k}')
