from sklearn.naive_bayes import MultinomialNB
from dados import read_with_pandas_without_dummies

modelo = MultinomialNB()


def main():
    x, y = __get_dados()
    x_fit = x[:int(len(x)*0.9) + 1]
    y_fit = y[:int(len(y)*0.9) + 1]
    modelo.fit(x_fit, y_fit)
    taxa_acerto, resultado = __testar_modelos(x, y)
    print('==============================')
    print('Modelo treinado')
    print('Taxa de acerto = ', taxa_acerto, '%')
    print('Resultado final = ', resultado)
    print('             Fim              ')
    print('==============================')


def __testar_modelos(x, y):
    x_teste = x[-(int(len(x) * 0.1)):]
    y_teste = y[-(int(len(y) * 0.1)):]
    resultado = modelo.predict(x_teste)
    diferencas = resultado - y_teste
    acertos = [d for d in diferencas if d == 0]
    taxa_acerto = 100 * len(acertos) / len(x_teste)
    return taxa_acerto, resultado


def __get_dados():
    return read_with_pandas_without_dummies('./csv/acesso', 'comprou', ['home', 'como_funciona', 'contato'])


if __name__ == '__main__':
    main()
