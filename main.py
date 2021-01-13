"""
Author : İlker Rişvan
13.01.2021
Dijkstra Alghoritm & Visualization

"""
from tkinter import * ## https://docs.python.org/3/library/tkinter.html
from graph import createGraph,drawGraph
from dijkstra import dijkstra
import tkinter.messagebox ## https://docs.python.org/3/library/tkinter.messagebox.html
import time ## used for counter , https://docs.python.org/3/library/time.html#time.perf_counter

n = 0       ## input, number of nodes
source = 0  ## input, source node
dest = 0    ## input, destination node

## this method used for usage of input datas
def enter_button ():
    ## get values from GUI ##
    n = int(n_value.get()) ## node number
    source = int(s_value.get())
    dest = int(d_value.get())

    ## If the node number smaller than 2 and bigger than 20 our program won't run.Because paths are not clear for understand.
    if not n >= 2 or not n <= 20:
        tkinter.messagebox.showwarning("Warning","Please select N Value between 2 and 20.")
    if  dest > n or source > n: ## exception
        tkinter.messagebox.showwarning("Warning", "Please check your inputs again.")

    else:
        graph = createGraph(n) ## create a graph via other script
        time_counter = time.perf_counter() ## begin the counter,the counter keep nanosecond
        path,total_cost = dijkstra(graph, source, dest) ## learn the shortest path and total cost with using dijkstra algorithm
        total_time = time.perf_counter() - time_counter ## learn to total time of dijkstra
        ## this method used for a button,shows the path as PNG with using drawGraph method.
        def show_path() :
            drawGraph(graph, path)

        ## this method used for a button,shows the results of the algorithm, time, path etc.
        def show_results():
            ## GUI ##
            result_window = Tk()
            result_window.geometry("600x300")
            result_window.title("Shortest Path With Dijkstra")
            result_window.configure(background="orange")
            ## about text in tkinter: https://www.tutorialspoint.com/python/tk_text.htm
            result_text = Text(result_window,height = 600,width =300)
            result_text.insert(INSERT,"RESULTS \n")
            result_text.insert(INSERT,f"TOTAL TIME : {total_time * 1000000} millisecond \n") ## totaltime was nanosecond,1 nanosecond = 10^6 milliseconds
            result_text.insert(INSERT,f"COST IS {total_cost}.\n")
            result_text.insert(INSERT,"PATH IS BELOW \n")
            for i in range(len(path)):
                result_text.insert(INSERT,f"{path[i]} \n")

            result_text.config(state="disabled",background = "orange")
            result_text.pack()
            result_window.mainloop()

        button_path = Button(text="SHOW THE PATH", command=show_path, activebackground="red", background="orange",
                        font="terminal", height="2")
        button_results = Button(text="SHOW RESULTS", command=show_results, activebackground="red", background="orange",
                         font="terminal", height="2")

        button_path.pack(side=LEFT, fill=X)
        button_results.pack(side=RIGHT, fill=X)

# -------------------------- GUI PART WITH TKINTER -------------------------- #

window = Tk()
window.title("Enter Values For Find Shortest Path With Dijkstra")
window.geometry("900x300")
window.configure(background = "darkblue")

n_label = Label(text = "        N Value:",fg = "yellow",bg = "darkblue" ).place(x = 20 , y = 21)
s_label = Label(text = "        Source:",fg = "yellow",bg = "darkblue" ).place(x = 300 , y = 20)
d_label = Label(text = "        Destination:",fg = "yellow",bg = "darkblue" ).place(x = 575 , y = 20)

## INPUTS ##
n_input = StringVar()
n_value = Entry(background = "orange",borderwidth = 3,font ="bold 10",textvariable=n_input)
n_value.place(x = 120, y = 18)

s_input = StringVar()
s_value = Entry(background = "orange",borderwidth = 3,font ="bold 10",textvariable=s_input)
s_value.place(x = 393 , y = 18)

d_input = StringVar()
d_value = Entry(background = "orange",borderwidth = 3,font ="bold 10",textvariable=d_input)
d_value.place(x = 700 , y = 18)

## TEXT IN THE MAIN SCREEN ##
information_text = Text(window, height=8, width=20)
information_text.insert(INSERT, "Please restart for\nnew values.You will get the path as PNG.\n\nPLEASE CLICK SHOW\nTHE PATH BEFORE THE SHOW RESULTS!")

information_text.config(state="disabled",background = "orange")
information_text.place(x= 395, y = 60)

## ENTER BUTTON, FOR USE THE VALUES IN MAIN SCREEN ##
button = Button(text= "ENTER",command = enter_button,activebackground = "red",background = "orange",font = "terminal",height = "2")
button.pack(side = BOTTOM,fill = X)

window.mainloop()
