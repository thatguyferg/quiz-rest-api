#!/usr/bin/env python3

from project import create_app

if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)
