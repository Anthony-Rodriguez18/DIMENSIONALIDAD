import matplotlib.pyplot as plt
import math

def read_distances(file_name):
    distances = []
    with open(file_name, 'r') as file:
        for line in file:
            distance = float(line.strip())
            distances.append(distance)
    return distances

def plot_distances(file_name, dim, tic):
    distances = read_distances(file_name)
    
    # Genera los valores para los bins
    bin_values = [i * 0.3 for i in range(0, 100)]
    
    # Genera las etiquetas para el eje x
    x_ticks = [i * tic for i in range(0, 10)]
    
    # Dibuja el histograma
    plt.hist(distances, bins=20, color='#F2AB6D', rwidth=0.85)
    plt.xlabel('Distancia Euclidiana')
    plt.ylabel('Frecuencia')
    plt.title(f'Distribucion de Distancias Euclidianas (Dimension {dim})')
    plt.xticks(x_ticks)
    plt.grid(True)
    plt.show()

# Ejemplo de uso para un archivo de distancias en una dimensión de 10
dim = r'C:\Users\RVDO\source\repos\Maldicion\Maldicion\distancias_dim_10.txt'
plot_distances(dim, 10, 0.25)

dim = r'C:\Users\RVDO\source\repos\Maldicion\Maldicion\distancias_dim_50.txt'
plot_distances(dim, 50, 0.5)
dim = r'C:\Users\RVDO\source\repos\Maldicion\Maldicion\distancias_dim_100.txt'
plot_distances(dim, 100, 0.65)
dim = r'C:\Users\RVDO\source\repos\Maldicion\Maldicion\distancias_dim_500.txt'
plot_distances(dim, 500, 0.95)
dim = r'C:\Users\RVDO\source\repos\Maldicion\Maldicion\distancias_dim_1000.txt'
plot_distances(dim, 1000, 1.5)
dim = r'C:\Users\RVDO\source\repos\Maldicion\Maldicion\distancias_dim_2000.txt'
plot_distances(dim, 2000, 2.0)
dim = r'C:\Users\RVDO\source\repos\Maldicion\Maldicion\distancias_dim_5000.txt'
plot_distances(dim, 5000, 3.0)
