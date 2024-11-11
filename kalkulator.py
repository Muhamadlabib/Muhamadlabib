import tkinter as tk

def tombol_klik(item):
    global ekspresi
    ekspresi = ekspresi + str(item)
    input_teks.set(ekspresi)
       
def tombol_hapus(): 
    global ekspresi
    ekspresi = "" 
    input_teks.set("")
 
def tombol_hasil():
        try:
            hasil = str(eval(ekspresi.replace('%', '/100')))
            input_teks.set(hasil)
            ekspresi = ""
        except:
            input_teks.set("Error")
            ekspresi = "" 
    
       
window=tk.Tk()

ekspresi=""
input_teks=tk.StringVar()

frame1=tk.Frame(window,bg="blue",width=500,height=300)
frame1.pack()

greeting=tk.Label(frame1, text=" kalkulator labib PPLG 1",width=30)
greeting.pack()

label2 =tk.Label ( frame1, text="Hello word",textvariable=input_teks)
label2 .pack()

frame2=tk.Frame(window,bg="red",width=500,height=300)
frame2.pack()	

tombolAC =tk.Button(frame2, text="AC",bg="black",fg="white",
command=lambda:tombol_hapus())
tombolAC.grid(row=0,column=0)

tombolplusminus =tk.Button(frame2,
 text="+/-",bg="black",fg="white")
tombolplusminus.grid(row=0,column=1)

tombolpersen =tk.Button(frame2, text="%",bg="black",fg="white",
command=lambda:tombol_klik("%"))
tombolpersen.grid(row=0,column=2)

tombolbagi =tk.Button(frame2, text="/",bg="orange",fg="white",
command=lambda:tombol_klik("/"))
tombolbagi.grid(row=0,column=3)

tomboltujuh =tk.Button(frame2, text="7",bg="gray",fg="white",
command=lambda:tombol_klik("7"))
tomboltujuh.grid(row=1,column=0)

tomboldelapan =tk.Button(frame2, text="8",bg="gray",fg="white",
command=lambda:tombol_klik("8"))
tomboldelapan.grid(row=1,column=1)

tombolsembilan =tk.Button(frame2, text="9",bg="gray",fg="white",
command=lambda:tombol_klik("9"))
tombolsembilan.grid(row=1,column=2)

tombolkali =tk.Button(frame2,
 text="x",bg="orange",fg="white",
 command=lambda:tombol_klik("*"))
tombolkali.grid(row=1,column=3)

tombolempat =tk.Button(frame2, text="4",bg="gray",fg="white",
command=lambda:tombol_klik("4"))
tombolempat.grid(row=2,column=0)

tombollima =tk.Button(frame2, text="5",bg="gray",fg="white",
command=lambda:tombol_klik("5"))
tombollima.grid(row=2,column=1)

tombolenam =tk.Button(frame2, text="6",bg="gray",fg="white",
command=lambda:tombol_klik("6"))
tombolenam.grid(row=2,column=2)

tombolkurang =tk.Button(frame2,
 text="-",bg="orange",fg="white",
 command=lambda:tombol_klik("-"))
tombolkurang.grid(row=2,column=3)

tombolsatu=tk.Button(frame2, text="1",bg="gray",fg="white", command=lambda:tombol_klik("1"))
tombolsatu.grid(row=3,column=0)

tomboldua =tk.Button(frame2, text="2",bg="gray",fg="white",
command=lambda:tombol_klik("2"))
tomboldua.grid(row=3,column=1)

tomboltiga =tk.Button(frame2, text="3",bg="gray",fg="white",
command=lambda:tombol_klik("3"))
tomboltiga.grid(row=3,column=2)

tomboltambah =tk.Button(frame2,
 text="+",bg="orange",fg="white",
 command=lambda:tombol_klik("+"))
tomboltambah.grid(row=3,column=3)

tombol0 =tk.Button(frame2, text="0", width=10,bg="gray",fg="white",command=lambda:tombol_klik("0"))
tombol0.grid(row=4,column=0,columnspan=2)



tomboltitik =tk.Button(frame2, text=",",bg="gray",fg="white")
tomboltitik .grid(row=4,column=2)

tombolsamadengan =tk.Button(frame2,
 text="=",bg="orange",fg="white",
 command=lambda:tombol_hasil())
tombolsamadengan.grid(row=4,column=3)




window.mainloop()