fr = open('sing.in','r',encoding='utf-8')
fw = open('sing.out','w',encoding='utf-8')

scores ={}
for line in fr:
    items = line.strip().split(',')
    name = items[0]
    score = [float(x) for x in items[1:]]
    score.sort()
    score = score[1:-1]
    average = round(sum(score) / len(score), 2)
    average = '{:.2f}'.format(average)
    scores[name] = average
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
for name, score in sorted_scores:
    fw.write(f'{name}:{score}\n')
