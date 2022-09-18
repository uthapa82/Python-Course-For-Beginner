#New chapter FUNCTION()..
def rental_car(user):
    """Display a simple greeting."""
    print("Hello," + user.title() + " 'Let me see if i can find you a Subaru!'")

#rental_car('abhi')

def user_name(ram):
    """diaplay a simple greetings"""
    print("hello," + ram.title() + " where are you from")

#user_name('abhishek')

def main():
    rental_car('abhi')
    user_name('abhishek')

if __name__ == "__main__":
    main()