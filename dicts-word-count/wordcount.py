def word_counter(file_name):
    """"count the # of times a word is in a txt"""
    words = open(file_name)
    #open file and give a veriable
    dictionary = {}
    #creating an empty dictionary to hold word from words 
    for line in words:
        #creating a loop to itirate over words line by line
        line = line.rstrip()
        line = line.lower()
        #stripping the current line of blank space on the right side
        split_line = line.split(" ")
        #returing a list of strings broken up by one space
        for word in split_line:
            #creating a loop that itirates over split_line list item by item
            if ("." in word or "," in word or "?" in word):
                #creating a conditional statement to run more code if the condition is met
                word = word[:-1]
                #removing the last character from word
            dictionary[word] = dictionary.get(word, 0) + 1
                #assigning dictionary value of word 
    return dictionary            

         
print(word_counter("test.txt"))
