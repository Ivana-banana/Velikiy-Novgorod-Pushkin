import sqlite3


def never_look_back(*dist, mode=""):
    con = sqlite3.connect("journeys.db")
    cur = con.cursor()
    ans = []
    z = f'select description from landmarks ' \
        f'LEFT JOIN landmarks ON district_id.landmarks = (select id from places where district in ({dist}))' \
        f'LEFT JOIN landmarks ON mode_id.landmarks = (select id from objects where mode = {mode})' \
        f'ORDER BY places.area, description.landmarks'
    result = cur.execute(z).fetchall()
    for elem in result:
        ans.append(elem[0])
    return ans


data = ['Vardanzi', 'Ark', 'Varakhsha', 'Ramtin', 'Shahrud Canal']
print(*never_look_back(*data, mode='buildings'), sep='\n')


