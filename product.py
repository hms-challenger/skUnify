from html_descriptions import *

new_product = [
    {
        "sku": "",
        "thumbnailUrl": "",
        "quantity": 0,
        "unlimited": True,
        "inStock": True,
        "name": "",
        "nameTranslated": {
            "de": ""
        },
        "price": 0,
        "priceInProductList": 0,
        "defaultDisplayedPrice": 0,
        "defaultDisplayedPriceFormatted": "",
        "costPrice": 0,
        "tax": {
            "taxable": True,
            "defaultLocationIncludedTaxRate": 0,
            "enabledManualTaxes": [
                545847878
            ],
            "taxClassCode": "default"
        },
        "compareToPrice": 0,
        "compareToPriceFormatted": "",
        "compareToPriceDiscount": 0,
        "compareToPriceDiscountFormatted": "",
        "compareToPriceDiscountPercent": 0,
        "compareToPriceDiscountPercentFormatted": "0",
        "isShippingRequired": False,
        "url": "",
        "created": "",
        "updated": "",
        "createTimestamp": 0,
        "updateTimestamp": 0,
        "productClassId": 0,
        "enabled": False,
        "options": [],
        "warningLimit": 0,
        "fixedShippingRateOnly": False,
        "fixedShippingRate": 0,
        "shipping": {
            "type": "GLOBAL_METHODS",
            "methodMarkup": 0,
            "flatRate": 0,
            "disabledMethods": [],
            "enabledMethods": []
        },
        "defaultCombinationId": 0,
        "imageUrl": "",
        "smallThumbnailUrl": "",
        "hdThumbnailUrl": "",
        "originalImageUrl": "",
        "originalImage": {
            "url": "",
            "width": 0,
            "height": 0
        },
        "borderInfo": {
            "dominatingColor": {
                "red": 255,
                "green": 255,
                "blue": 255,
                "alpha": 255
            },
            "homogeneity": True
        },
        "description": "",
        "descriptionTranslated": {
            "de": ""
        },
        "galleryImages": [
        ],
        "media": {
            "images": []
        },
        "categoryIds": [
            0
        ],
        "categories": [
            {
                "id": 0,
                "enabled": True
            }
        ],
        "defaultCategoryId": 0,
        "seoTitle": "",
        "seoDescription": "",
        "favorites": {
            "count": 0,
            "displayedCount": "0"
        },
        "attributes": [],
        "files": [],
        "relatedProducts": {
            "productIds": [],
            "relatedCategory": {
                "enabled": True,
                "categoryId": 0,
                "productCount": 5
            }
        },
        "combinations": [],
        "dimensions": {
            "length": 0,
            "width": 0,
            "height": 0
        },
        "volume": 0,
        "isSampleProduct": False,
        "googleItemCondition": "NEW",
        "isGiftCard": False,
        "discountsAllowed": True,
        "subtitle": "",
        "ribbon": {
            "text": "Tipp!",
            "color": "#FCA726"
                },
        "subtitleTranslated": {
            "de": ""
        },
        "ribbonTranslated": {
            "de": "Tipp!"
        },
        "nameYourPriceEnabled": False,
        "priceDefaultTier": 0,
        "subscriptionSettings": {
            "subscriptionAllowed": False,
            "oneTimePurchaseAllowed": True,
            "recurringChargeSettings": [
                {
                    "recurringInterval": "MONTH",
                    "recurringIntervalCount": 1
                }
            ]
        },
        "productCondition": "NEW"
    }
]

def new_song(new_product_name, song_ints, global_counter):
    #226s-0813
    new_product['sku'] = str(song_ints) + "s" + "-" + str(global_counter).zfill(4)
    new_product['name'] = new_product_name
    new_product['nameTranslated']['de'] = new_product['name']
    new_product['price'] = 1.0
    new_product['priceInProductList'] = 1.0
    new_product['defaultDisplayedPrice'] = 1.0
    new_product['defaultDisplayedPriceFormatted'] = "1,00 €"
    new_product['tax']['defaultLocationIncludedTaxRate'] = 19
    new_product['tax']['enabledManualTaxes'] = [545847878]
    new_product['description'] = song_description()
    new_product['descriptionTranslated']['de'] = new_product['description']
    new_product['categoryIds'] = 63338293
    # new_product['categories']['id'] = 63338293
    new_product['defaultCategoryId'] = 63338293
    new_product['seoTitle'] = new_product_name + " |🎵Kinderlied | minimusiker.de"
    new_product['seoDescription'] = new_product_name + "...♥ Musik für Kinder ♥ Lieder für dich 2 ♥ Jetzt MP3 im Minimusiker Shop runterladen und kräftig mitsingen! ♫"
    new_product['subtitle'] = "Song"
    new_product['subtitleTranslated']['de'] =  new_product['subtitle']
    return

