from cx_Freeze import setup, Executable

setup(name = "TelegramBot" ,
      version = "1.0" ,
      description = "" ,
      executables = [Executable("main.py")])