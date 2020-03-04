import os
import http.server
import socketserver
import tkinter as tk
from tkinter import filedialog

pkgdir = ""
projectname = ""



class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        

    def create_widgets(self):
        newpkgdir = pkgdir
        self.proj_label = tk.Label(self, text="Project Name: ")
        self.proj_label.pack(side="top")
        self.proj_dir_label = tk.Label(self, text="Current Project Folder: ")
        self.proj_dir_label.pack(side="bottom")
        self.proj_dir_name = tk.Label(self,bd=5,text=newpkgdir)
        self.proj_dir_name.pack(side="right")
   
      
        self.find_game_directory = tk.Button(self)
        self.find_game_directory["text"] = "Assign Game Directory"
        self.find_game_directory["command"] = self.find_pkg_directory
        self.find_game_directory.pack(side="top")
        self.run_server = tk.Button(self,fg="blue")
        self.run_server["text"] = "Start Server!"
        self.run_server["command"] = self.StartServer
        self.run_server.pack(side="top")
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    # end create widgets

    def find_pkg_directory(self):
        global pkgdir
        pkgdir =  filedialog.askdirectory()
        with os.scandir(pkgdir) as entries:
            for entry in entries:
                print(entry.name)


    def StartServer(self):
        PORT = 8000
        handler = http.server.SimpleHTTPRequestHandler
        os.chdir(pkgdir)
        
        my_server = socketserver.ThreadingTCPServer(("",PORT),handler)
        print("Server started at localhost:" + str(PORT))
        my_server.serve_forever(2.0)

 



    

    # def get_proj_name(self):




root = tk.Tk()
#root.withdraw()
app = Application(master=root)
app.mainloop()



# print(pkgdir)
# StartServer()


# class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
#     def do_GET(self):
#         if self.path == pkgdir:
#             self.path = projname + ".html"
#         return http.server.SimpleHTTPRequestHandler.do_GET(self)

