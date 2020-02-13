


def run():
    with open('numeros.txt', 'w') as f:
        for i in range(20):
            f.write(str(i))


if __name__ == '__main__':
    run()
