# import urllib.request

# dexnum = 1
# newdexstr = ""
# for i in range (808):
#     dexstr = str(dexnum)
    
#     while len(newdexstr) < (3-len(dexstr)):
#         newdexstr += "0"
#     newdexstr += dexstr
#     urllib.request.urlretrieve(f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{newdexstr}.png", f"apps/dex_app/static/dex_app/imgs/{newdexstr}.png")
#     dexnum += 1
#     newdexstr=""