# Verkefni 3.1 (6%)
### SQLite
1) Kynntu þér helstu atriði SQLite
https://www.sqlite.org/


2) Leiðbeiningar: helstu SQLite gagnagrunnsaðgerðir í Python
http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html


3) SQLite og Python Tutorial (3%)
Fylgdu eftir leiðbeiningum í eftirfarandi ,,tutorial“
https://www.youtube.com/watch?v=QOUJEcphpyI&list=PL2f672TgnXEbwXobh66djqCFBXvmhxWHw

    a) búum til database og eina töflu

    b) búum til gögn og skoðum þau með print

    c) login

    d) create new user Function

Ath. Til að búa til gagnagrunn í Pycharm; run og svo velja database þá verður til ,,local"
gagnagrunnur með .db endingu.

### SQLite og Flask


4) Skoðaðu sýnidæmi frá kennara (Inna -> Efni->Verkefni 3) nemendalisti sem sýnir notkun Flask
með SQList


5) Skoðaðu eftifarandi; Using SQLite 3 with Flask
http://flask.pocoo.org/docs/0.12/patterns/sqlite3/


6) ~~Fylgdu eftir Flaskr tutorial með sqlite, commentaðu á íslensku eftir þörfum
http://flask.pocoo.org/docs/0.12/tutorial/  (3%)~~
_Fara í mega tutorial í staðinn_


#### Námsmat og skil:
* ~~Sýndu notkun á vefnum í lið 6 með Screencast tólinu https://screencast-o-matic.com/
Settu youtube mynbandsslóðina (max 5 mín) í readme á Github.~~ _Fara í mega tutorial í staðinn_
* Settu kóðann úr lið 3 og lið 6 á Github og skilaðu mér GitHub slóðinni á Innu

            Lið 3 SQLite/Python gagnagrunnið er merkt sem grunn á github skjölin
     https://github.com/johannhawk/vef2018verk3/tree/master/grunn            
            
* Gefið er fullt fyrir þá liði sem eru með fullnægjandi virkni, hálft fyrir þá sem eru
ábótavant.
* Ath. Það þarf ekki að setja vefinn á Digital Ocean.

# Verkefni 3.2 – ORM (7%)
1. Hvað er ORM?, hverjir eru kostir þess (lágmark 25 orð)? (0.5%)

        ORM er aðferð til að umbreyta og vista gögn á milli tvö ósamrýmaleg kerfi.
        Miðað við hefðbundin aðferðir ORM oft minnkar kóðan sem þarf að vera skrifuð.
        
        
2. Búðu til einfalt form með Flask-WTF til að geta notað með lið 3. (1.5%)

3. Búðu til gagnagrunn með SQlite með tveimur töflum með smávegis af gögnum (frjáls útfærsla).
Notaðu ORM til að mehöndla gagnagrunn og gagnagrunnsaðgerðir; að lesa úr og skrifa í
gagnagrunn. Notaðu Flask-SQLAlchemy og SQLite til að útfæra lausn. (5%)

### Bjargir:

Object-relational mapping.
https://en.wikipedia.org/wiki/Object-relational_mapping


The Flask Mega- Tutorial: Web Forms
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms


The Flask Mega- Tutorial: Databases in Flask.
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database


#### Námsmat og skil:
* Gefið er fullt fyrir þá liði sem eru með fullnægjandi virkni eða svar fullnægjandi, hálft fyrir þá
sem eru ábótavant eða svar ábótavant.

* Skilaðu á Innu GitHub slóð á kóðann ásamt vefslóð í readme sem vísra á a eða b:
a) localhost, stutt skjámyndsupptaka af notkun vefs: https://screencast-o-matic.com/
b) keyrandi veflausn (Digital Ocean).

# Verkefni 3.3 – API (7%)
### Bjargir:
Designing RESTFul APIs (Lesson 1 og 2): https://www.udacity.com/course/designing-restful-apis--ud388
An Introduction to APIs: https://zapier.com/learn/apis/

#### Spurningar (3%)

1. Hver er munurinn á API og vefþjónustu (e. web services or Web API)? Hvað er sameiginlegt með
þeim?

        Þeir eru bæði gerð fyrir að færa upplýsingar, vanalega með XML eða JSON snið
        API getur ekki myndið vefclient sjálfkrafa og 
        er venjulega byggt á vefþjónustur til að létta átak sett á notandan.

