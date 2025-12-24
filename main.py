from kivy.uix.accordion import StringProperty
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from plyer import filechooser
from kivymd.uix.label import MDLabel
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast.kivytoast.kivytoast import toast
from android.permissions import request_permissions, Permission

request_permissions([
    Permission.READ_EXTERNAL_STORAGE,
    Permission.WRITE_EXTERNAL_STORAGE
])
Window.keyboard_anim_args ={'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"
import os
import platform
import json
from kivy.core.window import Window
# Vérifier si le système est Windowse
if platform.system() == 'Windows':
    os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
import json
from pathlib import Path
class Player(MDFloatLayout):
    name = StringProperty()
    rang= StringProperty()
    image_source=StringProperty()
class Info_none(MDLabel):
    text=StringProperty()
    halign= "center"
    font_size= 35
    pos_hint={"center_x": .5, "center_y": .5}

class basketball_manager(MDApp):
    def on_start(self):
        try:
            with open("user_data.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                screen_manager.get_screen("Acceuil").user_name_and_salut.text = f"Salut {data['nom']}"
                screen_manager.get_screen("parameter").user_name.text =  data['nom']
                screen_manager.get_screen("parameter").email.text =  data["email"]
                screen_manager.get_screen("Acceuil").players_list.clear_widgets()
                joueurs=self.charger_donnees()
                joueurs_nombre=len(joueurs)
                screen_manager.get_screen("parameter").nombre_players.text=str(joueurs_nombre)
                classement = self.calculer_classement(joueurs)
                if len(joueurs)==0:
                    screen_manager.get_screen("Acceuil").players_list.size_hint_y = 0.5
                    screen_manager.get_screen("Acceuil").players_list.add_widget(Info_none(text="Pas de joueurs\ndisponible"))
                else:
                    num, info =str(float(len(joueurs)/2)).split(".")
                    screen_manager.get_screen("Acceuil").players_list.size_hint_y = ((int(num)+int(info)/5)*0.3)
                    for range_info, joueur in enumerate(classement, 1):
                        screen_manager.get_screen("Acceuil").players_list.add_widget(Player(image_source=joueur["image_add"], name=joueur['nom'], rang=str(range_info)))
                    toast("Joueur ajouté avec succès...!")
                screen_manager.transition.direction = "down"
                screen_manager.current = "Acceuil"
        except:
            screen_manager.current = "welcome"
    def deconnect(self):
        screen_manager.transition.direction = "right"
        screen_manager.current = "welcome"
        for i in ["user_data", "joueurs"]:
            p = Path(f"{i}.json")
            if p.exists():
                p.unlink()
                print(f"Fichier supprimé : {p}")
            else:
                print(f"Le fichier n'existe pas : {p}")
            
    def build(self):
        global screen_manager, joueurs
        joueurs=[]
        self.path = ""  # Variable pour stocker le chemin du fichier
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("welcome.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("sign_up.kv"))
        screen_manager.add_widget(Builder.load_file("home.kv"))
        screen_manager.add_widget(Builder.load_file("print_lab.kv"))
        screen_manager.add_widget(Builder.load_file("add.kv"))
        screen_manager.add_widget(Builder.load_file("parameter.kv"))
        return screen_manager
    def login(self, id):
        if id==2:
            screen_manager.transition.direction = "left"
            screen_manager.current ="sign_up"
        elif id==3:
            screen_manager.transition.direction = "right"
            screen_manager.current ="login"
        elif id==4:
            screen_manager.transition.direction = "left"
            screen_manager.current ="login"
    def data_login_on(self, nom_user, password):
        all=screen_manager.get_screen("Acceuil")
        data={
                "nom": "Admin",
                "photo": "user_photo.png",
                "email": "alexdynamo1952@gmail.com",
                "password": "Admin"
            }
        try:
            with open("user_data.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except:
            pass
        if nom_user == "":
            toast(f"imformation incorrectée...", duration=1)
        elif password != data["password"]:
            toast(f"imformation incorrectée...", duration=1)
        elif nom_user ==data["email"] and password==  data["password"]:
            all.user_name_and_salut.text = f"Salut {data['nom']}"
            screen_manager.transition.direction = "left"
            screen_manager.current = "Acceuil"
            toast(f"Connecté...", duration=1)
        else:
            toast(f"imformation incorrectée...", duration=3)
    def sign_in(self, nom_user, user_mail, user_password, user_repassword_confirm):
        data={
                    "nom": nom_user,
                    "email": user_mail,
                    "password": user_password
                }
        if user_password=="" or user_password!=user_repassword_confirm:
            toast("Mot de passe incorrect!")
        else:
            try:
                all=screen_manager.get_screen("Acceuil")
                screen_manager.get_screen("Acceuil").user_name_and_salut.text = f"Salut {data['nom']}"
                screen_manager.get_screen("parameter").user_name.text =  data['nom']
                screen_manager.get_screen("parameter").email.text =  data["email"]
                screen_manager.get_screen("Acceuil").players_list.add_widget(Info_none(text="Pas de joueurs\ndisponible"))
                classement = self.calculer_classement(joueurs)
                num, info =str(float(len(joueurs))).split(".")
                screen_manager.get_screen("Acceuil").players_list.size_hint_y = str(int(num)+int(info)/5)
                for range_info, joueur in enumerate(classement, 1):
                    screen_manager.get_screen("Acceuil").players_list.add_widget(Player(image_source=joueur["image_add"], name=joueur['nom'], rang=str(range_info)))
                screen_manager.transition.direction = "left"
                screen_manager.current = "Acceuil"
                toast(f"Connecté...", duration=1)
                with open("user_data.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
            except:
                pass
    def add_picture(self):
        filechooser.open_file(on_selection= self.add_now)
    def add_now(self, selected):
        if selected:
            image_profile= selected[0]
            screen_manager.get_screen("sign_up").picture.source =image_profile
    def sauvegarder_donnees(self, joueurs, nom_fichier="joueurs.json"):
        """
        Sauvegarde les données des joueurs dans un fichier JSON.
        
        :param joueurs: Liste de joueurs à sauvegarder
        :param nom_fichier: Nom du fichier où les données seront sauvegardées
        """
        with open(nom_fichier, "w") as f:
            json.dump(joueurs, f, indent=4)

    def charger_donnees(self, nom_fichier="joueurs.json"):
        """
        Charge les données des joueurs depuis un fichier JSON.
        
        :param nom_fichier: Nom du fichier à charger
        :return: Liste des joueurs chargés depuis le fichier
        """
        try:
            with open(nom_fichier, 'r') as f:
                joueurs = json.load(f)
            return joueurs
        except FileNotFoundError:
            return []

    def calculer_classement(self, joueurs):
        """
        Calcule le total de compétence pour chaque joueur et retourne un classement des joueurs
        basé sur leur total de compétences.
        
        :param joueurs: Liste de dictionnaires, chaque dictionnaire représente un joueur et contient
                        les compétences 'tir', 'defense', 'passe' et 'dribble'.
        :return: Liste des joueurs triés par leur total de compétence, du plus fort au plus faible.
        """
        # Calcul du total de compétences pour chaque joueur
        for joueur in joueurs:
            joueur['total_competence'] = sum([joueur['tir'], joueur['defense'], joueur['passe'], joueur['dribble']])
        
        # Tri des joueurs par total de compétences (du plus élevé au plus faible)
        classement = sorted(joueurs, key=lambda x: x['total_competence'], reverse=True)

        return classement
    
    def add_player(self, add_picture, prenom, nom, tir_bar, def_bar, pas_bar, dbl_bar):
        screen_manager.get_screen("Acceuil").players_list.clear_widgets()
        joueurs=self.charger_donnees()
        joueurs.append({"image_add": add_picture, 'nom': prenom+" "+nom, 'tir': tir_bar, 'defense': def_bar, 'passe': pas_bar, 'dribble': dbl_bar})
        screen_manager.get_screen("parameter").nombre_players.text=str(len(joueurs))
        self.sauvegarder_donnees(joueurs)
        classement = self.calculer_classement(joueurs)
        num, info =str(float(len(joueurs)/2)).split(".")
        screen_manager.get_screen("Acceuil").players_list.size_hint_y = ((int(num)+int(info)/5)*0.3)
        for range_info, joueur in enumerate(classement, 1):
            screen_manager.get_screen("Acceuil").players_list.add_widget(Player(image_source=joueur["image_add"], name=joueur['nom'], rang=str(range_info)))
        toast("Joueur ajouté avec succès...!")
        screen_manager.get_screen("add").prenom.text = ""
        screen_manager.get_screen("add").nom.text = ""
        pass
    def show_player(self, name, rang):
        rang=""
        show_=screen_manager.get_screen("player_data")
        joueurs=self.charger_donnees()
        classement = self.calculer_classement(joueurs)
        show_.player_name.text=name
        for range_info, joueur in enumerate(classement, 1):
            if joueur['nom']==name:
                rang =f"Rang # {range_info}"
                break
        show_.player_rang.text=str(rang)
        for joueur in joueurs:
            name_player = joueur['nom']
            if name == name_player:
                show_.player_profile.source = joueur["image_add"]
                show_.list_data.tir_id.text = str(joueur['tir']) + "/10"
                show_.list_data.pas_id.text = str(joueur['passe']) + "/10"
                show_.list_data.def_id.text = str(joueur['defense']) + "/10"
                show_.list_data.dbl_id.text = str(joueur['dribble']) + "/10"
                show_.sc.total_id.text = str(sum([joueur['tir'], joueur['defense'], joueur['passe'], joueur['dribble']])) + "/40"
                break
        screen_manager.transition.direction = "left"
        screen_manager.current = "player_data"
    def handle_name(self, player_name):
        try:
            prenom, nom = player_name.text.split(" ", 1)  # Split at first space
        except ValueError:  # If there's no space in the "player_name"
            prenom = player_name.text
            nom = ''  # when there are empty "nom"
        return prenom, nom
    
    def show_file_manager(self):
        # Créer et ouvrir le gestionnaire de fichiers
        self.manager = MDFileManager(
            select_path=self.select_file,  # Callback pour sélectionner le fichier
            ext=[".jpg", ".png", ".jpeg"]  # Filtre pour les images
        )
        self.manager.show('/')  # Ouvre le gestionnaire de fichiers depuis la racine

    def select_file(self, path):
        # Callback appelé quand un fichier est sélectionné
        screen_manager.get_screen("add").add_picture.image= path
        toast("Photo ajoutée avec succès!")
        # Fermer le gestionnaire de fichiers immédiatement après la sélection
        self.manager.close()
if __name__=="__main__":
    basketball_manager().run()

