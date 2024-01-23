from app.main import create_app
from app.config.config import Config

if __name__ == '__main__':
    app = create_app(Config)
    app.run(debug=True)
