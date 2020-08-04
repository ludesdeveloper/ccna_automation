import os
import sqlite3
from flask import Flask, render_template, request, redirect, jsonify
from flask_cors import CORS
#configuration
app = Flask(__name__)
CORS(app)
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_db = os.path.join(THIS_FOLDER, 'automation.db')
#additional function
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
#route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/part_1')
def part_1():
    return render_template('part_1.html')

@app.route('/part_2')
def part_2():
    return render_template('part_2.html')

@app.route('/part_3')
def part_3():
    return render_template('part_3.html')

@app.route('/part_4')
def part_4():
    return render_template('part_4.html')

@app.route('/part_5')
def part_5():
    return render_template('part_5.html')

@app.route('/part_6')
def part_6():
    return render_template('part_6.html')

@app.route('/view_crud')
def view_crud():
    #create view db
    con = sqlite3.connect(my_db)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from automation")
    records = cur.fetchall()
    return render_template('view_crud.html', records=records)

@app.route('/add_crud')
def add_crud():
    return render_template('add_crud.html')

@app.route('/add_crud', methods=['POST'])
def add_expense():
    #get value from front
    katakata = request.form['katakata']
    #insert database
    db = sqlite3.connect(my_db)
    cursor = db.cursor()
    cursor.execute('''INSERT INTO automation(katakata)
                        VALUES(?)''', (katakata,))
    db.commit()
    db.close()
    return redirect('/view_crud')

@app.route('/update_crud_page', methods=['POST'])
def update_crud_page():
    #get value from front
    id = request.form['id']
    katakata = request.form['katakata']
    return render_template('update_crud.html', id=id, katakata=katakata)

@app.route('/update_crud', methods=['POST'])
def update_crud():
    #get value from front
    id = request.form['id']
    katakata = request.form['katakata']
    print(id)
    print(katakata)
    #update database
    db = sqlite3.connect(my_db)
    cursor = db.cursor()
    sql_update_query = """Update automation set katakata = ? where id = ?"""
    columnValues = (katakata, id)
    cursor.execute(sql_update_query, columnValues)
    db.commit()
    db.close()
    return redirect('/view_crud')

@app.route('/delete_crud/<int:id>', methods=['POST','GET'])
def delete_crud(id):
    #delete database
    db = sqlite3.connect(my_db)
    sql = 'DELETE FROM automation WHERE id=?'
    cur = db.cursor()
    cur.execute(sql, (id,))
    db.commit()
    db.close()
    return redirect('/view_crud')

@app.route('/api_instruction', methods=['GET'])
def api_instruction():
    return render_template('api_instruction.html')

@app.route('/api', methods=['GET','POST'])
def api():
    query_parameters = request.args

    id = query_parameters.get('id')

    query = "SELECT * FROM automation WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if not id:
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect(my_db)
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__":
    app.run(debug=True)