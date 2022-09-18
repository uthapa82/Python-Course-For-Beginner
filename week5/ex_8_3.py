def make_shirt(size, text_message):
    """display information about t-shirt"""
    print("The size of the t-shirt is " + str(size))
    print("The message printed on a t-shirt is " + text_message.upper())

def main():
    make_shirt(20, 'ram')
    make_shirt(size = 20, text_message = 'ram')

if __name__ == "__main__":
    main()