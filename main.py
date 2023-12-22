import os
import datetime

class Calendar:
    def __init__(self):
        self.events = {}

    def create_event(self, event_name, event_date, event_time, event_details):
        event_id = len(self.events) + 1
        event = {
            'id': event_id,
            'name': event_name,
            'date': event_date,
            'time': event_time,
            'details': event_details
        }
        self.events[event_id] = event
        return event_id

    def read_event(self, event_id):
        if event_id in self.events:
            return self.events[event_id]
        return 'Event not found'

    def edit_event(self, event_id, new_details):
        if event_id in self.events:
            self.events[event_id]['details'] = new_details
        return 'Event not found'

    def delete_events(self, event_id):
        if event_id in self.events:
            del self.events[event_id]
        return 'Event not found'

    def display_events(self):
        for event_id, event in self.events.items():
            print(f"Event ID: {event_id}, Name: {event['name']}, Date: {event['date']}, Time: {event['time']}, Details: {event['details']}")