# -*- coding: utf-8 -*-
"""routes.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18VY8R2fvvy3gEcGgx30biKMQo3aDFqzs
"""

from app import app
from config.config import HOST, PORT

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)