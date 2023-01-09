import pickle


test_list = [1,2,3]

with open("test.pickle", "wb") as outfile:
    pickle.dump(test_list, outfile)


with open("test.pickle", "rb") as infile:
    test_dict_reconstructed = pickle.load(infile)
print(test_dict_reconstructed)
