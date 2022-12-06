import requests

user_name = input("digite aqui o seu usuário do gitlab: ")
response = requests.get(f"https://gitlab.com/api/v4/users/{user_name}/projects")

lista_meus_projetos = response.json()

for projeto in lista_meus_projetos:
    print(f"nome do projeto: {projeto['name']} \nURL do projeto: {projeto['web_url']}\n")
