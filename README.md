# **Calculadora em Python com Tkinter**

Uma calculadora interativa criada com Python, que utiliza a biblioteca **Tkinter** para a interface gráfica.

---

## **📋 Funcionalidades**
- Entrada de números e operadores via teclado ou interface gráfica.
- Exibição dos cálculos e resultados.
- Histórico interativo para reutilização de cálculos anteriores.
- Tratamento de erros, como divisões por zero e expressões inválidas.
- Interface visual customizada com cores e estilo próprios.

---

## **🛠 Estrutura do Projeto**
O código foi estruturado para facilitar a manutenção e a escalabilidade, seguindo os princípios de modularidade.

### **Principais Arquivos**
### 1. **`calculator_logic.py`**
   - Este módulo contém toda a lógica por trás dos cálculos realizados pela calculadora.
   - A classe `Calculator` é definida aqui e implementa os principais métodos para:
     - **Adicionar valores à equação** (`value_setter`).
     - **Avaliar a equação matemática** (`results`).
     - **Limpar a tela** (`clean_screen`).
     - **Limpar o histórico de cálculos** (`clean_historic`).
     - **Gerenciar o histórico de cálculos realizados** (`historic`).

### 2. **`calculator_buttons.py`**
   - Este módulo é responsável pela criação e gerenciamento dos botões na interface gráfica.
   - Ele define os botões de números, operadores e outras funções como "Limpar", "Historico", etc.
   - Cada botão é configurado para interagir com a lógica da calculadora, chamando os métodos apropriados quando pressionados.
   - O layout e as interações dos botões são definidos neste módulo para garantir a usabilidade da interface.

### 3. **`calculator_colours.py`**
   - Este módulo gerencia as cores da interface da calculadora.
   - Ele define a classe `ProjectColours`, que mantém um dicionário de cores organizadas, permitindo que as cores da interface sejam facilmente reutilizadas e modificadas em um único local.
   - As cores são usadas em diferentes partes da interface para melhorar a estética e a experiência do usuário.

### 4. **`calculator_window.py`**
   - Este módulo é responsável pela criação e configuração da janela principal da calculadora.
   - Ele usa a biblioteca **Tkinter** para definir a estrutura da janela e organizar os diferentes frames (áreas de exibição da equação, histórico e botões).
   - A interface gráfica é criada neste módulo, onde os elementos visuais são dispostos para o usuário interagir.

### 5. **`main.py`**
   - Arquivo principal da aplicação, que inicializa a calculadora.
   - Ele importa e conecta todos os outros módulos para garantir que a aplicação funcione corretamente.
   - Este módulo é o ponto de entrada da aplicação, onde a janela da calculadora é aberta e os diferentes componentes interagem.

---

## **🎨 Interface Gráfica**
- Construída com **Tkinter**, a interface possui dois frames principais:
  - **Display**: Exibe a equação e o resultado.
  - **Body**: Exibe os botões e sinais matemáticos.
  - **Historic**: Lista as operações realizadas, permitindo selecionar e reutilizar resultados.

---

## **⚙ Como Executar o Código**
### **Pré-requisitos**
- Python 3.8 ou superior instalado no sistema.
- Git

### **Instruções**
1. Clone este repositório:
   ```bash
   git clone https://github.com/renanrbrasil/calculator-tkinter.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd calculator-tkinter
   ```

3. Execute o arquivo principal:
   ```bash
   python main.py
   ```

### **Observação**
O código foi escrito em inglês porque estou estudando o idioma e aplicando ele na prática.

