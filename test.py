import yaml
import emoji
import re

# with open("syria2.yaml", "r") as input_file:
#     data = yaml.load(input_file)
#     print(len(data))
#     for item in data:
#         print (item)
#     print(data[1])




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


# def process_emoji(filein):
#     emoji_list = []
#     emoji_file = open(filein, 'r').read().split('\n')

#     for line in emoji_file:
#         line = line[2:]
#         line = line.lower()
#         # line = line.replace(' ', '_')
#         emoji_list.append(line)
#     return emoji_list

# emoji_list = process_emoji("emoji-explain.txt")
# # print(emoji_list)

# string = ""
# text_file = open("emoji2.txt", "w")
# for line in emoji_list:
#     string += line + "\n"
# text_file.write(string)
# text_file.close()



# def load_emoji(filename):
    
#     dict_emoji = {}
#     emoji_file = open(filename,'r').read().split('\n')
#     for line in emoji_file:
#         emoji_sysbol, text = line.partition("\t")[::2]
#         dict_emoji[emoji_sysbol.strip()] = text
#     return dict_emoji



# emoji2 = load_emoji('dictionary/emoji2.txt')

# # print(emoji2)
# emoji = load_emoji('dictionary/emoji.txt')
# # print(emoji)

# emoji2.update(emoji)
# print(emoji2)

# for key, value in emoji.items():
#     print(key, '=', value)

# string = ""
# text_file = open("emojiall.txt", "w")
# for atr in sorted(emoji2):
#     string += atr +"\t" +emoji2[atr]+ "\n"
# text_file.write(string)
# text_file.close()




# tweet = "@MarvelStudios it’s not available in my country 😭 #Avengers #InfinityWar"
# tokens = pre_process(tweet)
# print(tokens)

# query = "Select :Information:,AdditionalInformation,Price from Table"
# lista = "Information"
# var = "hide"

# pat = re.compile(r'\b' + lista + r'\b')
# query = pat.sub(var, query)
# print(query)


# tweet = "@MarvelStudios it’s not available in my country :loudly_crying_face: #Avengers #InfinityWar"
# emoji = "loudly_crying_face"
# dicte = "very good"

# pat2 = re.compile(r'\b' + emoji + r'\b')
# token2 = pat2.sub(dicte, tweet)

# token3 = tweet.replace(":loudly_crying_face:", "ok")
# print(token3)


print(emoji.demojize('\U0001F643 \U0001F618 \U0001F60C \U0001F917 \n 😍😂 😭 😎 \n ❤️\n 💖'))
