import sqlite3

def create_connection (db = "Metrics.db") :

    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row

    return conn


def create_table(conn) :
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS metrics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        time INTEGER NOT NULL,
        cpu REAL NOT NULL,
        ram REAL NOT NULL,
        disk_total INTEGER NOT NULL,
        disk_used INTEGER NOT NULL,
        disk_free INTEGER NOT NULL,
        disk_percent REAL NOT NULL,
        net_up INTEGER NOT NULL,
        net_down INTEGER NOT NULL,
        up_speed REAL NOT NULL,
        down_speed REAL NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )""")

    conn.commit()


def insert_table(conn, metrics) :
    cursor = conn.cursor()

    for metric in metrics :
        cursor.execute("""INSERT INTO metrics (time, cpu, ram,
                        disk_total, disk_used, disk_free, disk_percent,
                        net_up, net_down, up_speed, down_speed) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                        (metric.time, metric.cpu, metric.ram, 
                         metric.disk[0], metric.disk[1], metric.disk[2], metric.disk[3],
                         metric.net_up, metric.net_down, metric.up_speed, metric.down_speed)
                         
                         
        )

    conn.commit()







