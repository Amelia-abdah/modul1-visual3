import PySimpleGUI as sg

window = sg.Window(title="Latihan Pertama", 
                    layout=[[sg.Text("NPM      : 2210010146")],
                            [sg.Text("Nama     : Nur Amelia Abdah")],
                            [sg.Text("Kelas    : 5B NONREG TI BJM")],
                            [sg.Text("Matkul   : VISUAL 3")]], 
                    size=(400,200))
window()
window.close()