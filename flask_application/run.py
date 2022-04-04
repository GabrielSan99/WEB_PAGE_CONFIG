from app import manager

if __name__ == "__main__":
    manager.run()


"""
Terminal commands:
    - python run.py runserver (run application)
    - export FLASK_APP=app (show to flask your app directory)
    - flask run (after export FLASK_APP this command is equals to python run.py)
    - flask run --host 0.0.0.0 -p [port] (this form allows connect others devices connected in this netwrok)
    - To connect: [host_ip]:[port] -> Example to connect: 192.168.0.14:5000)

    - export FLASK_ENV=development (to activate debug on flask, changes are automatically done)
    - export FLASK_ENV=product (final version, debug off)
"""
