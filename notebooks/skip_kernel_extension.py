def skip(line, cell=None):
    """
    Notebook cell magic:
      %%skip <expr>     # True => sla cell over; False => voer uit
    """
    if eval(line):
        return
    get_ipython().run_cell(cell)

def load_ipython_extension(shell):
    # Registers the skip magic when the extension loads
    shell.register_magic_function(skip, 'line_cell')
    print("Skip kernel extension loaded!")

def unload_ipython_extension(shell):
    # Unregisters the skip magic when the extension unloads
    del shell.magics_manager.magics['cell']['skip']
    print("Skip kernel extension unloaded!")

