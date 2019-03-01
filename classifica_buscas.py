from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import AdaBoostClassifier
from dados import read_with_pandas_x_dummies
from validacao_base import analize

__modelo = MultinomialNB()
__modeloAda = AdaBoostClassifier()
__porcentagem_treino = 0.8
__porcentagem_teste = 1 - __porcentagem_treino


def main():
    x, y = __get_dados()
    x_fit = x[:int(len(x)*__porcentagem_treino)]
    y_fit = y[:int(len(y)*__porcentagem_treino)]
    __modelo.fit(x_fit, y_fit)
    __modeloAda.fit(x_fit, y_fit)
    analize(y_fit)
    taxa_acerto, acertos, taxa_acertoAda, acertosAda = __testar_modelos(x, y)
    print('==============================')
    print('Modelo treinado MultinomialNB')
    print('Taxa de acerto = ', taxa_acerto, '%')
    print('==============================')
    print('Modelo treinado AdaBoostClassifier')
    print('Taxa de acerto = ', taxa_acertoAda, '%')
    print('==============================')
    print('             Fim              ')


def __testar_modelos(x, y):
    x_teste = x[-(int(len(x) * __porcentagem_teste)):]
    y_teste = y[-(int(len(y) * __porcentagem_teste)):]
    resultado = __modelo.predict(x_teste)
    resultadoAda = __modeloAda.predict(x_teste)
    diferencas = resultado - y_teste
    diferencasAda = resultadoAda - y_teste
    acertos = [d for d in diferencas if d == 0]
    acertosAda = [d for d in diferencasAda if d == 0]
    taxa_acerto = 100 * len(acertos) / len(x_teste)
    taxa_acertoAda = 100 * len(acertosAda) / len(x_teste)
    return taxa_acerto, acertos, taxa_acertoAda, acertosAda


def __get_dados():
    return read_with_pandas_x_dummies('./csv/buscas', 'comprou', ['home', 'busca', 'logado'])


if __name__ == '__main__':
    main()
