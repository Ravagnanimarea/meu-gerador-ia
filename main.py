import torch # Biblioteca base para processamento de inteligência artificial
from diffusers import StableDiffusionPipeline # Ferramenta que gerencia o modelo de geração de imagens
from PIL import Image # Biblioteca utilizada para manipular e salvar arquivos de imagem

# 1. Definição do modelo
# Aqui escolhemos o Stable Diffusion v1.5, uma versão equilibrada entre qualidade e peso
model_id = "runwayml/stable-diffusion-v1-5"

# 2. Carregamento do sistema
print("Iniciando o modelo... Este processo consome bastante memória RAM.")

# O comando abaixo prepara o 'pipeline' (o fluxo de trabalho da IA) usando o modelo escolhido
pipe = StableDiffusionPipeline.from_pretrained(model_id)

# Como o seu computador não possui placa de vídeo NVIDIA (CUDA), 
# configuramos explicitamente para que o processador (CPU) faça todo o trabalho.
pipe = pipe.to("cpu") 

# 3. Definição da instrução (Prompt)
# Para melhores resultados, utilizamos termos em inglês e descritores de qualidade (8k, cinematic)
prompt = "A majestic astronaut riding a horse on Mars, cinematic lighting, masterpiece, 8k"

# 4. Processo de geração
print(f"Processando a imagem: {prompt}")
# Nesta etapa, a IA converte o texto em pixels. No processador (CPU), isso pode levar alguns minutos.
# O resultado final é extraído da lista de imagens geradas.
image = pipe(prompt).images[0]

# 5. Finalização e salvamento
# Salva a imagem gerada no formato PNG no mesmo diretório do script
image.save("resultado.png")

print("Processo concluído! O arquivo 'resultado.png' foi criado com sucesso.")