import re
import regexes as regexes
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



text = 'RT @tom_watson: face_with_tears_of_joy aight Russia \u201Cwe\u2019ll give you evidence \U0001F609\U0001F609\u201D on UK air strikes in Syria very good. https://t.co/Pf45W4I7wZ dsds'




text_demoji = emoji.demojize(text)
print(text_demoji)

dict_emoji = load_emoji('emoji.txt')
tokens = replace_emoji(text_demoji, dict_emoji)
print(tokens)
tokens = remove_special_text(tokens)
print(tokens)

tokens = nltk.word_tokenize(tokens)
print(tokens)

# tweet_url_cleaned = remove_urls(tweet_text) # 3. Remove urls
#     tokens = nltk.word_tokenize(tweet_url_cleaned) # 2. Tokenize the text
#     tokens = remove_tweet_specific_chars(tokens)
#     tokens = replace_slang(tokens,dicoSlang)