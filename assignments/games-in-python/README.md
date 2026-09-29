# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Praticar o uso de strings, laços, condicionais e entrada de dados do usuário para criar um jogo interativo de adivinhação de palavras.

## 📝 Tarefas

### 🛠️ Configuração da palavra secreta

#### Descrição
Crie uma lista com palavras e escolha uma delas aleatoriamente para iniciar a partida.

#### Requisitos
O programa concluído deve:

- Definir uma lista de palavras com diferentes níveis de dificuldade
- Selecionar uma palavra aleatória para o jogo
- Guardar a palavra escolhida de forma que o jogador não a veja

### 🛠️ Entrada e validação das letras

#### Descrição
Permita que o jogador insira letras e verifique se a letra faz parte da palavra secreta.

#### Requisitos
O programa concluído deve:

- Solicitar uma letra ao jogador
- Verificar se a letra informada está presente na palavra
- Mostrar ao usuário o progresso atual da palavra, com letras já reveladas e espaços para as ainda não descobertas
- Evitar que letras repetidas sejam contabilizadas como tentativas novas

### 🛠️ Sistema de tentativas e resultado final

#### Descrição
Implemente as regras do jogo, incluindo contagem de erros, vitória e derrota.

#### Requisitos
O programa concluído deve:

- Acompanhar o número de tentativas restantes
- Diminuir as tentativas quando a letra estiver errada
- Encerrar o jogo quando a palavra for completamente adivinhada
- Encerrar o jogo quando as tentativas acabarem
- Exibir mensagens claras de vitória ou derrota ao final da partida