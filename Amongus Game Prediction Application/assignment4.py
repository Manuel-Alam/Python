player_colours = ["red", "blue", "green", "yellow", "brown", "pink", "orange"]


def load_map(file_path):
    rooms = {}

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip().replace(":", ",").split(",")

            room_name = line.pop(0)

            rooms[room_name] = [x.strip() for x in line]

        return rooms


def simplify_testimony(chat, rooms):
    message = ""

    edited_chat = chat.strip().replace(":", "").replace("!","").replace(",", "").replace(".", "").replace("?", "").split()

    current_speaker = edited_chat.pop(0)

    rooms_list = list(rooms.keys())
    room_in_chat = any(element for element in rooms_list if(element in chat))
    colour_in_chat = any(element in edited_chat for element in player_colours)


    if ("voted" in edited_chat):
        message = chat.strip()

    elif (room_in_chat == False):

        message = ""

    if (room_in_chat == True and colour_in_chat == False):
        current_location = [element for element in rooms_list if (element in chat)][0]

        message = "{}: {} in {}".format(current_speaker, current_speaker, current_location)

    if (room_in_chat == True and colour_in_chat == True):
        other_player = [x for x in edited_chat if x in player_colours][0]
        other_player_location = [element for element in rooms_list if (element in chat)][0]

        message = "{}: {} in {}".format(current_speaker, other_player, other_player_location)

    return (message)


def load_chat_log(filename, rooms):
    messages = []

    with open(filename, "r") as f:
        for line in f:
            messages.append(simplify_testimony(line, rooms))

        messages = list(filter(None, messages))

        return messages


def tally_votes(chat_log):
    player_votes = {}

    for i in player_colours:
        player_votes[i] = 0

    player_votes["skip"] = 0

    for i in chat_log:

        i = i.split()

        if (i[1] == "voted" and i[2] != "skip"):
            player_votes[i[2]] += 1

        if (i[1] == "voted" and i[2] == "skip"):
            player_votes["skip"] += 1

    return player_votes


def get_paths(chat_log):
    player_paths = {}

    for i in player_colours:
        player_paths[i] = []

    for j in chat_log:

        j = j.replace(":", "").split()

        if(j[0] == j[1] and len(j) < 5):
            player_paths[j[0]].append(j[3])

        elif(j[0] == j[1] and len(j) == 5):
            player_paths[j[0]].append(j[3]+" "+j[4])

    return player_paths


def get_sus_paths(path_dict, rooms):
    players_lying = []

    for i in path_dict:

        for j in range(len(path_dict[i])):

            if (j < len(path_dict[i]) - 1):

                current_room = path_dict[i][j]
                next_room = path_dict[i][j + 1]

                if (next_room not in rooms[current_room]):
                    players_lying.append(i)

    return set(players_lying)


def main():
    #print(load_map("skeld.txt"))
    #print(load_chat_log("chatlog.txt", load_map("skeld.txt")))
    #print(tally_votes(load_chat_log("chatlog.txt", load_map("skeld.txt"))))
    #print(get_paths(load_chat_log("chatlog.txt", load_map("skeld.txt"))))
    print(get_sus_paths(get_paths(load_chat_log("chatlog.txt", load_map("skeld.txt"))), load_map("skeld.txt")))


if __name__ == "__main__":
    main()
