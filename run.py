from app import app
from app import conf as config

app.run(
        debug=config.DEBUG,
        port=config.PORT,
        host=config.HOST
        )
