import csv
import time


def read_request():
    line = ""
    with open("run_service.txt", 'r+') as file:
        line = file.readline()
        file.truncate(0) #clear clear run_services.txt
    return line

def get_food():
    food_item = ""
    with open("food_info.txt", 'r+') as food_file: #send variable log into this file as a string seperated by commas
        food_item = food_file.readline()
        food_file.truncate(0)
    return food_item


def write_csv(format_data):
    with open("food_log.csv", 'a', newline='') as csv_file:
        csv_write = csv.writer(csv_file)
        csv_write.writerow(format_data)


def log_food():
    food_item = get_food()
    print(f"Read line: {food_item.strip()}")
    data = food_item.split(',')
    #format to send data [name, servings, calories, water, ....]
    format_data = [data[0], data[1]] + [round(float(value), 2) for value in data[2:]]
    write_csv(format_data)


def write_total(data):
    with open('total.txt', 'w') as outfile:
        outfile.write(f"\ncalories: {round(data[0],2)}\n"
                f"water (g): {round(data[1],2)}\n"
                f"protein (g): {round(data[2],2)}\n"
                f"carbs (g): {round(data[3],2)}\n"
                f"sugar (g): {round(data[4],2)}\n"
                f"fiber (g): {round(data[5],2)}\n"
                f"fat (g): {round(data[6],2)}\n")
            

def get_total():
    data = [0]*7

    print("Calculating total nutritional values")
    with open("food_log.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            data[0] += float(row['calories'])
            data[1] += float(row['water_g'])
            data[2] += float(row['protein_g'])
            data[3] += float(row['carbs_g'])
            data[4] += float(row['sugar_g'])
            data[5] += float(row['fiber_g'])
            data[6] += float(row['fat_g'])

    write_total(data)


while True:
    time.sleep(3)
    line = read_request()
    if line == "log":
        log_food() #store food

    # retrieve total calories, water, protein, carbs, sugar, fiber and fat
    elif line == "get_total":
        get_total()

    else:
        time.sleep(1)


