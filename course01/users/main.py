from course01.users.Event import Event


def get_event_date(event):
    return event.date


def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout" and event.user in machines[event.machine]:
            machines[event.machine].remove(event.user)
    return machines


def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            users_list = ", ".join(users)
            print("{}:\n{}\n".format(machine, users_list))


if __name__ == '__main__':
    events = [
        Event("2020-01-21 12:45:56", "login", "myworkstation.local", "jordan"),
        Event("2020-01-22 15:53:42", "logout", "webserver.local", "jordan"),
        Event("2020-01-21 18:53:21", "login", "webserver.local", "jane"),
        Event("2020-01-22 10:25:34", "logout", "myworkstation.local", "jordan"),
        Event("2020-01-21 08:20:01", "login", "webserver.local", "jordan"),
        Event("2020-01-23 11:24:30", "logout", "mailserver.local", "chris"),
        Event("2020-01-23 11:24:35", "login", "mailserver.local", "chris")
    ]

    generate_report(current_users(events))
