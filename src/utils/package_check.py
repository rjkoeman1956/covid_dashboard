import importlib
import ipywidgets
import matplotlib.pyplot as plt
import sys
from IPython.display import display, clear_output


def check_required_packages(packages=None):
    """
    Controleer of opgegeven Python packages beschikbaar zijn.
    """
    if packages is None:
        packages = ['ipywidgets', 'geopandas', 'fiona', 'shapely', 'matplotlib', 'xlrd', 'zipfile', 'requests', 'shutil', 'reportlab', 'openpyxl']
    print("Checking required packages:")
    for pkg in packages:
        try:
            importlib.import_module(pkg)
            print(f"✅ {pkg} is installed")
        except ImportError:
            print(f"⚠️ {pkg} is NOT installed")


def get_environment_info():
    """
    Geef een dict terug met details over de huidige Python-omgeving.
    """
    return {
        "Python executable": sys.executable,
        "Python version": sys.version,
        "ipywidgets version": ipywidgets.__version__,
    }


def show_widget_test_plot():
    """
    Toon een eenvoudige testplot via ipywidgets en matplotlib om GUI-functionaliteit te controleren.
    """
    output = ipywidgets.Output()

    def show_plot(_=None):
        with output:
            clear_output(wait=True)
            fig, ax = plt.subplots()
            ax.plot([1, 2, 3], [4, 5, 6])
            plt.show()
            plt.close(fig)

    button = ipywidgets.Button(description="Test Plot")
    button.on_click(show_plot)
    display(ipywidgets.VBox([button, output]))
