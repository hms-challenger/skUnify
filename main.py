import json
import requests
from product import *
from lists import *
from skunify_logo import *
from config import *

sku = []
id_counter = []
global_counter = []
ewcid_cat = []
cat = [
    "Exit",
    ["Song", "Playback", "Noten", "Text"],
    " Minimusiker-Songpaket",
    " kreative Liedersammlung",
    ["CD", "digital"], 
    " Tonie", 
    " Minimusiker-Buch", 
    " Lugert-Buch",
    " Materialpaket",
    " Lernvideo",
    "Rhythmical",
    "Klanggeschichte",
    "Poster",
    "Hörbuch",
    "Coppenrath-Buch"
    ]

i = 0
j = 0
offset = 0

"""DOWNLOAD JSON FILE FROM ECWID STORE --- .GET AND WRITE IN NEW JSON FILE --- .DUMPS"""
def download_data(id, offset, token):
    for i in range(7):
        response = requests.get("https://app.ecwid.com/api/v3/"+str(id)+"/products?offset="+str(offset)+"&limit=100&token="+str(token))
        data = response.json()
        json_object = json.dumps(data, indent=4, ensure_ascii=False)
        with open("data"+str(i)+".json", "w") as outfile:
            outfile.write(json_object)
        offset += 100
        i += 1

def write_json(j, new_product):
    """TEST-WRITING IN NEW JSON"""
    productcheck = input("Eintrag überprüfen? j/n ")
    if productcheck == "j" or productcheck == "J":
        print("Es wurde eine JSON Datei lokal im Ordner gespeichert!\n")
        json_object = json.dumps([new_product], indent=4, ensure_ascii=False)
        with open("new_product"+str(j)+".json", "w") as outfile:
            outfile.write(json_object)
    elif productcheck == "n" or productcheck == "N":
        print("Es wurde keine JSON Datei lokal im Ordner gespeichert!\n")
        return
    
def upload_json(new_product):
    """UPLOAD NEW PRODUCT(s?)"""
    abfrage2 = input("Eintrag hochladen? j/n ")
    """JSON TO FILL"""
    headers = {
        "Accept": "custom-app-39150140-2/json",
        "Content-Type": "custom-app-39150140-2/json"
    }
    if abfrage2 == "j" or abfrage2 == "J":
        print("\n>>> NEUES PRODUKT WURDE HOCHGELADEN! <<<\n")
        url = "https://app.ecwid.com/api/v3/39150140/products"
        response = requests.request("POST", url, json=str(new_product), headers=headers)
        print(response.text)
    elif abfrage2 == "n" or abfrage2 == "N":
        print("Es wurde kein Produkt hochgeladen!\n")
        return

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n>>> Willkommen bei:\n")
logo()

"""INIALIZING DOWNLOAD"""
start = input("Download Ecwid-Datensätze? j/n ")
if start == "j" or start == "J":
    id = input("Insert Ecwid-ID: ")
    token = input("Insert Access Token: ")
    download_data(id, offset, token)
else:
    pass

"""LIBRARY AND COUNTERS"""
for i in range(7):
    with open("data"+str(i)+".json", "r") as f:
        data = json.load(f)
        
        for products in data['items']:
            id_counter.append(products.get('id')) #ecwid id counter
            sku.append(products.get('sku')) #global counter
            names.append(products.get('name'))
            p_subtitle = products.get('subtitle')
            p_categoryIds = products.get('categoryIds')
            if p_categoryIds not in ewcid_cat:
                ewcid_cat.append(p_categoryIds)

            i += 1
f.close()

"""ECWID ID COUNTER"""
id_counter.sort()
id_ints = int(id_counter[-1])

