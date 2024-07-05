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

**Possiveis soluções para erros**
Caso tenha erro ao tentar executar a escrita no banco de dados deve-se verificar e corrigir a permissão de escrita do arquivo e respectivo diretorio, conforme a seguir :  
  * chmod 755 /instance
  * chmod 666 /instance/activities.db
  * chown seu_usuario:seu_grupo /instance/activities.db 
