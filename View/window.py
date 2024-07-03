from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas(
            self.__root,
            bg="white",
            width=width,
            height=height
        )
        self.canvas .pack(fill=BOTH, expand=1)
        self.is_running = False

        # Connect the delete window button to the self.close function
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        """will redraw all the graphics in the window.
        """
        self.canvas.update_idletasks()
        self.canvas.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False
