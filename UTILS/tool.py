import re
from datetime import datetime

def get_results (rows) :
    for row in rows :
            id = row["id"]
            time = row["time"]
            cpu = row["cpu"]
            ram = row["ram"]
            disk_total = row["disk_total"]
            disk_used = row["disk_used"]
            disk_free = row["disk_free"]
            disk_percent = row["disk_percent"]
            net_up = row["net_up"]
            net_down = row["net_down"]
            up_speed = row["up_speed"]
            down_speed = row["down_speed"]
            created_at = row["created_at"]

            print(f"ID: {id} | Time: {time} | CPU: {cpu}% | RAM: {ram}% | "
                  f"Disk total: {disk_total} | Disk used: {disk_used} | Disk free: {disk_free} | "
                  f"Disk percentage: {disk_percent}% | Network up: {net_up} | Network down: {net_down} | "
                  f"Up speed: {up_speed} | Down speed: {down_speed} | Created at: {created_at}")
        




def get_last_metrics(conn) :
    cursor = conn.cursor()

    while True :
        user = input("Enter the number of metrics to retrieve from last run or 'exit' to  quit : ").strip()

        if user.lower() == "exit" :
            print("Quitting ...")
            break

        elif not user.isdigit() :
            print("Invalid input. Please enter a number or 'exit' to quit.")
            continue

        user = int(user)

        cursor.execute("""SELECT * FROM metrics ORDER BY id DESC LIMIT ?""", (user,))

        rows = cursor.fetchall()

        if not rows :
            print("No metrics found.")
            continue

        get_results(rows)


def get_metrics_date_range(conn) :
    cursor = conn.cursor()

    while True :
        user_1 = input("Enter the first date in the format (YYYY-MM-DD) or 'exit' to  quit : ").strip()

        if user_1.lower() == "exit" :
            print("Quitting ...")
            break

        elif not re.match(r"\d{4}-\d{2}-\d{2}", user_1) :
            print("Invalid input. Please enter a date in the format (YYYY-MM-DD) or 'exit' to quit.")
            continue

        user_2 = input("Enter the second date in the format (YYYY-MM-DD) : ").strip()

    
        if not re.match(r"\d{4}-\d{2}-\d{2}", user_2) :
            print("Invalid input. Please enter a date in the format (YYYY-MM-DD) .")
            continue


        cursor.execute("""SELECT * FROM metrics WHERE date(time, 'unixepoch') BETWEEN ? AND ? ORDER BY id ASC""", (user_1, user_2))

        rows = cursor.fetchall()

        if not rows :
            print("No metrics found.")
            continue

        get_results(rows)

    



        