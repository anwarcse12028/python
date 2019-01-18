import  math
d1 = 'the cat sat on the hat'
d2 = 'the dog ate the cat and the hat'

d1_list = d1.split()
d1_dic = {}

#  Counting number of times each word comes up in the list
for dll in d1_list:
     d1_dic[dll] = d1_dic.get(dll, 0) + 1

d2_list = d2.split()
d2_dic = {}
for dll in d2_list:
     d2_dic[dll] = d2_dic.get(dll, 0) + 1  # count each word


combine = d1 +' '+ d2 # combine all string in a single string
unique_list = sorted(set(combine.split())) # split each word and sort unique word

# -----------------    Count Vector -------------------------
print('\n\n--------------------Using Count Vector: Word Embedding Matrix is ----------------------------\n\n')
print('Here D = 2 and Term = ',len(unique_list))
print('key word = ', end='  ')
for ll in unique_list:
    print(ll, end= ' ')
print('\nd1       = ', end= '  ')
for ll in unique_list:
    print(d1_dic.get(ll, 0), end = '   ')
print('\nd2       =', end= '   ')
for ll in unique_list:
    print(d2_dic.get(ll, 0), end = '   ')



# ----------TF-IDF( Term Frequency times inverse document frequency )----------------------

# TF = (Number of times term t appears in a document)/(Number of terms in the document)
def TF(t,tn):
    return t/tn

# IDF = log(N/n), where, N is the number of documents and n is the number of documents a term t has appeared in.
def IDF(total_doc, no_doc_for_t):
    return math.log(total_doc/no_doc_for_t)

# TF-IDF(t, document) = TF(t, document) * IDF(t)

def TF_IDF(no_of_t, total_term_in_a_doc, total_doc, no_doc_for_t):
    return  TF(no_of_t,total_term_in_a_doc)*IDF(total_doc, no_doc_for_t)
print('\n\n--------------------Using TF - IDF : Word Embedding Matrix is(Consider term from d2 string only) ----------------------------\n\n')
print('Word   TF-IDF')
for li in unique_list:
    no_of_doc_for_li = 0
    if d1_dic.get(li, 0) > 0:
        no_of_doc_for_li += 1
    if d2_dic.get(li, 0) > 0:
        no_of_doc_for_li += 1

    print(li+' = ', TF_IDF(d2_dic.get(li, 0), len(d2.split()), 2, no_of_doc_for_li))

# ------- Co-Occurrence Matrix with a fixed context window -----------------

#count(w(next)|w(current))

def total_count(length, word1,word2, str):
    str_list = str.split()
    count = 0
    flag = 0
    str_len = len(str_list)
    for ll in range(len(str_list)):
        if(word1 == str_list[ll]):
            for i in range(length):
                if((ll+i+1)<str_len):
                    if(word2 == str_list[ll+i+1]):
                        flag = 1
                        break
            if(flag == 1):
                count +=1

    return count

print('\n\n-------------------- Using Co-Occurrence Matrix : Word Embedding Matrix is(Fixed length is 2) ----------------------------\n\n')
string = 'He is not lazy. He is intelligent. He is smart.'
string = string.replace('.','',)
print(string)
string_list = list(set(string.split()))

for ii in range(len(string_list)):
    for ij in range(len(string_list)):
        print(string_list[ii], string_list[ij], total_count(2, string_list[ii], string_list[ij], string))


