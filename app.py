import streamlit as st  # Importa o framework para criar a interface visual do site
import requests          # Permite que o Python "converse" com servidores na internet
import io                # Ajuda a lidar com os dados da imagem como se fossem um arquivo
from PIL import Image    # Biblioteca para processar e exibir a imagem final

# Define o título e o ícone que aparecem na aba do seu navegador
st.set_page_config(page_title="IA Ultra Rápida", page_icon="⚡")

# --- CONFIGURAÇÃO DA API ---
# Chave de acesso pessoal para identificar quem está usando os serviços da Hugging Face
API_TOKEN = "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"

# Endereço do servidor que processa o modelo Stable Diffusion XL (mais potente)
API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"

# Cabeçalho de segurança que envia seu token para autorizar o uso da API
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    # Organiza os dados que serão enviados: o texto (prompt) e configurações extras
    data = {
        "inputs": payload["inputs"],
        "parameters": {
            "negative_prompt": "ugly, blurry, poor quality, distorted, extra fingers", # Lista o que a IA deve evitar
            "guidance_scale": 7.5, # Controla o quanto a IA deve seguir rigorosamente o seu texto
        }
    }
    # Envia uma requisição POST para o servidor com as informações acima
    response = requests.post(API_URL, headers=headers, json=data)
    # Retorna o conteúdo da resposta (que deve ser a imagem em formato binário)
    return response.content

# --- INTERFACE ---
st.title("⚡ Gerador de Imagem via API")
st.write("Rodando nos servidores da nuvem - Rápido e Leve!")

# Cria uma caixa de texto para o usuário digitar o que deseja gerar
prompt = st.text_input("O que você quer ver?", placeholder="Ex: Um dragão de cristal voando sobre uma floresta neon")

# Verifica se o botão "Gerar" foi clicado
if st.button("Gerar Imagem Agora 🚀"):
    if prompt:
        # Garante que o usuário substituiu o texto de exemplo pelo token real
        if "COLE_AQUI" in API_TOKEN:
            st.error("⚠️ Você precisa colar seu Token lá no topo do código!")
        else:
            # Exibe uma animação de carregamento enquanto a API processa
            with st.spinner("A nuvem está processando..."):
                image_bytes = query({"inputs": prompt})
            
            try:
                # Tenta transformar os dados recebidos da internet em uma imagem real
                image = Image.open(io.BytesIO(image_bytes))
                # Exibe a imagem na tela do site
                st.image(image, caption="Imagem gerada via API", use_container_width=True)
                
                # Cria um botão para o usuário salvar a imagem no próprio computador
                st.download_button("Baixar Imagem", data=image_bytes, file_name="ai_image.png", mime="image/png")
            except Exception as e:
                # Caso a API envie um erro (como 'servidor carregando'), ele será exibido aqui
                st.error(f"Erro da API: {image_bytes.decode('utf-8', errors='ignore')}")
                st.info("Dica: Se aparecer 'Model is loading', apenas espere um pouco e clique de novo.")
    else:
        # Aviso caso o usuário tente gerar algo com a caixa de texto vazia
        st.warning("✍️ Digite um prompt primeiro!")