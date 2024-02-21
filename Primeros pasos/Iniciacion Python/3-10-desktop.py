import PySimpleGUI as sg

win_rows = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def players_names():
    sg.theme("DarkRed")
    layout = [[sg.Text("Nombre jugador numero uno")], [sg.InputText()],
              [sg.Text("Nombre jugador numero dos")], [sg.InputText()],
              [sg.Button("ok", key="-ok-")]]
    window = sg.Window("3 in row", layout)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == "-ok-":
            if values[0] != "" and values[1] != "":
                p_n_1, p_n_2 = values[0], values[1]
                window.close()
                return p_n_1, p_n_2


def game_table():
    sg.theme("Darkpurple6")
    deck = [0, 0, 0,
            0, 0, 0,
            0, 0, 0]

    layout = [
        [sg.Button("", key="-0-", size=(8, 4)),
         sg.Button("", key="-1-", size=(8, 4)),
         sg.Button("", key="-2-", size=(8, 4))],

        [sg.Button("", key="-3-", size=(8, 4)),
         sg.Button("", key="-4-", size=(8, 4)),
         sg.Button("", key="-5-", size=(8, 4))],

        [sg.Button("", key="-6-", size=(8, 4)),
         sg.Button("", key="-7-", size=(8, 4)),
         sg.Button("", key="-8-", size=(8, 4))],
        [sg.Button("exit", key="-ok-"), sg.Button("retry", key="-retry-")]
    ]
    return deck, layout


def main_bucle(layout, deck):
    PLAYER_ONE = "X"
    PLAYER_TWO = "O"

    name_1, name_2 = players_names()

    current_player = PLAYER_ONE

    window = sg.Window("3 in row", layout)
    end_game = False
    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED or event == "-ok-":
            break

        if window.Element(event).ButtonText == "" and not end_game:
            index = int(event.replace("-", ""))
            deck[index] = current_player
            window.Element(event).update(text=current_player)
            if 0 not in deck:
                sg.popup("Juego teminado, ha sido empate")
                end_game = True
            for win_row in win_rows:
                if deck[win_row[0]] == deck[win_row[1]] == deck[win_row[2]] != 0:
                    if deck[win_row[0]] == PLAYER_ONE:
                        sg.popup(f"{name_1} ha ganado")
                        end_game = True
                    else:
                        sg.popup(f"{name_2} ha ganado")
                        end_game = True

            if current_player == PLAYER_ONE:
                current_player = PLAYER_TWO
            else:
                current_player = PLAYER_ONE

        if event == "-retry-":
            window.close()
            return main()


def main():
    deck, layout = game_table()
    main_bucle(layout, deck)


if __name__ == "__main__":
    main()
