from ben_cogs.bot import BenCogsBot

class Auxil(BenCogsBot):
	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs, setup_db=False)
		self.description = self.config.get('description')

	startup_extensions = [
		'ben_cogs.debug',
		'ben_cogs.misc',
		'ben_cogs.stats',
		'jishaku'
	]
