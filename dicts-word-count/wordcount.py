def word_counter(file_name):
    """"count the # of times a word is in a txt"""
    words = open(file_name)
    dictionary = {}
    for line in words:
        line = line.rstrip()
        split_line = line.split(" ")
        for word in split_line:
            if "." in word:
                word = word[:-1]
                print(word)
    print()            
   





word_counter("test.txt")
#.rstrip(,)