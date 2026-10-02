# Cotação do Dólar

Automação em Python que abre o Chrome, pesquisa a cotação do dólar no Google, copia o valor em reais e grava em um arquivo CSV com data e hora.

## Tecnologias

- Python 3
- PyAutoGUI
- Pyperclip

## Como rodar

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python codigo.py
```

## Resultado

O arquivo `cotacoes.csv` recebe uma linha a cada execução:

```
data,hora,valor_real
2026-10-02,22:07:00,5.23
```

## Limitação

Os cliques usam coordenadas fixas da tela. Em outro computador, é preciso ajustar o `x` e o `y` do clique.  