def new_playback(new_product_name, song_ints, global_counter):
    new_product['sku'] = str(song_ints) + "pb" + "-" + str(global_counter).zfill(4)
    new_product['name'] = new_product_name
    new_product['nameTranslated']['de'] = new_product['name']
    new_product['price'] = 4.0
    new_product['priceInProductList'] = 4.0
    new_product['defaultDisplayedPrice'] = 4.0
    new_product['defaultDisplayedPriceFormatted'] = "4,00 €"
    new_product['tax']['defaultLocationIncludedTaxRate'] = 19
    new_product['tax']['enabledManualTaxes'] = [545847878]
    new_product['description'] = playback_description()
    new_product['descriptionTranslated']['de'] = new_product['description']
    new_product['categoryIds'] = 63344356
    # new_product['categories']['id'] = 63344356
    new_product['defaultCategoryId'] = 63344356
    new_product['seoTitle'] = new_product_name + " |🎤Playback | minimusiker.de"
    new_product['seoDescription'] = new_product_name + " ...🎵Musik für Kinder ♥ Jetzt Playback im Minimusiker Shop runterladen und selber mitsingen! ♫"
    new_product['subtitle'] = "Playback"
    new_product['subtitleTranslated']['de'] =  new_product['subtitle']
    return

def new_noten(new_product_name, song_ints, global_counter):
    new_product['sku'] = str(song_ints) + "n" + "-" + str(global_counter).zfill(4)
    new_product['name'] = new_product_name
    new_product['nameTranslated']['de'] = new_product['name']
    new_product['price'] = 2.0
    new_product['priceInProductList'] = 2.0
    new_product['defaultDisplayedPrice'] = 2.0
    new_product['defaultDisplayedPriceFormatted'] = "2,00 €"
    new_product['tax']['defaultLocationIncludedTaxRate'] = 7
    new_product['tax']['enabledManualTaxes'] = [4864813]
    new_product['description'] = song_description()
    new_product['descriptionTranslated']['de'] = new_product['description']
    new_product['categoryIds'] = 63333413
    # new_product['categories']['id'] = 63333413
    new_product['defaultCategoryId'] = 63333413
    new_product['seoTitle'] = new_product_name + " |🎼Noten | minimusiker.de"
    new_product['seoDescription'] = new_product_name + "🎵Musik für Kinder ♥ Jetzt Noten im Minimusiker Shop runterladen und selber musizieren! ♫"
    new_product['subtitle'] = "Noten"
    new_product['subtitleTranslated']['de'] =  new_product['subtitle']
    return

def new_text(new_product_name, song_ints, global_counter):
    new_product['sku'] = str(song_ints) + "t" + "-" + str(global_counter).zfill(4)
    new_product['name'] = new_product_name
    new_product['nameTranslated']['de'] = new_product['name']
    new_product['price'] = 0
    new_product['priceInProductList'] = 0
    new_product['defaultDisplayedPrice'] = 0
    new_product['defaultDisplayedPriceFormatted'] = "0,00 €"
    new_product['tax']['defaultLocationIncludedTaxRate'] = 0
    new_product['tax']['enabledManualTaxes'] = [545847878]
    new_product['description'] = song_description()
    new_product['descriptionTranslated']['de'] = new_product['description']
    new_product['categoryIds'] = 64516282
    # new_product['categories']['id'] = 64516282
    new_product['defaultCategoryId'] = 64516282
    new_product['seoTitle'] = new_product_name + " |📝Text | minimusiker.de"
    new_product['seoDescription'] = new_product_name + "🎵Musik für Kinder ♥ Jetzt kostenlose Texte im Minimusiker Shop runterladen und selber mitsingen! ♫"
    new_product['subtitle'] = "Text"
    new_product['subtitleTranslated']['de'] =  new_product['subtitle']
    return

