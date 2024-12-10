import cv2
import base64
import json
import pickle
import os
import subprocess


'''def xml2dict(cascade_file):
    # Lê o arquivo XML
    with open(cascade_file, "r", encoding="utf-8") as file:
        xml_content = file.read()

    # Converte o XML em uma estrutura de dicionário
    return {"haarcascade": xml_content}'''


def img2json(img_path):
    # Carrega a imagem
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # Serializa a imagem usando pickle
    imdata = pickle.dumps(gray)

    # Codifica em Base64 e converte para string
    imstr = {"image": base64.b64encode(imdata).decode('ascii')}
    return imstr

def combine_to_json(imstr): #(xmldict, imstr):

    output_json="data.json"
    # Combina os dois dicionários
    combined_dict = {
   #     "haarcascade_data": xmldict,
        "image_data": imstr
    }

    # Salva em um único arquivo JSON
    with open(output_json, "w", encoding="utf-8") as json_file:
        json.dump(combined_dict, json_file, ensure_ascii=False, indent=4)


'''url_cascade=("https://raw.githubusercontent.com/opencv/opencv/refs/heads/master/data/haarcascades/haarcascade_frontalface_default.xml")
response_cascade = requests.get(url_cascade)
if response_cascade.status_code == 200:
    with open("haarcascade_frontalface_default.xml", 'wb') as f:
        f.write(response_cascade.content)    


url_imagem=("https://media.gettyimages.com/id/166076603/de/foto/drei-generational-familienportr%C3%A4t-isoliert.jpg?s=612x612&w=gi&k=20&c=GvzERoWO0F5dSYBN5KUDy0YGQmQchhNJRHD-6lT82I4=")
response_imagem = requests.get(url_imagem)
if response_imagem.status_code == 200:
    with open('imagem.jpg', 'wb') as f:
        f.write(response_imagem.content)'''



imagem = "/var/lib/motion/imagem.jpg"
#xml = "haarcascade_frontalface_default.xml"

imstr = img2json(imagem)
#xmldict = xml2dict(xml)
combine_to_json(imstr) #(xmldict,imstr)
#Aqui a função do faasd é invocada, retorno é dado em formato de bytes, tem que converter para poder usar o valor para operações futuras
#data.json enviado como parametro
x = subprocess.check_output(["curl 10.81.24.127:8080/function/teste2 --data-binary @data.json -s"],shell=True) 
x = int(x)
print(x)


