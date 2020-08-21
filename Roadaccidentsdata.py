from tkinter import *
import csv
import matplotlib.pyplot as plt
import numpy as np


"""exampleFile = open('roads1.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
exampleFile = open('roads2.txt')
example = exampleFile.read()"""





def converter():
    def plot_graph():
        label = ['Andhrapradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana',
                 'Himachal Pradesh', 'Jammu & Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh',
                 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan',
                 'Telangana']
        # index = np.arange(len(label))
        index = np.arange(len(label))
        plt.xlabel('states', fontsize=5)
        plt.ylabel('No of accidents', fontsize=5)
        plt.xticks(index, label, fontsize=5, rotation=90)
        plt.title('ROAD ACCIDENTS IN INDIA 2013-2017')
        # plt.bar(index, no_movies)
        # plt.show()
        # plt.xlabel('states', fontsize=15)
        # plt.ylabel('No of accidents', fontsize=15,rotation=90)
        # plt.xticks(label, rotation='vertical',fontsize=8)
        # plt.title('ROAD ACCIDENTS IN INDIA 2013-2017')
        if selected.get() == '2014':
            no_accidents = [29931, 308, 6499, 6640, 13157, 1879, 22493, 8944, 5576, 8043, 4356, 56831, 41096, 55335,
                            40455, 1295, 311, 234, 230, 11087, 4127, 27453, 21636]
            plt.bar(index, no_accidents)
            plt.show()

        elif selected.get() == '2015':
            no_accidents = [29439, 359, 7068, 6835, 13426, 2055, 21448, 10794, 5108, 8142, 4038, 56971, 43735, 55815,
                            39606, 1201, 319, 103, 74, 11825, 4414, 26153, 22948]
            plt.bar(index, no_accidents)
            plt.show()
        elif selected.get() == '2016':
            no_accidents = [30051, 391, 6127, 5651, 12955, 2026, 19949, 10531, 5764, 7692, 3793, 54556, 44108, 57873,
                            35884, 955, 354, 68, 120, 11312, 4351, 24103, 24217]
            plt.bar(index, no_accidents)
            plt.show()
        else:
            no_accidents = [27475, 316, 6163, 6014, 12550, 1922, 16802, 10339, 5452, 7419, 3918, 52961, 42671, 57532,
                            32128, 1027, 354, 55, 375, 11198, 4218, 22071, 23990]
            plt.bar(index, no_accidents)
            plt.show()

    list_opt = ['2014', '2015', '2016', '2017']

    root = Tk()

    root.title("ROAD ACCIDENTS IN INDIA")

    root.geometry("200x200")

    root.resizable(0, 0)

    selected = StringVar(root)

    root.configure(background='cyan')
    selected.set(' ')
    w = Label(root, text='SELECT YEAR', background='tomato')
    w.pack()
    dropdown = OptionMenu(root, selected, '2014', '2015', '2016', '2017')
    dropdown.configure(background='blue')
    dropdown.place(x=70, y=20)
    button = Button(root, text='PLOT', background='orange', command=plot_graph)
    button.place(x=80, y=80)

    root.mainloop()


converter()


