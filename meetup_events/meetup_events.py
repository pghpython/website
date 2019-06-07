import requests
from pelican import signals

class MeetupEventsPluginError(Exception):
  pass

def get_events():
  """
  Get Upcoming Events JSON from Meetup API
  """
  url = 'https://api.meetup.com/2/events?&sign=true&photo-host=public&group_urlname=python-pittsburgh&page=20'
  resp = requests.get(url)
  resp.raise_for_status()
  events_json = resp.json()
  return events_json

def add_meetup_events(gen, metadata):
  """
  Make events info accessible
  """
  gen.context['meetup_events'] = get_events()


def register():
  signals.page_generator_context.connect(add_meetup_events)
