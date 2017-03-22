#Given two strings, write a method to decide if one is a permutation of the other.

def permutation(a,b):
	return set(a) == set(b)

def main():
	print(permutation('John Doe','Doe John'))
	print(permutation('John Doe','Kartoon'))
	print(permutation('abbcdd','abb'))
	print(permutation('abbcdd','xyz'))
	print(permutation("abcdefgh","abcdefhg"))

		       
if __name__ == '__main__':
		main()	
        
        
#!/usr/bin/env python

from datetime import datetime
from collections import namedtuple

import sys


Event = namedtuple('Event', ['id', 'start_time', 'end_time'])
ConflictedTimeWindow = namedtuple('ConflictedTimeWindow', ['start_time', 'end_time', 'conflicted_event_ids'])

class Calendar(object):
    def __init__(self):
        self.events = []
    # Should allow multiple events to be scheduled over the same time window.
    def schedule(self, event):
        # IMPLEMENT ME
        self.events.append(event)
        
    def find_conflicted_time_windows(self):
        # IMPLEMENT ME
        self.events = sorted(self.events,key=lambda x:x.start_time)
        res = []
        for event in self.events:
           #print("Cur Event:", event)
            # find all overlapping events
            overlap = []
            for an_event in self.events:
                if an_event.id == event.id: 
                    continue
                #print("Considering:", an_event)
                start_bet = event.start_time < an_event.start_time < event.end_time
                end_bet = an_event.start_time < event.end_time < an_event.end_time
                if start_bet or end_bet:
                    overlap.append(an_event)
                if start_bet:
                    obj = ConflictedTimeWindow(an_event.start_time, event.end_time, [event.id, an_event.id])
                    res.append(obj)
                elif end_bet:
                    obj = ConflictedTimeWindow(event.start_time, an_event.end_time, [event.id, an_event.id])
                    res.append(obj)
                
            #print("Clashing with: ", event, " are: ",  overlap)
        return res

def main(argv):
    calendar = Calendar()
    calendar.schedule(Event(1,
        datetime.strptime('2014-01-01 10:00', '%Y-%m-%d %H:%M'),
        datetime.strptime('2014-01-01 11:00', '%Y-%m-%d %H:%M')))
    calendar.schedule(Event(2,
        datetime.strptime('2014-01-01 11:00', '%Y-%m-%d %H:%M'),
        datetime.strptime('2014-01-01 12:00', '%Y-%m-%d %H:%M')))
    calendar.schedule(Event(3,
        datetime.strptime('2014-01-01 12:00', '%Y-%m-%d %H:%M'),
        datetime.strptime('2014-01-01 13:00', '%Y-%m-%d %H:%M')))

    calendar.schedule(Event(4,
        datetime.strptime('2014-01-02 10:00', '%Y-%m-%d %H:%M'),
        datetime.strptime('2014-01-02 11:00', '%Y-%m-%d %H:%M')))
    calendar.schedule(Event(5,
        datetime.strptime('2014-01-02 09:30', '%Y-%m-%d %H:%M'),
        datetime.strptime('2014-01-02 11:30', '%Y-%m-%d %H:%M')))
    calendar.schedule(Event(6,
        datetime.strptime('2014-01-02 08:30', '%Y-%m-%d %H:%M'),
        datetime.strptime('2014-01-02 12:30', '%Y-%m-%d %H:%M')))

    calendar.schedule(Event(7,
        datetime.strptime('2014-01-03 10:00', '%Y-%m-%d %H:%M'),
        datetime.strptime('2014-01-03 11:00', '%Y-%m-%d %H:%M')))
    calendar.schedule(Event(8,
        datetime.strptime('2014-01-03 09:30', '%Y-%m-%d %H:%M'),
        datetime.strptime('2014-01-03 10:30', '%Y-%m-%d %H:%M')))
    calendar.schedule(Event(9,
        datetime.strptime('2014-01-03 09:45', '%Y-%m-%d %H:%M'),
        datetime.strptime('2014-01-03 10:45', '%Y-%m-%d %H:%M')))

    print calendar.find_conflicted_time_windows()
    # Should print something like the following

    # [ConflictedTimeWindow(start_time=datetime.datetime(2014, 1, 2, 9, 30),
    #                       end_time=datetime.datetime(2014, 1, 2, 10, 0),
    #                       conflicted_event_ids=[5, 6]),
    #  ConflictedTimeWindow(start_time=datetime.datetime(2014, 1, 2, 10, 0),
    #                       end_time=datetime.datetime(2014, 1, 2, 11, 0),
    #                       conflicted_event_ids=[4, 5, 6]),
    #  ConflictedTimeWindow(start_time=datetime.datetime(2014, 1, 2, 11, 0),
    #                       end_time=datetime.datetime(2014, 1, 2, 11, 30),
    #                       conflicted_event_ids=[5, 6]),
    #  ConflictedTimeWindow(start_time=datetime.datetime(2014, 1, 3, 9, 45),
    #                       end_time=datetime.datetime(2014, 1, 3, 10, 0),
    #                       conflicted_event_ids=[8, 9]),
    #  ConflictedTimeWindow(start_time=datetime.datetime(2014, 1, 3, 10, 0),
    #                       end_time=datetime.datetime(2014, 1, 3, 10, 30),
    #                       conflicted_event_ids=[7, 8, 9]),
    #  ConflictedTimeWindow(start_time=datetime.datetime(2014, 1, 3, 10, 30),
    #                       end_time=datetime.datetime(2014, 1, 3, 10, 45),
    #                       conflicted_event_ids=[7, 9])]

main("")

        