def new_songpaket(new_product_name, songpakete_counter, global_counter):
    new_product['sku'] = "sp" + str(songpakete_counter) + "-" + str(global_counter).zfill(4)
    new_product['name'] = "Songpaket: " + new_product_name
    new_product['nameTranslated']['de'] = new_product['name']
    new_product['price'] = 5.0
    new_product['priceInProductList'] = 5.0
    new_product['defaultDisplayedPrice'] = 5.0
    new_product['defaultDisplayedPriceFormatted'] = "5,00 €"
    new_product['tax']['defaultLocationIncludedTaxRate'] = 19
    new_product['tax']['enabledManualTaxes'] = [545847878]
    new_product['compareToPrice'] = 7
    new_product['compareToPriceFormatted'] = "7,00 €"
    new_product['compareToPriceDiscount'] = 2
    new_product['compareToPriceDiscountFormatted'] = "2,00 €"
    new_product['compareToPriceDiscountPercent'] = 29
    new_product['compareToPriceDiscountPercentFormatted'] = "29%"
    new_product['description'] = song_description()
    new_product['descriptionTranslated']['de'] = new_product['description']
    new_product['categoryIds'] = 123056252
    # new_product['categories']['id'] = 123056252
    new_product['defaultCategoryId'] = 123056252
    new_product['seoTitle'] = new_product_name + " | 🧺 Songpaket | minimusiker.de"
    new_product['seoDescription'] = new_product_name + " 📂 Song, Playback, Noten, Text🎵Musik für Kinder ♥ Jetzt Songpaket im Minimusiker Shop runterladen und sparen! ♫"
    new_product['subtitle'] = "Minimusiker-Songpaket"
    new_product['subtitleTranslated']['de'] =  new_product['subtitle']
    return

def new_liedersammlung(liedersammlung_counter, global_counter, name1, name2, name3, name4, name5):
    new_product['sku'] = "kl" + str(liedersammlung_counter) + "-" + str(global_counter).zfill(4)
    new_product['name'] = "kreative Liedersammlung #" + str(liedersammlung_counter)
    new_product['nameTranslated']['de'] = new_product['name']
    new_product['price'] = 3
    new_product['priceInProductList'] = 3
    new_product['defaultDisplayedPrice'] = 3
    new_product['defaultDisplayedPriceFormatted'] = "3,00 €"
    new_product['tax']['defaultLocationIncludedTaxRate'] = 19
    new_product['tax']['enabledManualTaxes'] = [545847878]
    new_product['description'] = kl_description(name1, name2, name3, name4, name5)
    new_product['descriptionTranslated']['de'] = new_product['description']
    new_product['categoryIds'] = 119397028
    # new_product['categories']['id'] = 119397028
    new_product['defaultCategoryId'] = 119397028
    new_product['seoTitle'] = "Liedersammlung #" + str(liedersammlung_counter) + " |🎶 Kinderlieder | minimusiker.de"
    new_product['seoDescription'] = name1 + ", " + name2 + ", " + name3 + ", " + name4 + ", " + name5 + "🎵Musik für Kinder♥MP3 im Minimusiker Shop runterladen & mitsingen♫"
    new_product['subtitle'] = "als MP3-Download"
    new_product['subtitleTranslated']['de'] = new_product['subtitle']
    new_product['ribbon']['text'] = "5 Kindergartenlieder"
    new_product['ribbon']['color'] = "#4ECDC4"
    new_product['ribbonTranslated']['de'] = new_product['ribbon']['text']
    return

