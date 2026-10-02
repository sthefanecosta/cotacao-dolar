# ===== AUTOMAÇÃO: COTAÇÃO DO DÓLAR =====

# 0. Importar as bibliotecas
import pyautogui, pyperclip, time, csv, os
from datetime import datetime

# 0.1 Configurar o PAUSE do pyautogui
pyautogui.PAUSE = 0.5

# 1. Abrir o Chrome
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
time.sleep(3)

# 2. Pesquisar a cotação
pyautogui.write("Cotacao dolar")
pyautogui.press("enter")
time.sleep(3)

# 3. Clicar na caixa do REAL
pyautogui.click(x=323, y=492)
pyautogui.hotkey("ctrl", "a")

# 4. Copiar o valor para dentro do Python
pyautogui.hotkey("ctrl", "c")
valor = pyperclip.paste()
print(valor)

# 5. Converter o texto em número
#    - o valor vem como texto com vírgula (ex: "5,43")
valor = valor.replace(",", ".")
valor = float(valor)

# 6. Pegar a data e a hora atuais
momento_atual = datetime.now()
data = momento_atual.date()
hora = momento_atual.strftime("%H:%M:%S")


# 7. Gravar no CSV
tamanho = os.path.getsize("cotacoes.csv") if os.path.exists("cotacoes.csv") else 0

with open("cotacoes.csv", "a", newline="", encoding="utf-8") as arquivo:
    escrita = csv.writer(arquivo)
    if tamanho == 0:
        escrita.writerow(["data", "hora", "valor_real"])
    escrita.writerow([data, hora, valor])

# 8. Fechar o Chrome
time.sleep(1)
pyautogui.hotkey("ctrl", "w")
print("Código finalizado!")
