import tkinter
import Stats



class SimulatorView():
    """A graphical view of the simulation grid.

    The view displays a colored rectangle for each location
    representing its contents. The rectangle is surrounded by
    a circle.
    :author: David J. Barnes and Michael Kolling
    :author: Peter Sander
    """
    # class attributes
    _EMPTY_COLOR = 'white'
    _STEP_PREFIX = "Step: "
    # _POPULATION_PREFIX = "Population: "
    _STATS_PREFIX = "States: "

    def __init__(self, root: object, size):
        """Create a view with the given size.
        """
        self.size = size
        self.frame = tkinter.Frame(root)
        # graphics initializations
        self.stepLabel = tkinter.Label(self.frame, text=SimulatorView._STEP_PREFIX)
        self.stepLabel.grid(row=1, column=0)
        # self.population = tkinter.Label(self.frame, text=SimulatorView._POPULATION_PREFIX)
        # self.population.grid(row=1, column=2)
        self.statsLabel = tkinter.Label(self.frame, text = SimulatorView._STATS_PREFIX)
        self.statsLabel.grid(row=1,column=2)

        self.fieldView = FieldView(self.frame, size)
        self.fieldView.grid(row=0, columnspan=3)
        self.frame.grid()

    def showStatus(self, step, sapienses: list) -> None:
        """Show the current status of the field.

        :step: Which iteration step it is.
        :sapienses: List of sapiens for calculating status.
        """
        self.stepLabel['text'] = SimulatorView._STEP_PREFIX + str(step)
        # self.population['text'] = SimulatorView._POPULATION_PREFIX + str(sapienses.__len__())
        self.statsLabel['text'] = SimulatorView._STATS_PREFIX + "['S=" + str(Stats.S) +"' ,'I="+str(Stats.I)+"' ,'R="+str(Stats.R)+"' ,'D="+str(Stats.D)+"' ] R="+str(Stats.calculateR(sapienses))

        self.fieldView.preparePaint()
        self.fieldView.delete('all')
        for sapiens in sapienses:
            self.fieldView.drawMark(sapiens.location.row, sapiens.location.col,
                                    sapiens.colour)
        ##self.frame.update_idletasks()
        self.frame.update()


class FieldView(tkinter.Canvas):
    """Provide a graphical view of the square field.

    :author: David J. Barnes and Michael Kolling
    :author: Peter Sander
    :author: ZHENG Yannan
    """
    _GRID_VIEW_SCALING_FACTOR = 10

    def __init__(self, root: object, size):
        tkinter.Canvas.__init__(self, root,
                                height=size * self._GRID_VIEW_SCALING_FACTOR,
                                width=size * self._GRID_VIEW_SCALING_FACTOR,
                                background=SimulatorView._EMPTY_COLOR)
        self.gridHeight = size
        self.gridWidth = size
        self.size = [0, 0]

    def getPreferredSize(self) -> list:
        """Tell the GUI manager how big we would like to be.
        """
        return [self.gridHeight * self._GRID_VIEW_SCALING_FACTOR,
                self.gridWidth * self._GRID_VIEW_SCALING_FACTOR]

    def preparePaint(self):
        """Prepare for a new round of painting. Since the component may be
        resized, compute the scaling factor again.
        """
        size = [float(self['height']), float(self['width'])]
        if self.size != size:
            #  if the size has changed...
            self.size = size
            self.xScale = size[0] / self.gridWidth
            if self.xScale < 1:
                self.xScale = FieldView._GRID_VIEW_SCALING_FACTOR
            self.yScale = size[1] / self.gridHeight
            if self.yScale < 1:
                self.yScale = FieldView._GRID_VIEW_SCALING_FACTOR

    def drawMark(self, x, y, colour):
        """Paint on grid location on this field in a given colour.
        """
        self.create_rectangle(x * self._GRID_VIEW_SCALING_FACTOR, y * self._GRID_VIEW_SCALING_FACTOR,
                              (x + 1) * self._GRID_VIEW_SCALING_FACTOR, (y + 1) * self._GRID_VIEW_SCALING_FACTOR,
                              fill=colour, outline='')
        self.create_oval((x - 1) * self._GRID_VIEW_SCALING_FACTOR, (y - 1) * self._GRID_VIEW_SCALING_FACTOR,
                         (x + 2) * self._GRID_VIEW_SCALING_FACTOR, (y + 2) * self._GRID_VIEW_SCALING_FACTOR,
                         fill='', outline=colour)
