def sort_sentence(sentence):
    sentence = list(map(str, sentence.split()))
    a = []
    for i in range(0, len(sentence)):
        a.append(min(sentence, key=len))
        sentence.remove(min(sentence, key=len))
    ch = a[::-1].pop().title()
    a.remove(a[0])
    return ch + ' ' + ' '.join(a).lower()