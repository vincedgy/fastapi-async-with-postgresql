from .logging import builder

if __name__ == '__main__':
  logging = builder(name='main')
  logging.info("Starting...")