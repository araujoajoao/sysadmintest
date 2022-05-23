# SysAdminTest

- Criar um script Vagrant que suba uma máquina CentOS 7.x com 2 CPUs (2 cores de processador), 2 GB de memória RAM e 20gb de HD chamada “teste-superset”.

- Criar um script em python (usando Paramiko para conexão SSH) que faça a instalação do Python 3 e do Apache Superset na máquina Centos 7 criada e suba o webserver do Superset.

- Adicionar ao script Python a instalação do MySQL e a integração dele com o Superset.

- Adicionar ao script Python a instalação do Redis e a integração dele com o Superset.


```
python3 -m venv virtualenv

```

```
source virtualenv/bin/activate

```

```
pip3 install apache-superset

```
```
pip3 install mysql-connector-python

```
```
pip3 install paramiko
```

```
python3 -m pip install -r requirements.txt

```
```
python3 ssh_python.py
```




