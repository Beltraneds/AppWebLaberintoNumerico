# 🧩 App Web Laberinto Numérico

Esta es una aplicación web desarrollada con **Flask** que permite resolver un laberinto numérico donde solo puedes moverte a celdas adyacentes si su número divide exactamente al número actual. El sistema valida las rutas usando una búsqueda en profundidad (**DFS**) y entrega una posible ruta si existe.

---

## 🚀 Características

- Permite ingresar una matriz numérica de hasta 10x10.
- Puedes definir coordenadas de inicio y fin.
- Calcula y muestra una ruta válida usando DFS.
- Visualiza el laberinto con estilo interactivo.
- Valida entradas incorrectas y muestra mensajes claros.

---

## 🛠️ Requisitos

- Python 3.7 o superior
- pip (instalador de paquetes de Python)
- Flask

---

## ⚙️ Instalación

### ✅ Opción 1: Con entorno virtual (recomendado)

1. Clona este repositorio:

```bash
git clone https://github.com/Beltraneds/AppWebLaberintoNumerico.git
cd laberinto_numerico
```

2. Crea y activa un entorno virtual:

### En Windows:
```bash
python -m venv env
env\Scripts\activate
```

### En macOS/Linux:
```bash
python3 -m venv env
source env/bin/activate
```

3. Instala las dependencias:

```bash
pip install flask
```

4. Ejecuta la aplicación:

```bash
flask --app app run
```

5. Abre el navegador y ve a:

```bash
http://127.0.0.1:5000/
```

### 🔧 Opción 2: Sin entorno virtual

Asegúrate de tener Flask instalado globalmente.

1. Clona el repositorio y accede a la carpeta:

```bash
git clone https://github.com/Beltraneds/AppWebLaberintoNumerico.git
cd laberinto_numerico
```

2. Instala Flask (si no lo tienes):

```bash
pip install flask
```

3. Ejecuta el servidor:

```bash
flask --app app run
```

4. Abre tu navegador en:

```bash
http://127.0.0.1:5000/
```

## 📁 Estructura de carpetas

```cpp
laberinto-numerico/
├── app.py
├── static/
│   ├── style.css
│   └── script.js
├── templates/
│   └── index.html
├── README.md
```