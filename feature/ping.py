import sys
import os

class Ping():
    def ping(latency):
        return f'Ping is {round((latency)*1000)}ms'