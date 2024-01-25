#!/usr/bin/env python
# coding: utf-8

# In[1]:


# This line of code reads the contents of the Excel file located.
import pandas as pd

links = pd.read_excel("A:/Excel/assinment test/Input.xlsx") # Store all file in dataFrame where the dataFrame name is links


# In[2]:


#  This line of code to read  the Excel file where the output has to be saved.
excel_file_path = 'A:/Excel/assinment test/Output Data Structure.xlsx'
output = pd.read_excel(excel_file_path) # output is name of DataFrame


# In[3]:


index_number = 10 # Privide the number that calculate all the values for link that is present at index_number
url = links['URL'][index_number] # This code access the link from a particuler index by givving index number
ind = index_number


# In[ ]:





# In[4]:


# These all lines of code to ferch the Data from a specific wesite
import requests
from bs4 import BeautifulSoup

def extract_article(url):
    # Make an HTTP request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find and extract the title of the article
        title = soup.title.text.strip() if soup.title else "No Title"
        
        # Find and extract the article text
        article_text = ''
        article_body = soup.find('article')  # You may need to adjust this based on the HTML structure of the website

        if article_body:
            # Extract text from paragraphs within the article body
            paragraphs = article_body.find_all('p')
            article_text = '\n'.join([p.get_text() for p in paragraphs])
        else:
            # If there is no specific article tag, try extracting text from the entire page
            article_text = soup.get_text()

        return title, article_text
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None, None

# Example usage
title, article_text = extract_article(url)


# In[ ]:


if title and article_text:
    print(f"Title: {title}")
    print("\nArticle Text:")
    print(article_text)


# In[5]:


All_article_text =title + article_text # All text from Website


# In[ ]:


All_article_text


# In[ ]:


# This code is to save All_article_text in a text file at a location in pc
def save_string_to_file(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)
        print(f'Successfully saved the string to {file_path}')
    except Exception as e:
        print(f'Error: {e}')

file_location = "A:/Excel/assinment test/Text file/blackassign0001.txt" # Location of file with its name

save_string_to_file(All_article_text, file_location)


# In[ ]:


article_text


# In[6]:


article_text = article_text.lower()  # Change into lowerCase.


# In[7]:


len(article_text) # Check number of alphabets


# In[8]:


article_text


# In[9]:


import string


# In[10]:


article_text = article_text.replace("\n", " ").replace("\xa0", " ") # Remove "\n" and "\xa0" from string article_text


# In[11]:


article_text


# In[12]:


len(article_text)


# ### Import all Stop_word file and assign all words in single list

# In[13]:


# Specify the paths to your text files
file_paths = [
    'A:/Excel/assinment test/StopWords_Auditor.txt',
    'A:/Excel/assinment test/StopWords_Currencies.txt',
    'A:/Excel/assinment test/StopWords_DatesandNumbers.txt',
    'A:/Excel/assinment test/StopWords_Generic.txt',
    'A:/Excel/assinment test/StopWords_GenericLong.txt',
    'A:/Excel/assinment test/StopWords_Geographic.txt',
    'A:/Excel/assinment test/StopWords_Names.txt'
]

files_content = []  # Change the variable name to avoid naming conflicts

# Loop through each file path
for file_path in file_paths:
    # Open the file in read mode
    with open(file_path, 'r') as current_file:
        # Read the contents of the file and append to the list
        files_content.append(current_file.read())

# Now, files_content contains the content of each file in the file_paths list


# ### StopWords_Auditor

# In[14]:


Stop_Auditor = files_content[0] # Fetch Stop_Auditor from a list files_content


# In[15]:


Stop_Auditor


# In[16]:


Stop_Auditor = Stop_Auditor.replace("\n", " ").replace(" ", " ").lower() # Remove "\n" and "\xa0" from string article_text


# In[17]:


Stop_Auditor


# In[18]:


# Convert string to words of List
StopWords_Auditor = Stop_Auditor.split() 


# In[19]:


StopWords_Auditor


# ### StopWords_Currencies

# In[20]:


StopWords_Currencies = files_content[1]


# In[21]:


StopWords_Currencies


# In[22]:


StopWords_Currencies = StopWords_Currencies.replace("\n", " ").replace("|", " ").lower()


# In[23]:


StopWords_Currencies


# In[24]:


StopWords_Currencies =(str(StopWords_Currencies).lower()).split()


# In[25]:


StopWords_Currencies


# ### StopWords_DatesandNumbers

# In[26]:


#StopWords_DatesandNumbers
StopWords_DatesandNumbers =files_content[2]  # Fetch StopWords_DatesandNumbers from a list files_content