"""GET INIDVIDUAL SKUs"""
for item in sku:
    if "lug" in item:
        my_lugert_books.append(item)
        my_lugert_books.sort()
    if "b0" in item:
        my_mini_books.append(item)
        if item.startswith("hb"):
            my_mini_books.remove(item)
        my_mini_books.sort()
    if "cop" in item:
        my_coppenrath_books.append(item)
        my_coppenrath_books.sort()         
    if "p" in item:
        my_pos_ints = []
        my_poster.append(item)
        if item.startswith("cop"):
            my_poster.remove(item)
        elif item.startswith("mp"):
            my_poster.remove(item)
        elif item.startswith("sp"):
            my_poster.remove(item)
        if "pb" in item:
            my_poster.remove(item)
        for pos_ints in my_poster:
            try:
                pos_ints = int(pos_ints[-1])
                my_pos_ints.append(pos_ints)
            except:
                print("Keine Zahl vorhanden")
            my_poster.sort()
            my_pos_ints.sort()
    if "cd" in item:
        my_cds.append(item)
        my_cds.sort()
        if "digi" in item:
            my_cds.remove(item)
    if "digi" in item:
        my_digitals.append(item)
        my_digitals.sort()
    if "ton" in item:
        my_tonies.append(item)
        my_tonies.sort()
    if "kg" in item:
        my_klanggeschichten.append(item)
        my_klanggeschichten.sort()
    if "hb" in item:
        my_hoerbuecher.append(item)
        my_hoerbuecher.sort()
    if "kl" in item:
        my_kl_ints = []
        my_liedersammlungen.append(item)
        for kl_ints in my_liedersammlungen:
            try:
                my_kl_ints.append(int(kl_ints.split("-")[0][2:]))
                my_kl_ints.sort()
            except:
                print("Keine Zahl vorhanden")
        my_liedersammlungen.sort()
    if "mp" in item:
        my_mp_ints = []
        my_materialpakete.append(item)
        for mp_ints in my_materialpakete:
            try:
                my_mp_ints.append(int(mp_ints.split("-")[0][2:]))
                my_mp_ints.sort()
            except:
                print("Keine Zahl vorhanden")
        my_materialpakete.sort()
    if "sp" in item:
        my_songpakete.append(item)
        my_songpakete.sort()
    if "vid" in item:
        my_videos.append(item)
        my_videos.sort()
    if "rhy" in item:
        my_rhythmicals.append(item)
        my_rhythmicals.sort()
    if "s" in item:
        my_song_ints = []
        my_songs.append(item)
        if "sp" in item:
            my_songs.remove(item)
        my_songs.sort()
        for song_ints in my_songs:
            try:
                song_ints = int(song_ints[0:3])
                my_song_ints.append(song_ints)
            except:
                pass

    item_spit = item.split("-")
    try:
        itemint = int(item_spit[1])
        global_counter.append(itemint)
    except:
        # print("SKU konnte nicht zugeordnet werden:", item) # soon to be removed
        pass

"""SET GLOBAL COUNTER"""
global_counter.sort()
global_counter = int(global_counter[-1])

"""SET INDIVIUAL COUNTERS"""
cop_counter = int(len(my_coppenrath_books))
poster_counter = int(len(my_poster))
mini_counter = int(len(my_mini_books))
lugert_counter = int(len(my_lugert_books))
klanggeschichten_counter = int(len(my_klanggeschichten))
liedersammlung_counter = int(my_kl_ints[-1])
songpakete_counter = int(len(my_songpakete))
materialpakete_counter = int(my_mp_ints[-1])
rhythmical_counter = int(len(my_rhythmicals))
video_counter = int(len(my_videos))
cd_counter = int(len(my_cds))
tonie_counter = int(len(my_tonies))
hoerbuch_counter = int(len(my_hoerbuecher))

