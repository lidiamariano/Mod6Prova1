# Módulo 6 - Ponderada 1 - Desenhando com turtlesim
## Breve descrição:

## Como instalar e rodar o sistema?
### 1) Clone o repositório: 
Primeiramente clone ou baixe o zip do seguinte repositório https://github.com/lidiamariano/Mod6Prova1
### 2) Instale as dependências: 
Na pasta raiz do repositório existe o arquivo requirements.txt, que será necessário para instalar os pacotes necessários para rodar o projeto. Faça isso pelo seguinte comando:<br/>
`pip install -r requirements.txt`
### 3) Rodando o turtlesim
Abra um terminal dentro da pasta do seu repositório e execute: `ros2 run turtlesim turtlesim_node`
### 5) Construindo ambiente ros:
Ainda na pasta raiz do diretório execute:
`colcon build` e `source install/local_setup.bash` 
Em seguida execute:
`ros2 pkg executables ola_mundo`
Então, podemos finalmente rodar o arquivo com ROS:
`ros2 run ola_mundo ola`
