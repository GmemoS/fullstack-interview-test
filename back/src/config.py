from utilities.parser import CustomEncoder


class CustomConfig:
    RESTFUL_JSON = {'cls': CustomEncoder}

    @staticmethod
    def init_app(app):
        app.config['RESTFUL_JSON']['cls'] = app.json_encoder = CustomEncoder
