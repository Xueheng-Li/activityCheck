from flask import Flask, render_template, request, redirect, url_for, send_file
import csv_utils
from datetime import datetime
import os


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('clean_table'):
            return render_template('index.html', activity_list=csv_utils.read_activity_list_from_csv())
        elif request.form.get('delete_uuid'):
            csv_utils.delete_activity_by_uuid(request.form.get('delete_uuid'))
            return redirect(url_for('index'))
        else:
            activity = request.form.get('activity')
            csv_utils.write_activity_to_csv(activity)
            return redirect(url_for('index'))
    activities = csv_utils.read_activities_from_csv()
    activity_list = csv_utils.read_activity_list_from_csv()
    return render_template('index.html', activities=activities, activity_list=activity_list)


@app.route('/add', methods=['POST'])
def add():
    activity = request.form.get('new_activity')
    csv_utils.add_new_activity(activity)
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
    activity = request.form.get('activity_to_delete')
    csv_utils.delete_activity_from_list(activity)
    return redirect(url_for('index'))

@app.route('/activity/<activity>', methods=['GET'])
def record_activity(activity):
    csv_utils.write_activity_to_csv(activity)
    return redirect(url_for('index'))

@app.route('/download', methods=['GET'])
def download():
    return send_file('data/activities.csv', as_attachment=True)

@app.route('/insert', methods=['POST'])
def insert():
    activity = request.form.get('insert_activity')
    timestamp = request.form.get('insert_timestamp')
    csv_utils.insert_activity_to_csv(activity, timestamp)
    return redirect(url_for('index'))

if __name__ == '__main__':
    if not os.path.exists('data'):
        os.makedirs('data')
    app.run(debug=True, host='0.0.0.0', port=9093)
