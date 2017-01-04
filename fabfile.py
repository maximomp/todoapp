from fabric.api import local, run, env, put, sudo
from fabric.context_managers import prefix

env.hosts = ["test@104.238.190.112"]
#env.passwords = {"test@104.238.190.112":"test"}


def deploy():
    #put("todoapp","./todoapp/")
    
    put("requirements.txt","./todoapp/")
    put("manage.py","./todoapp/")

    with prefix("source venv/bin/activate"):
        run("pip install -r ./todoapp/requirements.txt")
        
    sudo("service apache2 reload")
