#!/usr/bin/env python
# coding: utf-8


import pdfplumber
import csv
from collections import Counter
import string
from nltk.corpus import stopwords


# Opening the PDF file and extracting it to csv file

with pdfplumber.open("C:\\Users\\MGC\\Downloads\\Rich Dad Poor Dad ( PDFDrive ).pdf") as pdf:
    text = ""

    # Extracting text from each page
    for page in pdf.pages:
        text += page.extract_text()

    # Removing punctuation and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()

    # Splitting text into words
    words = text.split()

    # Removing stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # Getting the most common word
    word_counts = Counter(words)
    most_common_word = word_counts.most_common(1)[0][0]

    # Writing the extracted text to a CSV file
    with open('output.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Text'])
        writer.writerow([text])

    print("Most common word:", most_common_word)

