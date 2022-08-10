import pytest
from lambda_handler import suma


def test_suma_correcta():
    evento = {
        "operando_a": 5,
        "operando_b": 9
    }
    res = suma(evento, {})
    assert res["suma"] == 14


def test_suma_incorrecta():
    try:
        evento = {
            "operando_a": "valor_invalido",
            "operando_b": 9
        }
        res = suma(evento, {})
        assert False
    except Exception as e:
        error = str(e)
        assert error == 'Parametros no son numeros enteros'
