import pandas
import string


alphabets = list(string.ascii_lowercase)
hindi= pandas.read_csv("csv_file.csv")
sp = pandas.read_csv("special.csv")

hindi_dict = hindi.to_dict(orient="list")
sp_dict = sp.to_dict(orient="list")
print(hindi_dict)

word_list = hindi_dict["Word"]
sp_word = sp_dict["special"]
print(sp_word)
print(word_list)

alphabets.extend(sp_word)
print(alphabets)
final_name=[]

for name in word_list:
    for letter in name:
        if letter not in alphabets:
            final_name.append(letter)
    final_name.append(" ")

str1 = ''.join(final_name)
winner = str1.split(" ")

if "ẽ" in alphabets:
    print("yes")

freq_hindi = pandas.DataFrame(winner)
freq_hindi.to_csv("hindi_only.csv", index= False)