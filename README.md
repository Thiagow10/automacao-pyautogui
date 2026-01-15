# Automação de Cadastro de Produtos com PyAutoGUI

## 📌 Descrição do Projeto
Este projeto consiste em uma automação desenvolvida em Python para realizar o cadastro de produtos em um site de forma automática. A aplicação lê uma base de dados com mais de 200 itens e preenche os campos necessários no sistema, como código, marca, tipo, categoria e outras informações, otimizando tempo e reduzindo erros manuais.

A automação foi construída utilizando a biblioteca **PyAutoGUI**, que permite controlar o mouse e o teclado para interação direta com a interface gráfica do site.

---

## 🚀 Funcionalidades
- Leitura de base de dados com múltiplos produtos  
- Cadastro automático de produtos em site/sistema web  
- Preenchimento de campos como:
  - Código
  - Marca
  - Tipo
  - Categoria
  - Outros dados do produto
- Redução de tempo e esforço em tarefas repetitivas  

---

## 🛠️ Tecnologias Utilizadas
- Python
- PyAutoGUI
- Pandas
- Time

---

## 📂 Estrutura do Projeto
automacao-cadastro-produtos/
│── main.py
│── base_dados.xlsx # ou .csv
│── README.md


---

## ⚙️ Como Executar o Projeto

1. Clone o repositório:
git clone https://github.com/Thiagow10/automacao-pyautogui.git

2. Instale as dependências:
pip install pyautogui pandas

3. Ajuste o script conforme necessário:
- Resolução da tela
- Posições do mouse
- Tempo de espera (`sleep`)
- Caminho da base de dados

4. Execute o script:
python main.py


---

## ⚠️ Observações Importantes
- A automação depende da resolução da tela e do layout do site.
- Não utilize o mouse ou teclado durante a execução do script.
- Recomenda-se testar com poucos registros antes de executar a base completa.

---

## 📈 Possíveis Melhorias
- Validação de erros durante o cadastro  
- Geração de logs de execução  
- Interface gráfica para configuração  
- Integração com Selenium ou APIs  

---

## 👨‍💻 Autor
Desenvolvido por **Thiago Machado**  
Projeto criado para fins de aprendizado e automação de processos repetitivos.
