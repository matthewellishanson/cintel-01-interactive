import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

#set page title
ui.page_opts(title="PyShiny App with Plot", fillable=True)

#create sidebar with input slider for selected number of bins and min, max, start values
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of bins", 0, 100, 20)

#render plot with histogram
@render.plot(alt="A histogram")
def histogram():
    #set random seed with numpy to ensure reproducibility
    np.random.seed(3)
    # generate random data
    x = 100 + 15 * np.random.randn(437)

    # Use plt.hist to generate histogram using np array and slider input
    plt.hist(x, input.selected_number_of_bins(), density=True, color="gold")
