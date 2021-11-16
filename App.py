import re
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
#Mysql connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'basededatos'
mysql = MySQL(app)

#Settings
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos')
    data = cur.fetchall()
    return render_template('index.html', productos = data)

@app.route('/add_products', methods=['POST'])
def add_products():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        medida = request.form['medida'] 
        precio = request.form['precio']
        fechaDeVencimiento = request.form['fechaDeVencimiento']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO productos(nombre, cantidad, medida, precio, fechaDeVencimiento) VALUES (%s, %s, %s, %s, %s)',
        (nombre, cantidad, medida, precio, fechaDeVencimiento))
        mysql.connection.commit()
        flash('Producto agregado satisfactoriamente')
        return redirect(url_for('index'))

@app.route('/edit/<id>')
def get_product(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos WHERE id=%s', (id))
    data = cur.fetchall()
    return render_template('edit_product.html', producto = data[0] )
    
@app.route('/update/<id>', methods=['POST'])
def update_product(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        medida = request.form['medida'] 
        precio = request.form['precio']
        fechaDeVencimiento = request.form['fechaDeVencimiento']
        cur = mysql.connection.cursor() #MySQLdb._exceptions.ProgrammingError 12*11
        cur.execute("""
            UPDATE productos
            SET nombre=%s,
                cantidad=%s, 
                medida=%s,
                precio=%s,
                fechaDeVencimiento=%s
            WHERE id=%s
            """, (nombre, cantidad, medida, precio, fechaDeVencimiento, id))
        mysql.connection.commit()
        flash('Producto editado exitosamente')
        return redirect(url_for('index'))




@app.route('/delete/<string:id>')
def delete_product(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM productos WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Producto borrado exitosamente')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=3000, debug=True)