def number_letter_counts(target):
    """
    Question: If the numbers 1 to 5 are written out in words: one, two, three,
    four, five, then there are 3+3+5+4+4=19 letters used in total.
    If all the numbers from 1 to 1000 inclusive were written out in words, how
    many letters would be used?
    Note: Do not count spaces or hyphens. For example, 342(three hundred and forty-two) contains 23 letters and 115(one hundred and fifteen)
    contains 20 letters. The use of "and" when writing out numbers is in
    compliance with British usage.
    """
    # create a mapping from number to string
    ones = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
    }
    tens = {
        2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
        6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'
    }

    def number_to_words(n):
        if n == 0:
            return ''
        elif n <= 19:
            return ones[n]
        elif n < 100:
            return tens[n // 10] + (ones[n % 10] if n % 10 != 0 else '')
        elif n < 1000:
            if n % 100 == 0:
                return ones[n // 100] + 'hundred'
            else:
                return ones[n // 100] + 'hundredand' + number_to_words(n % 100)
        elif n == 1000:
            return 'onethousand'
        else:
            return ''

    total_letters = 0
    for i in range(1, target + 1):
        words = number_to_words(i)
		# remove blackspace and hyphen from string
        total_letters += len(words.replace(' ', '').replace('-', ''))

    return total_letters

if __name__ == "__main__":
    print(number_letter_counts(5))
    print(number_letter_counts(1000))
