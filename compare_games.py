import json
import io

with open('./boardgame_exchange/boardgameexchange.json') as boardgameexchange_file:

    boardgameexchange_json_data = json.load(boardgameexchange_file)
    boardgameexchange_games = []

    for game in boardgameexchange_json_data:
        boardgameexchange_games.append(game['title'].lower())

    with open('./spielbound/spielbound.json') as spielbound_file:

        spielbound_json_data = json.load(spielbound_file)
        spielbound_games = []

        for game in spielbound_json_data:
            spielbound_games.append(game['title'].lower())

        spielbound_only_games = set(spielbound_games).difference(set(boardgameexchange_games))
        boardgameexchange_only_games = set(boardgameexchange_games).difference(set(spielbound_games))
        shared_games = set(boardgameexchange_games).intersection(set(spielbound_games))

        with io.open("shared.txt", "w", encoding='utf8') as file:
            for game in shared_games:
                file.write(game + "\n")

        with io.open("speilbound_only.txt", "w", encoding='utf8') as file:
            for game in spielbound_only_games:
                file.write(game + "\n")

        with io.open("bgx_only.txt", "w", encoding='utf8') as file:
            for game in boardgameexchange_only_games:
                file.write(game + "\n")
