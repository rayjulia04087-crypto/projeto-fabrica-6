# 🧮 Função `somaImposto` — Versão Simples

Mini‑projeto em **Python** para implementar a função **`somaImposto(taxaImposto, custo)`**, que retorna o **custo** de um item **acrescido do imposto** sobre vendas.

Foco em **funções puras**, **porcentagem** e **formatação de saída**.

---

## 🎯 Objetivo Educacional
- Praticar a criação e o uso de **funções** em Python.
- Reforçar o cálculo de **porcentagens** aplicado a um problema real (imposto de vendas).
- Exercitar **entrada de dados**, **conversão para número** e **exibição formatada**.

---

## 📝 Enunciado (adaptado ao mundo real)
Você foi contratado para padronizar o cálculo de preço final de produtos em uma loja.  
Implemente uma função chamada **`somaImposto`** que receba:
- **`taxaImposto`**: porcentagem do imposto sobre vendas (ex.: `17.5` para 17,5%)
- **`custo`**: preço do item **antes** do imposto

A função deve **retornar o custo com imposto incluído**.

> Fórmula: `preco_final = custo * (1 + taxaImposto/100)`

---

## 🔎 Exemplo de execução (CLI)
```
=== Cálculo de Preço com Imposto ===

Digite a taxa de imposto (%): 17.5
Digite o custo do item (antes do imposto): 200

Preço final com imposto: R$ 235.00
```

---

## 💻 Como executar

**Pré‑requisito:** Python **3.8+**

1) Clone este repositório ou baixe os arquivos.
```bash
git clone https://github.com/seu-usuario/projeto-fabrica-6.git
cd projeto-fabrica-6
```

2) No terminal, rode:
```bash
python projeto-fabrica-6.py
```
> **Windows:** se `python` não funcionar, tente `py projeto-fabrica-6.py`.

---

## 🧠 Conceitos trabalhados
- Funções puras (`somaImposto`)  
- Porcentagem e aritmética básica  
- Entrada com `input()` e conversão para `float`  
- Saída formatada com f‑strings (`:.2f`)

---

## 🚀 Extensões sugeridas
- Validar entradas (impedir valores negativos; aceitar vírgula como decimal).
- Exibir também o **valor do imposto** (diferença entre final e custo).
- Aplicar a uma **lista de itens** e somar o custo total da compra.
- Salvar o relatório em `.csv`.

---

## 📂 Estrutura
```
soma-imposto-simples/
├─ soma_imposto.py
├─ README.md
└─ tests/
   └─ test_soma_imposto.py
```

---

## 📝 Licença
Este projeto está sob licença **MIT** — use e adapte à vontade. ✨
