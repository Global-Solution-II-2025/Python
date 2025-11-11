from datetime import datetime
import pytz

def utcnow():
    return datetime.utcnow()

def parse_time_hhmm(s: str):
    h, m = s.split(":")
    return int(h), int(m)
