with open("sample.txt", "r", encoding="utf-8") as f:
  raw_text = f.read()

print("The total number of character:", len(raw_text))

import re
preprocessed = re.split(r'(\.\.\.|[,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print (preprocessed)



#2 Creating token Ids now
#making vocabulary
all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
print(vocab_size)

#3 assigning token IDs
vocab = {token:integer for integer, token in enumerate(all_words)}

for i, item in enumerate(vocab.items()):
  print(item)
  if i>= 50:
    break
#it will make a dictionary of the token IDs.


#4 We have to implement the tokenizer class with encode method and decode method
class simpleTokenizerV1:
  def __init__(self, vocab):
    self.str_to_int = vocab
    self.int_to_str = {i:s for s, i in vocab.items() }

  def encode(self, text):
    preprocessed = re.split(r'([,.:;?_"()\']|--|\s)', text)
    preprocessed = [item.strip() for item in preprocessed if item.strip()]
    ids = [self.str_to_int[s] for s in preprocessed]
    return ids
  
  def decode(self, ids):
    text = " ".join([self.int_to_str[i] for i in ids])
    #Replacing the spaces before the special functions
    text = re.sub(r'\s+([,.:;?!"])', r'\1', text)
    return text
  
tokenizer = simpleTokenizerV1(vocab)
text = """And others are busy showing off their fake life"""
ids = tokenizer.encode(text)
print (ids)
decode = tokenizer.decode(ids)
print("Decoded:", decode)






#Well GPTs dont use these word based tokenizer because there is a major disadvantage, if you come across a text which is not present in the vocabulary, you will get an error.
#To augmente the existing problem we come with the two new tokens <|unk|> and <|endoftext|>.

# <|endoftext|> also use to train GPTs.
#When working with multiple text sources, we add <|endoftext|> token between the texts.

all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend (["<|endoftext|>", "<|unk|>"])

vocab = {token:integer for integer, token in enumerate(all_tokens)}
new_tokens = len(vocab.items())
print("After adding the new 2 new tokens, The new total number of the tokens are:", (new_tokens))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Modify  the class
class simpleTokenizerv2:
  def __init__(self, vocab):
    self.str_to_int = vocab
    self.int_to_str = {i:s for s, i in vocab.items()}
  def encode(self, text):
    preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
    preprocessed = [item.strip() for item in preprocessed if item.strip()]
    preprocessed = [item if item in self.str_to_int else "<|unk|>" for item in preprocessed]
    ids = [self.str_to_int[s] for s in preprocessed]
    return (ids)
  def decode(self, ids):
    text = " ".join([self.int_to_str[i] for i in ids])
    #Replacing the space with the punctuations
    text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text)
    return text
  
tokenizer = simpleTokenizerv2(vocab)
text1 = "Hello, do you like And?"
text2 = "In another Reelers universe?"
text = " <|endoftext|> ".join((text1, text2))
ids = tokenizer.encode(text)
print (text)
word = tokenizer.decode(tokenizer.encode(text))
print (ids)

for i, item in enumerate(vocab.items()):
  print(item)
  if i>= 50:
    break