'''
Who said it? Part 1: This program reads a shortened version of Hamlet and
Pride and Prejudice, and for each text, it will create and return a dictionary
of word counts of each word in both texts.

Miki Ando
'''
# Takes a word and returns the same word with all non-letters removed 
# and converted to lowercase
def normalize(word):
    word =  "".join(letter for letter in word if letter.isalpha()).lower()
    return (word)

# Takes a filename and generates a dictionary. Keys: words. Values: counts for
# each word(key).
def getcounts(filename):
    
    #make an empty dictionary and open the file
    result_dict = {}
    file = open(filename)

    # for every line in the file, removes the /n and splits each word
    for line in file:
        line = line.strip()
        words = line.split()

        # for every split word, it normalizes by the function
        for word in words:
            word = normalize(word)

            # if the word is already in the dictionary, adds onto the count
            if word in result_dict:
                result_dict[word] += 1
            # if the word is not in the dictionary yet, adds the word as a key
            else:
                result_dict[word] = 1
   
    return (result_dict)


# Get the counts for the two shortened versions of the texts
shakespeare_counts = getcounts("hamlet-short.txt")
austen_counts = getcounts("pride_and_prejudice-short.txt")

# Check the contents of the dictionaries for both texts with a divider 
for key in shakespeare_counts:
    print (key + ": " + str(shakespeare_counts[key]))

print ("-----")

for key in austen_counts:
    print (key + ": " + str(austen_counts[key]))


    
    