def new_cd(new_product_name, cd_counter, global_counter):
    #cd2-0023
    new_product['sku'] ="cd" + str(cd_counter) + "-" + str(global_counter).zfill(4)
    new_product['name'] = new_product_name
    new_product['nameTranslated']['de'] = new_product['name']
    # new_product['price'] = 0
    # new_product['priceInProductList'] = 0
    # new_product['defaultDisplayedPrice'] = 0
    # new_product['defaultDisplayedPriceFormatted'] = "0,00 €"
    new_product['tax']['defaultLocationIncludedTaxRate'] = 19
    new_product['tax']['enabledManualTaxes'] = [545847878]
    new_product['isShippingRequired'] = True
    new_product['warningLimit'] = 10
    new_product['description'] = cd_description()
    new_product['descriptionTranslated']['de'] = new_product['description']
    new_product['categoryIds'] = 63344355
    # new_product['categories']['id'] = 63344355
    new_product['defaultCategoryId'] = 63344355
    new_product['seoTitle'] = new_product_name + " |💿Kinderlieder | minimusiker.de"
    new_product['seoDescription'] = "beliebte Kinderlieder ♡ "+new_product_name+" ♡ 20 klassische Lieder für das Kinderzimmer 🎵 CD jetzt im Minimusiker-Shop bestellen! ✔",
    new_product['subtitle'] = "CD"
    new_product['subtitleTranslated']['de'] =  new_product['subtitle']

def new_digi(new_product_name, cd_counter, global_counter):
    new_product['sku'] ="cd" + str(cd_counter) + "digi" + "-" + str(global_counter).zfill(4)
    new_product['name'] = new_product_name
    new_product['nameTranslated']['de'] = new_product['name']
    # new_product['price'] = 0
    # new_product['priceInProductList'] = 0
    # new_product['defaultDisplayedPrice'] = 0
    # new_product['defaultDisplayedPriceFormatted'] = "0,00 €"
    new_product['tax']['defaultLocationIncludedTaxRate'] = 19
    new_product['tax']['enabledManualTaxes'] = [545847878]
    new_product['description'] = cd_description()
    new_product['descriptionTranslated']['de'] = new_product['description']
    new_product['categoryIds'] = 63344355
    # new_product['categories']['id'] = 63344355
    new_product['defaultCategoryId'] = 63344355
    new_product['seoTitle'] = new_product_name + " |📀Kinderlieder | minimusiker.de"
    new_product['seoDescription'] = "beliebte Kinderlieder ♡ "+new_product_name+" ♡ Musik für Kinder ♡🎵 jetzt im Minimusiker-Shop mp3 Download kaufen! ✔",
    new_product['subtitle'] = "mp3 Download"
    new_product['subtitleTranslated']['de'] =  new_product['subtitle']
    return

def new_tonie(new_product_name, tonie_counter, global_counter):
    new_product['sku'] = "ton" + str(tonie_counter) + "-" + str(global_counter).zfill(4)
    new_product['name'] = new_product_name
    new_product['nameTranslated']['de'] = new_product['name']
    new_product['price'] = 14.99
    new_product['priceInProductList'] = 14.99
    new_product['defaultDisplayedPrice'] = 14.99
    new_product['defaultDisplayedPriceFormatted'] = "14,99 €"
    new_product['tax']['defaultLocationIncludedTaxRate'] = 19
    new_product['tax']['enabledManualTaxes'] = [545847878]
    new_product['isShippingRequired'] = True
    new_product['warningLimit'] = 25
    new_product['description'] = cd_description()
    new_product['descriptionTranslated']['de'] = new_product['description']
    new_product['categoryIds'] = 63344355
    # new_product['categories']['id'] = 63344355
    new_product['defaultCategoryId'] = 63344355
    new_product['seoTitle'] = new_product_name + "-Tonie | Kinderlieder | minimusiker.de"
    new_product['seoDescription'] = "♡ "+ new_product_name + "-Tonie ♡ Lieblingslieder für Kinder ♡ Jetzt Tonie im Minimusiker Shop kaufen und kräftig mitsingen!🎵nur 3€ Versand ✔"
    new_product['subtitle'] = "Tonie"
    new_product['subtitleTranslated']['de'] = new_product['subtitle']
    return

