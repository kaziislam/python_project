import requests

# this for GitLAB
# response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")

#this is for Github
response = requests.get("https://api.github.com/users/kaziislam/repos")
# print(response)

# print(type(response.json()))
print(response.json()[0])
my_projects = response.json()

for project in my_projects:
    # for Gitlab
    # print(f"Project Name: {project['name']}\n Project Url: {project['web_url']}\n")
    # for Github
    print(f"ID: {project['id']}\n Name: {project['name']}\n Project Url: {project['url']}\n Deployment URL: {project['deployments_url']}\n")