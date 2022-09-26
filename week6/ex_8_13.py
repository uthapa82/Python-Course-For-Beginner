def build_profile(first, last, **user_info):
    profile = {
        'first name': first,
        'last name': last,
    }
  
    for key, value in user_info.items():
        profile[key] = value
    return profile

def main():
    user_info = build_profile('abhishek', 'lamichhane', age = 19, address = 'kharibot', profile = 'student')
    print(user_info)

if __name__ == '__main__':
    main()