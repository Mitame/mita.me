from mita_site import app as application, config

if __name__ == "__main__":
    application.run(config["bind_addr"], config["port"], config["debug"])
