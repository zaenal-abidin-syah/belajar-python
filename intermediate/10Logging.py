# import logging
# # logging.basicConfig(level=logging.DEBUG, format="%s{asctime}- %s{name}s %{levelname}s %s{message}s", detefmt='%m/%d/%y %H:%M:%s')

# # logging.debug("this is a debug message")
# # logging.info("this is a info message")
# # logging.warning("this is a warning message")
# # logging.error("this is a error message")
# # logging.critical("this is a critical message")

# # fail gk jelas 360

# logger=logging.getLogger(__name__)

# stream_h=logging.StreamHandler()
# file_h=logging.FileHandler("file.log")


# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)

# formater = logging.Formatter("%{name}s -{levelname}s - %{message}s")
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)

# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# logger.warning("this is warning")
# logger.error("this is error")










# import logging
# # from logging.handlers import RotatingFileHandlers

# print("\n".join(dir(logging.Handler)))

# logger=logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
# logger.addHandler(handler)

# for i in range(10000):
#     logging.info("hello world")