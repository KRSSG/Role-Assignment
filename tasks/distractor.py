import math
from utils.config import *
from utils.geometry import *
from skills import skills_union
from skills import sGoToPoint
from skills import sGoToBall
from skills import sKickToPoint




class TDistractor(object):
	def __init__(self, arg):
		super(TDistractor, self).__init__()
		self.arg = arg
	def execute(self,state,bot_id,play_type=0):
		pass