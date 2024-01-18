Question Twelve
================
Plotting packages offer a variety of methods for displaying data. Write an interactive
plotting application for two-dimensional curves. Your application should allow the user
to choose the mode (line strip or polyline display of the data, bar chart, or pie chart),
colors, and line styles.

PlottingApp Class
-----------------

.. py:class:: PlottingApp

   A class representing an interactive plotting application using PyQt5.

   .. method:: __init__()

      Initialize the plotting application.

   .. method:: initUI()

      Initialize the user interface.

   .. method:: update_plot()

      Update the plot when the user changes options.

   .. method:: generate_plot()

      Generate the plot based on user selections.

   Constants:
      - width (int): Width of the plot image (600).
      - height (int): Height of the plot image (400).

   User Interface Elements:
      - QLabel image_label: Display the generated plot.
      - QComboBox mode_combobox: Select the plotting mode (Line Strip, Polyline, Bar Chart, Pie Chart).
      - QComboBox color_combobox: Select the plot color (Red, Green, Blue, Black).
      - QComboBox line_style_combobox: Select the line style (Solid, Dashed, Dotted).
      - QPushButton generate_button: Generate the plot based on user selections.

   Example Usage:
      - Create an instance of PlottingApp.
      - Interact with the user interface to select plotting options.
      - Click the "Generate Plot" button to update and display the plot.

   Example:

   .. code-block:: python

      if __name__ == '__main__':
          app = QApplication(sys.argv)
          plotting_app = PlottingApp()
          plotting_app.show()
          sys.exit(app.exec_())

