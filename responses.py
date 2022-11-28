import math
import random
import datetime
import time
import classes

# global vars init
deadlines = classes.Members()


# determines path based on message content
def get_response(author, message: str) -> str:
    # splitting message into dif parts - uses divy_message class
    p_message = message.lower()
    p_list = p_message.split()

    # fixes list index out of range issue
    if len(p_list) == 1:
        ready_message = classes.Divy_message(
            command=p_list[0],
            aux_one=0,
            aux_two=0
        )
    elif len(p_list) == 2:
        ready_message = classes.Divy_message(
            command=p_list[0],
            aux_one=p_list[1],
            aux_two=0
        )
    else:
        ready_message = classes.Divy_message(
            command=p_list[0],
            aux_one=p_list[1],
            aux_two=' '.join(p_list[2:])
        )
    print('split success')
    # print(ready_message.command)
    # ^ tests to see if divy_message class init properly

    # different path depending on contents
    if ready_message.command == 'hello':
        done_notif = 'Hey there!'

    elif ready_message.command == 'roll':
        print('rolling')
        done_notif = set_roll_func(int(ready_message.aux_one))
        print('rolling complete')

    elif ready_message.command == 'help':
        done_notif = 'Hello! You have requested assistance with our commands.\n' + \
                     'Our current working features are as follows:\n' + \
                     '1. %hello - Say hello!\n' + \
                     '2. %roll [number] - Generate a number from 1-n! Make sure to enter a positive numerical value.\n' + \
                     '3. %timer [number] [sec/min]- Set a timer by stating how many minutes/seconds you want to wait.\n' + \
                     '4. %deadline [date] [description] - Records an upcoming deadline/appointment.\n' + \
                     '5. %schedule - Shows all deadline entries registered under that username.\n'

    elif ready_message.command == 'timer':
        done_notif = set_timer_func(ready_message.aux_one, ready_message.aux_two, author)
        print('timer accessed')

    elif ready_message.command == 'deadline':
        print('deadline now')
        done_notif = add_sched_listings(ready_message.aux_one, ready_message.aux_two, author)

    elif ready_message.command == 'schedule':
        print('showing sched')
        done_notif = show_schedule(author)

    else:
        done_notif = 'Please enter a valid command. Type %help for a list of commands.'

    # done_notif is basically the response the bot will post in the discord server.
    # diff commands generate diff done_notif
    return done_notif


def set_roll_func(max_roll):
    print('roll func')
    if math.isnan(max_roll):
        print('nan')
        return 'Please enter a positive numerical value for the maximum value achievable after %roll.\n' + \
               'Ex: %roll 20'
    if max_roll < 1:
        print('neg')
        return 'You must enter a number above 1.'
    print('valid num, making string')
    return 'You rolled: ' + str(random.randint(1, max_roll))


# handling reminder command
def set_timer_func(timer_length, time_unit, author):
    if math.isnan(int(timer_length)):
        return 'Please give a numerical value after %timer.' + \
               '\nEx: %timer 10 sec'
    delta = int(timer_length)
    if time_unit == 'sec' or time_unit == 'seconds':
        delta *= 1
    elif time_unit == 'min' or time_unit == 'minutes':
        delta *= 60
    else:
        return 'Please give a proper declaration of units of time.' + \
               '\nEx: %timer 10 sec OR %timer 10 seconds' + \
               '\nEx: %timer 10 min OR %timer 10 minutes'
    time.sleep(delta)
    print('tic toc')
    return 'Time\'s up, @' + str(author) + '!'


def add_sched_listings(due_date, descript, author):
    new_entry = classes.Sched_object(due_date, descript)
    print(new_entry)
    classes.Members.add_entry(deadlines, author, new_entry)
    return 'Entry Registered: ' + str(new_entry)


def show_schedule(author):
    format_str = 'Showing schedule for: @' + str(author) + '\n'
    print(author)
    z = 0
    y = 0
    for x in deadlines.members:
        print(x)
        if x == author:
            print('matchers')
            y += 1
            format_str += str(y) + '. ' + str(deadlines.schedules[z]) + '\n'
        z += 1
    if y == 0:
        return 'You have not made an entry. There is nothing to show.'
    return format_str
