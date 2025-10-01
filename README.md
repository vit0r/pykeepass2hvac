# pykeepass2hvac

export keepass2 secrets and import to hashicorp vault

## setup

```console
python3 -m virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.sample .env
# atualizar os valores em .venv para seu caso
python main.py 
```
