from plotting_module import *
from interactive_plotting import *
import tkinter
from tkinter import filedialog

"""
filename = "/home/solli/Documents/Prosjektoppgave/Data_files/depth_profile/151118h.dp_rpc_asc"
test = plotter(filename)
test.plot_machine()


filename_2 = "/home/solli/Documents/Prosjektoppgave/Data_files/mass_spectrometry/ITO_mass-spectra_A.ms_rpc_asc"
test_2 = plotter(filevname_2)
test_2.plot_machine()
"""


def file_location(self, filename):
	root = tkinter.Tk()
	files = filedialog.askopenfilenames(parent=root,title='Choose files')
	files = root.tk.splitlist(files)
	return files


filename = file_location()

"""["/home/solli/Documents/Prosjektoppgave/Data_files/depth_profile/160112b.dp_rpc_asc"
			,"/home/solli/Documents/Prosjektoppgave/Data_files/depth_profile/160112d.dp_rpc_asc"
			,"/home/solli/Documents/Prosjektoppgave/Data_files/depth_profile/160112f.dp_rpc_asc"
			,"/home/solli/Documents/Prosjektoppgave/Data_files/depth_profile/160112h.dp_rpc_asc"
			,"/home/solli/Documents/Prosjektoppgave/Data_files/depth_profile/time_x_axis.dp_rpc_asc"]"""
test = interactive_plotting(filename)
test.data_generation()
test.plotting()

