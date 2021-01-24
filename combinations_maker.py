from time import time


# predefined vocabulary, you can add and use as many as you want
dictionary = {
'voc_comp': ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'v', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'V', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '×', '÷', '=', '/', '_', '€', '!', '@', '#', '$', '%', '^', '&', '*', '-', ':', ';', ' '],
'voc_alfab': ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'v', 'x', 'y', 'z'],
'voc_dbug': ['0', '1', '2'],
'voc_numb': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
'voc_example': ['*', '&', '@']}


def getCombinations(vocab, length_word):
	start_time = time()
	stop_time = ''
	list_word = '' #will be changed to list
	list_comb = []
	prob = len(vocab) ** length_word	
	# creating the length of password
	list_word = [list_word + vocab[0] for n in range(length_word)]
	print('creating ', prob, ' combinations...')	
	# start recursive function 
	list_comb = __make_iter__(list_word, list_comb, vocab, length_word)	
	# creating output informations
	stop_time = str(time() - start_time)
	out_info = 'created ' + str(prob) + ' combinations in: ' + stop_time[:len(stop_time) - 13] + ' seconds'
	return list_comb, out_info


def __make_iter__(list_word, list_comb, vocab, lenght_word, pos = 0):
	string = ''
	for item in vocab:
		try:
			list_word[pos] = item
		except IndexError: 
			break
		pos += 1
		list_comb = __make_iter__(list_word, list_comb, vocab, lenght_word, pos)
		pos -= 1
		# transforn list_word in string
		for char in list_word:
			string += char
		list_comb.append(string)
		# avoid reprinting the last item
		if (string == list_comb[len(list_comb) - 2]) and (string != (vocab[0] * lenght_word)):
			list_comb.pop(len(list_comb) - 1)
		string = ''
	return list_comb


def combinationMaker(dictionary, columns=8, print_out=True):
	# creating the 'menu'
	list_assign = []
	main_mex = 'Choice the vocabulary:\n0 - exit\n'
	iter = 1
	for name_voc in dictionary.keys():
		main_mex +=  str(iter) + ' - ' + name_voc + '\n'
		list_assign.append(name_voc)
		iter += 1
	# start
	while True:
		try:
			vocab_choice = int(input(main_mex))
			if vocab_choice == 0:
				break
			length = int(input('Insert the length: '))
		except ValueError:
			continue
		try:
			vocab_choice = list_assign[vocab_choice - 1]
		except IndexError:
			print('\nno vocabulary linked to ', vocab_choice, '\n')
			continue
		list_prob, out_info = getCombinations(dictionary[vocab_choice], length)
		# printing the output
		if print_out == True:
			list_chunk = []
			for n in range(len(list_prob)):
				list_chunk.append(list_prob[n])
				
				if (((n + 1) % columns) == 0) and (n != 0):
					print(list_chunk)
					list_chunk.clear()
			print(list_chunk)
		print(out_info)


'''
you can change the display of the output by modifying 
the 'columns' and 'print_out' variables, which by
default are '8' and 'True', for example:
combinationMaker(dictionary, columns=10)
'''
combinationMaker(dictionary)