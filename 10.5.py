import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, "r", encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


if __name__ == "__main__":
    file_names = ["file 1.txt", "file 2.txt", "file 3.txt", "file 4.txt"]
    start1 = datetime.datetime.now()
    for file_name in file_names:
        read_info(file_name)
    end1 = datetime.datetime.now()
    print(f"Время линейноо вызова: {end1 - start1} ")

    start2 = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, file_names)
    end2 = datetime.datetime.now()
    print(f"Время мультипроцессорного вызова: {end2 - end1}")
