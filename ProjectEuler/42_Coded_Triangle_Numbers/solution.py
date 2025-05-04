import string

def read_and_preprocess(file_path):
    """
    Reads and preprocesses a .txt file.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.read().replace('"', '').split(',')
            words = [word.strip() for word in lines if word.strip()]
            return words
    except FileNotFoundError:
        raise FileNotFoundError("The file does not exist.")
    except Exception as e:
        raise Exception("A fatal error occurred while reading the file.")

def coded_triangle_numbers(file_path):
    """
    Question: The nth term of the sequence of triangle numbers is given by,
    tn = 0.5 * n * (n + 1), So the first ten triangle numbers are:
        1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
    By converting each letter in a word to a number corresponding to its
    alphabetical position and adding these values, we form a word value. For
    example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is
    a triangle number, then we shall call the word a triangle word.
    Using words.txt, a 16k text file containing nearly two-thousand common
    English words, how many are triangle words?
    """
    # Create a dictionary to map each letter to its alphabetical position
    alphabetical_table = {char: index for index, char in enumerate(string.ascii_uppercase, start=1)}

    # Generate a list of triangle numbers up to a reasonable limit
    triangle_numbers = {int(0.5 * n * (n + 1)) for n in range(1, 100)}

    # Calculate the word scores and check if they are triangle numbers
    triangle_word_count = 0
    words = read_and_preprocess(file_path)
    for word in words:
        word_score = sum(alphabetical_table[char] for char in word.upper())
        if word_score in triangle_numbers:
            triangle_word_count += 1

    return triangle_word_count

if __name__ == "__main__":
    file_path = "words.txt"  # Ensure this is the correct path to your file
    print(coded_triangle_numbers(file_path))
