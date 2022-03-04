def read_motion(location_name):
    rooms_list = []

    filename = location_name + ".motion.txt"

    with open(filename, "r") as f:

        for line in f:

            line = line.strip().split(",")

            if (line[2] == "detected"):
                rooms_list.append(line[0])

    return list(set(rooms_list))


def read_emf(location_name):

    rooms_list = []

    filename = location_name + ".emf.txt"

    with open(filename, "r") as f:

        number_lines = f.read().splitlines()

        for i in range(len(number_lines)):

            line = number_lines[i]

            if(line.isdigit()):
                current_number += 1
                current_sum += int(line)
                #print(str(current_number))

                if(i < len(number_lines)-1):
                    next_line = number_lines[i+1]

                    if(next_line.isdigit() is False):

                        current_average = current_sum / current_number
                        #print(str(current_average))

                        if (current_average > 3):
                            rooms_list.append(current_room)

                if(i == len(number_lines)-1):
                    current_average = current_sum / current_number
                    #print(str(current_average))

                    if (current_average > 3):
                        rooms_list.append(current_room)

            if (line.isdigit() is False):
                current_room = line
                current_number = 0
                current_sum = 0
                current_average = 0
                #print(current_room)

    return list(set(rooms_list))


def is_valid_temp(val):

    val = val.strip("-").split(".")

    if(val[0].isdigit()):

        val = val[0]

        return True

    else:

        return False


def read_temp(location_name):

    rooms_list = []

    filename = location_name + ".temp.txt"

    with open(filename, "r") as f:

        number_lines = f.read().splitlines()

        for i in range(len(number_lines)):

            line = number_lines[i]

            check_line = is_valid_temp(line)

            if(check_line is True):

                #print(line)

                if(i < len(number_lines)-1):

                    previous_line = number_lines[i - 1]
                    next_line = number_lines[i + 1]

                    if(line[0] == "-" and next_line[0] == "-" or line[0] == "-" and previous_line[0] == "-"):
                        current_negative_number += 1

                    if (is_valid_temp(next_line) is False):

                        #print("Consecutive negative numbers: " + str(current_negative_number))

                        if (current_negative_number >= 5):
                            rooms_list.append(current_room)

                if (i == len(number_lines) - 1):

                    #print("Consecutive negative numbers: " + str(current_negative_number))

                    if (current_negative_number >= 5):
                        rooms_list.append(current_room)

            if(check_line is False):

                current_room = line
                current_negative_number = 0
                #print(current_room)

    return list(set(rooms_list))


def generate_report(location, motion, emf, temp):

    filename = "ghost_report."+location+".txt"

    with open(filename, "w") as f:

        #print(motion)
        #print(emf)
        #print(temp)
        list_MET = [] #motion, emf, temp
        list_ME = [] #motion, emf
        list_MT = [] #motion, temp
        list_ET = [] #emf, temp

        for room in motion:
            if(room in emf and room in temp):
                if(room not in list_MET):
                    list_MET.append(room)

            if(room in emf):
                if(room not in list_ME):
                    list_ME.append(room)

            if(room in temp):
                if(room not in list_MT):
                    list_MT.append(room)

        for room in emf:
            if(room in temp):
                if(room not in list_ET):
                    list_ET.append(room)

        f.write("== Raven Ghost Hunting Society Haunting Report == \nLocation: house")

        if(len(list_MET) > 0):
            for i in range(len(list_MET)):
                f.write("\nPoltergeist in "+list_MET[i])

        if(len(list_ME) > 0):
            for j in range(len(list_ME)):
                f.write("\nOni in " + list_ME[j])

        if(len(list_MT) > 0):
            for k in range(len(list_MT)):
                f.write("\nBanshee in " + list_MT[k])

        if(len(list_ET) > 0):
            for l in range(len(list_ET)):
                f.write("\nPhantom in " + list_ET[l])

def main():
    #print(read_motion("house"))
    #print(read_emf("house"))
    #print(read_temp("house"))
    generate_report("house", read_motion("house"), read_emf("house"), read_temp("house"))


if __name__ == "__main__":
    main()



