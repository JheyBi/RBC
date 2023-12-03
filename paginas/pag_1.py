import json
import PySimpleGUI as sg

def pag_1():
    area_damaged = ["areas baixas", "espalhado", "campo inteiro", "areas superiores", "Desconhecido"]

    canker_lesion = ["Bronzeado a marrom", "marrom", "marrom escuro", "Desconhecido"]

    crop_hist = ["dif-1 ano", "mesmo-1 ano", "mesmo-2 ano", "mesmo-7 ano", "Desconhecido"]

    date = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro",
            "Dezembro", "Desconhecido"]

    external_decay = ["Ausente", "Firme-seco", "Desconhecido"]

    Fruit_spots = ["Ausente", "Colore", "Escuro", "Desconhecido"]

    fruiting_bodies = ["Ausente", "Presente", "Desconhecido"]

    fruit_pods = ["Normais", "Pouco presente", "Doente", "Desconhecido"]

    germination = ["90-100%", "80-89%", "lt-80%", "Desconhecido"]

    hail = ["Sim", "Não", "Desconhecido"]

    int_discolor = ["Nenhuma", "Marrom", "Preto", "Desconhecido"]

    leaf_malf = ["Ausente", "Presente", "Desconhecido"]

    leaf_mild = ["Ausente", "Superficial", "Abundante", "Desconhecido"]

    leaf_shread = ["Ausente", "Presente", "Desconhecido"]

    leafspots_halo = ["Ausente", "Sem Aereolado", "Com Aereolado", "Desconhecido"]

    leafspot_size = ["lt-1/8", "gt-1/8", "Desconhecido"]

    leafspot_marg = ["Sem Marg", "Com marg", "Desconhecido"]

    leaves = ["Normais", "Anormais", "Desconhecido"]

    lodging = ["Sim", "Não", "Desconhecido"]

    mold_growth = ["Ausente", "Presente", "Desconhecido"]

    mycelium = ["Ausente", "Presente", "Desconhecido"]

    plant_growth = ["Normais", "Anormais", "Desconhecido"]

    plant_stand = ["Normal", "lt-normal", "Desconhecido"]

    precip = ["gt-normais", "lt-normais", "normais", "Desconhecido"]

    roots = ["Normal", "Podre", "Cortadas-off", "Desconhecido"]

    sclerotia = ["Ausente", "Presente", "Desconhecido"]

    seed = ["Normais", "Abnormais", "Desconhecido"]

    seed_discolor = ["Ausente", "Presente", "Desconhecido"]

    seed_size = ["Normais", "lt-normais", "Desconhecido"]

    seed_tmt = ["Nenhum", "Fungicida", "Outro", "Desconhecido"]

    severity = ["Leve", "Serio", "Muito serio", "Desconhecido"]

    shriveling = ["Ausente", "Presente", "Desconhecido"]

    stem = ["Normais", "Anormais", "Desconhecido"]

    stem_cankers = ["Ausente", "Coberto", "Descoberto", "Acima do segundo", "Desconhecido"]

    temp = ["lt-normais", "normais", "gt-normais", "Desconhecido"]

    sz1 = (25, 1)
    sz2 = (15, 0)

    col1 = [
        [sg.Text('Área danificada', size=sz1,background_color='light grey'), sg.Combo(area_damaged, key='area_damaged', size=sz2)],
        [sg.Text('Lesão de cancro', size=sz1,background_color='light grey'), sg.Combo(canker_lesion, key='canker_lesion', size=sz2)],
        [sg.Text('Histórico da cultura', size=sz1,background_color='light grey'), sg.Combo(crop_hist, key='crop_hist', size=sz2)],
        [sg.Text('Data', size=sz1,background_color='light grey'), sg.Combo(date, key='date', size=sz2)],
        [sg.Text('Decaimento externo', size=sz1,background_color='light grey'), sg.Combo(external_decay, key='external_decay', size=sz2)],
        [sg.Text('Descoloração interna', size=sz1,background_color='light grey'), sg.Combo(int_discolor, key='int_discolor', size=sz2)],
        [sg.Text('Malformação de folhas', size=sz1,background_color='light grey'), sg.Combo(leaf_malf, key='leaf_malf', size=sz2)],
        [sg.Text('Manchas foliares',size=sz1,background_color='light grey'), sg.Combo(leaf_mild, key='leaf_mild',size=sz2)],
        [sg.Text('Rasgo de folhas',size=sz1,background_color='light grey'), sg.Combo(leaf_shread, key='leaf_shread',size=sz2)],
        [sg.Text('Halo de manchas foliares',size=sz1,background_color='light grey'), sg.Combo(leafspots_halo, key='leafspots_halo',size=sz2)],
        [sg.Text('Micélio',size=sz1,background_color='light grey'), sg.Combo(mycelium, key='mycelium',size=sz2)],
        [sg.Text('Crescimento da planta',size=sz1,background_color='light grey'), sg.Combo(plant_growth, key='plant_growth',size=sz2)],
        [sg.Text('Precipitado',size=sz1,background_color='light grey'), sg.Combo(precip, key='precip',size=sz2)],
        [sg.Text('Raízes',size=sz1,background_color='light grey'), sg.Combo(roots, key='roots',size=sz2)],
        [sg.Text('Murchando', size=sz1,background_color='light grey'), sg.Combo(shriveling, key='shriveling', size=sz2)],
        [sg.Text('Caule', size=sz1,background_color='light grey'), sg.Combo(stem, key='stem', size=sz2)],
        [sg.Text('Temperatura', size=sz1,background_color='light grey'), sg.Combo(temp, key='temp', size=sz2)]
    ]

    col2 = [
        [sg.Text('Manchas de frutas', size=sz1,background_color='light grey'), sg.Combo(Fruit_spots, key='Fruit_spots', size=sz2)],
        [sg.Text('Corpos de frutificação', size=sz1,background_color='light grey'), sg.Combo(fruiting_bodies, key='fruiting_bodies', size=sz2)],
        [sg.Text('Vagens de frutas', size=sz1,background_color='light grey'), sg.Combo(fruit_pods, key='fruit_pods', size=sz2)],
        [sg.Text('Germinação', size=sz1,background_color='light grey'), sg.Combo(germination, key='germination', size=sz2)],
        [sg.Text('Granizo', size=sz1,background_color='light grey'), sg.Combo(hail, key='hail', size=sz2)],
        [sg.Text('Tamanho das manchas foliares', size=sz1,background_color='light grey'), sg.Combo(leafspot_size, key='leafspot_size', size=sz2)],
        [sg.Text('Margem das manchas foliares', size=sz1,background_color='light grey'), sg.Combo(leafspot_marg, key='leafspot_marg', size=sz2)],
        [sg.Text('Folhas', size=sz1,background_color='light grey'), sg.Combo(leaves, key='leaves', size=sz2)],
        [sg.Text('Lodging', size=sz1,background_color='light grey'), sg.Combo(lodging, key='lodging', size=sz2)],
        [sg.Text('Crescimento de mofo', size=sz1,background_color='light grey'), sg.Combo(mold_growth, key='mold_growth', size=sz2)],
        [sg.Text('Esclerócio', size=sz1,background_color='light grey'), sg.Combo(sclerotia, key='sclerotia', size=sz2)],
        [sg.Text('Semente', size=sz1,background_color='light grey'), sg.Combo(seed, key='seed', size=sz2)],
        [sg.Text('Descoloração da semente', size=sz1,background_color='light grey'), sg.Combo(seed_discolor, key='seed_discolor', size=sz2)],
        [sg.Text('Tamanho da semente', size=sz1,background_color='light grey'), sg.Combo(seed_size, key='seed_size', size=sz2)],
        [sg.Text('Seed Tmt', size=sz1,background_color='light grey'), sg.Combo(seed_tmt, key='seed_tmt', size=sz2)],
        [sg.Text('Severidade', size=sz1,background_color='light grey'), sg.Combo(severity, key='severity', size=sz2)],
        [sg.Text('Suporte para plantas', size=sz1,background_color='light grey'), sg.Combo(plant_stand, key='plant_stand', size=sz2)],
        [sg.Text('Cancro no caule', size=sz1,background_color='light grey'), sg.Combo(stem_cankers, key='stem_cankers', size=sz2)],
    ]


    next_button= [
        [sg.Button('Proximo')],
    ]

    layout = [
        [sg.Text('Caso Problema:'), sg.Text()],
        [sg.Column(col1), sg.Column(col2)], [sg.Text('CNF  Minima:')],
        [sg.Output()],
        [sg.Column(next_button, element_justification='right', expand_x=True)],
    ]

    window = sg.Window('Cadastro de Produtos', layout)

    novo_caso = {}

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            break

        elif event == 'Proximo':
            novo_caso = values.copy()
            break

    window.close()


    # Colocando todos os valores nulos como "Desconhecido"
    for key in novo_caso:
        if novo_caso[key] == '':
            novo_caso[key] = "Desconhecido"

    with open('similiriadade.json', 'r') as f:
        similaridade = json.load(f)

    for key in novo_caso:
        novo_caso[key] = similaridade[key][novo_caso[key]]

    with open('novo_caso.json', 'w') as f:
        json.dump(novo_caso, f)