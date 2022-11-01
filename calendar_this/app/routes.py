from flask import Blueprint, render_template
import os

bp = Blueprint('main', __name__, '/')
DB_FILE = os.environ.get("DB_FILE")

@bp.route("/")
def main():

  with sqlite3.connect(DB_FILE) as conn:
        curs = conn.cursor()
        curs.execute(
            """
            SELECT id, name, start_datetime, end_datetime
            FROM appointments
            ORDER BY start_datetime
            """
        )
  return render_template('main.html')


#ran this code in sqlite3 CLI to create table

# CREATE TABLE appointments (
#   id INTEGER PRIMARY KEY,
#   name VARCHAR(200) NOT NULL,
#   start_datetime TIMESTAMP NOT NULL,
#   end_datetime TIMESTAMP NOT NULL,
#   description TEXT,
#   private BOOLEAN NOT NULL
# );

# INSERT INTO appointments (name, start_datetime, end_datetime, description, private)
# VALUES
# ('My appointment', '«DATE» 14:00:00', '«DATE» 15:00:00',
#  'An appointment for me', false);
