import re
import nltk
import emoji
import yaml


def remove_special_text(tweet):
    tokens = re.sub(r'(http\S+)|(@\S+)|RT|\#|\.|:', ' ', tweet)
    
    return tokens

def load_emoji(filename):
    
    dict_emoji = {}
    with open(filename) as emoji_file:
        for line in emoji_file:
            line = line[:-1]
            emoji_sysbol, text = line.partition("\t")[::2]
            dict_emoji[emoji_sysbol.strip()] = text
    return dict_emoji

def replace_emoji(tokens, dict_emoji):

    for emoji in dict_emoji:
        tokens = tokens.replace(emoji, dict_emoji[emoji])

    return tokens

def load_dictionary(filename):
    dic = [line.strip() for line in open(filename, 'r')]
    return dic

def load_boost_word(filename):
    boost_word = {}
    with open(filename) as boost_file :
        for line in boost_file:
            line = line[:-1]
            word, score = line.partition("\t")[::2]
            boost_word[word.strip()] = int(score)
    return boost_word


def boost_word_score(i, tokens):
    word = ""
    if i>0:
        word = tokens[i-1]

    if word in boost_word:
        return boost_word[word]
    else:
        return 0

def evalue_score(tokens):
    pos_score = 0
    neg_score = 0
    for i,word in enumerate(tokens):
        if word in positve_dict:
            pos_score += (1 + boost_word_score(i, tokens) )
        elif word in negative_dict:
            neg_score += (1 + boost_word_score(i, tokens))
    
    # print("Pos: ", pos_score, "Neg: ", neg_score)
    return pos_score , neg_score

def pre_process(tweet):
    
    tweet_demoji = emoji.demojize(tweet)            # Convert emojition to text
    dict_emoji = load_emoji('dictionary/emoji.txt')            # Load file emoji
    tokens =replace_emoji(tweet_demoji, dict_emoji) # Replace emoji to text
    
    tokens = remove_special_text(tokens)            # Remove special text
    tokens = nltk.word_tokenize(tokens)             # Tokenize tweet
    
    return tokens

def process_dataset(input_file):
    
    with open(input_file, "r") as dataset :
        data = yaml.load(dataset)
        print(len(data))
        id =0
        str_file = "ID\tPositive_score\tNegative_score\tContent\n"

        for tweet in data:
            tokens = pre_process(tweet)
            #Evalue score:
            pos_score, neg_score = evalue_score(tokens)
            
            str_file += str(id) + "\t"+ str(pos_score) +"\t" + str(neg_score) + "\t" + tweet + "\n"
            id+=1

    text_file = open("output.txt", "w")
    text_file.write(str_file)
    text_file.close()


# tokens = pre_process(tweet)
# print(tokens)

#Load file:
positve_dict = load_dictionary('dictionary/positive-words.txt')
negative_dict = load_dictionary('dictionary/negative-words.txt')
boost_word = load_boost_word('dictionary/boost-word.txt')


process_dataset('syria2.yaml')
