import sys

class count_word():
    '''
    Method to pass string of words.
    '''
    def pmdbts_apply(self, counts, input_buf):
        input_bufsz = sys.getsizeof(input_buf)
        print("String size in bytes:", input_bufsz)

        words = input_buf.split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        
        return counts

    '''
    Method to read dict and pass the word to 
    count the number of occurrences.
    '''
    def pmdbts_read(self, reply_buf, request_buf):
        #Return the value from dictionary.
        for key, value in reply_buf.items():
            if key == request_buf:
                return value
            

#Create instance of class
obj = count_word()

#Input text
input_buf = '''
        The textwrap module can be used to format text for output in situations in many text editors
        where pretty-printing is desired.  It offers programmatic functionality similar
        to the paragraph wrapping or filling features found in many text editors.
        '''

#Create Dictionary        
count_dict = dict()

'''
It will update value of word when function gets called.
'''
i = 0
while(i<5):
    dict_result = obj.pmdbts_apply(count_dict, input_buf)
    print(dict_result)
    word_freq = obj.pmdbts_read(dict_result, "in")
    print("Count of word is: ", word_freq)
    i += 1


