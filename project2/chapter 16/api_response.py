import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Store API response in a variable.
response_dict = r.json()

print("Total repositories:", response_dict['total_count'])
# Explore information about the repositories.
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# Examine the first repository.
repo_dict = repo_dicts[0]

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])