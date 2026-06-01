from CORE import display, history, storage
from ANALYSIS import metrics_analysis, graph
from DATA import database
from UTILS import tool

def main() :
    while True :
        print("1. Display metrics in real time")
        print("2. View metrics as graph")
        print("3. Analysis")
        print("4. History utils")
        print("5. Database tools")



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
        
if __name__ =="__main__" :
    conn = 2
    database_tools(conn)