from statistics import mean

list = []
for x in range(10):
    mi_num = int(input("Deme un número: "))
    list.append(mi_num)

print("Suma:", sum(list), "\n"
      "Promedio:", mean(list), "\n"
      "Mayor", max(list), "\n"
      "Min", min(list), "\n")