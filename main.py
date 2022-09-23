import requests

user_name = input("digite aqui o seu usuário do gitlab: ")
response = requests.get(f"https://gitlab.com/api/v4/users/{user_name}/projects") #type -> <class 'requests.models.Response'>
lista_meus_projetos = response.json() #type -> <class 'list'> O metodo json converte o tipo para lista

for projeto in lista_meus_projetos:
    print(f"nome do projeto: {projeto['name']} \nURL do projeto: {projeto['web_url']}\n")