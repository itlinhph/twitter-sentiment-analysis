import re
import nltk
import emoji


def remove_special_text(tweet):
    tokens = re.sub(r'(http\S+)|(@\S+)|RT|\#|\.|:', ' ', tweet)
    
    return tokens

def load_emoji(filename):
    
    dict_emoji = {}
    with open(filename) as emoji_sys_file:
        for line in emoji_sys_file:
            line = line[:-1]
            emoji_sysbol, text = line.partition("\t")[::2]
            dict_emoji[emoji_sysbol.strip()] = text
    # print(dict_emoji)
    return dict_emoji

def replace_emoji(tokens, dict_emoji):

    for emoji in dict_emoji:
        tokens = tokens.replace(emoji, dict_emoji[emoji])

    # tokens = [token if not token in dict_emoji else dict_emoji[token] for token in tokens]
    return tokens

def load_dictionary(filename):
    dic = [line.strip() for line in open(filename, 'r')]
    return dic


def evalue_score(tokens, positve_dict, negative_dict):
    
    pos_score = 0
    neg_score = 0
    for word in tokens:
        if word in positve_dict:
            pos_score = pos_score +1
            print(word)
        elif word in negative_dict:
            neg_score = neg_score +1
    print("pos_score: ", pos_score, "neg: ", neg_score)
    return pos_score - neg_score



text = 'RT @tom_watson: face_with_tears_of_joy aight Russia \u201Cwe\u2019ll give you evidence \U0001F609\U0001F609\u201D on UK air strikes in Syria very good. https://t.co/Pf45W4I7wZ dsds'




text_demoji = emoji.demojize(text)

dict_emoji = load_emoji('emoji.txt')
tokens = replace_emoji(text_demoji, dict_emoji)
tokens = remove_special_text(tokens)

tokens = nltk.word_tokenize(tokens)

positve_dict = load_dictionary('positive-words.txt')
negative_dict = load_dictionary('negative-words.txt')

# positve_dict = load_dictionary('test.txt')
# negative_dict = load_dictionary('test.txt')

score = evalue_score(tokens, positve_dict, negative_dict)

if score > 0 :
    print("Positive!")
elif score <0 :
    print("Negative!")
else:
    print("Neutral!")