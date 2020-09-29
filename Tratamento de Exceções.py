# Realizar a divisão de dois números inteiros positivos
# Identificar e tratar os possíveis erros.

try:
    a = int(input('Informe um número inteiro positivo: '))
    b = int(input('Informe um número inteiro positivo: '))
    # Se algum número for negativo, provoca uma exceção
    if a < 0 or b < 0:
        raise RuntimeError               # raise: gera uma exceção no programa       
    c = a / b
    print('Resultado da divisão: ', c)  
except ZeroDivisionError:
    print('Erro. Ocorreu uma divisão por zero')
except ValueError:
    print('Erro. O valor informado não é do tipo inteiro.')
except NameError:
    print('Erro. Nome de variável inválido.')
except RuntimeError:
    print('Erro. O número informado deve ser positivo.')
except Exception:                       
    # Exception: ocorre para qualquer outro tipo de erro
    print("Erro. Ocorreu um erro inesperado.")
else:
    # O else é executado caso nenhum erro aconteça
    print('Programa executado com sucesso.')
finally:
    # O finally é executado em qualquer situação
    print('Obrigado por utilizar esse programa.')


# Realizar a divisão de dois números inteiros positivos
# Identificar e tratar os possíveis erros.
# Solicitar os dados novamente caso o usuário informar valores inválidos


repetir = True                      # variavel para controlar a repetição 
while repetir == True:
    try:
        a = int(input('Informe um número inteiro positivo: '))
        b = int(input('Informe um número inteiro positivo: '))
        # Se algum número for negativo, provoca uma exceção
        if a < 0 or b < 0:
            raise RuntimeError            # raise: gera uma exceção no programa       
        c = a / b
        print('Resultado da divisão: ', c)  
    except ZeroDivisionError:
        print('Erro. Ocorreu uma divisão por zero')
    except ValueError:
        print('Erro. O valor informado não é do tipo inteiro.')
    except NameError:
        print('Erro. Nome de variável inválido.')
    except RuntimeError:
        print('Erro. O número informado deve ser positivo.')
    except Exception:                       
        # Exception: ocorre para qualquer outro tipo de erro
        print("Erro. Ocorreu um erro inesperado.")
    else:
        # O else é executado caso nenhum erro aconteça
        print('Programa executado com sucesso.')
        # Altera valor da variável, para interromper a repetição while
        repetir = False


# Preencher dicionario com nome cpf e nome de cinco de pessoas.
# Não deve permitir cpfs repetidos.

cadastro = {}

# solicitar o nome de cinco pessoas
while len(cadastro) < 5:                
    try:
        cpf = input('Cpf: ')
        nome = input('Nome: ')
        # se a chave já existir, gera exceção KeyError
        if cpf in cadastro:
            raise KeyError
        cadastro[cpf] = nome
    except KeyError:
        print('O CPF informado já existe.')
    except Exception:
        print('Ocorreu um erro no programa.')
    else:                           
        # quando não ocorrer exceção
        print('CPF e Nome cadastrado !')
    
print(cadastro)