# In[27]:


StopWords_DatesandNumbers = StopWords_DatesandNumbers.replace("\n", " ").replace("|", " ").lower()


# In[28]:


StopWords_DatesandNumbers


# In[29]:


StopWords_DatesandNumbers =str(StopWords_DatesandNumbers).split()
StopWords_DatesandNumbers


# ## StopWords_Generic

# In[30]:


StopWords_Generic = files_content[3]


# In[31]:


StopWords_Generic = StopWords_Generic.replace("\n", " ").replace("|", " ").lower()


# In[32]:


StopWords_Generic


# In[33]:


StopWords_Generic =str(StopWords_Generic).split()
StopWords_Generic


# ### StopWords_GenericLong

# In[34]:


StopWords_GenericLong = files_content[4]  # Fetch StopWords_GenericLong from a list files_content


# In[35]:


StopWords_GenericLong


# In[36]:


StopWords_GenericLong = StopWords_GenericLong.replace("\n", " ").replace("|", " ").lower()


# In[37]:


StopWords_GenericLong =str(StopWords_GenericLong).split()


# ### StopWords_Geographic

# In[38]:


StopWords_Geographic = files_content[5] # Fetch StopWords_Geographic from a list files_content


# In[39]:


StopWords_Geographic


# In[40]:


StopWords_Geographic = StopWords_Geographic.replace("\n", " ").replace("|", " ").lower()
StopWords_Geographic


# In[41]:


StopWords_Geographic =str(StopWords_Geographic).split()


# In[42]:


StopWords_Geographic


# ### StopWords_Names

# In[43]:


StopWords_Names = files_content[6] # Fetch StopWords_Names from a list files_content
StopWords_Names


# In[44]:


StopWords_Names = StopWords_Names.replace("\n", " ").replace("|", " ").lower()
StopWords_Names


# In[45]:


StopWords_Names =str(StopWords_Names).split()


# In[46]:


StopWords_Names


# ### All Stop Words in a single string

# In[47]:


Stop_Words = StopWords_Auditor + StopWords_Currencies + StopWords_DatesandNumbers + StopWords_Generic + StopWords_GenericLong + StopWords_Geographic +StopWords_Names


# In[48]:


len(Stop_Words)


# In[49]:


# This code segment is setting up NLTK for processing English text data by importing the necessary modules and 
# obtaining a list of English stopwords and import word_tokenize

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

word = stopwords.words('english')


# In[50]:


All_Stop_Words = Stop_Words + word # Add All_Stop_Words in a single list


# In[51]:


len(All_Stop_Words) # Total number of Stop Words


# # Remove_stop_words

# In[52]:


# Remove the stop Words from the text
def remove_stop_words(text):
    new_text = []
    for word in text.split():
        if word in All_Stop_Words:
            new_text.append('')
        else:
            new_text.append(word)
            
            
    x =   new_text[:]
    new_text.clear()
    return " ".join(x)


# In[53]:


article_wo = remove_stop_words(article_text)


# In[54]:


# Use regular expression to remove numbers
import re

def remove_numbers(input_string):
    
    result = re.sub(r'\d+', '', input_string)
    return result

# Example usage:
article_wo = remove_numbers(article_wo)

print("Output String:", article_wo)


# In[55]:


article_wo


# In[ ]:





# In[56]:


article_w1 = article_wo.replace("   ", " ").replace(",", " ").lower()
article_w1


# In[57]:


article_w2 = article_w1.replace("  ", " ").replace(".", " ").lower()
article_w2


# In[58]:


article_w3 = article_w2.replace("   ", " ").replace(":", " ").lower()
article_w3


# In[60]:


len(article_w3)


# In[61]:


Clean_text =  ''.join(article_w3)


# In[62]:


# Convert string to list of words
Clean_list = Clean_text.split()


# In[63]:


Clean_list


# In[64]:


len(Clean_list)

The code "from nltk.tokenize import word_tokenize, sent_tokenize" imports the 
word_tokenize and sent_tokenize functions from the Natural Language Toolkit (nltk) for 
tokenizing words and sentences, respectively.
# In[65]:


import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Download NLTK data 
nltk.download('punkt')


# In[66]:


text_token = word_tokenize(Clean_text)


# In[67]:


text_token


# In[68]:


len(text_token)


# In[69]:


# This line od code to remove characters
def remove_special_characters(input_string):
    # Define the characters you want to remove
    special_characters = ['.',',', ':','-','.','-']

    # Remove special characters from the input string
    cleaned_string = ' '.join(char for char in input_string if char not in special_characters)

    return cleaned_string

cleaned_text = remove_special_characters(text_token)


