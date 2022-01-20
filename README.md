# Projeto Pinball
## FPRO/LEIC, 2021/22
## António Rama (up202108801)
## 1LEIC12

### Objetivo

1. Criar uma versão do clássico pinball da atari 2600.

### Repositório de código

1) Link para o repositório do GitHub: https://github.com/antoniorama/pinball

### Descrição

*---É um jogo de puzzle em que o jogador manipula duas palhetas de modo a evitar que a bola caia
na parte existente na parte inferior da área de jogo. A bola, quando entra em contacto com certos 
objetos espalhados pela área de jogo, aumenta a pontuação do jogador. ---*

### UI

<img width="998" alt="imagem" src="https://user-images.githubusercontent.com/96125703/150325544-17e8871d-644e-4719-a881-420c2dd50d71.png">

Nota: O design do jogo é extremamente simples, foquei-me apenas na programação.

### Pacotes

- Pygame
- Math
- Random

### Tarefas

Neste projetos, as tarefas foram criar:
- os menus (main menu e game over menu);
- os obstáculos e as físicas de colisão da bola com os mesmos;
- o sistema de score: o score aumenta quando a bola colide com certos o obstáculos os atravessa certas áreas;
- as físicas da bola: alteração do sinal da sua velocidade quando colide com obstáculos e com as palhetas;
- o mecanismo das palhetas: o jogadores controla-as com as setas do teclado;
- as hitboxes das palhetas;
