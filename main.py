import pandas as pd
from time import process_time
class Hilbert(object):
	def __init__(self):
		rooms = []
		channels = []
	def insert_room(self):
		pass
	def remove_room(self):
		pass
	def get_rooms(self):
		return self.rooms
	def get_channels(self):
		return self.channels
	def sort_rooms(self):
		pass
	def find_room(self):
		pass
	def print_empty_room(self):
		pass
	def get_processed_time(self):
		pass
	def create_submission(self, filename, room_id, channel_id):
		dict = {"Room_id":room_id,"channel_id":channel_id}
		df = pd.DataFrame(dict)
		df.to_csv(filename)
hilbert = Hilbert()
if __name__ == "__main__":
	hilbert.create_submission("submission.csv", hilbert.room_id, hilbert.channel_id)
