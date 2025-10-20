# Crear una lista de ejemplo
my_list = [45, 12, 78, 23, 56, 89, 34, 67, 91, 5]
print(f"Lista original: {my_list}")
print()

# ENCONTRAR EL MÁXIMO usando métodos de lista
# Ordenamos una copia y tomamos el último elemento
sorted_list = my_list.copy()
sorted_list.sort()
maximo = sorted_list.pop()  # pop() sin argumentos elimina y retorna el último
print(f"Elemento máximo: {maximo}")

# ENCONTRAR EL MÍNIMO usando métodos de lista
# Ya tenemos la lista ordenada (aunque modificada por pop)
minimo = sorted_list.pop(0)  # pop(0) elimina y retorna el primer elemento
print(f"Elemento mínimo: {minimo}")

# Longitud contando con count()
# Crear una lista temporal y contar cuántos elementos agregamos
temp = []
for elem in my_list:
    temp.append(1)  # Agregamos 1 por cada elemento
longitud = temp.count(1)  # Contamos cuántos "1" hay
print(f"Longitud: {longitud}")
