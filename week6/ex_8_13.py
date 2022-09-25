def build_profile(first, last, **user_info):
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()

    return user_info


def main():
    user_profile = build_profile('abhishek', 'lamichhane', age = 19, address = 'kharibot', profile = 'student')
    print(user_profile)

if __name__ == '__main__':
    main()