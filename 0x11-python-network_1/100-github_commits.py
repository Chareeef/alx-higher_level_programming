#!/usr/bin/python3
'''
Script that list 10 commits (from the most recent to oldest)
for the both passed user's repository
'''

if __name__ == '__main__':
    from sys import argv
    import requests

    repo = argv[1]
    owner = argv[2]

    url = f'https://api.github.com/repos/{owner}/{repo}/commits'

    response = requests.get(url)

    commits_list = response.json()

    if type(commits_list) != list:
        exit()

    max_commits = 10 if len(commits_list) > 10 else len(commits_list)

    for i in range(max_commits):
        sha = commits_list[i]['sha']
        author_name = commits_list[i]['commit']['author']['name']

        print(sha + ': ' + author_name)
