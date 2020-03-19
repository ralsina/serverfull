import importlib
from functools import partial

from flask import Flask, request

app = Flask("serverfull")

bees = ["a", "b"]  # TODO: get this from somewhere


def generic_handler(real_handler):
    print("Generic handler called")
    return real_handler(request)


for bee in bees:
    bee_path = f"bees.{bee}"
    print(f"Importing {bee_path}")
    bee_mod = importlib.import_module(bee_path)
    bee_mod = importlib.reload(bee_mod)  # TODO: be smarter, but who cares
    print(f"/bees/{bee} => {bee_mod.handler}")
    app.add_url_rule(
        f"/bees/{bee}", f"bee.{bee}", partial(generic_handler, (bee_mod.handler))
    )
