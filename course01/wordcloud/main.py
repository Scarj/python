def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we",
                           "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was",
                           "were", "be",
                           "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by", "with",
                           "from", "here", "when",
                           "where", "how", "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor",
                           "too", "very",
                           "can", "will", "just", "in", "on"]

    words_frequencies = {}

    words = file_contents.split()

    for word in words:
        cleaned_word = ""
        letter: str
        for letter in word:
            if letter.isalpha() and letter not in punctuations:
                cleaned_word += letter.lower()

        if cleaned_word not in uninteresting_words and len(cleaned_word) > 1:
            if cleaned_word in words_frequencies:
                words_frequencies[cleaned_word] += 1
            else:
                words_frequencies[cleaned_word] = 1

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies({"word", 1})
    return cloud.to_array()


if __name__ == '__main__':
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    cloud.to_file("myfile.jpg")
