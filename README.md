# timerActivities API
PYTHON FLASK SWAGGER API - CRUD para criar e gerenciar tarefas
 
## Requisitos

- Python 3.x
- pip (gerenciador de pacotes Python)

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

### 2.  Crie e ative um ambiente virtual
python3 -m venv venv
source venv/bin/activate

### 3.  Instale as bibliotecas necessárias
pip install -r statics/requirements.txt









 
 
**/////1 ) Instalação de Blibliotecas  Necessárias :///////**

 

**WINDOWS/LINUX :**

pip install  flask

pip install flask-restful

pip install flask-swagger-ui

Pip install -U Flask-SQLAlchemy

pip  install flask-cors


 
**MAC OS :**

 
Para criae o ambiente virtual python siga esse tutorial  : **https://www.youtube.com/watch?v=0hInltB9QNY**

//a seguir adicione o FLASK USANDO O PIP, se não tem o pio instalado verifique este tutorial : **https://www.youtube.com/watch?v=B1Qcb5xQ96M**

pip3 install Flask
  
pip3 install  flask

pip3 install flask-restful

pip3 install flask-swagger-ui

Pip3 install -U Flask-SQLAlchemy

pip3  install flask-cors


//verifica bibliotecas instaladas no ambiente

pip3 list


 

**//////2 )  Rodando o Projeto :///////**

//Verifique se tem o python instalado em seu terminal verificando a versão do Python   : 

python3 —version


// Se não tem o python instalado , siga no link a seguir e instale, e então reinicie o seu terminal.
// Baixe e Instale aqui : https://www.python.org/downloads/ ; 

//Após reiniciar o terminar verifique novamente se tem o python instalado em seu terminal verificando a versão do Python   : 
python3 —version

//Uma vez que você teve sucesso em verificar a versão do Phyton , proceda para iniciar a instância e digite o código a seguir em seu terminal . 

python3 app.py      

**//////3 )  PRONTO///////**

**Você receberá uma mensagem do tipo :**

 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 608-878-228


E então já  poderá acessar a API no endereço a a seguir  : **http://127.0.0.1:5000**  :

A rota  para o SWAGGER com a documentação da api está a seguir  : **http://127.0.0.1:5000/swagger/**


**//////Possiveis soluções para erros///////**

Caso tenha erro ao tentar executar a escrita no banco de dados deve-se verificar e corrigir a permissão de escrita do arquivo e respectivo diretorio, conforme a seguir :  
  * chmod 755 /instance
  * chmod 666 /instance/activities.db
  * chown seu_usuario:seu_grupo /instance/activities.db 
