from run import APP

if __name__ == "__main__":
    APP.logger.info("GUNICORN APP running on port: 7080")
    APP.run()
