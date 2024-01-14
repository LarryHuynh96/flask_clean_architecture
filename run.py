from app.main import create_app
from app.config.dev_config import DevConfig

if __name__ == '__main__':
    app = create_app(DevConfig)
    app.run(debug=True)