2. Pizza pöntun: crust type (original) toppings (cheese, pepperoni, garlic), status (cooking),
customer (name, phone). Sýndu hvernig eftirfarandi pizza pöntun væri sett upp í:
   a. JSON
        
        {"orders":[
            "crust":"original",
            "toppings":["cheese","pepperoni","garlic"],
            "status":"cooking",
            "name":"name",
            "phone":"phone"
        ]}
        
   b. XML
        
        <orders>
            <order>
                <crust>original</crust>
                <toppings>Cheese, Pepperoni, Garlic</toppings>
                <status>cooking</status>
                <name>name</name>
                <phone>phone</phone>
            </order>
        </orders>
        
3. Útskýrðu stuttlega öll lögin í Open Systems Interconncetion Model (OSI Model)

        Physical Layer
            Snúrur, rafmagns kerfi, miðstöðvar, bylgjur.
        Data Link Layer
            Setur skilaboð í "umslög" fyrir flutningu
        Network Layer
            Velur hvaða leið til að koma skilaboðinu til skila, 
        Transport Layer
            Passar að skilaboðið kemur til leiðarenda án villur og upplýsinga tap
        Session Layer
            setur up "fund" á milli tenginga og vélar
        Presentation Layer
            "þýðir" upplýsingar fyrir næsta liðið
        Application Layer
            "gluggin" fyrir notandan
        
4. Hvað er Restful API?

        Það er byggt á "representational state transfer" (REST), arkitektúr og nálgunar stíl fyrir samskipti með API
        RESTful API brýtur niður samskipti í röð af litlum bútum.
        Hver bútur fjallar um þeir eigin sérstakan hluta af samskiptum.
        Með þessa tækni er hægt að skapa mjög sveiganleg kerfi
        enn það er erfitt að byggja frá engu enn fyrirbyggð módel eru í boði.
        
5. Sýndur sundurliðunina á eftirfarandi:

      a. Http Request message
      
        <request-line>
        <general-headers>
        <request-headers>
        <entity-headers>
        <empty-line>
        [<message-body>]
        [<message-trailers>]

      b. Http Respond message
      
        <status-line>
        <general-headers>
        <response-headers>
        <entity-headers>
        <empty-line>
        [<message-body>]
        [<message-trailers>]
        
6. Open Authorization (OAuth) og Token Base authentication. Útskýrðu hvað og hvernig þetta
virkar

        Token based gefur þig "token" þegar þú gerir vanalega öryggis atriðin að setja in username og password
        Þetta token gefur þeim aðgang að verndaðar upplýsingar í takmarkaðan tíma.
        Það getur verið gefin til einhvern annan eða eitthvað tölvukerfi
        ef þú treysti það eða þá ekki nóg með passwordið þitt.
       

        OAuth er rammi sem gefur önnur forrit leyfi til að nota takmarkaða upplýsingar tengt við þig
        svo að þú þarf ekki gefa allar upplýsingarnar tengd emailið þitt sem er of mikið leyfi og
        nóg leyfi til að sjálfvirka hluti fyrir þig.
        
#### Verkefni (4%) 2 af 4 verkefnum gilda.
https://www.udacity.com/course/designing-restful-apis--ud388

7. Notaðu curl tólið til að að senda Get Request á soundCloud (frjálst efnisval) (sjá lesson 2:6 í
Udacity).
* https://curl.haxx.se/
* https://soundcloud.com/ (þarft að skrá þig)

8. Notaðu Postman (chrome extension) til að búa til request til að fá latitude og longitude hnit fyrir
Vörðuskóla. (sjá lesson 2:7 í Udacity)
Geocoding API: https://developers.google.com/maps/documentation/geocoding/intro

9. Notaðu Foursquare API og finndu alla pizzustaði í Reykjavík. Ath þú þarft að nota lat og long fyrir
Reykjavík. https://developer.foursquare.com/ (sjá lesson 2:8 í Udacity)

10. Skrifaðu eigið python app sem skilar long og lat frá heimabænum þínum. (sjá lesson 2:9 í
Udacity)

#### Námsmat og skil.
Gefið er fullt fyrir fullnægjandi lausnir og svör, hálft fyrir lausnir eða svör sem eru ábótavant en virkar.
Skilaðu Github slóð á Innu sem hýsir kóðann þinn og svör 