# In[70]:


cleaned_text


# In[71]:


len(cleaned_text)


# In[72]:


# Convert string to list of words
token_text = cleaned_text.split(' ')


# In[73]:


token_text


# ## 1.3 Extracting Derived variables
We convert the text into a list of tokens using the nltk tokenize module 
and use these tokens to calculate the 4 variables described below:1. Positive Score 
2. Negative Score 
3. Polarity Score 
4. Subjectivity ScoreImport text file positive-words and asign in list
# In[74]:


# Specify the path to your text file
file_path = 'A:/Excel/assinment test/positive-words.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the contents of the file
    positive_words = file.read()


# In[75]:


positive_words = (positive_words.replace("\n", " ").replace("+", " ")).split(' ')
positive_words


# In[76]:


# Count the Sum of all positive words 
Positive_Score = 0
for word in token_text:
    if word in positive_words:
        Positive_Score += 1


# #### positive_words

# In[77]:


print("Sum of all positive words  :", Positive_Score)

Import text file Negaitive-words and asign in list
# In[78]:


# Specify the path to your text file
file_path = 'A:/Excel/assinment test/negative-words.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the contents of the file
    negative_words = file.read()


# In[79]:


negative_words


# In[80]:


negative_words = (negative_words.replace("\n", " ").replace("+", " ")).split(' ')
negative_words


# In[81]:


# Count the Sum of all Negative words 
Negative_Score = 0
for word in token_text:
    if word in negative_words:
        Negative_Score -= -1


# #### Negative_Score

# In[82]:


print("Sum of all Negative words  :", Negative_Score)


# #### Polarity_Score

# In[83]:


Polarity_Score = (Positive_Score - Negative_Score)/((Positive_Score + Negative_Score) + 0.000001)


# In[84]:


Polarity_Score


# In[85]:


len(token_text)


# #### Subjectivity_Score
Subjectivity Score = (Positive Score + Negative Score)/ ((Total Words after cleaning) + 0.000001)
# In[86]:


Subjectivity_Score = (Positive_Score + Negative_Score)/ ((len(token_text)) + 0.000001)


# In[87]:


Subjectivity_Score


# ### 2. Analysis of Readability
Average Sentence Length = the number of words / the number of sentences
# In[88]:


article_text


# In[89]:


sent = sent_tokenize(article_text)


# In[90]:


sent


# In[91]:


count = 0
for i in sent:
    if type(i)==str:
        count += 1


# In[92]:


the_number_of_sentences =  count


# In[93]:


the_number_of_sentences


# In[94]:


the_number_of_words  = len(article_text.split())


# In[95]:


the_number_of_words

Average Sentence Length = the number of words / the number of sentences
# In[96]:


Average_Sentence_Length = (the_number_of_words) / (the_number_of_sentences)


# #### Average_Sentence_Length

# In[97]:


Average_Sentence_Length


# #### Percentage of Complex words
Percentage of Complex words = the number of complex words / the number of words 
48.5207100591716
# In[98]:


word = article_text.split()


# In[99]:


word


# In[100]:


vow = ['a','e','i','o','u']


# In[101]:


the_number_of_complex_words = 0
for i in word:
    vowel = 0
    for v in i:
        if v in vow:
            vowel += 1
            if vowel > 2:
                the_number_of_complex_words +=1    
                


# In[102]:


the_number_of_complex_words


# In[103]:


Percentage_of_Complex_words = the_number_of_complex_words / the_number_of_words


# In[104]:


Percentage_of_Complex_words*100


# #### Fog Index
Fog Index = 0.4 * (Average Sentence Length + Percentage of Complex words)
# In[105]:


# Average Sentence Length = the number of words / the number of sentences


# In[106]:


Average_Sentence_Length = the_number_of_words / the_number_of_sentences
Average_Sentence_Length


# In[107]:


Percentage_of_Complex_words


# In[108]:


Fog_Index = 0.4 * (Average_Sentence_Length + Percentage_of_Complex_words)
Fog_Index


# ### 3 Average Number of Words Per Sentence

# In[109]:


Average_Number_of_Words_Per_Sentence = the_number_of_words / the_number_of_sentences


# In[110]:


Average_Number_of_Words_Per_Sentence


# ### 4. Complex Word Count

# In[111]:


the_number_of_complex_words


# ### 5. Word Count
We count the total cleaned words present in the text by
# In[112]:


token_text


# In[113]:


Word_Count = len(token_text)
Word_Count


# ### 6.Syllable Count Per Word

# In[ ]:


# This line of code count the syllables where the Exceptions for words ending with "es" or "ed"


# In[114]:


