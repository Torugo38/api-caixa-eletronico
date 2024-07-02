from flask import Blueprint, request, jsonify

bp = Blueprint('routes', __name__)

def calcular_cedulas(valor):
    cedulas = [100, 50, 20, 10, 5, 2]
    resultado = {cedula: 0 for cedula in cedulas}
    for cedula in cedulas:
        if valor >= cedula:
            quantidade, valor = divmod(valor, cedula)
            resultado[cedula] = quantidade

    if valor == 1 and resultado[5] > 0:
        resultado[5] -= 1
        resultado[2] += 3
        valor -= 1

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