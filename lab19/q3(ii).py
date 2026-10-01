#a
from DistUpgrade.utils import capitalize_first_word

name=["Reethika","Triveni","Anand","Sranya","Saran","Rithika","Rithu","Reethu","Bujju","Bannu"]
for x in name:
    x=x.upper()
    print(x)
m=[x.upper() for x in name ]
print(m)

#b
name=["jayashree nagesh","nithya ramakrishnan","shyam rajgopalan","swathi alagesan"]
reversed_list=[]
for n in range(len(name)):
    x=name[n].split(" ")
    rev_name=x[::-1]
    reversed_name=" ".join(rev_name)
    reversed_list.append(reversed_name)
print(reversed_list)


#reversed_list=list(reversed(reversed_list))
#print(reversed_list)

#c
names = ["jayashree nagesh","nithya ramakrishnan","shyam rajgopalan","swathi alagesan"]


formatted_names = [f"{first.capitalize()}.{last.capitalize()}" for first, last in names]



#(iii)
sentence = "She sells sea shells that she collects from the sea floor"
words = sentence.split()


longest_words = [word for word in words if len(word) == max(len(w) for w in words)]

print(longest_words)
