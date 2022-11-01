import sqlite3
from flask import Blueprint, render_template
import os
from datetime import datetime

from .forms import NewAppointmentForm

bp = Blueprint('main', __name__, '/')
DB_FILE = os.environ.get("DB_FILE")

@bp.route("/")
def main():
  form = NewAppointmentForm()
  with sqlite3.connect(DB_FILE) as conn:
        curs = conn.cursor()
        curs.execute(
            """
            SELECT id, name, start_datetime, end_datetime
            FROM appointments
            ORDER BY start_datetime
            """
        )
        rows = curs.fetchall()
        new_rows = []
        for row in rows:
          datetime_start_obj =  datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
          formatted_start_date = datetime_start_obj.strftime("%H:%M")

          datetime_end_obj =  datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
          formatted_end_date = datetime_end_obj.strftime("%H:%M")

          new_tuple = row[0],row[1], formatted_start_date, formatted_end_date
          new_rows.append(new_tuple)
  return render_template('main.html', rows=new_rows, form = form)


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
