from booking.booking import Booking
try:
    with Booking() as bot:
        bot.load()
        bot.choosecurrency(currency="INR")
        bot.search(data='Ahmedabad')
        bot.persons()
        bot.allow()
except Exception as p:
    if 'in PATH' in str(p):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise