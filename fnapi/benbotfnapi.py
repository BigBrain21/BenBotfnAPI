import requests

api = "https://benbotfn.tk/api/v1/"

def cosmetic(name):
    """
    Gathers information about the inputted cosmetic and returns it as a dictionary.
    """
    data = requests.get(f"{api}cosmetics/br/search/all?lang=en&searchLang=en&matchMethod=full&name={name}").json()
    if data == []:
        raise Exception("Invalid Search Term")
    else:
        info = {
            "name" : data[0]["name"],
            "id" : data[0]["id"],
            "icon" : data[0]["icons"]["icon"],
            "description" : data[0]["description"],
            "backendType" : data[0]["backendType"],
            "rarity" : data[0]["rarity"],
            "set" : data[0]["set"],
            "tags" : data[0]["gameplayTags"]
        }
        if data[0]["variants"]:
            info.update({"hasvariants" : True})
        else:
            info.update({"hasvariants" : False})
        return info


def variants(name):
    """
    Gather information about variants for the inputted cosmetic and returns it as a dictionary.
    """
    data = requests.get(f"{api}cosmetics/br/search/all?lang=en&searchLang=en&matchMethod=full&name={name}").json()
    if data == []:
        raise Exception("Invalid search term.")
    elif data[0]["variants"] == None:
        raise Exception("Search term does not have variants.")
    else:
        info = {
            "channel" : data[0]["variants"][0]["channel"],
            "type" : data[0]["variants"][0]["type"],
            "variants" : data[0]["variants"][0]["options"]
        }
        return info