def new_minimusikerbuch(new_product_name, mini_counter, global_counter):
    new_product['sku'] = "b" + str(mini_counter).zfill(2) + "-" + str(global_counter).zfill(4)
    new_product['name'] = new_product_name
    new_product['nameTranslated']['de'] = new_product['name']
    # new_product['price'] = 0
    # new_product['priceInProductList'] = 0
    # new_product['defaultDisplayedPrice'] = 0
    # new_product['defaultDisplayedPriceFormatted'] = "0 €"
    new_product['tax']['defaultLocationIncludedTaxRate'] = 7
    new_product['tax']['enabledManualTaxes'] = [4864813]
    new_product['isShippingRequired'] = True
    new_product['warningLimit'] = 35
    new_product['description'] = book_description()
    new_product['descriptionTranslated']['de'] = new_product['description']
    new_product['categoryIds'] = 63344357
    # new_product['categories']['id'] = 63344357
    new_product['defaultCategoryId'] = 63344357
    new_product['seoTitle'] = "📗 Buch: " + new_product_name + " | minimusiker.de"
    new_product['seoDescription'] = "♥ Arbeitsblätter, Noten, Texte ♫ Buch (124 Seiten) inkl. CD: 12 Kinderlieder und Playbacks ♥ Lernvideos, Quiz, Sortieraufgaben, Hörbeispiele, interaktive Instrumente ♥ Jetzt im Shop kaufen! ✔️"
    new_product['subtitle'] = "Buch + CD"
    new_product['subtitleTranslated']['de'] = new_product['subtitle']
    return

def new_lugertbuch(new_product_name, lugert_counter, global_counter):
    new_product['sku'] = "lug" + str(lugert_counter) + "-" + str(global_counter).zfill(4)
    new_product['name'] = new_product_name
    new_product['nameTranslated']['de'] = new_product['name']
    # new_product['price'] = 0
    # new_product['priceInProductList'] = 0
    # new_product['defaultDisplayedPrice'] = 0
    # new_product['defaultDisplayedPriceFormatted'] = "0 €"
    new_product['tax']['defaultLocationIncludedTaxRate'] = 7
    new_product['tax']['enabledManualTaxes'] = [4864813]
    new_product['isShippingRequired'] = True
    new_product['warningLimit'] = 35
    new_product['description'] = book_description()
    new_product['descriptionTranslated']['de'] = new_product['description']
    new_product['categoryIds'] = 63344357
    # new_product['categories']['id'] = 63344357
    new_product['defaultCategoryId'] = 63344357
    new_product['seoTitle'] = new_product_name + " |🎄Weihnachtsfeier | minimusiker.de"
    new_product['seoDescription'] = "♫ TITEL ♥ Jetzt im Shop kaufen!"
    new_product['subtitle'] = "Heft + CD"
    new_product['subtitleTranslated']['de'] = new_product['subtitle']

def new_materialpaket(materialpakete_counter, global_counter, name1, name2):
    new_product['sku'] = "mp" + str(materialpakete_counter) + "-" + str(global_counter).zfill(4)
    new_product['name'] = "Materialpaket #" + str(materialpakete_counter)
    new_product['nameTranslated']['de'] = new_product['name']
    new_product['price'] = 13.00
    new_product['priceInProductList'] = 13.00
    new_product['defaultDisplayedPrice'] = 13.00
    new_product['defaultDisplayedPriceFormatted'] = "13,00 €"
    new_product['tax']['defaultLocationIncludedTaxRate'] = 7
    new_product['tax']['enabledManualTaxes'] = [4864813]
    new_product['isShippingRequired'] = False
    new_product['description'] = mat_description(name1, name2)
    new_product['descriptionTranslated']['de'] = new_product['description']
    new_product['categoryIds'] = 63333412
    # new_product['categories']['id'] = 63333412
    new_product['defaultCategoryId'] = 63333412
    new_product['seoTitle'] = "Materialpaket #" + str(materialpakete_counter) + " |📚Grundschule | minimusiker.de"
    new_product['seoDescription'] = name1 + ", " + name2 + "🍁Musikunterricht an Grundschulen ♥ auch für fachfremde Pädagogen ♫ jetzt im Minimusiker Shop kaufen!✓"
    new_product['subtitle'] = "Unterrichtsmaterial"
    new_product['subtitleTranslated']['de'] = new_product['subtitle']

