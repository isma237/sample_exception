buses = ['bus-A', 'bus-B', 'bus-C']

def get_bus(index):
    try:
        return buses[index]
    except IndexError:
        print("{} n'est pas compris dans la plage des index tableau".format(index))
        return "Bus-D"
    except TypeError:
        print("L'index doit etre un entier")
        return "Bus-D"
    except Exception:
        print("Un probleme est survenu")
        return "Bus-D"


bus = get_bus('2')
print(bus)
print("Nouvelle demande")