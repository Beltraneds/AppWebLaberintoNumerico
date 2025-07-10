from flask import Flask, render_template, request

app = Flask(__name__)

# Función que convierte el texto ingresado por el usuario en un "laberinto" de números enteros
# Cada fila está separada por saltos de línea (\n) y cada número por espacios
def parsear_laberinto(texto):
    return [list(map(int, fila.split())) for fila in texto.strip().split('\\n')]

# Esta función implementa una búsqueda en profundidad (DFS) para encontrar un camino
# desde el punto de inicio hasta el punto de destino en la "laberinto", cumpliendo la regla de divisibilidad
def buscar_camino(laberinto, inicio, destino):
    filas, columnas = len(laberinto), len(laberinto[0])
    visitado = [[False] * columnas for _ in range(filas)]
    camino = []

    # Función recursiva que explora las celdas adyacentes válidas
    def dfs(x, y):
        
        # verifica límites y si la celda ya fue visitada
        if not (0 <= x < filas and 0 <= y < columnas) or visitado[x][y]:
            return False
        
        camino.append((x, y))
        visitado[x][y] = True

        if (x, y) == destino:
            return True

        # Explorar las cuatro direcciones: arriba, abajo, izquierda, derecha
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < filas and 0 <= ny < columnas and not visitado[nx][ny]:
                
                #Verifica que la celda adyacente sea divisible por la celda actual
                if laberinto[x][y] % laberinto[nx][ny] == 0:
                    if dfs(nx, ny):
                        return True
                    
        # Si no se encuentra un camino, retrocede
        camino.pop()
        return False

    # Ejecuta DFS desde el punto de inicio
    return camino if dfs(inicio[0], inicio[1]) else None

@app.route('/', methods=['GET', 'POST'])
def index():
    laberinto = []
    inicio = (0, 0)
    fin = (0, 0)
    input_laberinto = ""
    
    if request.method == 'POST':
        input_laberinto = request.form["dimensiones"]
        laberinto = parsear_laberinto(input_laberinto)
        inicio = (int(request.form["inicio_fila"]), int(request.form["inicio_columna"]))
        fin = (int(request.form["fin_fila"]), int(request.form["fin_columna"]))
        camino = buscar_camino(laberinto, inicio, fin)

    else:
        camino = None
    return render_template('index.html', laberinto=laberinto, inicio=inicio, fin=fin, camino=camino, input_laberinto=input_laberinto)

if __name__ == '__main__':
    app.run(debug=True)