new_notes = []
new_times = []
current_note = [0, 0, 0, 0]
current_time = "3820"

with open("D:\\program project\\python_project\\Games\\mayo_music_game\\1214 cs class\\osu.txt", "r") as osu:
    for i in osu:
        if i[0] == "6":
            line_time = i[7] + i[8] + i[9] + i[10]
            if line_time != current_time:
                new_times.append(current_time)
                note = ""
                for j in current_note:
                    note += str(current_note[j])
                new_notes.append(note)
                current_note = [0, 0, 0, 0]
                current_time = ""
                note = ""
            current_time = i[7] + i[8] + i[9] + i[10]
            current_note[0] = 1
                
        if i[0] == "1":
            line_time = i[8] + i[9] + i[10] + i[11]
            if line_time != current_time:
                new_times.append(current_time)
                note = ""
                for j in current_note:
                    note += str(current_note[j])
                new_notes.append(note)
                current_note = [0, 0, 0, 0]
                current_time = ""
                note = ""
            current_time = i[8] + i[9] + i[10] + i[11]
            current_note[0] = 1
            current_note[1] = 1
        if i[0] == "3":
            line_time = i[8] + i[9] + i[10] + i[11]
            if line_time != current_time:
                new_times.append(current_time)
                note = ""
                for j in current_note:
                    note += str(current_note[j])
                new_notes.append(note)
                current_note = [0, 0, 0, 0]
                current_time = ""
                note = ""
            current_time = i[8] + i[9] + i[10] + i[11]
            current_note[0] = 1
            current_note[2] = 1
        if i[0] == "4":
            line_time = i[8] + i[9] + i[10] + i[11]
            if line_time != current_time:
                new_times.append(current_time)
                note = ""
                for j in current_note:
                    note += str(current_note[j])
                new_notes.append(note)
                current_note = [0, 0, 0, 0]
                current_time = ""
                note = ""
            current_time = i[8] + i[9] + i[10] + i[11]
            current_note[0] = 1
            current_note[3] = 1
        
        new_note = ""
        
        
print(new_notes)
print(new_times)