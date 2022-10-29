import pandas as pd

word_size = 3

# read data
df = pd.read_csv('data2.csv')
df['words'] = df['words'].astype('str')
df = df.loc[(df['words'].str.len() == word_size) & (~df['words'].str.contains('[0-9]')) & (~df['words'].str.contains('[.]')), :]
df = df['words']
words = df.to_list()
words = [word.upper() for word in words]

# preprocess
word_dict = {}
for word in words:
    for i in range(word_size):
        if word[:i+1] not in word_dict:
            word_dict[word[:i+1]] = []
        word_dict[word[:i+1]].append(word)

horizontals = []
verticals = []

# generator


def gen_horizontal():
    global word_size
    idx = len(verticals)
    prefix = ''.join([verticals[i][idx] for i in range(len(verticals))])
    if prefix not in word_dict:
        return False
    else:
        horizontals.append(word_dict[prefix][0])
        return True


def gen_vertical():
    global word_size
    idx = len(verticals)
    prefix = ''.join([horizontals[i][idx] for i in range(len(horizontals))])
    if prefix not in word_dict:
        return False
    else:
        verticals.append(word_dict[prefix][0])
        return True


def gen(start_word):
    global word_size, horizontals, verticals
    horizontals = [start_word]
    verticals = []
    while len(verticals) < word_size:
        if len(horizontals) > len(verticals):
            if not gen_vertical():
                return False
        else:
            if not gen_horizontal():
                return False
    return True


# results
for word in words:
    if gen(word):
        for line in horizontals:
            print(line)
        print('-'*word_size)
