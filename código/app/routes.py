from flask import Blueprint, request, jsonify

bp = Blueprint('routes', __name__)

def calcular_cedulas(valor):
    cedulas = [100, 50, 20, 10, 5, 2]
    resultado = {}
    for cedula in cedulas:
        quantidade, valor = divmod(valor, cedula)
        resultado[cedula] = quantidade
    return resultado

@bp.route('/api/saque', methods=['POST'])
def saque():
    dados = request.get_json()
    if 'valor' not in dados:
        return jsonify({"erro": "Valor do saque não fornecido"}), 400
    valor = dados['valor']
    if not isinstance(valor, int) or valor <= 0:
        return jsonify({"erro": "Valor do saque deve ser um inteiro positivo"}), 400
    resultado = calcular_cedulas(valor)
    return jsonify(resultado)