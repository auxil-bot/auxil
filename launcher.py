from auxil.bot import Auxil


def run_bot() -> None:
    bot = Auxil()
    bot.run()

def dev() -> None:
    from dotenv import load_dotenv, find_dotenv
    """ Launches the bot in development mode"""
    load_dotenv(find_dotenv())
    run_bot()

def main():
    """Launches the bot."""

    run_bot()