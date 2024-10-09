import re

def basic_tokenizer(text):
    """
    Tokenizes the input text into words and punctuation.
    """
    tokens = re.findall(r'\w+|\S', text)
    return tokens

if __name__ == "__main__":
    sample_text = "Hello, world! Let's tokenize this sentence."
    tokens = basic_tokenizer(sample_text)
    print("Tokens:", tokens)

