import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd
import PyPDF2 as pdf
import sys
import os
import pdf_stuff as p_s

textbox_width = 30

class MainApplication(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		self.parent = parent
		self.initialize()

	def initialize(self):
		#setup
		self.parent.title("PDF Stacker - by Dave Foote")
		self.parent.geometry("640x480")

		self.frame = tk.Frame(self.parent)
		self.frame.pack(fill=tk.X, padx=5, pady=5)

		#top file stuff
		self.top_label = tk.Label(self.frame, text="Top File")
		self.top_label.grid(row=0, column=0)

		self.topstring = tk.StringVar()
		self.topstring.set("Path to top file")

		self.top_entry = tk.Entry(self.frame, textvariable=self.topstring,
			width=textbox_width)
		self.top_entry.grid(row=1, column=0)

		self.browse(2, 0, 'top')

		#bottom file stuff
		self.bottom_label = tk.Label(self.frame, text="Bottom File")
		self.bottom_label.grid(row=0, column=1)

		self.bottomstring = tk.StringVar()
		self.bottomstring.set("Path to bottom file")

		self.bottom_entry = tk.Entry(self.frame, textvariable=self.bottomstring,
			width=textbox_width)
		self.bottom_entry.grid(row=1, column=1)

		self.browse(2, 1, 'bottom')

		#new file stuff
		self.new_label = tk.Label(self.frame, text="Name your new file:")
		self.new_label.grid(row=3, column=0)

		self.newstring = tk.StringVar()
		self.newstring.set("Directory of choice/filename of choice.pdf")

		self.new_entry = tk.Entry(self.frame, textvariable=self.newstring,
			width=textbox_width)
		self.new_entry.grid(row=3, column=1)

		self.run_button = tk.Button(self.frame, text="Run", command=self.run)
		self.run_button.grid(row=4, column=0, sticky='S')

		self.close_button =  tk.Button(self.frame, text="Bye!", command=self.parent.quit)
		self.close_button.grid(row=4, column=1, sticky='S')

	def run(self):
		patht = self.topstring.get()
		pathb = self.bottomstring.get()
		newpath = self.newstring.get()
		p_s.pdf_stack(patht, pathb, newpath)

	def browse(self, row, col, position):
		'''
		get the file you want
		'''
		self.button = ttk.Button(self.frame, text="Browse", command=
			lambda: self.fileDialog(position))
		self.button.grid(row=row, column=col)

	def fileDialog(self, position):
		if position == 'top':
			self.topstring.set(fd.askopenfilename(initialdir = os.getcwd(),
				title="Select File", filetypes=(("PDF Files", "*.pdf"),
				("all files", "*.*"))))
		if position == 'bottom':
			self.bottomstring.set(fd.askopenfilename(initialdir = os.getcwd(),
				title="Select File", filetypes=(("PDF Files", "*.pdf"),
				("all files", "*.*"))))




if __name__ == "__main__":
	root=tk.Tk()
	app = MainApplication(root)
	app.parent.mainloop()