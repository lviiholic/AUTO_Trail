import sqlite3

def generate_template(template, data):
    filled_template = template.format(**data)
    return filled_template


def get_data_from_database(trail_id):
    conn = sqlite3.connect('hiking.db')
    cursor = conn.cursor()

    # 执行 SQL
    cursor.execute("""
    SELECT t.trail_name, p.park_name, t.region, t.difficulty, t.length, t.time, t.star
    FROM Trail t
    JOIN Park p ON t.park_id = p.park_id
    WHERE t.trail_id = ?
""", (trail_id,))
    row = cursor.fetchone()

    # 将查询结果转换为字典形式
    data = {
        'trail_name': row[0],
        'park_name': row[1],
        'region': row[2],
        'difficulty': row[3],
        'length': row[4],
        'time': row[5],
        'star': row[6]
    }

    conn.close()

    return data


# 与用户交互获取要查询的路线ID
trail_id = input("请输入要查询的路线ID: ")

# 从数据库获取数据
data = get_data_from_database(trail_id)

# 定义模板
template = "The {trail_name} is located in the {park_name} country park in the {region}, the difficulty level of the hiking route is {difficulty}, the total length is {length}km, the estimated time to complete the hike is {time} hours, and the overall rating of the hiking experience is {star} star(s)."

# 生成填充后的模板
filled_template = generate_template(template, data)
print(filled_template)