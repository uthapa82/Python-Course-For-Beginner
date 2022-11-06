"""
word count using .txt file
"""
def word_count(file):
    """
    count the word in .txt file
    """
    try:
        with open(file) as f:
            contents = f.read()
            
    except FileNotFoundError:
        msg = "Sorry, the file " + file + " doesn't exist."
        
    else:
        words = contents  #contents.split()
        result = words.lower().count('the') # len(words)
        print("The file " + file + " has about " + str(result) + " 'the' words.")

def main():
    filename = 'copy.txt'
    word_count(filename)

if __name__ == '__main__':
    main()