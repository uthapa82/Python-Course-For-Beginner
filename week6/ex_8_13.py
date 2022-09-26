def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('abhishek', 'lamichhane',
age = 19, address = 'kharibot', profile = 'student')

def main():
    print(user_profile)

if __name__ == '__main__':
    main()