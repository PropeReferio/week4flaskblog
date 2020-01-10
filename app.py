from decemberblog import app, routes

if __name__ == "__main__": #Will be true as long as app.py is not imported, not
# a slave. If a slave, __name__ == app, in which case this block of code
# won't execute.
    app.run(debug=True)
