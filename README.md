# timerActivities API
API  para gerenciar e cronometrar  tarefas usando PYTHON, FLASK e SWAGGER .

Acesse aqui  o github com um exemplo do front-end para a aplicação : https://github.com/morettonijose/timerActivities-frontEnd
 
## Requisitos

- Python 3.x
- pip (gerenciador de pacotes Python)

## Instalação

Verifique se tem o python instalado em seu terminal verificando a versão do Python   : 
```bash
python3 —version
```

 Se não tem o python instalado , siga no link a seguir e instale, e então reinicie o seu terminal.

Baixe e Instale aqui : https://www.python.org/downloads/ ; 

Após reiniciar o terminar verifique novamente se tem o python instalado em seu terminal verificando a versão do Python   : 

```bash
python3 —version
```


Uma vez que você teve sucesso em verificar a versão do Phyton , proceder para iniciar a instância e digite o código a seguir em seu terminal . 


### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```



### 2.  Crie e ative um ambiente virtual


####  FOR WINDOWS / LINUX 
```bash
python -m venv venv
```


####  FOR MAC Crie e ative um ambiente virtual
```bash
python3 -m venv venv
```


```bash
source venv/bin/activate
. venv/bin/activate
```




### 3.   Instale as bibliotecas necessárias

#### FOR WINDOWS/LINUX  
```bash
pip install -r static/requirements.txt
```


####  FOR MAC 
```bash
pip3 install -r static/requirements.txt
```



### 4. Rodando o Projeto

**WINDOWS / LINUX**
```bash
python app.py
```

**MAC OS**
```bash
python3 app.py
```


### 5. Acesse o link para verificar a API  no navegador

**Você receberá uma mensagem do tipo :**
```bash
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 608-878-228
```


E então já  poderá acessar a API no endereço a a seguir  : **http://127.0.0.1:5000/activities**  

A rota  para o SWAGGER com a documentação da api está a seguir  : **http://127.0.0.1:5000/swagger/**



### 6. Possíveis soluções de erros



**//////ERRO DE ESCRITA NO BANCO DE DADOS ///////**

Caso tenha erro ao tentar executar a escrita no banco de dados deve-se verificar e corrigir a permissão de escrita do arquivo e respectivo diretorio, conforme a seguir :  

```bash
  * chmod 755 /instance
  * chmod 666 /instance/activities.db
  * chown seu_usuario:seu_grupo /instance/activities.d
```

**/////////////////////////////////////////////////////////////////**


**//////ERRO DE INSTALACAO DAS BIBLIOTECAS ///////**

**///// Para instalar manualmente as Blibliotecas  Necessárias :///////**

**WINDOWS/LINUX :**
```bash

pip install  flask

pip install flask-restful

pip install flask-swagger-ui

Pip install -U Flask-SQLAlchemy

pip  install flask-cors

//verifica bibliotecas instaladas no ambiente
pip list
```



 
**MAC OS :**

```bash
pip3 install Flask
  
pip3 install  flask

pip3 install flask-restful

pip3 install flask-swagger-ui

Pip3 install -U Flask-SQLAlchemy

pip3  install flask-cors

//verifica bibliotecas instaladas no ambiente
pip3 list
```
 
**/////////////////////////////////////////////////////////////////**



