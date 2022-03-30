import dists as dists

# goal sempre sera 'bucharest'
def a_star(start, goal='Bucharest'):
    """
    Retorna uma lista com o caminho de start até 
    goal segundo o algoritmo A*
    """
    h = dists.straight_line_dists_from_bucharest

    """ cria a variavel border que recebe um array de com os caminhos percorridos em ordem.
            Onde: 
                (custo total do caminho até a cidade, 
                    cidade, 
                    distancia percorrida da cidade anterior) """
    border = [[(h[start],start,0)]]

    """ Nó que esta sendo explorado atualmente, sempre igual ao caminho mais proximo da borda pois ela será ordenada conforme o custo total. min > max """
    no = border[0]

    """ Realiza o loop se o nó explorado não for o destino """
    while no[-1][-2] != goal:

        """ Se a borda estiver vazia significa que não existe caminho ao destino """
        if not border:
            break

        """ Pega os caminhos possiveis apartir do no explorado """
        paths = dists.dists[no[-1][-2]]

        """ Remove o no explorado, pois ele será dividido entre seus possiveis """
        border = border[1:]

        """ Pega o custo total do no explorado """
        f = no[-1][-3]

        """ Percorre os caminhos possiveis """
        for path in paths:
            """ Pega a cidade e a heuristica """
            city,dist = path
            """ Calcula o custo total com o novo caminho """
            heuristic = h[city] + dist + f
            """ Cria a tupla a ser inserida na borda """
            new_path = (heuristic,city,dist)
            """ Cria um novo caminho com base no nó explorado """
            new_way = list(no)
            """ Adiciona ao final o novo destino do caminho """
            new_way.append(new_path)
            """ Adiciona novo caminho a borda """
            border.append(new_way)
        
        """ Ordena a borda conforme o valor custo total de cada caminho """
        border.sort(key=lambda x: x[-1][-3])
        """" Atualiza nó explorado """
        no = list(border[0])

    """ Ao final retorna caminho de mais baixo custo """
    return border[0]

a_star('Oradea')

