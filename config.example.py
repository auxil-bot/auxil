dict(
	prefixes = ['!'],

	tokens = dict(
		discord = '...',
		stats = {
			'discord.bots.gg': None,
			'discordbots.org': None,
			'lbots.org': None
		},
	),

	ignore_bots = dict(
		default = False,
		overrides = dict(
			guilds = set(),
			channels = set()
		),
	),

	hasura_graphql_admin_secret = 'dumb',
	graphql_endpoint = 'http://localhost:8080/v1/graphql',
)
