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

# En Windows
python -m venv env
env\Scripts\activate
