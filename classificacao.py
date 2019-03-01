        ##gordinho, perninha curta, faz au au
porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
porco4 = [1, 1, 1]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]
cachorro4 = [1, 1, 0]

dados = [porco1, porco2, porco3, porco4, cachorro1, cachorro2, cachorro3, cachorro4]

marcacoes = [1, 1, 1, 1, -1, -1, -1, -1]

misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 1]
misterioso4 = [0, 1, 0]
teste = [misterioso1, misterioso2, misterioso3, misterioso4]
marcacoes_teste = [-1, 1, -1, 1]
from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)
resultado = modelo.predict(teste)
diferencas = resultado - marcacoes_teste
print(resultado)
acertos = [d for d in diferencas if d==0]
total_acertos = len(acertos)
total_elementos = len(teste)
taxa_acerto = 100 * total_acertos / total_elementos
print(taxa_acerto)



