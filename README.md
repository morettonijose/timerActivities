# timerActivities
PYTHON FLASK SWAGGER API - CRUD para criar e gerenciar tarefas

 
**Instalação de Blibliotecas  Necessárias :**
 
**WINDOWS/LINUX :**

pip install  flask

pip install flask-restful

pip install flask-swagger-ui

Pip install -U Flask-SQLAlchemy

pip  install flask-cors

 
**MAC OS :**

pip3 install  flask

pip3 install flask-restful

pip3 install flask-swagger-ui

Pip3 install -U Flask-SQLAlchemy

pip3  install flask-cors


**Rodando o Projeto :**

//Verifique se tem o pythin instalado em seu terminal e teste a versão do Python   : 

python3 —version


// Se não tem o python instalado , siga no link a seguir e instale, e então reinicie o seu terminal.
// Baixe e Instale aqui : https://www.python.org/downloads/ ; 

//Verifique se tem o pythin instalado em seu terminal e teste a versão do Python   : 
python3 —version

//Uma vez que você teve sucesso em verificar a versão do Phyton , processa para iniciar a  a instância e digite o código a seguir em seu terminal . 

python3 app.py      

**/////PRONTO///////**

Você deverá  ver uma resposta do tipo , com o endereço para acesso a API : **http://127.0.0.1:5000**  :

 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 608-878-228


PARA ACESSAR O SWAGGER DA DOCUMENTAÇÃO acesse o seguinte link: **http://127.0.0.1:5000/swagger/**


**Possiveis soluções para erros**
Caso tenha erro ao tentar executar a escrita no banco de dados deve-se verificar e corrigir a permissão de escrita do arquivo e respectivo diretorio, conforme a seguir :  
  * chmod 755 /instance
  * chmod 666 /instance/activities.db
  * chown seu_usuario:seu_grupo /instance/activities.db 
