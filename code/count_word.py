import string

class Search_Word:

    counts = {}
    #Method to read file contents
    def read_file(self, filename):
        f_name = "%s.txt" % (filename)
       
        with open(f_name, 'r') as fr: 
            split_data = fr.readlines() 
            self.counts = {}
            for line in split_data: 
                # Remove the leading spaces and newline character
                line = line.strip()
                '''
                Convert the characters in line to
                lowercase to avoid case mismatch
                '''
                line = line.lower()

                # Remove the punctuation marks from the line 
                line = line.translate(line.maketrans("", "", string.punctuation))
        
                data = line.split() 
                print(data)

                for word in data:
                    if word in counts:
                       counts[word] += 1
                    else:
                       counts[word] = 1
           
        return counts   

            
    def count_word(self, key):
        self.counts = {}
        # Print the contents of dictionary
        for key in list(counts.keys()):
            print(key, ":", counts[key])
