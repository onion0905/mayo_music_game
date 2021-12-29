times = []
with open("D:\\program project\\python_project\\Games\\mayo_music_game\\times.txt", "r") as f_time:
    for i in f_time:
        times.append(int(i) + 400)
with open("D:\\program project\\python_project\\Games\\mayo_music_game\\times.txt", "w") as f_time:
    for i in times:
        f_time.write(str(i))
        f_time.write("\n")