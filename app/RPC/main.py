import eel
from .Gretting import say_hello 


fn_map = {
    "say_hello": say_hello
}

@eel.expose
def handler(params={}):
    """
    Debe recibir un diccionario de la siguiente forma.
    {
        'fnName': 'Nombre de la función a ejecutar',
        'params': {}, // parámetros de la función
    }
    """
    fn_name = params['fnName']
    fn_params = params['fnParams']

    return fn_map[fn_name](**fn_params)
