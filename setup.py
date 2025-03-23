from setuptools import setup, find_packages  # Importando as funções necessárias do setuptools para configurar o pacote e encontrar pacotes no projeto.

# Lendo o conteúdo do arquivo README.md, que contém uma descrição mais longa do pacote
with open("README.md", "r") as f:
    page_description = f.read()

# Lendo o conteúdo do arquivo requirements.txt, que lista as dependências do projeto
with open("requirements.txt") as f:
    requirements = f.read().splitlines()  # Dividindo as linhas para criar uma lista de dependências

# Configurando as informações do pacote com a função setup()
setup(
    name="package_name",  # Nome do pacote (substitua por um nome real)
    version="0.0.1",  # Versão do pacote
    author="Paulo23k",  # Nome do autor do pacote
    author_email="paulosilvaponted@gmail.com",  # E-mail do autor
    description="Projeto image processing package",  # Descrição curta do pacote
    long_description=page_description,  # Descrição longa, obtida do README.md
    long_description_content_type="markdown",  # Especificando que a descrição longa está em Markdown
    url="https://github.com/Paulo23k/image-processing-package.git",  # URL do repositório do projeto
    packages=find_packages(),  # Encontrando automaticamente os pacotes dentro do projeto
    install_requires=requirements,  # Dependências do projeto, lidas do arquivo requirements.txt
    python_requires='>=3.13',  # Especificando que o pacote requer Python 3.13 ou superior
)
