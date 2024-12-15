import tkinter as tk
from PIL import Image, ImageTk
import random
import os

# Automātiska ceļa noteikšana
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# Jautājumi un atbildes par sportu
jautajumi = [
    {
        "jautajums": "Kurš futbolists ir uzvarējis visvairāk Ballon d'Or balvas?",
        "attels": os.path.join(BASE_PATH, "attels1.png"),
        "atbildes": ["Lionels Mesi", "Krištianu Ronaldu", "Zinedins Zidāns", "Nedžels De Jong"],
        "pareiza": "Lionels Mesi"
    },
    {
        "jautajums": "Kā sauc visilgāk spēlējošo NBA spēlētāju?",
        "attels": os.path.join(BASE_PATH, "attels2.png"),
        "atbildes": ["LeBron James", "Michael Jordan", "Kareem Abdul-Jabbar", "Vince Carter"],
        "pareiza": "Vince Carter"
    },
    {
        "jautajums": "Kurā gadā Latvija ieguva savu pirmo Olimpisko zeltu?",
        "attels": os.path.join(BASE_PATH, "attels3.png"),
        "atbildes": ["2000", "1988", "1992", "1924"],
        "pareiza": "1988"
    },
    {
        "jautajums": "Kurā sporta veidā ir izmantots Termins 'slam dunk'?",
        "attels": os.path.join(BASE_PATH, "attels4.png"),
        "atbildes": ["Basketbolā", "Futbolā", "Regbijā", "Hokejā"],
        "pareiza": "Basketbolā"
    },
    {
        "jautajums": "Kurš sportists ir uzvarējis visvairāk Zelta medaļas Olimpiskajās spēlēs?",
        "attels": os.path.join(BASE_PATH, "attels5.png"),
        "atbildes": ["Michael Phelps", "Usain Bolt", "Simone Biles", "Carl Lewis"],
        "pareiza": "Michael Phelps"
    },
    {
        "jautajums": "Kurā gadā tika aizvadīts pirmais Pasaules Kausa izcīņas turnīrs futbolā?",
        "attels": os.path.join(BASE_PATH, "attels6.png"),
        "atbildes": ["1930", "1920", "1940", "1950"],
        "pareiza": "1930"
    },
    {
        "jautajums": "Kāds ir sporta veids, kurā tiek izmantota termins 'offside'?",
        "attels": os.path.join(BASE_PATH, "attels7.png"),
        "atbildes": ["Futbolā", "Basketbolā", "Regbijā", "Hokejā"],
        "pareiza": "Futbolā"
    },
    {
        "jautajums": "Kura pilsēta ir uzņēmusies 2024. gada Olimpiskās spēles?",
        "attels": os.path.join(BASE_PATH, "attels8.png"),
        "atbildes": ["Parīze", "Tokija", "Londonas", "Losandželos"],
        "pareiza": "Parīze"
    },
    {
        "jautajums": "Kurā valstī ir notikušas Pasaules kausa sacensības hokejā 2018. gadā?",
        "attels": os.path.join(BASE_PATH, "attels9.png"),
        "atbildes": ["Zviedrijā", "Kanādā", "Krievijā", "Somijā"],
        "pareiza": "Zviedrijā"
    },
    {
        "jautajums": "Kurš bija pirmais cilvēks, kurš piedalījās visās Olimpiskajās spēlēs pēc 100 gadiem?",
        "attels": os.path.join(BASE_PATH, "attels10.png"),
        "atbildes": ["Michael Phelps", "Carl Lewis", "Lindsey Vonn", "Nadia Comăneci"],
        "pareiza": "Michael Phelps"
    },
    {
        "jautajums": "Kurš ir uzvarējis visvairāk Formula 1 pasaules čempionātu titulus?",
        "attels": os.path.join(BASE_PATH, "attels11.png"),
        "atbildes": ["Lewis Hamilton", "Michael Schumacher", "Ayrton Senna", "Sebastian Vettel"],
        "pareiza": "Michael Schumacher"
    },
    {
        "jautajums": "Kādā sporta veidā tiek rīkots turnīrs ar nosaukumu 'Wimbledon'?",
        "attels": os.path.join(BASE_PATH, "attels12.png"),
        "atbildes": ["Tenisā", "Golfā", "Beisbolā", "Peldēšanā"],
        "pareiza": "Tenisā"
    },
    {
        "jautajums": "Kurā valstī pirmo reizi tika aizvadītas Ziemas Olimpiskās spēles?",
        "attels": os.path.join(BASE_PATH, "attels13.png"),
        "atbildes": ["Šveicē", "Norvēģijā", "Francijā", "Itālijā"],
        "pareiza": "Šveicē"
    },
    {
        "jautajums": "Kura komanda ir uzvarējusi visvairāk Super Bowl čempionātus?",
        "attels": os.path.join(BASE_PATH, "attels14.png"),
        "atbildes": ["Pittsburgh Steelers", "New England Patriots", "Dallas Cowboys", "San Francisco 49ers"],
        "pareiza": "New England Patriots"
    },
    {
        "jautajums": "Kurā valstī notika 2016. gada vasaras Olimpiskās spēles?",
        "attels": os.path.join(BASE_PATH, "attels15.png"),
        "atbildes": ["Brazīlijā", "Vācijā", "Japānā", "Amerikā"],
        "pareiza": "Brazīlijā"
    }
]

class ViktorinaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sporta Viktorīna")
        self.root.geometry("700x600")
        self.root.configure(bg="lightblue")

        self.jautajumi = random.sample(jautajumi, len(jautajumi))  # Sajauc jautājumus
        self.jautajums_index = 0
        self.pareizas_atbildes = 0

        self.create_start_page()

    def create_start_page(self):
        self.start_frame = tk.Frame(self.root, bg="lightblue")
        self.start_frame.pack(fill="both", expand=True)

        title_label = tk.Label(
            self.start_frame, text="Laipni lūdzam Sporta Viktorīnā!",
            font=("Arial", 24, "bold"), bg="lightblue", fg="darkblue"
        )
        title_label.pack(pady=50)

        instructions_label = tk.Label(
            self.start_frame,
            text="Pārbaudi savas zināšanas par sportu!\n"
                 "Atbildi uz jautājumiem un uzzini savu novērtējumu.",
            font=("Arial", 16), bg="lightblue", fg="black", wraplength=600, justify="center"
        )
        instructions_label.pack(pady=30)

        start_button = tk.Button(
            self.start_frame, text="Sākt Viktorīnu",
            font=("Arial", 14), bg="green", fg="white",
            command=self.start_quiz
        )
        start_button.pack(pady=20)

    def start_quiz(self):
        self.start_frame.pack_forget()
        self.create_quiz_UI()
        self.paradit_jautajumu()

    def create_quiz_UI(self):
        self.jautajums_label = tk.Label(self.root, text="", font=("Arial", 16), bg="lightblue", wraplength=650)
        self.jautajums_label.pack(pady=10)

        self.attels_label = tk.Label(self.root, bg="lightblue")
        self.attels_label.pack(pady=20)

        self.atbilde_var = tk.StringVar()
        self.atbilde_var.set(None)

        self.atbilde_radiobuttons = [
            tk.Radiobutton(self.root, text="", variable=self.atbilde_var, font=("Arial", 12), bg="lightblue", command=self.enable_next_button)
            for _ in range(4)
        ]
        for rb in self.atbilde_radiobuttons:
            rb.pack(anchor="center")

        self.nakamo_jautajumu_btn = tk.Button(self.root, text="Nākamais jautājums", command=self.nakamo_jautajumu, font=("Arial", 14), bg="lightblue", state=tk.DISABLED)
        self.nakamo_jautajumu_btn.pack(pady=30)

        self.jautajuma_numurs_label = tk.Label(self.root, text="Jautājums: 1", font=("Arial", 10), bg="lightblue")
        self.jautajuma_numurs_label.pack(pady=5, anchor="se", padx=10)

    def paradit_jautajumu(self):
        jautajums = self.jautajumi[self.jautajums_index]
        self.jautajums_label.config(text=jautajums["jautajums"])
        self.jautajuma_numurs_label.config(text=f"Jautājums: {self.jautajums_index + 1}/{len(self.jautajumi)}")

        try:
            attels = Image.open(jautajums["attels"]).resize((300, 200))
            self.attels_image = ImageTk.PhotoImage(attels)
            self.attels_label.config(image=self.attels_image)
        except Exception as e:
            print(f"Kļūda ielādējot attēlu {jautajums['attels']}: {e}")
            self.attels_label.config(image="", text="(Attēls nav pieejams)", font=("Arial", 12), fg="red")

        for i, atbilde in enumerate(jautajums["atbildes"]):
            self.atbilde_radiobuttons[i].config(text=atbilde, value=atbilde)

        self.atbilde_var.set(None)
        self.nakamo_jautajumu_btn.config(state=tk.DISABLED)

    def enable_next_button(self):
        if self.atbilde_var.get():
            self.nakamo_jautajumu_btn.config(state=tk.NORMAL)

    def nakamo_jautajumu(self):
        if self.atbilde_var.get() == self.jautajumi[self.jautajums_index]["pareiza"]:
            self.pareizas_atbildes += 1

        self.jautajums_index += 1
        if self.jautajums_index < len(self.jautajumi):
            self.paradit_jautajumu()
        else:
            self.beigt_viktorinu()

    def beigt_viktorinu(self):
        novertējums = "Tu esi sporta meistars!" if self.pareizas_atbildes >= 13 else \
                      "Tu esi sporta entuziasts!" if self.pareizas_atbildes >= 8 else \
                      "Tu esi sporta iesācējs!"

        self.jautajums_label.pack_forget()
        self.attels_label.pack_forget()
        for rb in self.atbilde_radiobuttons:
            rb.pack_forget()
        self.nakamo_jautajumu_btn.pack_forget()
        self.jautajuma_numurs_label.pack_forget()

        rezultats_label = tk.Label(self.root, text=f"Tu pareizi atbildēji uz {self.pareizas_atbildes} jautājumiem!\n{novertējums}", font=("Arial", 16), bg="lightblue", fg="green")
        rezultats_label.pack(pady=50)

# Galvenā programma
if __name__ == "__main__":
    sakne = tk.Tk()
    app = ViktorinaApp(sakne)
    sakne.mainloop()
