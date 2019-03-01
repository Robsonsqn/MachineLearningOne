import csv
import pandas as pd


def carregar_acessos():
    x = []
    y = []

    arquivo = open('./csv/acesso.csv', 'r')
    leitor = csv.reader(arquivo)
    next(leitor)
    for home, como_funciona, contato, comprou in leitor:
        x.append([int(home), int(como_funciona), int(contato)])
        y.append(int(comprou))
    return x, y


def carregar_buscas():
    x = []
    y = []

    arquivo = open('buscas.csv', 'r')
    leitor = csv.reader(arquivo)
    next(leitor)
    for home, busca, logado, comprou in leitor:
        x.append([int(home), busca, int(logado)])
        y.append(int(comprou))
    return x, y


def read_with_pandas_without_dummies(fileName, yname, xname):
    df = pd.read_csv(fileName+'.csv')
    y_df = df[yname]
    x_df = df[xname]
    x = x_df.values
    y = y_df.values
    return x, y


def read_with_pandas_x_dummies(fileName, yname, xname):
    df = pd.read_csv(fileName+'.csv')
    y_df = df[yname]
    x_df = df[xname]
    x_dummies_df = pd.get_dummies(x_df)
    y_dummies_df = pd.get_dummies(y_df)
    x = x_dummies_df.values
    y = y_dummies_df[0].values
    return x, y


if __name__ == '__main__':
    read_with_pandas_x_dummies()
