from count_word import Search_Word

#create instance of class
obj = Search_Word()

collect_data = obj.read_file("sample")
print(collect_data)

s_word = obj.count_word(collect_data, "of")
print(s_word)
