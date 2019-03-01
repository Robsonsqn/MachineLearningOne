from collections import Counter


def main():
    print('wip')


def analize(y_array):
    maior = max(Counter(y_array).values())
    taxa_acerto_base = 100.0 * maior / len(y_array)
    print('==============================')
    print('Modelo treinado Base')
    print(taxa_acerto_base, '%')
    print('==============================')


if __name__ == '__main__':
    main()
