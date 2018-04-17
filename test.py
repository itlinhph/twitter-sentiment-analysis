import yaml
import emoji
import re

# with open("syria2.yaml", "r") as input_file:
#     data = yaml.load(input_file)
#     print(len(data))
#     for item in data:
#         print (item)
#     print(data[1])


print(emoji.demojize( '\u2019 😭😭😭'))


# myvars = {}
# with open("emoij.txt") as myfile:
#     for line in myfile:
#         name, var = line.partition("\t")[::2]
#         myvars[name.strip()] = var

# print(myvars)

# if '121' in myvars:
#     print(myvars['121'])


# def remove_special_text(tweet):
#     # tokens = tweet.split(' ')
#     tokens = re.sub(r'http\S+', '', tweet)
#     URLless_string = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', tweet)
#     print(URLless_string)
#     print(tokens)
#     return tokens

# text = 'RT @tom_watson: face_with_tears_of_joy afaik Link to the full legal advice on UK air strikes in Syria. https://t.co/Pf45W4I7wZ sdsds'

# print(remove_special_text(text))

# def load_boost_word(filename):
#     boost_word = {}
#     with open(filename) as boost_file :
#         for line in boost_file:
#             line = line[:-1]
#             word, score = line.partition("\t")[::2]
#             boost_word[word.strip()] = int(score)
#     return boost_word

# boost = load_boost_word('boost-word.txt')
# print(boost)