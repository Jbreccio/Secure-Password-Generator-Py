# 🔐 Gerador de Senhas Seguras

Um gerador de senhas personalizável que cria senhas seguras com diferentes critérios de complexidade.

## 📋 Funcionalidades

- 🔢 Controle de tamanho da senha
- 🔤 Opção de letras maiúsculas
- 🔡 Opção de letras minúsculas
- 🔢 Opção de números
- 🔣 Opção de símbolos especiais
- 🚫 Exclusão de caracteres ambíguos
- 💾 Geração de múltiplas senhas
- 🔍 Verificação de força da senha
- 📊 Análise de segurança

## 🛠️ Tecnologias Utilizadas

- Python 3.7+
- Módulo `random` (nativo)
- Módulo `secrets` (mais seguro)
- Módulo `string` (nativo)

## 🚀 Como Executar

1. Clone o repositório
2. Navegue até a pasta do projeto
3. Execute o comando:
```bash
python main.py
```

## 📖 Como Usar

1. Execute o programa
2. Defina o tamanho da senha
3. Escolha os tipos de caracteres
4. Decida se quer excluir caracteres ambíguos
5. Escolha quantas senhas gerar
6. Veja as senhas geradas e sua análise

## 🎯 Tipos de Caracteres

- **Maiúsculas**: A-Z
- **Minúsculas**: a-z
- **Números**: 0-9
- **Símbolos**: !@#$%^&*()_+-=[]{}|;:,.<>?

## 🚫 Caracteres Ambíguos (Opcionais)

- **Números**: 0, 1
- **Letras**: O, I, l (facilmente confundidos)

## 🔍 Análise de Força

- 🔴 **Fraca**: < 8 caracteres ou poucos tipos
- 🟡 **Média**: 8-11 caracteres com tipos variados
- 🟢 **Forte**: 12+ caracteres com todos os tipos

## 🎯 Conceitos Aprendidos

- Módulo secrets (criptograficamente seguro)
- Módulo random
- Módulo string
- Manipulação de strings
- Validação de entrada
- Análise de complexidade
- Boas práticas de segurança

## 📝 Exemplo de Uso

```
🔐 GERADOR DE SENHAS SEGURAS
Tamanho da senha (8-128): 16
Incluir maiúsculas? (s/n): s
Incluir minúsculas? (s/n): s
Incluir números? (s/n): s
Incluir símbolos? (s/n): s
Excluir caracteres ambíguos? (s/n): s
Quantas senhas gerar? (1-10): 3

Senhas geradas:
1. Kp@9mVx7RtYw3#Nq (Força: 🟢 Forte)
2. Bz$5fHj8LmPr2&Xs (Força: 🟢 Forte)
3. Ck#4nQs9WtGv6!Zy (Força: 🟢 Forte)
```

## 🔧 Melhorias Futuras

- Salvamento de senhas em arquivo
- Verificação contra vazamentos
- Geração baseada em palavras
- Interface gráfica
- Integração com gerenciadores de senhas

## 📄 Licença

Este projeto está sob a licença MIT.
