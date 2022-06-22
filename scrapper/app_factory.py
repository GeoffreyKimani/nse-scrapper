import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from scrapper.constants import APP_CONFIG_ENV, PROD_CONFIG_VAR, DEV_CONFIG_VAR, APP_NAME, SECRET_KEY


def get_config_type():
    """
        from the environment get and return the environment variable that holds the packages and the environment
         configuration type i.e. is it development mode or production.
    :return:
    """
    return os.environ.get(APP_CONFIG_ENV, DEV_CONFIG_VAR).lower().strip()


def config_app(app_instance):
    """
        Take the app instance and merge all configurations here.
        :param app_instance:
        :return:
    """
    config_type = get_config_type()

    # possible configurations as a dictionary
    configs = {
        DEV_CONFIG_VAR: "scrapper.config.DevelopmentConfig",
        PROD_CONFIG_VAR: "scrapper.config.ProductionConfig"
    }

    app_instance.config.from_object(configs[config_type])
    config_file_path = os.environ.get(APP_NAME + "_CONFIG_FILE")

    if config_file_path and os.path.exists(config_file_path):
        app_instance.config.from_pyfile(config_file_path)

    # Ensure flask doesn't redirect to trailing slash endpoint
    app_instance.url_map.strict_slashes = False


db = SQLAlchemy()


def extensions_set_up(app_instance):
    """
        Initialize/instantiate any extensions e.g. JWT, SQLALCHEMY, DB MIGRATIONS, MAIL etc here for global view.
        :param app_instance:
        :return:
    """
    app_instance.config['SECRET_KEY'] = os.getenv(SECRET_KEY)

    # Database and Migrations setup
    db.init_app(app_instance)
    migrate = Migrate(app_instance, db, compare_type=True)

    return {'db': db, 'migrate': migrate}


# Application Factory
def create_app(test_config=None):
    """
        This is the application factory, it takes as an argument a test_config variable and if it exists, the mode for
        running the application switches to allow for tests to run, if no configuration is passed or False, then we
        call the config_app function to setup the application appropriately.
        The result of this factory is an application ready for use.
        :param test_config:
        :return app:
    """
    app = Flask(__name__, instance_relative_config=True)

    if test_config:
        app.config.from_mapping(test_config)
    else:
        config_app(app)

    # Ensure instance path exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Extensions SetUp
    ext = extensions_set_up(app)

    @app.shell_context_processor
    def make_shell_processor():
        return {
            'db': db,
        }

    @app.route('/')
    def index():
        return '<h1>Learn something interesting</h1>'

    @app.route('/scrapper')
    def scrapper():
        from scrapper.pdf_scrapper import pdf_scrapper
        return pdf_scrapper()

    return app
