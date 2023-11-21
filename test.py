import sqlite3
from sqlite3 import Error

def generate_template(template, data):
    filled_template = template.format(**data)
    return filled_template


def get_data_from_database(trail_id):
    try:
        conn = sqlite3.connect('data/hiking.db')
    except Error as e:
        print(e)
    
    cursor = conn.cursor()

    # 执行 SQL
    cursor.execute("""
    SELECT t.trail_name, p.park_name, t.region, t.difficulty, t.length, t.time, t.star
    FROM Trail t
    JOIN Park p ON t.park_id = p.park_id
    WHERE t.trail_id = ?
""", (trail_id,))
    row = cursor.fetchone()
    print(row)
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


'''SELECT t.trail_name, p.park_name, t.length, t.time
FROM Trail AS t
JOIN Park AS p ON t.park_id = p.park_id,
WHERE t.trail_name = 'Chi Ma Wan Country Trail'
'''

'''SELECT
  SUM(CASE WHEN trail_name LIKE '%MacLehose Trail%' THEN length END) AS sum_of_length1,
  SUM(CASE WHEN trail_name LIKE '%Wilson Trail%' THEN length END) AS sum_of_length2,
  SUM(CASE WHEN trail_name LIKE '%Lantau Trail%' THEN length END) AS sum_of_length3,
  SUM(CASE WHEN trail_name LIKE '%Hong Kong Trail%' THEN length END) AS sum_of_length4
FROM
  Trail
WHERE
  trail_name LIKE '%MacLehose Trail%'
  OR trail_name LIKE '%Wilson Trail%'
  OR trail_name LIKE '%Lantau Trail%'
  OR trail_name LIKE '%Hong Kong Trail%'
'''
'''
SELECT park_name, area
FROM Park
WHERE area = (SELECT MAX(area) FROM Park)
UNION ALL
SELECT park_name, area
FROM Park
WHERE area = (SELECT MIN(area) FROM Park)
'''

'''
SELECT
  p.park_name AS park_name1,
  COUNT(t.trail_id) AS number_of_trail1
FROM
  Park AS p
JOIN
  Trail AS t
ON
  t.park_id = p.park_id
GROUP BY
  p.park_name
ORDER BY
  number_of_trail1 DESC
LIMIT 2;
'''