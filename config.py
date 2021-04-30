from collections import namedtuple
import client
import os 

Login = namedtuple('Login', 'token, catching_channels')
ACCOUNTS = [
    Login(token = os.environ.get("token1"), catching_channels = [819707295696945202, 820275305166929941]),
    Login(token = os.environ.get("token2"), catching_channels = [0]),
    Login(token = os.environ.get("token3"), catching_channels = [0]),
    Login(token = os.environ.get("token4"), catching_channels = [0]),
    Login(token = os.environ.get("token5"), catching_channels = [0]),
]

SPAM_CHANNELS = [820149204680310794]
ADMIN =[781973032436498432, 818946937847152691]
