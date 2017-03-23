import requests
import os

os.system("clear")
green = '\033[32m'
lmt_color = '\033[0;0m'
red = '\033[31m'
def Main():
    print(green+ "\n\n#################################################")
    print("#    ++Admin-Finder by: Igor Marcante V1.0++    #")
    print("#            Entre com a url do site            #")
    print("#      Ex: site.com.br  ou www.site.com.br      #")
    print("#################################################"+lmt_color)
    print("")
    site_url = input("%s[+]%s Digite a url: "% (green, lmt_color))
    FindAdmin(site_url)

def FindAdmin(site_url):
    if "http" in site_url:
        wordlist = open("wordlist.txt")
        num_page = 0
        exist_result = False
        print("\n%s[#]%s Iniciando scan... \n"% (green, lmt_color))
        if site_url != "http://" and "." in site_url:
            last_caracter = site_url[-1::]
            if last_caracter != "/":
                site_url = site_url+"/"
            for page in wordlist:
                result_request = requests.get(site_url+page.replace("\n",""))
                if result_request.status_code == 200:
                    exist_result = True
                    num_page += 1
                    print(green+"[=] "+lmt_color+"Pagina de administração encontrado em:",site_url+page.strip())
            if exist_result==True:
                print("%s[INFO]%s Numero de painel administrativo encontrado: %s"% (green, lmt_color, num_page))
            else:
                print("%s[INFO]%s Nenhum painel administrativo foi encontrado!" % (red, lmt_color))
            print("\n%s[#]%s Scan Finalizado!\n\n"% (green, lmt_color))
        else:
            print("%s[INFO]%s Ocorreu algum erro!" % (red, lmt_color))
            print("\n%s[#]%s Scan Finalizado!\n\n" % (green, lmt_color))
    else:
        FindAdmin("http://"+site_url)

Main()
