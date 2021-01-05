class Search_Word:

    #Method to read file contents
    def read_file(self, filename):
        f_name = "%s.txt" % (filename)
       
        with open(f_name, 'r') as fr: 
            
            counts = dict()

            for line in fr: 
                # Remove the leading spaces and newline character
                line = line.strip()
                '''
                Convert the characters in line to
                lowercase to avoid case mismatch
                '''
                line = line.lower()
 
                data = line.split(" ") 
                
                for word in data:
                    if word in counts:
                       counts[word] += 1
                    else:
                       counts[word] = 1
           
        return counts   
            
    def count_word(self, dict, word):
        # Print the contents of dictionary
        for key, value in dict.items():
            if key == word:
                return value
            #else:
            #    return 0
        
