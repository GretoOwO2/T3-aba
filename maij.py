
# Laberinto 9×9 del enunciado: encontrar todas las rutas con ≥ 23 puntos
# ------------------------------------------------
# 0 = pared
# 1 = paso libre (sin sumar puntos)
# 3 o 4 = paso que suma 3 o 4 puntos
# I (8,0) y F (0,0) se consideran valor 1.

def print_labyrinth(maze, path=None, start=(8,0), end=(0,0)):
    """Imprime el laberinto marcando el camino con '*' y 'I'/'F' en inicio/fin."""
    R, C = len(maze), len(maze[0])
    lab = [[' ']*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if (i,j) == start:
                lab[i][j] = 'I'
            elif (i,j) == end:
                lab[i][j] = 'F'
            else:
                lab[i][j] = str(maze[i][j])
    if path:
        for (r,c) in path:
            if (r,c) not in (start, end):
                lab[r][c] = '*'
    for fila in lab:
        print(' '.join(fila))
    print()

def solve_all_paths(maze, start, end, required_points):
    """
    Backtracking: explora todas las rutas de start a end,
    guarda las que acumulen ≥ required_points.
    Retorna lista de (path, puntos).
    """
    R, C = len(maze), len(maze[0])
    visited = [[False]*C for _ in range(R)]
    solutions = []
    # orden: arriba, derecha, abajo, izquierda
    directions = [(-1,0),(0,1),(1,0),(0,-1)]

    def backtrack(r, c, path, points):
        if (r, c) == end:
            if points >= required_points:
                solutions.append((path.copy(), points))
            return
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and maze[nr][nc] != 0:
                visited[nr][nc] = True
                extra = maze[nr][nc] if maze[nr][nc] in (3,4) else 0
                path.append((nr,nc))
                backtrack(nr, nc, path, points + extra)
                path.pop()
                visited[nr][nc] = False

    visited[start[0]][start[1]] = True
    backtrack(start[0], start[1], [start], 0)
    return solutions

def main():
    # Matriz del enunciado (F y I tratados como 1 internamente):
    maze = [
        [1,1,1,3,0,1,1,1,4],  # fila 0: F,1,1,3,0,1,1,1,4
        [3,0,0,1,0,1,0,0,1],
        [1,1,0,1,1,1,1,0,1],
        [0,1,0,1,0,0,1,1,1],
        [1,1,1,1,1,3,1,1,1],
        [3,0,1,0,0,0,1,0,4],
        [1,1,1,3,1,0,1,1,1],
        [1,0,0,1,0,1,1,1,1],
        [1,1,3,1,0,1,1,1,1],  # fila 8: I,1,3,1,0,1,1,1,1
    ]
    start = (8,0)   # I
    end   = (0,0)   # F
    required_points = 23

    print("\nLaberinto original (I=inicio, F=fin, 0=pared, 1=libre, 3/4=puntos):")
    print_labyrinth(maze, start=start, end=end)

    sols = solve_all_paths(maze, start, end, required_points)
    if not sols:
        print(f"No se encontraron rutas con al menos {required_points} puntos.")
    else:
        print(f"Se encontraron {len(sols)} rutas con ≥ {required_points} puntos:\n")
        for idx,(path,pts) in enumerate(sols,1):
            print(f"--- Ruta #{idx}: {pts} puntos ---")
            print_labyrinth(maze, path=path, start=start, end=end)

if __name__ == "__main__":
    main()
