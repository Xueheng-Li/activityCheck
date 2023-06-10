import csv
from datetime import datetime,  timedelta
import uuid



def write_activity_to_csv(activity):
    with open('data/activities.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([str(uuid.uuid4()), activity, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])



def read_activities_from_csv():
    try:
        with open('data/activities.csv', mode='r') as file:
            reader = csv.reader(file)
            all_activities = list(reader)

            # Check whether UUIDs are missing
            needs_update = any(len(row) < 3 for row in all_activities)
            if needs_update:
                all_activities = add_missing_uuids(all_activities)
                write_all_activities_to_csv(all_activities)

            recent_activities = [activity for activity in all_activities if
                                 datetime.strptime(activity[2], '%Y-%m-%d %H:%M:%S') > datetime.now() - timedelta(
                                     days=1)]

            # Sort the data by timestamp in descending order
            recent_activities.sort(key=lambda x: datetime.strptime(x[2], "%Y-%m-%d %H:%M:%S"), reverse=True)

            # Calculate time differences in hours:min format
            for i in range(len(recent_activities)-1):
                current_time = datetime.strptime(recent_activities[i][2], "%Y-%m-%d %H:%M:%S")
                previous_time = datetime.strptime(recent_activities[i+1][2], "%Y-%m-%d %H:%M:%S")
                time_difference = current_time - previous_time
                print(f"time_difference: {time_difference}")
                hours, remainder = divmod(time_difference.seconds, 3600)
                minutes = remainder // 60
                recent_activities[i].append(f"{hours}小时{minutes}分")
            recent_activities[-1].append(f"- -")
            
            # Calculate time difference from last activity to now
            if recent_activities:
                last_time = datetime.strptime(recent_activities[0][2], "%Y-%m-%d %H:%M:%S")
                time_difference = datetime.now() - last_time
                hours, remainder = divmod(time_difference.seconds, 3600)
                minutes = remainder // 60
                recent_activities[0].append(f"{hours}小时{minutes}分") # this is stored in recent_activities[0][4]

            return recent_activities
    except FileNotFoundError:
        return []



def add_missing_uuids(all_activities):
    for row in all_activities:
        if len(row) < 3:
            row.insert(0, str(uuid.uuid4()))
    return all_activities

def write_all_activities_to_csv(all_activities):
    with open('data/activities.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(all_activities)


def add_new_activity(activity):
    with open('data/activity_list.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([activity])


def read_activity_list_from_csv():
    try:
        with open('data/activity_list.csv', mode='r') as file:
            reader = csv.reader(file)
            return [row[0] for row in reader]
    except FileNotFoundError:
        return []




def delete_activity_from_list(activity):
    activities = read_activity_list_from_csv()
    activities.remove(activity)
    with open('data/activity_list.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for activity in activities:
            writer.writerow([activity])

def delete_activity_by_uuid(uuid_to_delete):
    try:
        with open('data/activities.csv', mode='r') as file:
            reader = csv.reader(file)
            all_activities = list(reader)

        with open('data/activities.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for activity in all_activities:
                if activity[0] != uuid_to_delete:
                    writer.writerow(activity)
    except FileNotFoundError:
        pass


def insert_activity_to_csv(activity, timestamp):
    timestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M")  # convert string to datetime object
    timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")  # convert back to string in correct format
    with open('data/activities.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([str(uuid.uuid4()), activity, timestamp])
