from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "secret"),
        database=os.getenv("DB_NAME", "contador_final")
    )

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM log')
        logs = cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        return f"<h1>Error al conectar BD: {e}</h1>"

    html_rows = ""
    for entry in logs:
        html_rows += f"""
        <div style="text-align: center; margin-bottom: 20px;">
          <img src="/static/img/logo.jpg" alt="Logo" style="max-width: 200px;">
        </div>
        <tr>
            <td>{entry['id']}</td>
            <td>{entry['hora']}</td>
            <td>{entry['actividad']}</td>
            <td>{entry['estado']}</td>
            <td>{entry['imagen']}</td>
        </tr>
        """

    return f"""
    <table border="1">
        <thead>
            <tr>
                <th>id</th>
                <th>hora</th>
                <th>actividad</th>
                <th>estado</th>
                <th>imagen</th>
            </tr>
        </thead>
        <tbody>
            {html_rows}
        </tbody>
    </table>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)