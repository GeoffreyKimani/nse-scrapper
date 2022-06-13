import os
from scrapper.app_factory import create_app

debug = True

# Bind to $PORT if defined, otherwise default to 5000.
port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    app = create_app()
    app.run(
        host='0.0.0.0',
        port=port
    )