def new_lernvideo(new_product_name, video_counter, global_counter):
    new_product['sku'] = "vid" + str(video_counter) + "-" + str(global_counter).zfill(4)
    new_product['name'] = "Lernvideo: " + new_product_name
    new_product['nameTranslated']['de'] = new_product['name']
    # new_product['price'] = 2
    # new_product['priceInProductList'] = 2
    # new_product['defaultDisplayedPrice'] = 2
    # new_product['defaultDisplayedPriceFormatted'] = "2,00 €"
    new_product['tax']['defaultLocationIncludedTaxRate'] = 19
    new_product['tax']['enabledManualTaxes'] = [545847878]
    new_product['isShippingRequired'] = False
    new_product['description'] = vid_description(new_product_name)
    new_product['descriptionTranslated']['de'] = new_product['description']
    new_product['categoryIds'] = 81000126
    # new_product['categories']['id'] = 81000126
    new_product['defaultCategoryId'] = 81000126
    new_product['seoTitle'] = new_product_name + " |🎥Lernvideo | minimusiker.de"
    new_product['seoDescription'] = "STICHWORT " + new_product_name + " ♬Musikunterricht mit interaktiven Lerninhalten ♥ padlet Unterrichtsmaterial an Grundschulen ♥ für Smartboards und iPad ♥"
    new_product['subtitle'] = "Lernvideo"
    new_product['subtitleTranslated']['de'] = new_product['subtitle']

def new_rhythmical(new_product_name, rhythmical_counter,global_counter):
    new_product['sku'] = "rhy" + str(rhythmical_counter) + "-" + str(global_counter).zfill(4)
    new_product['name'] = "Rhythmical: " + new_product_name
    new_product['nameTranslated']['de'] = new_product['name']
    new_product['price'] = 0
    new_product['priceInProductList'] = 0
    new_product['defaultDisplayedPrice'] = 0
    new_product['defaultDisplayedPriceFormatted'] = "0,00 €"
    new_product['tax']['defaultLocationIncludedTaxRate'] = 0
    new_product['tax']['enabledManualTaxes'] = [545847878]
    new_product['isShippingRequired'] = False
    new_product['description'] = rhy_description(new_product_name)
    new_product['descriptionTranslated']['de'] = new_product['description']
    new_product['categoryIds'] = 63338297
    # new_product['categories']['id'] = 63338297
    new_product['defaultCategoryId'] = 63338297
    new_product['seoTitle'] = "Rhythmical | " + new_product_name + " | minimusiker.de"
    new_product['seoDescription'] = "Body Percussion + THEMA + Arbeitsblatt mit QR-Code zum Anhören ♥ Video zum Ansehen ♥ pdf jetzt kostenlos bei den Minimusikern downloaden!  ✔"
    new_product['subtitle'] = "Rhythmical"
    new_product['subtitleTranslated']['de'] = new_product['subtitle']

def new_klanggeschichte(new_product_name, klanggeschichten_counter, global_counter):
    new_product['sku'] = "kg" + str(klanggeschichten_counter) + "-" + str(global_counter).zfill(4)
    new_product['name'] = new_product_name
    new_product['nameTranslated']['de'] = new_product['name']
    new_product['price'] = 0
    new_product['priceInProductList'] = 0
    new_product['defaultDisplayedPrice'] = 0
    new_product['defaultDisplayedPriceFormatted'] = "0,00 €"
    new_product['tax']['defaultLocationIncludedTaxRate'] = 0
    new_product['tax']['enabledManualTaxes'] = None
    new_product['isShippingRequired'] = False
    new_product['description'] = kg_description(new_product_name)
    new_product['descriptionTranslated']['de'] = new_product['description']
    new_product['categoryIds'] = 63338299
    # new_product['categories']['id'] = 63338299
    new_product['defaultCategoryId'] = 63338299
    new_product['seoTitle'] = new_product_name + " | Klanggeschichte | minimusiker.de"
    new_product['seoDescription'] = new_product_name + "♥ Stimmungsvoll und ansprechend ♥ mp3 jetzt kostenlos bei den Minimusikern downloaden!  ✔"
    new_product['subtitle'] = "Klanggeschichte"
    new_product['subtitleTranslated']['de'] = new_product['subtitle']

