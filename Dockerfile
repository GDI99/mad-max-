# Usa uma imagem base leve com Python
FROM python:3.11-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia todos os arquivos do projeto para dentro do container
COPY . .

# Comando padrão ao rodar o container
CMD ["python", "calcr.py"]
