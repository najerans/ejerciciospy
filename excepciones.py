
velor_verdadero = ['si', 'y']
valor_falso = ['no','n']

def str_to_bool(valor):
    valor=valor.lower()
    if valor in velor_verdadero:
        return True
    elif valor in valor_falso:
        return False
    else:
        raise ValueError('Entrada no valida')
    
    

