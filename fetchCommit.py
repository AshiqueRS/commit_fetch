import requests
# http request korar jonno


def fetch_commits(repo_owner, repo_name, per_page=50):
    """
    Parameters:
        repo_owner (str): The owner of the repository.
        repo_name (str): The name of the repository.
        per_page (int): Number of commits to fetch (default is 10).
    """
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits" # commit er jonno github er api endpoint
    params = {"per_page": per_page}  #request er jonno parameter set korbe
    response = requests.get(url, params=params) #api te get request korbe

    if response.status_code == 200:  # request successful kina check dibe
        commits = response.json()  # response JSON parse korbe
        for commit in commits:
            author = commit['commit']['author']['name']  #  author er  name
            message = commit['commit']['message']  # commit message
            print(f"Author: {author}\nMessage: {message}\n{'-' * 40}")
    else:
        print(f"Failed to fetch commits: {response.status_code}")


if __name__ == "__main__":
    repo_owner = "microsoft"
    repo_name = "playwright"
    fetch_commits(repo_owner, repo_name)  
