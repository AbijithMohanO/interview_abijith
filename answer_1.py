import datetime

def server_cost(d1, m1, y1, d2, m2, y2):
    create_dt = datetime.date(y1, m1, d1)
    delete_dt = datetime.date(y2, m2, d2)
    server_time = (delete_dt - create_dt).days

    if server_time == 0:
        cost = 20
    if server_time >= 1 and server_time < 31:
        cost = 30 * server_time
    if server_time >= 31 and server_time <= 365:
        cost = 1000 * (server_time// 30)
    if server_time > 365:
        cost = 20000
    return cost

if __name__ == '__main__':
    
    d1m1y1 = input().split()
    d1 = int(d1m1y1[0])
    m1 = int(d1m1y1[1])
    y1 = int(d1m1y1[2])

    d2m2y2 = input().split()
    d2 = int(d2m2y2[0])
    m2 = int(d2m2y2[1])
    y2 = int(d2m2y2[2])

    result = server_cost(d1, m1, y1, d2, m2, y2)
    print(str(result) + '\n')