"""MAIN LOOP skUNIFY"""
while True:
    init_skunify = input("Neues Produkt anlegen? j/n ")
    if init_skunify == "j" or init_skunify == "J":
        j += 1
        """SET PRODUCT CATEGORY"""
        while True:
            print("\n>>> PRODUKTKATEGORIE WÄHLEN <<<\n")
            global_counter += 1

            cat_counter = 0
            for choice in cat:
                print(cat_counter, choice)
                cat_counter += 1

            set_category = input("Produktkategorie-Nr.: ")
            if set_category == "0": #exit without writing
                exit()

            elif set_category == "1": # song, playback, noten, text
                song_ints += 1
                while True:
                    new_product_name = input("\nNeuer Song: ")
                    if new_product_name not in names:
                        names.append(new_product_name) # for searching in library?
                        my_songs.append(new_product_name)
                        break
                    else: 
                        print("Produkt schon vorhanden!")   
                        continue
                new_song(new_product_name, song_ints, global_counter)
                print("\n>>> NEUER SONG: ", song_ints, new_product_name, str(song_ints) + "s" + "-" + str(global_counter).zfill(4), "\n")
                write_json(j, new_product)
                upload_json(new_product)

                add_playback = input("Playback hinzufügen? j/n ")
                global_counter += 1
                j += 1
                if add_playback == "j" or add_playback == "J":
                    new_playback(new_product_name, song_ints, global_counter)
                    print("\n>>> NEUER PLAYBACK:", song_ints, new_product_name, str(song_ints) + "pb" + "-" + str(global_counter).zfill(4), "\n")
                    write_json(j, new_product)
                    upload_json(new_product)
                else:
                    pass

                add_noten = input("Noten hinzufügen? j/n ")
                global_counter += 1
                j += 1
                if add_noten == "j" or add_noten == "J":
                    new_noten(new_product_name, song_ints, global_counter)
                    print("\n>>> NEUE NOTEN:", song_ints, new_product_name, str(song_ints) + "n" + "-" + str(global_counter).zfill(4), "\n")
                    write_json(j, new_product)
                    upload_json(new_product)
                else:
                    pass

                add_text = input("Text hinzufügen? j/n ")
                global_counter += 1
                j += 1
                if add_text == "j" or add_text == "J":
                    new_text(new_product_name, song_ints, global_counter)
                    print("\n>>> NEUER TEXT:", song_ints, new_product_name, str(song_ints) + "t" + "-" + str(global_counter).zfill(4), "\n")
                    write_json(j, new_product)
                    upload_json(new_product)
                    break
                else:
                    break

            elif set_category == "2": # minimusiker-songpaket
                songpakete_counter += 1
                while True:
                    new_product_name = input("Neues Songpaket: ")
                    if new_product_name not in names:
                        names.append("Songpaket: " + new_product_name) # for searching in library?
                        my_songpakete.append("Songpaket: " + new_product_name)
                        break
                    else: 
                        print("Produkt schon vorhanden!")   
                        continue
                new_songpaket(new_product_name, songpakete_counter, global_counter)
                print("\n>>> NEUES SONGPAKET: Songpaket: " + new_product_name, new_product['sku'], "\n")
                write_json(j, new_product)
                upload_json(new_product)
                break

            elif set_category == "3": # kreative liedersammlung
                liedersammlung_counter += 1
                while True:
                    neue_liedersammlung = input("Neue Liedersammlung: ")
                    name1 = input("Song 1/5: ")
                    name2 = input("Song 2/5: ")
                    name3 = input("Song 3/5: ")
                    name4 = input("Song 4/5: ")
                    name5 = input("Song 5/5: ")
                    names.append("kreative Liedersammlung #" + str(liedersammlung_counter)) # for searching in library?
                    my_liedersammlungen.append("kreative Liedersammlung #" + str(liedersammlung_counter))
                    new_liedersammlung(liedersammlung_counter, global_counter, name1, name2, name3, name4, name5)
                    print("\n>>> NEUE LIEDERSAMMLUNG: kreative Liedersammlung #" + str(liedersammlung_counter), new_product['sku'], "\n")
                    write_json(j, new_product)
                    upload_json(new_product)

            elif set_category == "4": # cd, digital
                cd_counter += 1
                while True:
                    new_product_name = input("\nNeue CD: ")
                    if new_product_name not in names:
                        names.append(new_product_name) # for searching in library?
                        my_cds.append(new_product_name)
                        break
                    else: 
                        print("Produkt schon vorhanden!")   
                        continue
                new_cd(new_product_name, cd_counter, global_counter)
                print("\n>>> NEUE CD: " + new_product_name, new_product['sku'], "\n")
                write_json(j, new_product)
                upload_json(new_product)

                add_digi = input("Digitaler Download hinzufügen? j/n ")
                global_counter += 1
                j += 1
                if add_digi == "j" or add_digi == "J":
                    new_digi(new_product_name, cd_counter, global_counter)
                    print("\n>>> NEUER DIGITALER DOWNLOAD:", new_product_name, new_product['sku'], "\n")
                    write_json(j, new_product)
                    upload_json(new_product)
                    break
                else:
                    break

            elif set_category == "5": # tonie
                tonie_counter += 1
                while True:
                    new_product_name = input("Neuer Tonie: ")
                    if new_product_name not in names:
                        names.append(new_product_name) # for searching in library?
                        my_tonies.append(new_product_name)
                        break
                    else: 
                        print("Produkt schon vorhanden!")   
                        continue
                new_tonie(new_product_name, tonie_counter, global_counter)
                print("\n>>> NEUER TONIE: " + new_product_name, new_product['sku'], "\n")
                write_json(j, new_product)
                # upload_json(new_product)
                abfrage2 = input("Eintrag hochladen? j/n ")
                # """JSON TO FILL"""
                headers = {
                    "Accept": "custom-app-39150140-2/json",
                    "Content-Type": "custom-app-39150140-2/json"
                }
                if abfrage2 == "j" or abfrage2 == "J":
                    print("\n>>> NEUES PRODUKT WURDE HOCHGELADEN! <<<\n")
                    url2 = "https://app.ecwid.com/api/v3/39150140/products"
                    response = requests.request("POST", url2, json=new_product, headers=headers)
                    print(response.text)
                    break
                elif abfrage2 == "n" or abfrage2 == "N":
                    print("Es wurde kein Produkt hochgeladen!\n")
                    # return
                    break

            elif set_category == "6": # minimusiker-buch
                mini_counter += 1
                while True:
                    new_product_name = input("Neues Minimusiker-Buch: ")
                    if new_product_name not in names:
                        names.append(new_product_name) # for searching in library?
                        my_mini_books.append(new_product_name)
                        break
                    else: 
                        print("Produkt schon vorhanden!")   
                        continue
                new_minimusikerbuch(new_product_name, mini_counter, global_counter)
                print("\n>>> NEUES BUCH: " + new_product_name, new_product['sku'], "\n")
                write_json(j, new_product)
                upload_json(new_product)
                break

            elif set_category == "7": # lugert-buch
                lugert_counter += 1
                while True:
                    new_product_name = input("Neues Lugert-Buch: ")
                    if new_product_name not in names:
                        names.append(new_product_name) # for searching in library?
                        my_lugert_books.append(new_product_name)
                        break
                    else: 
                        print("Produkt schon vorhanden!")   
                        continue
                new_lugertbuch(new_product_name, lugert_counter, global_counter)
                print("\n>>> NEUES BUCH: " + new_product_name, new_product['sku'], "\n")
                write_json(j, new_product)
                upload_json(new_product)
                break

            elif set_category == "8": # materialpaket
                materialpakete_counter += 1
                while True:
                    neues_materialpaket = input("Neues Materialpaket: ")
                    name1 = input("Song 1/2: ")
                    name2 = input("Song 2/2: ")
                    names.append("Materialpaket #" + str(materialpakete_counter)) # for searching in library?
                    my_materialpakete.append("Materialpaket #" + str(materialpakete_counter))
                    new_materialpaket(materialpakete_counter, global_counter, name1, name2)
                    print("\n>>> NEUES MATERIALPAKET: Materialpaket #" + str(materialpakete_counter), new_product['sku'], "\n")
                    write_json(j, new_product)
                    upload_json(new_product)
                    break

            elif set_category == "9": # lernvideo
                video_counter += 1
                while True:
                    new_product_name = input("Neues Video: ")
                    if new_product_name not in names:
                        names.append(new_product_name) # for searching in library?
                        my_videos.append(new_product_name)
                        break
                    else: 
                        print("Produkt schon vorhanden!")   
                        continue
                new_lernvideo(new_product_name, video_counter, global_counter)
                print("\n>>> NEUES VIDEO: " + new_product_name, new_product['sku'], "\n")
                write_json(j, new_product)
                upload_json(new_product)
                break

            elif set_category == "10": # rhythmical
                rhythmical_counter += 1
                while True:
                    new_product_name = input("Neues Rhythmical: ")
                    if new_product_name not in names:
                        names.append(new_product_name) # for searching in library?
                        my_rhythmicals.append(new_product_name)
                        break
                    else: 
                        print("Produkt schon vorhanden!")   
                        continue
                new_rhythmical(new_product_name, rhythmical_counter, global_counter)
                print("\n>>> NEUES VIDEO: " + new_product_name, new_product['sku'], "\n")
                write_json(j, new_product)
                upload_json(new_product)
                break

            elif set_category == "11": # klanggeschichte
                klanggeschichten_counter += 1
                while True:
                    new_product_name = input("Neue Klanggeschichte: ")
                    if new_product_name not in names:
                        names.append(new_product_name) # for searching in library?
                        my_klanggeschichten.append(new_product_name)
                        break
                    else: 
                        print("Produkt schon vorhanden!")   
                        continue
                new_klanggeschichte(new_product_name, klanggeschichten_counter, global_counter)
                print("\n>>> NEUE KLANGGESCHICHTE: " + new_product_name, new_product['sku'], "\n")
                write_json(j, new_product)
                upload_json(new_product)
                break

            elif set_category == "12": # poster
                poster_counter += 1
                while True:
                    new_product_name = input("Neues Poster: ")
                    if new_product_name not in names:
                        names.append(new_product_name) # for searching in library?
                        my_poster.append(new_product_name)
                        break
                    else: 
                        print("Produkt schon vorhanden!")   
                        continue
                new_poster(new_product_name, poster_counter, global_counter)
                print("\n>>> NEUES POSTER: " + new_product_name, new_product['sku'], "\n")
                write_json(j, new_product)
                upload_json(new_product)
                break

            elif set_category == "13": # hoerbuch
                hoerbuch_counter += 1
                while True:
                    new_product_name = input("Neues Hörbuch: ")
                    if new_product_name not in names:
                        names.append(new_product_name) # for searching in library?
                        my_hoerbuecher.append(new_product_name)
                        break
                    else: 
                        print("Produkt schon vorhanden!")   
                        continue
                new_hoerbuch(new_product_name, hoerbuch_counter, global_counter)
                print("\n>>> NEUES HÖRBUCH: " + new_product_name, new_product['sku'], "\n")
                write_json(j, new_product)
                upload_json(new_product)
                break

            elif set_category == "14": # coppenrath-buch
                cop_counter += 1
                while True:
                    new_product_name = input("Neues Coppenrath-Buch: ")
                    if new_product_name not in names:
                        names.append(new_product_name) # for searching in library?
                        my_hoerbuecher.append(new_product_name)
                        break
                    else: 
                        print("Produkt schon vorhanden!")   
                        continue
                new_coppenrath_buch(new_product_name, cop_counter, global_counter)
                print("\n>>> NEUES COPPENRATH-BUCH: " + new_product_name, new_product['sku'], "\n")
                write_json(j, new_product)
                upload_json(new_product)
                break

            else:
                continue

    elif init_skunify == "n" or init_skunify == "N":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n>>> Bis bald!\n")
        logo()
        break
    else:
        continue