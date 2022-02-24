class Rocket:
    def __init__(self, mark, destination, engine):
        pass

    def launch(self):
        pass

    def getAbsolutePower(self):
        pass

    def addEngine(self, newEngine):
        pass


class Engine:
    def __init__(self, weight, e_class):
        pass

    def getPower(self):
        pass

    def getClass(self):
        pass


def main():
    n = int(input())
    for i in range(n):
        command = input()
        quazar_13 = Engine(12500, 'Quazar')
        R1 = Rocket('Falcon-1', 'Mars', quazar_13)
        if command == 'Launch':
            print(R1.launch())
        elif command == 'getAbsolutePower':
            print(R1.getAbsolutePower())
        elif command == 'addEngine':
            quazar_14 = Engine(25000, 'QuazarL')
            R1.addEngine(quazar_14)
            print(R1.getAbsolutePower())
        elif command == 'showEngineClasses':
            print(f'Engines of {R1.mark} are:')
            print(len(R1.engines))
            for i in R1.engines:
                print(i.getClass())


if __name__ == '__main__':
    main()
