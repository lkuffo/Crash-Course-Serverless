import datetime


def suma(event, context):
    operando_a = event['operando_a']
    operando_b = event['operando_b']
    if not isinstance(operando_a, int) or not isinstance(operando_b, int):
        raise Exception('Parametros no son numeros enteros')
    return {
        "status": 200,
        "message": "ok",
        "suma": operando_b + operando_a
    }


def fecha_actual(event, context):
    return {
        "status": 200,
        "message": "ok",
        "suma": datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%s')
    }

