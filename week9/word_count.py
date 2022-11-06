"""
word count using .txt file
"""
def word_count(file):
    """
    counts the words in a .txt file
    """    
    try:
        with open(file) as f:
            contents = f.read()
            
    except FileNotFoundError:
        msg = "Sorry, the file " + file + " doesn't exist."
    
    else:
        words = contents
        result = words.count('Python')
        print("The file " + file + " has about " + str(result) + " words.")
        
def main():
    filename = 'pep8.txt'
    word_count(filename)

if __name__ == '__main__':
    main()
