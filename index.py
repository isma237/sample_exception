buses = ['bus-A', 'bus-B', 'bus-C']

def get_bus(index):
    try:
        return buses[index]
    except IndexError:
        print("{} n'est pas compris dans la plage des index tableau".format(index))
        return "Empty"
    except TypeError:
        print("L'index doit etre un entier")
        return "Empty"
    except Exception:
        print("Un probleme est survenu")


bus = get_bus('2')
print(bus)
print("Nouvelle demande")