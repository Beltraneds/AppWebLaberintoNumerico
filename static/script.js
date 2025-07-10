const grid = document.getElementById("grid");
if (grid) {
    const matrix = JSON.parse(grid.dataset.matrix);
    const start = grid.dataset.start.split(',').map(Number);
    const end = grid.dataset.end.split(',').map(Number);
    let current = start;
    let path = [current.toString()];

    document.querySelectorAll(".cell").forEach(cell => {
        const [i, j] = cell.dataset.pos.split(',').map(Number);
        if (i === start[0] && j === start[1]) {
            cell.classList.add("start", "visited");
        }
        if (i === end[0] && j === end[1]) {
            cell.classList.add("end");
        }

        cell.addEventListener("click", () => {
            const [ci, cj] = current;
            const [ni, nj] = [i, j];

            const isAdjacent = Math.abs(ci - ni) + Math.abs(cj - nj) === 1;
            const notVisited = !path.includes([ni, nj].toString());
            const divisible = matrix[ci][cj] % matrix[ni][nj] === 0;

            if (isAdjacent && notVisited && divisible) {
                current = [ni, nj];
                path.push(current.toString());
                cell.classList.add("visited");

                if (ni === end[0] && nj === end[1]) {
                    Swal.fire("¡Completado!", "Has resuelto el laberinto 🎉", "success");
                }
            } else {
                cell.classList.add("wrong");
                Swal.fire("Error", "Movimiento no válido. El juego se reiniciará.", "error")
                    .then(() => location.reload());
            }
        });
    });
}

function validateForm() {
    const matrixText = document.getElementById("dimensiones").value.trim();
    const rows = matrixText.split("\\n");

    if (rows.length > 10) {
        Swal.fire("Error", "La matriz no puede tener más de 10 filas.", "warning");
        return false;
    }

    for (let r of rows) {
        const cols = r.trim().split(/\s+/);

        if (cols.length > 10) {
            Swal.fire("Error", "Cada fila no puede tener más de 10 columnas.", "warning");
            return false;
        }

        for (let val of cols) {
            if (!/^\d+$/.test(val)) {
                Swal.fire("Error", `Valor inválido: "${val}". Solo se permiten enteros positivos.`, "error");
                return false;
            }
        }
    }

    return true;

}

window.onload = () => {
    const grid = document.getElementById("grid");
    if (grid) {
        // desplazamos la vista suavemente hacia el laberinto
        grid.scrollIntoView({ behavior: "smooth", block: "center" });
    }
};