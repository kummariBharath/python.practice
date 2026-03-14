def adjacency_list_matrix_converter(adj_list):
    num_nodes=len(adj_list)
    matrix=[[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
    
