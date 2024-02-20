def is_valid(v, pos, path):
    # Check if this vertex is an adjacent vertex of
    # the previously added vertex
    if adj_matrix[path[pos - 1]][v] == 0:
        return False

    # Check if the vertex has already been included
    if v in path:
        return False

    return True


def hamiltonian_cycle_util(path, pos):
    # Base case: If all vertices are included in the path
    if pos == len(adj_matrix):
        # And if there is an edge from the last included vertex to the first vertex
        return adj_matrix[path[pos - 1]][path[0]] == 1

    # Try different vertices as a next candidate in Hamiltonian Cycle
    for v in range(1, len(adj_matrix)):
        if is_valid(v, pos, path):
            path[pos] = v

            # Recur to construct rest of the path
            if hamiltonian_cycle_util(path, pos + 1):
                return True

            # If adding vertex v doesn't lead to a solution, then remove it
            path[pos] = -1

    return False


def hamiltonian_cycle():
    path = [-1] * len(adj_matrix)

    # Let us put vertex 0 as the first vertex in the path
    path[0] = 0

    # If there is no Hamiltonian Cycle, then the path will not be feasible
    if not hamiltonian_cycle_util(path, 1):
        print("Solution does not exist")
        return False

    print("Solution exists, the path is: ")
    for vertex in path:
        print(vertex, end=" ")
    print(path[0], end=" ")

    return True


if __name__ == "__main__":
    # Define the adjacency matrix for your graph
    adj_matrix = [
        [0, 1, 1, 1, 0, 0],
        [1, 0, 1, 0, 1, 0],
        [1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0]
    ]

    # Call the function
    hamiltonian_cycle()
