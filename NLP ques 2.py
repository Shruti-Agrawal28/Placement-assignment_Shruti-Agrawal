#!/usr/bin/env python
# coding: utf-8

# ### IMPORTING STATEMENTS

# In[26]:


import pdfplumber
import csv
from collections import Counter
import string
from nltk.corpus import stopwords


# ### Opening the PDF file and extracting it to csv file

# In[25]:



# Open the PDF file
with pdfplumber.open("C:\\Users\\MGC\\Downloads\\Rich Dad Poor Dad ( PDFDrive ).pdf") as pdf:
    text = ""

    # Extract text from each page
    for page in pdf.pages:
        text += page.extract_text()

    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()

    # Split text into words
    words = text.split()

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # Get the most common word
    word_counts = Counter(words)
    most_common_word = word_counts.most_common(1)[0][0]

    # Write the extracted text to a CSV file
    with open('output.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Text'])
        writer.writerow([text])

    print("Most common word:", most_common_word)

