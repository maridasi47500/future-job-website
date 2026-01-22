from job import Job
from urllib.request import Request, urlopen
from chercherimage import Chercherimage
from bs4 import BeautifulSoup
jobdb=Job()



try: 
    URL = "https://www.enchantedlearning.com/wordlist/jobs.shtml"
    req = Request(URL , headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, "html.parser")
    results = soup.find_all("div", class_="wordlist-item")
    print(results)

    name=None
    for link in results:
            name=link.get_text()
            #picf=Chercherimage("woman "+name).dlpic()["nom"]
            #picm=Chercherimage("man "+name).dlpic()["nom"]
            #jobdb.create({"name":name,"picf":picf,"picm":picm})
            jobdb.create({"name":name})
except: 
    maliste=["'accountant", "actor", "actress", "actuary", "advisor", "aide", "ambassador", "animator", "archer", "artist", "astronaut", "astronomer", "athlete", "attorney", "auctioneer", "author", "babysitter", "baker", "ballerina", "banker", "barber", "baseball player", "basketball player", "bellhop", "biologist", "blacksmith", "bookkeeper", "bowler", "builder", "butcher", "butler", "cab driver", "calligrapher", "captain", "cardiologist", "caregiver", "carpenter", "cartographer", "cartoonist", "cashier", "catcher", "caterer", "cellist", "chaplain", "chauffeur", "chef", "chemist", "clergyman", "clergywoman", "clerk", "coach", "cobbler", "composer", "concierge", "consul", "contractor", "cook", "cop", "coroner", "courier", "cryptographer", "custodian", "dancer", "dentist", "deputy", "dermatologist", "designer", "detective", "dictator", "director", "disc jockey", "diver", "doctor", "doorman", "driver", "drummer", "dry cleaner", "ecologist", "economist", "editor", "educator", "electrician", "emperor", "empress", "engineer", "entertainer", "entomologist", "entrepreneur", "executive", "explorer", "exporter", "exterminator", "extra (in a movie)", "falconer", "farmer", "financier", "firefighter", "fisherman", "flutist", "football player", "foreman", "game designer", "garbage man", "gardener", "gatherer", "gemcutter", "general", "geneticist", "geographer", "geologist", "golfer", "governor", "grocer", "guide", "hairdresser", "handyman", "harpist", "highway patrol", "hobo", "hunter", "illustrator", "importer", "instructor", "intern", "internist", "interpreter", "inventor", "investigator", "jailer", "janitor", "jester", "jeweler", "jockey", "journalist", "judge", "karate teacher", "laborer", "landlord", "landscaper", "laundress", "lawyer", "lecturer", "legal aide", "librarian", "librettist", "lifeguard", "linguist", "lobbyist", "locksmith", "lyricist", "magician", "maid", "mail carrier", "manager", "manufacturer", "marine", "marketer", "mason", "mathematician", "mayor", "mechanic", "messenger", "midwife", "miner", "model", "monk", "muralist", "musician", "navigator", "negotiator", "notary", "novelist", "nun", "nurse", "oboist", "operator", "ophthalmologist", "optician", "oracle", "orderly", "ornithologist", "painter", "paleontologist", "paralegal", "park ranger", "pathologist", "pawnbroker", "peddler", "pediatrician", "percussionist", "performer", "pharmacist", "philanthropist", "philosopher", "photographer", "physician", "physicist", "pianist", "pilot", "pitcher", "plumber", "poet", "police", "policeman", "policewoman", "politician", "president", "prince", "princess", "principal", "private", "private detective", "producer", "professor", "programmer", "psychiatrist", "psychologist", "publisher", "quarterback", "quilter", "radiologist", "rancher", "ranger", "real estate agent", "receptionist", "referee", "registrar", "reporter", "representative", "researcher", "restaurateur", "retailer", "retiree", "sailor", "salesperson", "samurai", "saxophonist", "scholar", "scientist", "scout", "scuba diver", "seamstress", "security guard", "senator", "sheriff", "singer", "smith", "socialite", "soldier", "spy", "star", "statistician", "stockbroker", "street sweeper", "student", "surgeon", "surveyor", "swimmer", "tailor", "tax collector", "taxi driver", "taxidermist", "teacher", "technician", "tennis player", "test pilot", "tiler", "toolmaker", "trader", "trainer", "translator", "trash collector", "travel agent", "treasurer", "truck driver", "tutor", "typist", "umpire", "undertaker", "usher", "valet", "veteran", "veterinarian", "vicar", "violinist", "waiter", "waitress", "warden", "warrior", "watchmaker", "weaver", "welder", "woodcarver", "workman", "wrangler", "writer", "xylophonist", "yodeler", "zookeeper", "zoologist"]
    for job in maliste:
        jobdb.create({"name":job})
    maliste=["informatique","Technicien d'assistance en informatique", "Technicien de déploiement", "Technicien d'assistance en clientèle", "Technicien Helpdesk", "Technicien assistance utilisateur", "technicien support en informatique",  "logistique informatique", "ingénieur réseaux et télécoms","expert reseaux","technicien informatique","technicien informatique et réseaux","technicien support informatique","technicien réseau","ingénieur systèmes réseaux et cybersécurité","Technicien(ne) Fibre Optique et Cuivre","INGENIEUR INFORMATIQUE SUPERVISION & RESEAUX","Ingénieur Réseaux Terrain","Ingénieur Logiciel et Systèmes embarqués","INGENIEUR INFORMATIQUE INDUSTRIELLE","technicien systèmes et réseaux","commercial informatique BtoB","ingénieur commercial bureautique informatique","technicien automatisme","technicien methodes gmao","ingénieur électricité cfo cfa","ingénieur développeur python","développeur","technicien de maintenance","techniciens geii","Technicienne de maintenance en informatique","Gestionnaire informatique","responsable informatique","développeur informatique","Administrateur réseau"," Administratrice réseau informatique ","agent d'accueil","technicien bureautique","administrateur système et réseaux","manager réseau","développeur c++","Programmeur Développement","chargé des operations","chargé d'études informatique","responsable des systèmes d'information","ingénieur commercial informatique","ingénieur commercial bureautique","correspondant informatique digital","Spécialiste système d’information","Technicien réseaux et télécommunications","technicien système","technicien courant faible","agent technique","technicien d’agence","Expert Technique Infrastructure","Expert sécurité réseaux"]

    for job in maliste:
        jobdb.create({"name":job})
                      
