#!/usr/bin/python3

from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(11), User(10), User(21)]

#print(sorted(users, key=lambda s: s.user_id))

print(sorted(users, key=attrgetter('user_id')))
