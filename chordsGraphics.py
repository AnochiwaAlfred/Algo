from tkinter import *


class MusicChords:
    def get_chords():
        def calculate():
            if key in keys and ty in list(type.keys()):
                chord = [(key.get()).title()]
                for i in type[(ty.get()).title()]:
                    chord.append(keys[keys.index((key.get()).title())+i])
                label = Label(text='The notes of ' + (key.get()).title() + ' ' + (ty.get()).title() + ' are ' + '-'.join(chord), font=('monotype corsiva', 14))
                label.grid(row=21,column=0)
            # print('The notes of ' + key + ' ' + ty.get() + ' are ' + '-'.join(chord))
            else:
                error = Label(text='Error: Enter a valid key and chord type.',  font=('monotype corsiva', 11))
                error.grid(row=23, column=0)
                
        root = Tk()
        
        type = {'Major':[4,7], 'Minor':[3,7], 'Diminished':[3,6],
                'Augmented':[4,8], 'Minor Sixth':[3,7,9], 'Major Sixth':[4,7,9],  
                'Dominant Seventh':[4,7,10], 'Minor Seventh':[3,7,10], 'Major Seventh':[4,7,11], 
                'Minor Major Seventh':[3,7,11], 'Diminished Seventh':[3,6,10], 'Ninth':[4,7,11,2]}
        keys = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
        chordtypelabel = Label(text='CHORD TYPES', font=('monotype corsiva', 11))
        notelabel = Label(text='N/B: Capitalize Each Word!!!!', font=('monotype corsiva', 11))
        keylabel = Label(text='Enter key: ', font=('monotype corsiva', 11))
        chordlabel = Label(text='Enter chord type: ', font=('monotype corsiva', 11))
        
        # print('\nCHORD TYPES')
        chordtypelabel.grid(row=0, column=0,  columnspan=2)
        a=1
        for i in type.keys():
            j = Label(text=i, font=('monotype corsiva', 11))
            # print(i)
            j.grid(row=a, column=0, columnspan=2)
            a+=1
            
        # print('N/B: Capitalize Each Word!!!!')
        notelabel.grid(row=14, column=0, columnspan=2)
        
        keylabel.grid(row=16, column=0)
        # key = str(input('\nEnter Key: ')).title()
        key = Entry(font=('monotype corsiva', 11))
        key.grid(row=16, column=1)
        # if key == 'B#' or 'b#':
        #     key = 'C'
        # if key == 'E#' or 'e#':
        #     key = 'F'
        
        chordlabel.grid(row=17, column=0)
        # ty = str(input('Enter chord type: ')).title()
        ty = Entry(font=('monotype corsiva', 11))
        ty.grid(row=17, column=1)
        
        
        calc_button = Button(text='OK', font=('monotype corsiva', 11), bg='black', fg='white', command=calculate)
        calc_button.grid(row=18, column=0, columnspan=2, rowspan=3)
        
        

        mainloop()
 
        
    get_chords()
    










# class MusicChords2:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Music Chords")

#         # Create the chord types dictionary
#         self.type = {'Major':[4,7], 'Minor':[3,7], 'Diminished':[3,6],
#                      'Augmented':[4,8], 'Minor Sixth':[3,7,9], 'Major Sixth':[4,7,9],  
#                      'Dominant Seventh':[4,7,10], 'Minor Seventh':[3,7,10], 'Major Seventh':[4,7,11], 
#                      'Minor Major Seventh':[3,7,11], 'Diminished Seventh':[3,6,10], 'Ninth':[4,7,11,2]}
#         self.keys = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#']

#         # Create the labels and entry widgets
#         self.key_label = Label(root, text="Enter key:", font=("monotype corsiva", 11))
#         self.key_entry = Entry(root, font=("monotype corsiva", 11))
#         self.chord_label = Label(root, text="Enter chord type:", font=("monotype corsiva", 11))
#         self.chord_entry = Entry(root, font=("monotype corsiva", 11))
#         self.result_label = Label(root, font=("monotype corsiva", 14))
#         self.error_label = Label(root, text="", font=("monotype corsiva", 11))
        
#         # Place the labels and entry widgets on the grid
#         self.key_label.grid(row=0, column=0)
#         self.key_entry.grid(row=0, column=1)
#         self.chord_label.grid(row=1, column=0)
#         self.chord_entry.grid(row=1, column=1)
#         self.result_label.grid(row=2, column=0, columnspan=2)
#         self.error_label.grid(row=3, column=0, columnspan=2)

#         # Create the OK button
#         self.calculate_button = Button(root, text="OK", font=("monotype corsiva", 11), bg="black", fg="white", command=self.calculate)
#         self.calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

#     def calculate(self):
#             key = self.key_entry.get().title()
#             ty = self.chord_entry.get().title()

#             if key in self.keys and ty in list(self.type.keys()):
#                 chord = [key]
#                 for i in self.type[ty]:
#                     chord.append(self.keys[self.keys.index(key)+i])
#                 self.result_label.config(text='The notes of ' + key + ' ' + ty + ' are ' + '-'.join(chord))
#                 self.result_label.grid(row=21, column=0)
#             else:
#                 self.error_label.config(text='Error: Enter a valid key and chord type.')
#                 self.error_label.grid(row=23, column=0)

#     def display_result(self, key, ty, notes):
#         self.result_label.config(text='The notes of ' + key + ' ' + ty + ' are ' + '-'.join(notes))
#         self.result_label.grid(row=2, column=0, columnspan=2)
#         self.error_label.config(text='')
#         self.error_label.grid(row=3, column=0, columnspan=2)

# def run_program():
#     root = Tk()
#     app = MusicChords(root)
#     root.mainloop()
    
# run_program()
