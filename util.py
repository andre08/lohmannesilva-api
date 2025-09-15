

def montaNavegador(pagina, total):
    """Metodo para disponibilizar e configurar o navegador de tabela conforme a quantidade pagina e a pagina atual

    Args:
        pagina (int): Pagina atual que o navegador deve indicar
        total (int): Total de paginas que o navegador ira configurar

    Returns:
        Lista de dicionarios: Retorar uma lista com 7 elementos referente a
            lista = primeira pagina, pagina anterior, opcao 1, opcao 2, opcao 3, proxima pagina, ultima pagina
            Cada item tem 
                visivel (S ou N): Se o elemento de aparecer
                ativada (branco ou disabled): Se o elemento está desativado para cliente
                selecionada (branco ou active): Se o elemento indica a pagina atual
                destino: Pagina de destivo se acionado 
    """
    #Primeira pagina
    visivel = "N"
    ativada = "disabled"
    selecionada = ""
    destino = 0

    if pagina <= total:
        if total > 3:
            visivel = "S"
            destino = 1
            if pagina > 1:
                ativada = ""

    primeira = ["Primeira", visivel, ativada, selecionada, destino]

    #Pagina Anterior
    visivel = "N"
    ativada = "disabled"
    selecionada = ""
    destino = 0

    if pagina <= total:
        if total > 3:
            visivel = "S"
            if pagina - 1 >= 1:
                ativada = ""
                destino = pagina - 1
    
    anterior = ["Anterior", visivel, ativada, selecionada, destino]

    #Pagina 1 ou anterior - 1
    visivel = "N"
    ativada = "disabled"
    selecionada = ""
    destino = 0

    if pagina <= total:
        if total >= 1:
            visivel = "S"
            ativada = ""
            if pagina == 1:
                selecionada = "active"
                destino = 1
            elif pagina == 3 and total == 3:
                selecionada = ""
                destino = 1
            elif pagina == total and total > 2:
                destino = pagina - 2
            else:
                destino = pagina - 1

    pagina_1 = [destino, visivel, ativada, selecionada, destino]

    #Pagina 2 ou atual
    visivel = "N"
    ativada = "disabled"
    selecionada = ""
    destino = 0

    if pagina <= total:
        if total >= 2:
            visivel = "S"
            ativada = ""
            
            if (pagina == 1 and total > 3) :
                selecionada = ""
                destino = 2
            elif ((pagina == 1 or pagina == 3) and total <= 3) :
                selecionada = ""
                destino = 2
            elif (pagina == 2 and total <= 3):
                selecionada = "active"
                destino = 2
            elif pagina > 1 and pagina != total:
                selecionada = "active"
                destino = pagina
            elif pagina == total:
                destino = pagina - 1
            else:
                destino = pagina

    pagina_2 = [destino, visivel, ativada, selecionada, destino]    

    #Pagina 3 ou proxima + 1
    visivel = "N"
    ativada = "disabled"
    selecionada = ""
    destino = 0

    if pagina <= total:
        if total >= 3:
            visivel = "S"
            ativada = ""
            if pagina == 1:
                destino = 3
            elif pagina == total:
                selecionada = "active"
                destino = pagina
            else:
                destino = pagina + 1

    pagina_3 = [destino, visivel, ativada, selecionada, destino]    

    #Proxima Pagina
    visivel = "N"
    ativada = "disabled"
    selecionada = ""
    destino = 0

    if pagina <= total:
        if total > 3:
            visivel = "S"
            if pagina + 1 <= total:
                ativada = ""
                destino = pagina + 1

    proxima = ["Próxima", visivel, ativada, selecionada, destino]
    
    #Ultima Pagina
    visivel = "N"
    ativada = "disabled"
    selecionada = ""
    destino = 0

    if pagina <= total:
        if total > 3:
            visivel = "S"
            if pagina < total:
                ativada = ""
                destino = total

    ultima = ["Última", visivel, ativada, selecionada, destino]
    
    return {"primeira":primeira, 
            "anterior":anterior, 
            "pagina_1":pagina_1,
            "pagina_2":pagina_2,
            "pagina_3":pagina_3,
            "proximo ":proxima,
            "ultimo  ":ultima}
           