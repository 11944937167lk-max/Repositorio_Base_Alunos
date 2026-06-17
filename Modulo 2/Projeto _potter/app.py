import streamlit as st
import requests

# URL da api com todos os personagens
url = "https://hp-api.onrender.com/api/characters"

# Faz a requisição para pegar os dados
resposta = requests.get(url)
dados = resposta.json()

# Pegaapenas os nomes dos personagens
nomes = []
for personagem in dados :
    nomes.append(personagem['name'])
nomes.sort()

# titulo do app
st.title("personagens de harry potter")

# sidebar com lista de nomes
with st.sidebar:
    st.header("escolha um personagem")
    st.image("logo.png")
    nome_escolhido = st.selectbox("seleciona:", nomes)

    # procurar o personagem escolhido na lista de dados
    personagem = None 
    for p in dados :
        if p['name'] == nome_escolhido:
            personagem = p 
            break 

        # mostra o nome do personagem
st.header(personagem['name'])

# ===== IMAGEM EM DESTAQUE =====
# verificaf se o personagem tem imagem 

st.divider()
st.write(f"**casa:**{personagem['house']}")
st.write(f"**espécie:** {personagem['species']}")
st.write(f"**genero:** {personagem['gender']}")
st.write(f"**data de nascimento:**{personagem['dateOfBirth']}")
st.write(f"**ano de nascimento:**{personagem['yearOfBirth']}")

# informaçao da varinha 
st.write("**varinha:**")
st.write (f" - madera:{personagem['wand']['wood']}")
st.write(f"-nucleo{personagem['wand']['core']}")
st.write(f"- tamanho: {personagem['wand']['length']} polegadas")
         
st.write(f"**patrono:**{personagem['patronus']}")
st.write(f"**ator/atriz:**{personagem['actor']}")

#mostra se esta vivo 
if personagem['alive']:
    st.write(f"**esta vivo?** sim")
else:
    st.write(f"**esta vivo?** Não")
