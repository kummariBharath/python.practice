def adjacency_list_matrix_converter(adj_list):
    num_nodes=len(adj_list)
    matrix=[[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
    for node in adj_list:
        for neighbour in adj_list[node]:
            matrix[node][neighbour]=1

    for row in matrix:
        print(row)
                