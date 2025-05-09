import string
import itertools

def xor_decryption():
	"""
	Question: Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
	A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
	For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.
	Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
	Your task has been made easy, as the encryption key consists of three lower case characters. Using 0059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
	"""
	with open("cipher.txt", 'r') as f:
		encrypted = list(map(int, f.read().strip().split(",")))

	# 所有三位小写字母组合
	keys = itertools.product(string.ascii_lowercase, repeat=3)

	common_words = [' the ', ' and ', ' to ', ' of ', ' in ', ' that ', ' is ', 'he', 'be', 'it']

	best_score = 0
	best_text = ""
	best_key = ""

	for key_tuple in keys:
		key = [ord(c) for c in key_tuple]
		decrypted = [encrypted[i] ^ key[i % 3] for i in range(len(encrypted))]
		
		# 如果结果含有乱码字符，直接跳过
		if not all(32 <= c <= 126 for c in decrypted):
			continue
		
		text = ''.join(chr(c) for c in decrypted)
		score = sum(text.count(word) for word in common_words)
		
		if score > best_score:
			best_score = score
			best_text = text
			best_key = ''.join(key_tuple)

	# 输出最可能的正确解
	print("Best Key:", best_key)
	print("Decrypted Message (first 500 chars):\n", best_text[:500])
	return sum(ord(c) for c in best_text)

if __name__ == "__main__":
	print("Sum of ASCII values:", xor_decryption())

