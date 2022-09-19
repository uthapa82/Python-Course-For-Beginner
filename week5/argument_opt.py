#Making argument optional.
def person_name(first_name, last_name, middle_name=''):
    """return a full_name"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + last_name

    return full_name.title()

def main():
    name = person_name('ram', 'lamichhane')
    name= person_name('ram', 'lamichhane', 'bahadur')
    print(name)

if __name__ == "__main__":
    main()