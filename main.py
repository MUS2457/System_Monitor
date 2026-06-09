from CORE import display, history, storage
from ANALYSIS import metrics_analysis, graph
from DATA import database
from UTILS import tool

def pretty_print(title, data):
    print(f"\n--- {title} ---")

    if isinstance(data, list):
        if not data:
            print("No results found.")
        else:
            for item in data:
                print(item)
    else:
        print(data)

    print("-" * 30)



def database_tools(conn) :

    while True :
        print("1. Get lasts Metrics ")
        print("2. Get Metrics date range")
        print("3. Return to main menu")

        user = input("Enter a number based on menu ").strip()

        if not user.isdigit() or int(user) not in [1, 2, 3] :
            print("incorrect choice, enter a valid number ")
            continue


        elif int(user) == 1 :
            tool.get_last_metrics(conn)
        
        elif int(user) == 2 :
            tool.get_metrics_date_range(conn)

        elif int(user) == 3 :
            print("Returning...")
            return
        

def metrics_menu(Metrics):
    
    analysis = metrics_analysis.MetricsAnalysis(Metrics)

    while True:
        print("\n=== METRICS ANALYZER MENU ===")
        print("1. CPU above threshold")
        print("2. RAM above threshold")
        print("3. Disk above threshold")
        print("4. Average CPU usage")
        print("5. Average RAM usage")
        print("6. Max CPU usage")
        print("7. Max RAM usage")
        print("8. Min CPU usage")
        print("9. Min RAM usage")
        print("10. CPU trend")
        print("11. RAM trend")
        print("12. Disk trend")
        print("13. CPU volatility")
        print("14. RAM volatility")
        print("15. Disk volatility")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            pretty_print("CPU Above Threshold", analysis.cpu_above_threshold())
        elif choice == "2":
            pretty_print("RAM Above Threshold", analysis.ram_above_threshold())
        elif choice == "3":
            pretty_print("Disk Above Threshold", analysis.disk_above_threshold())
        elif choice == "4":
            pretty_print("Average CPU Usage", analysis.average_cpu_usage())
        elif choice == "5":
            pretty_print("Average RAM Usage", analysis.average_ram_usage())
        elif choice == "6":
            pretty_print("Max CPU Usage", analysis.max_cpu_usage())
        elif choice == "7":
            pretty_print("Max RAM Usage", analysis.max_ram_usage())
        elif choice == "8":
            pretty_print("Min CPU Usage", analysis.min_cpu_usage())
        elif choice == "9":
            pretty_print("Min RAM Usage", analysis.min_ram_usage())
        elif choice == "10":
            pretty_print("CPU Trend", analysis.trend_detection_cpu())
        elif choice == "11":
            pretty_print("RAM Trend", analysis.trend_detection_ram())
        elif choice == "12":
            pretty_print("Disk Trend", analysis.trend_detection_disk())
        elif choice == "13":
            pretty_print("CPU Volatility", analysis.volatility_cpu())
        elif choice == "14":
            pretty_print("RAM Volatility", analysis.volatility_ram())
        elif choice == "15":
            pretty_print("Disk Volatility", analysis.volatility_disk())
        elif choice == "0":
            print("Exiting menu...")
            break
        else:
            print("Invalid choice. Try again.")

def history_menu(collected) :
    
    while True :
        print("1. View history")
        print("2. Export history to file (log)")
        print("3. Read history from file (log)")
        print("4. Return to main menu")

        user = input("Enter a number based on menu ").strip()

        if not user.isdigit() or int(user) not in [1, 2, 3, 4] :
            print("incorrect choice, enter a valid number ")
            continue

        elif int(user) == 1 :
            history.view_history(collected)

        elif int(user) == 2 :
            history.export_history(collected)

        elif int(user) == 3 :
            history.read_history()

        elif int(user) == 4 :
            print("Returning...")
            return

def main() : 
    conn = database.create_connection()
    database.create_table(conn)
    Metrics = None
    

    while True :
        print("1. Display metrics in real time")
        print("2. View metrics as graph")
        print("3. Analysis")
        print("4. History utils")
        print("5. Database tools")
        print("0. Exit")

        user = input("Enter a number based on menu ").strip()

        if not user.isdigit() or int(user) not in [1, 2, 3, 4, 5, 0] :
            print("incorrect choice, enter a valid number ")
            continue

        elif int(user) == 1 :
            display.display_latest_metrics()
            Metrics = storage.metrics_buffer
            database.insert_table(conn,Metrics)
            

        elif int(user) == 2 :
            graph.show_graph()

        elif int(user) == 3 :
            if Metrics is None :
                print("No metrics found, run metrics displayer first.")
                continue
            metrics_menu(Metrics)

        elif int(user) == 4 :
            if not Metrics :
                print("No metrics found, run metrics displayer first.")
                continue

            history_menu(Metrics)

        elif int(user) == 5 :
    
            database_tools(conn)

        elif int(user) == 0 :
            print("Exiting ...")
            break


if __name__ == "__main__" :
    main()