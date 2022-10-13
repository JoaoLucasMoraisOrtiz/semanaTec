# realiza as importações
from concurrent.futures.process import _MAX_WINDOWS_WORKERS
import tkinter
from app.controller.mainController import mainController
from tkinter import mainloop

# instancia o mainController
main = mainController

# inicia a main
main.getMain()