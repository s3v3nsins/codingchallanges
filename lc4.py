def find_indexes(char):
	k = '#_23456789abcdefghijklmnopqrstuvwxyz'
	return (k.index(char) % 6, k.index(char) // 6)

def state_initialization(key):
	matrix = []
	for x in range(0, 36, 6):
		matrix.append(list(key[x:x+6]))
	return matrix

def decrypt_character(char, matrix, indexes):
	for index, row in enumerate(matrix):
		if char in row:
			char_index = (index, row.index(char))
			return matrix[char_index[0] - indexes[1]][char_index[1] - indexes[0]]

def encrypt_character(char, matrix, indexes):
	for index, row in enumerate(matrix):
		if char in row:
			char_index = (index, row.index(char))
			return matrix[(char_index[0] + indexes[1])%6][(char_index[1] + indexes[0])%6]

def right_rotate_row(matrix, decrypted_character):
	for index, row in enumerate(matrix):
		if decrypted_character in row:
			break
	matrix[index] = [matrix[index][-1]] + matrix[index][0:len(matrix[index])-1]
	return matrix

def down_rotate_row(matrix, encrypted_character):
	for index, row in enumerate(matrix):
		if encrypted_character in row:
			column = row.index(encrypted_character)
			break
	temp = [matrix[i][column] for i in range(len(matrix))]
	for i in range(len(temp) - 1):
		matrix[i + 1][column] = temp[i]
	matrix[0][column] = temp[-1]
	return matrix

def update_marker(matrix, marker, indexes):
	for r, row in enumerate(matrix):
		if marker in row:
			char_index = [r,row.index(marker)]
	marker = matrix[(char_index[0] + indexes[1])%6][(char_index[1] + indexes[0])%6]
	return marker

def decrypt_message(key, message, matrix, marker):
	decrypted_message = ''
	for x in message:
		decrypted_character = decrypt_character(x, matrix, find_indexes(marker))
		matrix = right_rotate_row(matrix, decrypted_character)
		matrix = down_rotate_row(matrix, x)
		marker = update_marker(matrix, marker, find_indexes(x))
		decrypted_message += decrypted_character
	return decrypted_message

def encrypt_message(key, message, matrix, marker):
	encrypted_message = ''
	for x in message:
		c = encrypt_character(x, matrix, find_indexes(marker))
		matrix = right_rotate_row(matrix, c)
		matrix = down_rotate_row(matrix, x)
		marker = update_marker(matrix, marker, find_indexes(x))
		encrypted_message += c
	return encrypted_message

if __name__ == '__main__':
	key = "s2ferw_nx346ty5odiupq#lmz8ajhgcvk79b"
	matrix = state_initialization(key)
	marker = matrix[0][0]
	print(decrypt_message(key, "tk5j23tq94_gw9c#lhzs", matrix, marker))
	print(encrypt_message(key, "aaaaaaaaaaaaaaaaaaaa", matrix, marker))
	print(encrypt_message(key, "k8b64caycepxam6zel5d", matrix, marker))