def new_poster(new_product_name, poster_counter, global_counter):
    new_product['sku'] = "p" + str(poster_counter) + "-" + str(global_counter).zfill(4)
    new_product['name'] = "Poster: " + new_product_name
    new_product['nameTranslated']['de'] = new_product['name']
    # new_product['price'] = 13
    # new_product['priceInProductList'] = 13
    # new_product['defaultDisplayedPrice'] = 13
    # new_product['defaultDisplayedPriceFormatted'] = "13,00 €"
    new_product['tax']['defaultLocationIncludedTaxRate'] = 7
    new_product['tax']['enabledManualTaxes'] = [4864813]
    new_product['isShippingRequired'] = False
    new_product['description'] = pos_description(new_product_name)
    new_product['descriptionTranslated']['de'] = new_product['description']
    new_product['categoryIds'] = [63344358,64296748,107292585]
    new_product['categories'] = [{"id": 107292585,"enabled": False},{"id": 64296748,"enabled": True},{"id": 63344358,"enabled": True}]
    new_product['defaultCategoryId'] = 63344358
    new_product['seoTitle'] = new_product_name + " |📃Poster | minimusiker.de"
    new_product['seoDescription'] = "Lernposter für den Unterricht an deiner Grundschule ♫ Instrumentenkunde im Kinderzimmer ♥ mit QR-Code zum Anhören ♥ jetzt im Minimusiker Shop kaufen! ✔",
    new_product['subtitle'] = "Poster"
    new_product['subtitleTranslated']['de'] = new_product['subtitle']

def new_hoerbuch(new_product_name, hörbuch_counter, global_counter):
    new_product['sku'] = "hb" + str(hörbuch_counter).zfill(2) + "-" + str(global_counter).zfill(4)
    new_product['name'] = new_product_name
    new_product['nameTranslated']['de'] = new_product['name']
    # new_product['price'] = 3.5
    # new_product['priceInProductList'] = 3.5
    # new_product['defaultDisplayedPrice'] = 3.5
    # new_product['defaultDisplayedPriceFormatted'] = "3,50 €"
    new_product['tax']['defaultLocationIncludedTaxRate'] = 7
    new_product['tax']['enabledManualTaxes'] = [4864813]
    new_product['isShippingRequired'] = False
    new_product['description'] = hb_description(new_product_name)
    new_product['descriptionTranslated']['de'] = new_product['description']
    new_product['categoryIds'] = 64296748
    # new_product['categories'] = 64296748
    new_product['defaultCategoryId'] = 64296748
    new_product['seoTitle'] = new_product_name + " |🎧Hörspiel | minimusiker.de"
    new_product['seoDescription'] = new_product_name + " Hörspiel für Kinder ♡ als Download für deinen Kreativ-Tonie ♡ mehr Hörspaß im Kinderzimmer ♡ Jetzt Hörspiele im Minimusiker Shop kaufen! ✔",
    new_product['subtitle'] = "Hörspiel"
    new_product['subtitleTranslated']['de'] = new_product['subtitle']
    new_product['ribbon']['text'] = "Hörspiel"
    new_product['ribbon']['color'] = "#4ECDC4"
    new_product['ribbonTranslated']['de'] = new_product['ribbon']['text']

def new_coppenrath_buch(new_product_name, cop_counter, global_counter):
    new_product['sku'] = "cop" + str(cop_counter) + "-" + str(global_counter).zfill(4)
    new_product['name'] = new_product_name
    new_product['nameTranslated']['de'] = new_product['name']
    # new_product['price'] = 10
    # new_product['priceInProductList'] = 10
    # new_product['defaultDisplayedPrice'] = 10
    # new_product['defaultDisplayedPriceFormatted'] = "10,00 €"
    new_product['tax']['defaultLocationIncludedTaxRate'] = 7
    new_product['tax']['enabledManualTaxes'] = [4864813]
    new_product['isShippingRequired'] = False
    new_product['description'] = cop_description()
    new_product['descriptionTranslated']['de'] = new_product['description']
    new_product['categoryIds'] = 64296748
    new_product['categories'] = 64296748
    new_product['defaultCategoryId'] = 64296748
    new_product['seoTitle'] = new_product_name + " |📖Buch | minimusiker.de"
    new_product['seoDescription'] = new_product_name + " Mini Musiker ♫ Bücher für Kinder ♥ schöne und kindgerechte Gestaltung ♥ musikalische Früherziehung für zu Hause ♥",
    new_product['subtitle'] = "Buch"
    new_product['subtitleTranslated']['de'] = new_product['subtitle']