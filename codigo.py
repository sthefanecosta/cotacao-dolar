# ===== AUTOMAÇÃO: COTAÇÃO DO DÓLAR =====

# 0. Importar as bibliotecas
import pyautogui, pyperclip, time, datetime, csv

# 0.1 Configurar o PAUSE do pyautogui
#     (lembra do que você usou no projeto da imersão)

# 1. Abrir o Chrome
#    - apertar a tecla win
#    - digitar chrome
#    - apertar enter
#    - esperar o Chrome abrir (time.sleep)

# 2. Pesquisar a cotação
#    - digitar "cotação dólar" na barra
#    - apertar enter
#    - esperar a página carregar (time.sleep)

# 3. Clicar na caixa do REAL
#    - usar as coordenadas (x, y) que você descobriu com pyautogui.position()
#    - selecionar o conteúdo da caixa

# 4. Copiar o valor para dentro do Python
#    - Ctrl+C
#    - ler o que foi copiado com pyperclip.paste()
#    - print() para conferir se veio certo

# 5. Converter o texto em número
#    - o valor vem como texto com vírgula (ex: "5,43")
#    - trocar a vírgula por ponto
#    - converter para float

# 6. Pegar a data e a hora atuais
#    - usar datetime

# 7. Gravar no CSV
#    - abrir o cotacao_dolar.csv em modo de adicionar (append)
#    - se o arquivo estiver vazio, escrever o cabeçalho: data, hora, valor_real
#    - escrever a linha com data, hora e valor

# 8. Fechar o Chrome (opcional, só depois de tudo funcionar)
