import math

def make_readable(seconds):
    readable_seconds = seconds%60
    readable_minutes = math.floor(seconds/60)%60
    readable_hours   = math.floor((seconds/3600))%100
    return str(readable_hours).zfill(2) +':'+ str(readable_minutes).zfill(2) +':'+ str(readable_seconds).zfill(2)