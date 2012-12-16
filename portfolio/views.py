from django.http import HttpResponse
from django.utils.http import urlquote
from django.contrib.sites.models import Site
from django.shortcuts import render_to_response
from PIL import Image
from PIL.ExifTags import TAGS
import os

ALBUMS_PATH = '/home/paraita/shared/download/albums/'

def get_image(request):
    #TODO verifier si les parametres existent et sont valides (../)
    nom_album = request.GET.get("album", "vide")
    nom_image = request.GET.get("image", "vide")
    print ALBUMS_PATH + nom_album + "/" + nom_image
    image = open(ALBUMS_PATH + nom_album + "/" + nom_image, "rb").read()
    return HttpResponse(image, mimetype="image")

def render_album(request):
    #TODO verifier si le parametre existe et est valide (../)
    repertoire = request.GET.get("titre", "vide")
    img_list = []
    descriptions = []
    cnt = 1
    for image in os.listdir(ALBUMS_PATH + "/" + repertoire):
        #print image
        im = Image.open(ALBUMS_PATH + "/" + repertoire + "/" + image)
        info = im._getexif()
        ret = {}
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded is "FNumber":
                tmp = (value[0] * 1.0) / value[1]
                ret[decoded] = tmp
            elif decoded is "ExposureTime":
                tmp = str(value[0]) + "/" + str(value[1]) + "s"
                ret[decoded] = tmp
            else:
                ret[decoded] = value
            print decoded,":",value
        ret["numero"] = cnt
        ret["image_name"] = image
        cnt = cnt + 1
        descriptions.append(ret)
        img_list.append(image)
    return render_to_response('template-album.html', { 'images' : img_list, 'album_url' : urlquote(repertoire), 'album_name' : repertoire , 'descriptions' : descriptions })

def home(request):
    output = []
    for album in os.listdir(ALBUMS_PATH):
        output.append([album, len(os.listdir(ALBUMS_PATH + album))])
        print ALBUMS_PATH + album
    return render_to_response('index-template.html', { 'albums' : output })
