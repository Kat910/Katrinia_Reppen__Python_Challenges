import string  
   
# create function and empty dictionary
def count_words_and_save(input_file, output_file):
    word_counts = {}  

    # Open and read the file
    with open(input_file, 'r') as file:
      text = file.read()

      # Convert all text to lowercase
      text = text.lower()

      # Split the text into words
      words = text.split()

      # Go through each word and remove punctuation
      for word in words:
        clean_word = word.translate(str.maketrans('', '', string.punctuation))

        # Add dictionary entries
        if clean_word:
            if clean_word in word_counts:
              word_counts[clean_word] += 1
            else:
              word_counts[clean_word] = 1

        # Write the word counts to a new file
    with open(output_file, 'w') as out_file:
      for word, count in sorted(word_counts.items()):
        out_file.write(f"{word}: {count}\n")

    print(f"Word counts have been saved to '{output_file}'.")

    return word_counts


count_words_and_save("input_wordcount.txt", "output_file.txt")