def count_syllables(word):
    # Exceptions for words ending with "es" or "ed"
    if word.endswith("es") or word.endswith("ed"):
        return 0
    
    # Counting vowels as syllables
    vowels = "aeiouAEIOU"
    syllable_count = 0
    prev_char_is_vowel = False
    
    for char in word:
        if char in vowels:
            if not prev_char_is_vowel:
                syllable_count += 1
            prev_char_is_vowel = True
        else:
            prev_char_is_vowel = False
    
    return syllable_count

def get_syllable_counts(article_text):
    words = article_text.split()
    syllable_counts = {}
    
    for word in words:
        # Removing punctuation
        word = word.strip(".,?!")

        # Counting syllables in each word
        syllable_count = count_syllables(word)

        syllable_counts[word] = syllable_count
    
    return syllable_counts

if __name__ == "__main__":
    syllable_counts = get_syllable_counts(article_text)

    for word, syllable_count in syllable_counts.items():
        print(f"{word}: {syllable_count} syllable(s)")


# In[115]:


syllable_per_word=get_syllable_counts(article_text)


# In[116]:


syllable_per_word


# ### 7. Personal Pronouns

# In[ ]:


# This lines of code to find the personal pronouns


# In[117]:


import re

def count_personal_pronouns(text):
    # Define a regex pattern to match the specified personal pronouns
    pronoun_pattern = re.compile(r'\b(I|we|my|ours|us)\b', flags=re.IGNORECASE)

    # Exclude occurrences of the country name "US"
    exclude_us_pattern = re.compile(r'\bUS\b', flags=re.IGNORECASE)

    # Apply the regex patterns to the text
    pronouns = pronoun_pattern.findall(text)
    exclude_us = exclude_us_pattern.findall(text)

    # Filter out occurrences of "US" from the pronouns list
    pronouns = [pronoun for pronoun in pronouns if pronoun.lower() != 'US' or pronoun.lower() not in exclude_us]

    # Count the occurrences of each pronoun
    pronoun_counts = {pronoun.lower(): pronouns.count(pronoun) for pronoun in pronouns}

    return pronoun_counts

# Calculate personal pronoun counts
pronoun_counts = count_personal_pronouns(article_text)

# Print the results
print("Personal Pronoun Counts:")
for pronoun, count in pronoun_counts.items():
    print(f"{pronoun.capitalize()}: {count}")


# In[118]:


personal_pronouns =count_personal_pronouns(article_text)


# In[119]:


personal_pronouns


# In[120]:


# Print the results
print("Personal Pronoun Counts:")
for pronoun, count in pronoun_counts.items():
    print(f"{pronoun.capitalize()}: {count}")


# ### 8. Average Word Length
Average Word Length is calculated by the formula:
Sum of the total number of characters in each word/Total number of wordsAverage Word Length = Sum of the total number of characters in each word/Total number of words
# In[121]:


article_text


# In[122]:


# Remove spaces and full stops
result_string = article_text.replace(" ", "").replace(".", "")


# In[123]:


total_number_of_characters = len(result_string)
total_number_of_characters


# In[124]:


Total_number_words = len(article_text.split())
Total_number_words


# In[125]:


Average_Word_Length = total_number_of_characters/Total_number_words
Average_Word_Length


# In[ ]:


# Output is the DataFrame where all calculated value has to be store by its index number one by one


# In[126]:


# Append the new common value to the specified column
output['POSITIVE SCORE'][ind] = Positive_Score
output['NEGATIVE SCORE'][ind] = Negative_Score
output['POLARITY SCORE'][ind] = Polarity_Score
output['SUBJECTIVITY SCORE'][ind]  = Subjectivity_Score
output['AVG SENTENCE LENGTH'][ind] = Average_Sentence_Length
output['PERCENTAGE OF COMPLEX WORDS'][ind] = Percentage_of_Complex_words
output['FOG INDEX'][ind]  = Fog_Index
output['AVG NUMBER OF WORDS PER SENTENCE'][ind] = Average_Number_of_Words_Per_Sentence
output['COMPLEX WORD COUNT'][ind] = the_number_of_complex_words
output['WORD COUNT'][ind] = Word_Count
output['SYLLABLE PER WORD'][ind] = syllable_per_word
output['PERSONAL PRONOUNS'][ind] = personal_pronouns
output['AVG WORD LENGTH'][ind] = Average_Word_Length


# In[ ]:


# Save the changes back to the original Excel file
output.to_excel(excel_file_path, index=False)

# Print a message to confirm the save
print(f"Changes saved to {excel_file_path}")


# In[127]:


output.tail()


# In[ ]:




