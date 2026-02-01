# Bestand





Publicatiedatum 30-10-2024 06:30

# Toelichting Wijk- en Buurtkaart 2022, 2023 en 2024

### Over deze publicatie

Dit is de toelichting op de Wijk- en Buurtkaart 2022, 2023 en 2024. Het betreft respectievelijk versie 3,2,1.

# 1. Gegevens geometrie

De Wijk-en Buurtkaart is opgebouwd uit de gedetailleerde geometrie van het bestand Burgerlijke Gemeentegrenzen van het Kadaster, afgeleid uit de Basisregistratie Kadaster (BRK), de bij CBS bekende begrenzingen van wijken en buurten, de grens tussen land en water volgens afbakening van het laatst gepubliceerde Bestand Bodemgebruik en de bijbehorende Kerncijfers Wijken en Buurten van CBS. Het bevat originele coördinaten en is niet gegeneraliseerd.

CBS stelt de wijk- en buurtcodes vast in het kader van de landelijke coördinatie van de wijk- en buurtindeling van gemeenten. Alle gemeenten, wijken en buurten krijgen een unieke code. Deze codes zijn voor de gemeenten en de daarbinnen gelegen wijken en buurten als volgt opgebouwd:

1. De code voor een gemeente wordt gevormd door vier cijfers met daaraan voorafgaand de letters “GM”;

2. De code voor een wijk binnen een gemeente wordt gevormd door zes cijfers met daaraan voorafgaand de letters “WK”. De eerste vier cijfers refereren naar de gemeentecode. WK000301 bijvoorbeeld betekent wijk 01 in gemeente 0003;

3. De code voor de buurt binnen een wijk wordt gevormd door acht cijfers met daaraan voorafgaand de letters “BU”. Bijv. BU00030102 betekent buurt 02 in wijk 01 van gemeente 0003.

### 1.1 Nauwkeurigheid

Het voornaamste doel van het digitale bestand van de burgerlijke gemeentegrenzen uit de BRK van het Kadaster is het zo nauwkeurig mogelijk weergeven van de administratieve grenzen van gemeenten. De grenzen van wijken en buurten zijn echter primair opgenomen ter visuele ondersteuning van wijk- en buurtcijfers. De mate van nauwkeurigheid van de grenzen verschilt daarom. De grenzen van de gemeenten en die van de kustlijnen uit de bodemgebruikskaart hebben een afwijking van maximaal 5 meter, terwijl de afwijking van de wijk- en buurtgrenzen binnen de gemeenten ongeveer 10 tot 50 meter bedraagt.

Voor de weergave van de grens tussen land en water is bij de wijk- en buurtgrenzen uitgegaan van de basistopografie van Nederland. Dit geldt voor de kustlijnen en begrenzingen van grote wateren, waaronder de Noordzee, de Waddenzee inclusief Eems en Dollard, het IJsselmeer, de randmeren van Flevoland, de afgesloten zeearmen van de Zeeuwse en Zuid-Hollandse wateren en het Lauwersmeer. Deze grenzen zijn overgenomen uit het laatst gepubliceerde Bestand Bodemgebruik van het CBS. Voor Wijk- en Buurtkaart 2022, 2023 en 2024 is dat Bestand Bodemgebruik 2017.

### 1.2 Fictieve buurten

De samenvoeging van bestanden tot het geharmoniseerde digitale bestand Wijk- en Buurtkaart, heeft voor een aantal gemeenten geleid tot het aanbrengen van één of meer fictieve buurten. Het gaat daarbij alleen om gebieden die bestaan uit grotere wateroppervlakten1).

Wanneer dit een gebied betreft dat behoort tot de Waddenzee (incl. Eems en Dollard), de Noordzee, de Ooster- of de Westerschelde, dan zijn deze fictieve buurten gecodeerd als 9998. Gaat het om gebied van een gemeente in het IJsselmeer, het Markermeer, het Haringvliet, het Hollands Diep, de Grevelingen, de Krammer, het Volkerak, het Veerse Meer, het Markizaatsmeer of in één van de randmeren van Flevoland, dan hebben deze fictieve buurten het buurtnummer 9997. In dit geval is er ook overeenkomst met de scheiding tussen land en water van het Bestand Bodemgebruik van het CBS.

De aan polygonen gekoppelde kerncijfers van buurten betreffen de cijfers over het totale gebied van deze buurtcode. Enkele keren komt het voor dat een buurtcode in meerdere afzonderlijke vlakken in de Wijk- en Buurtkaart voorkomt. Deze zijn dan wel opgenomen als één record.

### 1.3 Formaat

De digitale geometrie wordt geleverd als GeoPackage. De coördinaten worden weergegeven in meters volgens het stelsel van Rijksdriehoeksmeting (EPSG: 28992). Daarnaast zal het bestand in het laatste kwartaal van het publicatiejaar beschikbaar worden gesteld als WMS- en WFS-geoservice via [www.pdok.nl](http://www.pdok.nl/). Een deel van de Buurtkaart is ook online te bekijken via [Cijfers op de](https://www.cbs.nl/nl-nl/visualisaties/cijfers-op-de-kaart) [Kaart](https://www.cbs.nl/nl-nl/visualisaties/cijfers-op-de-kaart).

*1)* *Selectie* *op* *variabele* *“WATER”=* *“JA”.*

# 2. Algemene gegevens kerncijfers

De publicatie Kerncijfers wijken en buurten bevat statistische gegevens voor alle gemeenten, wijken en buurten van Nederland. De kerncijfers hebben hoofdzakelijk tot doel om vergelijkingen tussen de verschillende onderdelen van gemeenten mogelijk te maken en de verschillen zichtbaar te maken. Doordat de cijfers heel Nederland beslaan is het ook mogelijk om buurten van verschillende gemeenten met elkaar te vergelijken.

De wijk- en buurtindeling wordt in principe door de gemeenten vastgesteld. CBS verzorgt de landelijke coördinatie van de indeling. In de landelijke gebieden is de topografie het uitgangspunt bij de buurtindeling. In stedelijke gebieden spelen sociaal-economische verschillen vaak een rol bij de buurtafbakening. De wijkindeling is terug te voeren tot de kernen met hun omsloten buitengebied, of de zogenoemdestadswijken, die bestaan uit een aantal min of meer homogeen bebouwde en aaneengesloten buurten.

Bij de naamgeving van wijken en buurten is uitgegaan van de plaatselijk gangbare namen, die door de gemeenten zijn vastgesteld. De codering van de wijken en buurten is landelijk uniform. Iedere buurt heeft een unieke achtcijferige code. De eerste vier cijfers vormen de gemeentecode, de volgende twee cijfers zijn de wijkcode en de laatste twee cijfers zijn de buurtcode.
Naast de gegevens uit de publicatie Kerncijfers wijken en buurten zijn ook de nabijheidsstatistieken toegevoegd.

De meest recente cijfers uit Kerncijfers wijken en buurten en de de nabijheidsvoorzieningen zijn te raadplegen via [StatLine](https://opendata.cbs.nl/statline/CBS/nl/). Aanvullingen, bijstellingen en correcties worden eerst doorgevoerd op StatLine en in het laatste kwartaal ook in de WMS- en WFS-geoservice.

# 3. Definities en verklaring van symbolen

`Regio` : 

De gemeenten in Nederland zijn onderverdeeld in wijken en buurten. Buurten vormen het laagste regionale niveau. Wijken zijn optellingen van één of meer aaneengesloten buurten. De gemeente bepaalt zelf de indeling in wijken en buurten. Het CBS coördineert landelijk deze indeling.

`Wijk` : 

Onderdeel van een gemeente, bestaande uit één of meerdere buurten. Vaak komt een wijk overeen met een woonplaats of een deel van een grotere woonplaats.

`Buurt` : 

Onderdeel van een gemeente, dat vanuit bebouwingsoogpunt of sociaaleconomische structuur homogeen is afgebakend. Homogeen wil zeggen dat één functie dominant is, bijvoorbeeld woonfunctie (woongebied), werkfunctie (industriegebied) of recreatieve functie (natuurgebied). Functies kunnen echter ook gemengd voorkomen. 

**Verklaring van bijzondere waarden:**

`-99997` : waarde geheim of niet aanwezig

`-99995` : onderwerp wordt in een latere versie gepubliceerd

`-99991` : onderwerp wordt niet meer (op dit ruimtelijk niveau) gepubliceerd

# 4. Beschrijving van het onderliggende onderzoek

Om gegevens op buurtniveau te kunnen publiceren moet gebruik worden gemaakt van integrale waarnemingen of tellingen of van onderzoeken met een grote steekproefomvang. De gegevens in deze publicatie zijn afgeleid uit onder andere de Basisregistratie Personen (BRP), de Gedigitaliseerde kaart Bodemgebruik en het Geografisch basisregister. De Gemeentelijke Basisadministratie Persoonsgevens (GBA) en de Registratie Niet-Ingezetenen (RNI) vormen samen de Basisregistratie Personen (BRP).

Met ingang van 2012 wordt de koppeling van de buurtcode aan de adressen berekend uit de coördinaten van de adressen uit de Basisadministratie Adressen en Gebouwen (BAG).

## 4.1 Vergelijkingen

Een vergelijking van de kerncijfers van buurten in deze publicatie met die van vorige verslagjaren is niet altijd zonder meer mogelijk. Dit heeft twee redenen. Ten eerste zijn er gemeenten waarvan de wijk- en buurtindeling (soms ingrijpend) is gewijzigd. Daarnaast zijn sommige adressen door kwaliteitsverbeteringen van buurtcode gewisseld.

Om redenen van betrouwbaarheid en geheimhouding kunnen gegevens ontbreken. In de toelichting bij de diverse onderwerpen staat welke beveiligingsprocedure is gebruikt. Door afronding kan het voorkomen dat de totalen niet geheel overeenstemmen met de som van de afzonderlijke getallen.

## 4.2 Versie

Uitgangspunt bij het samenstellen van deze publicatie is een zo breed mogelijk aanbod van zo recent mogelijke kerncijfers. Omdat cijfers uit CBS-onderzoek soms in latere jaren beschikbaar komen, is met ingang van 2011 gekozen voor drie leveringsmomenten. De eerste levering vindt plaats in het najaar van het verslagjaar met een eerste kleine set gegevens. De twee daarop volgende updates bevatten dezelfde geometrie, maar meer kerncijfers.

Deze publicatie betreft respectievelijk de eerste, tweede en derde versie van de Kerncijfers 2024, 2023 en 2022.

# 5. Beschrijving kerncijfers

In dit hoofdstuk worden alle typen kerncijfers besproken die kunnen voorkomen in 2022,2023 en/of 2024. Dat wil niet zeggen dat ze allemaal voorkomen; hoe verder terug in de tijd hoe meer variabelen beschikbaar2) zijn.

## 5.1 WIJKEN EN BUURTEN

`buurtcode` : Buurtcode [code]

Voor de codering van de binnen wijken onderscheiden buurten is een code van acht posities opgenomen. Gemeentecode (4) + wijkcode (2) + buurtcode (2).

`buurtnaam` : Buurtnaam [naam]

De buurtnaam is opgegeven door de gemeente die hiervan eigenaar is.

`wijkcode` : Wijkcode [code]

Voor de codering van de binnen gemeenten onderscheiden wijken is een code van zes posities opgenomen. Gemeentecode (4) + wijkcode (2).

`wijknaam` : Wijknaam [naam]

De wijknaam is opgegeven door de gemeente die hiervan eigenaar is.

`gemeentecode` : Gemeentecode [code]

De gemeentecode geeft de numerieke aanduiding van gemeenten weer, die door CBS in overleg met het Ministerie van Binnenlandse Zaken en Koninkrijksrelaties (BZK) wordt vastgesteld. Deze viercijferige code is gekoppeld aan de naam van de gemeente: wijzigt de naam van een gemeente, dan wijzigt ook de code.

`gemeentenaam` : Gemeentenaam [naam]

De naam van de bestuurlijke gemeente. Deze naam volgt de officiële schrijfwijze.

`indelingswijziging_wijken_en_buurten` : Indelingswijziging wijken en buurten [code]

Deze indicator geeft per wijk en buurt aan of de cijfers uit deze tabel zonder problemen kunnen worden gekoppeld aan en vergeleken met de cijfers van een jaar eerder, of dat er wijzigingen in de Wijk- en Buurtindeling zijn waardoor dit niet kan. Detailinformatie over wijzigingen in de Wijk- en Buurtindeling kan worden verkregen door de wijk- en buurtkaart van twee opeenvolgende jaren met elkaar te vergelijken

De indicator kent drie mogelijke waarden:

1. De codering en afbakening van deze wijk/buurt is ongewijzigd ten opzichte van het voorgaande jaar. Het is wel mogelijk dat een naamswijziging heeft plaatsgevonden. De cijfers kunnen worden gekoppeld en vergeleken met die van het voorgaande jaar;

2. De codering van de wijk/buurt is veranderd ten opzichte van het voorgaande jaar. De afbakening is ongewijzigd. Om te kunnen koppelen met cijfers van het voorgaande jaar zal eerst moeten worden achterhaald wat de codering van het voorgaande jaar was. Is de koppeling eenmaal geslaagd dan kunnen de cijfers alsnog met elkaar worden vergeleken;

3. De afbakening van de wijk/buurt is veranderd ten opzichte van het voorgaande jaar. Dit kan gepaard zijn gegaan met een gewijzigde codering. De cijfers kunnen niet zonder meer worden vergeleken met die van het voorgaande jaar. Verschillen kunnen immers samenhangen met de verandering in de afbakening van de wijk of buurt.

Voor een wijk of buurt wordt alleen een wijziging in de afbakening geconstateerd wanneer een grens circa 5 meter of meer is verlegd. Kleinere grenswijzigingen worden
niet als significant beschouwd.

`water` : Land-Watergrens [code]

Een onderverdeling tussen land en grotere wateroppervlakten overeenkomend met het Bestand Bodemgebruik van het CBS.

De codering kent drie mogelijke waarden:

“JA” : water;

“NEE” : land;

"B” : Belgisch grondgebied rond Baarle Nassau. (GM0998 = Buitenland)

`meest_voorkomende_postcode` : Meest voorkomende postcode [code]

De meest voorkomende numerieke postcode in een buurt, op grond van het aantal adressen in het Geografisch Basisregister (GBR, definitieve versie) per 1 januari.

`dekkingspercentage` : Meest voorkomende postcode; dekkingspercentage [code]

Indicatie (in zes klassen) van het percentage adressen in een buurt met de meest voorkomende postcode. Dit percentage is ontleend aan het Geografisch Basisregister (GBR, definitieve versie).

De volgende klassenindeling is gehanteerd:

1.  90% van de adressen heeft dezelfde vermelde numerieke postcode;

2.  81-90% van de adressen heeft dezelfde vermelde numerieke postcode;

3.  71-80% van de adressen heeft dezelfde vermelde numerieke postcode;

4.  61-70% van de adressen heeft dezelfde vermelde numerieke postcode;

5.  51-60% van de adressen heeft dezelfde vermelde numerieke postcode;

6.  50% of minder van de adressen heeft dezelfde vermelde numerieke postcode.

`omgevingsadressendichtheid` : Omgevingsadressendichtheid [absoluut]

Het gemiddeld aantal adressen van een buurt, wijk of gemeente per vierkante kilometer binnen een cirkel met een straal van één kilometer op 1 januari van het betreffende jaar.

De OAD beoogt de mate van concentratie van menselijke activiteiten (wonen, werken, schoolgaan, winkelen, uitgaan etc.) weer te geven. CBS gebruikt de OAD om de stedelijkheid van een bepaald gebied te bepalen.

Voor de berekening hiervan wordt eerst voor ieder adres de OAD vastgesteld. Daarna is het gemiddelde berekend van de omgevingsadressendichtheden van alle afzonderlijke adressen binnen het beschouwde gebied. De adressen zijn afkomstig uit het Geografisch Basisregister van het betreffende jaar (definitieve versie). Dit register bevat alle adressen van Nederland die zijn voorzien van een postcode, gemeentecode en wijk- en buurtcode.

De gemeentelijke OAD in deze publicatie wijkt af van de gemeentelijke OAD in de Regionale Kerncijfers Nederland (RKN). In deze laatste publicatie wordt de OAD berekend zonder gegevens over de nieuwe adressen van het betreffende kalenderjaar. Het gemeentelijk cijfer van de OAD in deze publicatie komt overeen met de definitieve OAD in de publicatie Maatstaven ruimtelijke gegevens Financiële verhoudingswet (Fvw).

`stedelijkheid_adressen_per_km2` : Stedelijkheid [code]

Op grond van de omgevingsadressendichtheid is aan iedere buurt, wijk of gemeente een stedelijkheidsklasse toegekend. De volgende klassenindeling is gehanteerd:

1.  zeer sterk stedelijk >= 2 500 adressen per km²;

2.  sterk stedelijk 1 500 - 2 500 adressen per km²;

3.  matig stedelijk 1 000 - 1 500 adressen per km²;

4.  weinig stedelijk 500 - 1 000 adressen per km²;

5.  niet stedelijk < 500 adressen per km².

## 5.2 BEVOLKING

De bevolking van Nederland op 1 januari.

Bevolking: De inwoners van Nederland.

In de bevolkingsaantallen zijn uitsluitend personen begrepen die zijn opgenomen in het bevolkingsregister van een Nederlandse gemeente. In principe wordt iedereen die voor onbepaalde tijd in Nederland woont, opgenomen in het bevolkingsregister van de woongemeente. Personen die tot de bevolking van Nederland behoren, maar voor wie geen vaste woonplaats valt aan te wijzen, zijn opgenomen in het bevolkingsregister van de gemeente 's-Gravenhage.

In de bevolkingsregisters zijn niet opgenomen de in Nederland wonende personen waarvoor uitzonderingsregels gelden met betrekking tot opneming in de bevolkingsregisters (bijvoorbeeld diplomaten en NAVO militairen) en personen die niet legaal in Nederland verblijven. Om redenen van statistische geheimhouding zijn de aantallen op wijk- en buurtniveau aselect afgerond op veelvouden van 5.

Bij aselect afronden wordt door loten bepaald of een getal naar boven of naar beneden wordt afgerond. De daarbij gehanteerde kansen zijn omgekeerd evenredig met de afrondverschillen. Gemiddeld wordt een getal hierdoor op zichzelf afgerond. Het gemiddelde afrondverschil per getal is evenwel groter dan het geval is bij afronding op het dichtstbijzijnde veelvoud van 5. Door afrondverschillen is de som van afgeronde getallen niet altijd gelijk aan de afgeronde som.

Hierdoor kan het voorkomen dat wanneer een wijk uit één buurt bestaat of een gemeente uit één wijk, dit afgerond niet overeenkomt.

Het komt voor dat van inwoners wel bekend is binnen welke gemeente ze geregistreerd zijn, maar niet exact waar ze verblijven. Deze inwoners zijn daarom wel meegeteld in de gemeentecijfers, maar niet in de cijfers per wijk en buurt. De cijfers per gemeente kunnen daardoor afwijken van de onderliggende wijken of buurten, zelfs wanneer een gemeente slechts uit één wijk bestaat.

`aantal_inwoners` : Aantal inwoners [aantal]

`mannen` : Mannen [aantal]

`vrouwen` : Vrouwen [aantal]

`percentage_personen_0_tot_15_jaar` : Personen 0 tot 15 jaar [%]

`percentage_personen_15_tot_25_jaar` : Personen 15 tot 25 jaar [%]

`percentage_personen_25_tot_45_jaar` : Personen 25 tot 45 jaar [%]

`percentage_personen_45_tot_65_jaar` : Personen 45 tot 65 jaar [%]

`percentage_personen_65_jaar_en_ouder` : Personen 65 jaar en ouder [%]

`percentage_ongehuwd` : Ongehuwd [%]

Het aantal inwoners dat op 1 januari ongehuwd is. De burgerlijke staat ‘ongehuwd’ geeft aan dat een persoon nog nooit een huwelijk heeft gesloten of een geregistreerd partnerschap is aangegaan.

`percentage_gehuwd` : Gehuwd [%]

Het aantal inwoners dat op 1 januari gehuwd is. De burgerlijke staat ‘gehuwd’ ontstaat na sluiting van een huwelijk of het aangaan van een geregistreerd partnerschap. Tot de gehuwden worden ook personen gerekend die gescheiden zijn van tafel en bed, want zij blijven formeel gehuwd.

`percentage_gescheid` : Gescheiden [%]

Het aantal inwoners dat op 1 januari gescheiden is. De burgerlijke staat ‘gescheiden’ ontstaat na ontbinding van een huwelijk door echtscheiding of na ontbinding van een geregistreerd partnerschap anders dan door het overlijden van de partner. Personen die gescheiden zijn van tafel en bed worden tot de gehuwden gerekend.

`percentage_verweduwd` : Verweduwd [%]

Het aantal inwoners dat op 1 januari verweduwd is. De burgerlijke staat ‘verweduwd’ ontstaat na ontbinding van een huwelijk of geregistreerd partnerschap door overlijden van de partner.

`geboorte_totaal` : Geboorte totaal [aantal]

Het aantal levendgeborenen van 1 januari tot en met 31 december van het betreffende jaar. Levendgeborenen zijn kinderen die na geboorte enig teken van leven hebben vertoond, ongeacht de zwangerschapsduur.

`geboortes_per_1000_inwoners` : Geboorte relatief [per 1 000 inwoners]

Het aantal levendgeborenen van 1 januari tot en met 31 december, per duizend inwoners op 1 januari van het betreffende jaar.

Het relatieve aantal geboorten kan hoger uitvallen dan verwacht op basis van het inwonertal. Het relatieve cijfer betreft namelijk het aantal geboorten gedurende het jaar ten opzichte van het aantal inwoners op 1 januari. In nieuwbouwwijken kan het aantal inwoners sterk groeien in een jaar. Zo kunnen er in één jaar tien kinderen geboren worden in een wijk waarin op 1 januari slechts tien inwoners wonen, maar aan het eind van het jaar bijvoorbeeld 200 inwoners.

`sterfte_totaal` : Sterfte totaal [aantal]

Alle overledenen van 1 januari tot en met 31 december van het betreffende jaar waarbij een bevoegde arts een overlijdensakte heeft ondertekend.

sterfte_relatief: Sterfte relatief [per 1 000 inwoners] Het aantal overledenen van 1 januari tot en met 31 december, per duizend inwoners op 1 januari van het betreffende jaar.

Het relatieve aantal overledenen kan hoger uitvallen dan verwacht op basis van het inwonertal. Het relatieve cijfer betreft namelijk het aantal overledenen gedurende het jaar ten opzichte van het aantal inwoners op 1 januari. In een buurt met een verpleeghuis kunnen op 1 januari 100 mensen wonen, maar door overlijdensgevallen komen er steeds nieuwe inwoners (bewoners van het verpleeghuis). Zo kan het aantal overlijdensgevallen ook 100 zijn, terwijl er inmiddels al vele mensen in die buurt (of dat verpleeghuis) hebben gewoond.

`bevolkingsdichtheid_inwoners_per_km2` : Bevolkingsdichtheid [aantal inwoners per km2]

Het (niet afgeronde) aantal inwoners op 1 januari gedeeld door de (niet afgeronde) landoppervlakte. Wanneer een buurt minder dan 10 inwoners telt, is dit gegeven geheimgehouden (.).

## Particuliere huishoudens

Het aantal particuliere huishoudens op 1 januari.
Particuliere huishoudens bestaan uit één of meer personen die alleen of samen in een woonruimte zijn gehuisvest en zelf in hun dagelijks onderhoud voorzien. Naast eenpersoonshuishoudens bestaan er meerpersoonshuishoudens (niet-gehuwde paren, niet-gehuwde paren met kinderen, echtparen, echtparen met kinderen, eenouderhuishoudens en overige huishoudens). De institutionele huishoudens worden hiertoe niet gerekend.

`aantal_huishoudens` : Huishoudens totaal [aantal]

Het aantal particuliere huishoudens op 1 januari.

`percentage_eenpersoonshuishoudens` : Eenpersoonshuishoudens [%]

Het aantal huishoudens met één persoon, uitgedrukt in hele procenten van het totaal aantal particuliere huishoudens.

`percentage_huishoudens_zonder_kinderen` : Huishoudens zonder kinderen [%]

Het aantal meerpersoonshuishoudens zonder kinderen uitgedrukt in hele procenten van het totaal aantal particuliere huishoudens.

Meerpersoonshuishoudens zonder kinderen bestaan uit niet-gehuwde paren zonder kinderen, echtparen zonder kinderen en overige huishoudens.

`percentage_huishoudens_met_kinderen` : Huishoudens met kinderen [%]

Het aantal meerpersoonshuishoudens met kinderen uitgedrukt in hele procenten van het totaal aantal particuliere huishoudens.

Meerpersoonshuishoudens met kinderen bestaan uit niet-gehuwde paren met kinderen, echtparen met kinderen en eenouderhuishoudens.

`gemiddelde_huishoudsgrootte` : Gemiddelde huishoudensgrootte [aantal]

Het aantal in particuliere huishoudens levende personen gedeeld door het aantal particuliere huishoudens.

## Personen met een migratieachtergrond (wordt anders gedefineerd na 2022)

Het aantal personen met een migratieachtergrond op 1 januari. Persoon met een migratieachtergrond: Persoon van wie ten minste één ouder in het buitenland is geboren. 

Persoon met een eerste generatie migratieachtergrond: Persoon die in het buitenland is geboren met ten minste één in het buitenland geboren ouder.

Persoon met een tweede generatie migratieachtergrond: Persoon die in Nederland is geboren met ten minste één in het buitenland geboren ouder.

Personen met een migratieachtergrond worden onderverdeeld in westers en niet-westers op grond van hun geboorteland. Tot de categorie 'niet-westers' behoren personen met een migratieachtergrond uit Turkije, Afrika, Latijns-Amerika en Azië met uitzondering van Indonesië en Japan. Op grond van hun sociaaleconomische en sociaal- culturele positie worden personen met een migratieachtergrond uit deze twee landen tot personen met een westerse migratieachtergrond gerekend. Het gaat vooral om mensen die in voormalig Nederlands Indië zijn geboren en werknemers van Japanse bedrijven met hun gezin.

`percentage_westerse_migratieachtergrond`: Westers totaal [%] ( vervalt na 2022 )

Het aantal personen met een migratieachtergrond met een westerse herkomst op 1 januari, uitgedrukt in hele procenten van het aantal inwoners. Het betreft personen met een migratieachtergrond met als herkomstgroepering een van de landen in de werelddelen Europa (exclusief Turkije), Noord-Amerika en Oceanië of Indonesië of Japan.

Op grond van hun sociaaleconomische en sociaal-culturele positie worden personen met een migratieachtergrond uit Indonesië en Japan tot de westerse personen met een migratieachtergrond gerekend. Het gaat vooral om mensen die in het voormalig Nederlands-Indië zijn geboren en werknemers van Japanse bedrijven met hun gezin.

`percentage_niet_westerse_migratieachtergrond` : Niet- westers totaal [%] ( vervalt na 2022 )

Het aantal personen met een migratieachtergrond met een niet- westerse herkomst op 1 januari, uitgedrukt in hele procenten van het aantal inwoners. Het betreft personen met een migratieachtergrond met als herkomstgroepering een van de landen in de werelddelen Afrika, Latijns-Amerika en Azië (exclusief Indonesië en Japan) of Turkije.

Op grond van hun sociaaleconomische en sociaal-culturele positie worden personen met een migratieachtergrond uit Indonesië en Japan tot de westerse personen met een migratieachtergrond gerekend. Het gaat vooral om mensen die in het voormalig Nederlands-Indië zijn geboren en werknemers van Japanse bedrijven met hun gezin.

`percentage_uit_marokko` : Marokko [%] ( vervalt na 2022 )

`percentage_uit_nederlandse_antillen_en_aruba` : Nederlandse Antillen en Aruba [%] ( vervalt na 2022 )

Het aandeel personen met een migratieachtergrond met herkomstgroep van (voormalige) Nederlandse Antillen en Aruba op 1 januari, uitgedrukt in hele procenten van het aantal inwoners. Het betreft een samentelling van de eilanden die tot het grondgebied van de Nederlandse Antillen en Aruba van vóór 10 oktober 2010 behoorden. Het gaat om de eilanden Bonaire, Curaçao, Saba, Sint-Eustatius, Sint- Maarten en Aruba.

Vanaf 10 oktober 2010 zijn de Nederlands Antillen ontbonden. Het Koninkrijk der Nederlanden bestaat vanaf die datum uit vier landen: Nederland, Aruba, Curaçao en Sint Maarten. Alle eilanden hebben een nieuwe status. Curaçao en Sint Maarten zijn nieuwe landen binnen het Koninkrijk. Met een ‘Status aparte’ binnen het Koninkrijk zijn Curaçao en Sint Maarten autonome landen. De landen hebben een zelfstandig bestuur en zijn niet meer afhankelijk van Nederland. De openbare lichamen Bonaire, Sint Eustatius en Saba, ook wel Caribisch Nederland, hebben een diepere band met Nederland en functioneren als een bijzondere gemeente van Nederland.

Op 1 januari 1986 werd Aruba afgescheiden van de Nederlandse Antillen. Sinds die datum is Aruba een nieuw land binnen het Koninkrijk de Nederlanden. Met een 'Status aparte' binnen het Koninkrijk is Aruba een autonoom land. Aruba heeft een zelfstandig bestuur en is niet meer afhankelijk van Nederland.

`percentage_uit_suriname` : Suriname [%] ( vervalt na 2022 )

`percentage_uit_turkije` : Turkije [%] ( vervalt na 2022 )

`percentage_overige_nietwestersemigratieachtergrond` : Overig niet-westers [%] ( vervalt na 2022 )

Het aandeel personen met een migratieachtergrond met een overige niet-westerse herkomst op 1 januari, uitgedrukt in hele procenten van het aantal inwoners.

Het betreft het totaal niet-westers minus Marokko, (voormalige) Nederlandse Antillen en Aruba, Suriname en Turkije.

## Bevolking naar herkomst ( geintroduceerd in 2023 )

**Bevolking**: De inwoners van Nederland.

In de bevolkingsaantallen zijn uitsluitend personen begrepen die zijn opgenomen in het bevolkingsregister van een Nederlandse gemeente. In principe wordt iedereen die voor onbepaalde tijd in Nederland
woont, opgenomen in het bevolkingsregister van de woongemeente. Personen die tot de bevolking van Nederland behoren, maar voor wie geen vaste woonplaats valt aan te wijzen, zijn opgenomen in het bevolkingsregister van de gemeente 's-Gravenhage.

In de bevolkingsregisters zijn niet opgenomen de in Nederland wonende personen waarvoor uitzonderingsregels gelden met betrekking tot opneming in de bevolkingsregisters (bijvoorbeeld diplomaten en NAVO militairen) en personen die niet legaal in Nederland verblijven.

**Herkomst**: Kenmerk dat weergeeft in welk land iemand geboren is of waar diens ouders geboren zijn.

De herkomst van personen die in het buitenland zijn geboren wordt bepaald door hun eigen geboorteland. Bij personen die in Nederland geboren zijn, wordt de herkomst bepaald door het geboorteland van de ouders.

Wanneer beide ouders in het buitenland zijn geboren, is het geboorteland van de moeder leidend in het bepalen van de herkomst. De geboortegegevens van de moeder zijn vaker bekend dan die van de vader. Wanneer de moeder in Nederland is geboren of het geboorteland van de moeder onbekend is, dan wordt het geboorteland van de vader gebruikt.

`percentage_met_herkomstland_nederland` : Herkomstland Nederland [%]

`percentage_met_herkomstland_uit_europa_excl_nl` : Herkomstland Europa (excl. NL) [%]

De landen Armenië, Azerbeidzjan, Georgië, Kazachstan, Kirgizië, Oezbekistan, Tadzjikistan, Turkmenistan en Turkije vallen binnen deze indeling onder Azië.

`percentage_met_herkomstland_buiten_europa` : Herkomstland buiten Europa [aantal]



Totaal herkomst buiten Europa

`percentage_geb_in_nl_met_herkomstland_nederland` : geboren in Nederland ; herkomstland Nederland; [%]

`perc_geb_in_nl_met_herkomstland_in_europa_ex_nl`:  geboren in Nederland ; herkomstland Europa (excl. NL) [%]

De landen Armenië, Azerbeidzjan, Georgië, Kazachstan, Kirgizië, Oezbekistan, Tadzjikistan, Turkmenistan en Turkije vallen binnen deze indeling onder Azië.

`perc_geb_in_nl_met_herkomstland_buiten_europa` : geboren in Nederland ; herkomstland buiten Europa; [%]



Totaal buiten Europa.

`perc_geb_buiten_nl_met_herkomstlnd_in_europa_ex_nl` : geboren buiten Nederland ; herkomstland Europa (excl. NL); [%]

De landen Armenië, Azerbeidzjan, Georgië, Kazachstan, Kirgizië, Oezbekistan, Tadzjikistan, Turkmenistan en Turkije vallen binnen deze indeling onder Azië.

`perc_geb_buiten_nl_met_herkomstlnd_buiten_europa` : geboren buiten Nederland ; herkomstland buiten Europa [%]

Totaal buiten Europa.

## 5.3 BEDRIJVEN

Bedrijfsvestigingen naar activiteit op 1 januari (SBI 2008), exclusief bedrijfsvestigingen in de sectoren overheid, onderwijs en zorg.

Deze tabel bevat gegevens over het aantal vestigingen van bedrijven naar economische activiteit, gebaseerd op de Standaard Bedrijfsindeling 2008 (SBI 2008). De vestigingen zijn voorts ingedeeld naar de gemeentelijke indeling per 1 januari van het verslagjaar, naar wijken en naar buurten.

### Status van de cijfers:

De cijfers hebben een voorlopig karakter.

### Vestiging:

Elke afzonderlijk gelegen ruimte, terrein of complex van ruimten of terreinen, benut door een bedrijf voor uitoefening van de activiteiten. Ieder bedrijf bestaat uit ten minste één vestiging. Meerdere locaties van een bedrijf binnen één postcodegebied worden als één vestiging beschouwd.

Standaard
Bedrijfsindeling 2008 (SBI 2008):

De Nederlandse hiërarchische indeling van economische activiteiten die door het CBS wordt gebruikt om bedrijfseenheden in te delen naar hun hoofdactiviteit. De SBI 2008 is de versie die vanaf 2008 gebruikt wordt.

In deze tabel is gekozen voor de hoofdactiviteit (SBI) van de vestiging. Niet iedere vestiging van een bedrijf houdt zich bezig met de hoofdactiviteit (SBI) van het bedrijf als geheel. Om te weten welke activiteiten worden uitgevoerd in een regio is de hoofdactiviteit (SBI) van de vestiging gebruikt. In de tabel zijn de vestigingen (naast de totalen) ook naar de volgende zeven sectoren onderverdeeld:

|     |                                      |
| --- | ------------------------------------ |
| A   | Landbouw, bosbouw en visserij        |
| B-F | Nijverheid en energie                |
| G+I | Handel en horeca                     |
| H+J | Vervoer, informatie en communicatie  |
| K-L | Financiële diensten, onroerend goed  |
| M-N | Zakelijke dienstverlening            |
| O-Q | Overheid, onderwijs en zorg          |
| R-U | Cultuur, recreatie, overige diensten |

De sectoren overheid, onderwijs en zorg zijn niet opgenomen vanwege de onbetrouwbaarheid van deze gegevens.



Het aantal vestigingen is afgerond op een veelvoud van vijf. In geval van afrondingen kan het voorkomen, dat de totalen niet precies overeenstemmen met de som der opgetelde getallen.

In geval de wijk of buurt van het bedrijf onbekend is, wordt dit bedrijf alleen op gemeentelijk niveau meegeteld. De onderverdeling naar sectoren is alleen vermeld bij 20 of meer bedrijven per buurt.

`aantal_bedrijfsvestigingen` : Bedrijfsvestigingen totaal [aantal]

`aantal_bedrijven_landbouw_bosbouw_visserij` : A Landbouw, bosbouw en visserij [aantal]

`aantal_bedrijven_nijverheid_energie` : B-F Nijverheid en energie [aantal]

`aantal_bedrijven_handel_en_horeca` : G+I Handel en horeca [aantal]

`aantal_bedrijven_vervoer_informatie_communicatie` : H+J Vervoer, informatie en communicatie [aantal]

`aantal_bedrijven_financieel_onroerend_goed` : K-L Financiële diensten, onroerend goed [aantal]

`aantal_bedrijven_zakelijke_dienstverlening` : M-N Zakelijke dienstverlening [aantal]

`aantal_bedrijven_overheid_onderwijs_en_zorg` :O-Q Overheid, onderwijs en zorg [aantal]

`aantal_bedrijven_cultuur_recreatie_overige` : R-U Cultuur, recreatie, overige diensten [aantal]

## 5.4 WONEN

`woningvoorraad` : Woningvoorraad [aantal]

Het totale aantal woningen op 1 januari van het desbetreffende jaar.
Een woning is een verblijfsobject met minimaal een woonfunctie en eventueel één of meer andere gebruiksfuncties.

`gemiddelde_woningwaarde` : Gemiddelde woningwaarde [x 1000 euro]

De gemiddelde waarde onroerende zaken van woonobjecten gebaseerd op de Wet Waardering Onroerende Zaken (WOZ-waarde).

Voor de bepaling van de gemiddelde woningwaarde wordt alleen gebruik gemaakt van die WOZ-objecten omschreven als woningen dienend tot hoofdverblijf (WOZ-objectcode 10) en woningen met praktijkruimte (WOZ objectcode 11) met een waarde groter dan nul euro.

De (voorlopig) gemiddelde woningwaarde wordt bepaald met de waardepeildatum van voorgaand jaar, bijv: 2017: waardepeildatum 1 januari 2016

Wanneer de woningvoorraad kleiner is dan 20 woningen of het aantal WOZ-objecten kleiner is dan 50 wordt er geen WOZ-waarde opgenomen.

### Woningen naar type

Er worden twee typen woningen onderscheiden, eengezins en meergezins. Een woning heeft het type meergezins wanneer het samen met andere woningen of (bedrijfs)ruimten een geheel pand vormt.

Hieronder vallen flats, galerij-, portiek-, beneden- en bovenwoningen, appartementen en woningen boven bedrijfsruimten, voorzover deze zijn voorzien van een buiten de bedrijfsruimte gelegen toegangsdeur. Alle overige woningen hebben het type eengezins.

`percentage_eengezinswoning` : Percentage eengezinswoning [%]

Peildatum: 1 januari van het desbetreffende jaar.

Het aantal eengezinswoningen is vermeld als percentage van de totale woningvoorraad en wordt alleen vermeld bij minimaal 20 woningen. Eengezinswoning: Elke woning die tevens een geheel pand vormt.

Hieronder vallen vrijstaande woningen, aaneengebouwde woningen, zoals twee onder één kap gebouwde hele huizen, boerderijen met woningen en voorts alle rijenhuizen.

`percentage_meergezinswoning`: Percentage meergezinswoning [%]

Peildatum: 1 januari van het desbetreffende jaar.

Het aantal meergezinswoningen is vermeld als percentage van de totale woningvoorraad en wordt alleen vermeld bij minimaal 20 woningen.

### Woningen naar bewoning

Een woning is bewoond als er volgens de Basisregistratie Personen (BRP) op peildatum 1 januari minimaal 1 persoon stond ingeschreven op het bijbehorende adres. Alle overige woningen, die wel voor bewoning beschikbaar zijn, worden beschouwd als onbewoond.

`percentage_bewoond` : Bewoonde woningen [%]

Peildatum: 1 januari van het desbetreffende jaar.

Het aantal bewoonde woningen is vermeld als percentage van de totale woningvoorraad en wordt alleen vermeld bij minimaal 20 woningen.

Bewoonde woningen: Woningen waar op de peildatum 1 januari minimaal 1 persoon stond ingeschreven in de Basisregistratie Personen (BRP).

`percentage_leegstand_woningen` : Leegstand woningen [%]

Peildatum: 1 januari van het desbetreffende jaar.

Het aantal leegstaande woningen is vermeld als percentage van de totale woningvoorraad en wordt alleen vermeld bij minimaal 20 woningen.

Niet-bewoonde woningen: Woningen waar op de peildatum 1 januari niemand stond ingeschreven in de Basisregistratie Personen (BRP).

### Woningen naar eigendom

Informatie over huur- en koopwoningen wordt samengesteld uit een koppeling tussen verschillende bronnen.

`percentage_koopwoningen`:  Koopwoningen  [%] Woningen die eigendom zijn van de (toekomstige) bewoner(s) of in gebruik als tweede woning.

Peildatum: 1 januari van het desbetreffende jaar.

Het aantal is vermeld als percentage van het totaal aantal woningen en vermeld bij 20 woningen of meer per buurt en wanneer het aandeel woningen met eigendom onbekend 50 procent of minder bedroeg.

### Huurwoningen

Woningen die niet bewoond worden door de eigenaar van de woning. Bij woningen waar geen bewoner geregistreerd is, gaat het om woningen waarvan het aannemelijk is dat de woning bestemd is voor de huurmarkt.

`percentage_huurwoningen`: Huurwoningen totaal [%]

Het aantal huurwoningen als percentage van het totaal aantal woningen op 1 januari van het desbetreffende jaar. Dit wordt vermeld bij 20 woningen of meer per buurt en wanneer het aandeel woningen met eigendom onbekend 50 procent of minder bedroeg.

`perc_huurwoningen_in_bezit_woningcorporaties` : In bezit woningcorporatie [%]

Huurwoningen in eigendom van 'toegelaten instellingen volkshuisvesting'. Het betreft het aantal huurwoningen waarvan is vastgesteld dat de eigenaar een toegelaten instelling is. Het betreft niet het aantal sociale huurwoningen, omdat er alleen is vastgesteld wie de eigenaar is en er niet is gekeken naar de hoogte van de huurprijs.

`Toegelaten instellingen` : woningbouwvereniging, woningstichting, woningcorporatie.

`Sociale huurwoningen` : woningen met een huur onder de liberalisatiegrens.

Peildatum: 1 januari van het desbetreffende jaar.

Het aantal is vermeld als percentage van het totaal aantal woningen en vermeld bij 20 woningen of meer per buurt en wanneer het aandeel woningen met eigendom onbekend 50 procent of minder bedroeg.

`perc_huurwoningen_in_bezit_overige_verhuurders` : In bezit overige verhuurders [%]

Een huurwoning in eigendom van onder andere bedrijven, particulieren en institutionele beleggers. Huurwoningen waarvan het eigendom wel kon worden vastgesteld maar de eigenaar niet vallen hier ook onder.

**Bedrijven**: alle instellingen met een bedrijfsmatig karakter zoals bv's en nv's, zelfstandige ondernemers, makelaars en vastgoedhandelsmaatschappijen.

**Particulieren** : alle natuurlijke personen.

**Institutionele beleggers** : pensioenfondsen, beurs-, beleggings- en verzekeringsmaatschappijen.

Peildatum: 1 januari van het desbetreffende jaar.

Het aantal is vermeld als percentage van het totaal aantal woningen en vermeld bij 20 woningen of meer per buurt en wanneer het aandeel woningen met eigendom onbekend 50 procent of minder bedroeg.

`percentage_woningen_met_eigendom_onbekend` : Eigendom onbekend [%]

Woningen waarvan het eigendom niet afgeleid kon worden op basis van diverse registraties zoals het WOZ-register, Personenregister en het woningbestand Kadaster.

Peildatum: 1 januari van het desbetreffende jaar.

Het aantal is vermeld als percentage van het totaal aantal woningen en vermeld bij 20 woningen of meer per buurt en wanneer het aandeel woningen met eigendom onbekend 50 procent of minder bedroeg.

### Woningen naar bouwjaar

De aanduiding van het bouwjaar van een pand, waarin een woning zich bevindt. Oorspronkelijk als het pand bouwkundig gereed is of wordt opgeleverd. Latere wijziging aan een pand leidt niet tot wijziging van het bouwjaar. Bij een verblijfobject dat in meerdere panden is gelegen, wordt het oudste bouwjaar genomen.

De bouwjaarklasse heeft hier twee waarden:

1. in of na het jaar 2000 gebouwd;

2. vóór het jaar 2000 gebouwd.

`percentage_bouwjaarklasse_vanaf_2000` : Bouwjaarklasse vanaf 2000 [%]

Peildatum: 1 januari van het desbetreffende jaar.

Het aantal woningen met bouwjaar 2000 of later, uitgedrukt in hele procenten van het totaal aantal woningen. Het percentage is vermeld bij 20 woningen of meer per buurt.

`percentage_bouwjaarklasse_tot_2000` : Bouwjaarklasse tot 2000 [%]

Peildatum: 1 januari van het desbetreffende jaar.

Het aantal woningen met bouwjaar vóór 2000, uitgedrukt in hele procenten van het totaal aantal woningen. Het percentage is vermeld bij 20 woningen of meer per buurt.

## 5.5 ENERGIEVERBRUIK PARTICULIERE WONINGEN

### Gemiddeld aardgasverbruik

Het gemiddeld jaarverbruik voor aardgas van particuliere woningen berekend uit gegevens van de aansluitingenregisters van de energienetbedrijven.

Bij de berekening van het gemiddeld aardgasverbruik zijn woningen met een zeer laag of zelfs nulverbruik meegeteld indien er sprake is van stadsverwarming. Hierdoor valt in gebieden waar stadsverwarming aanwezig is het gemiddeld aardgasverbruik van woningen laag uit.

De cijfers zijn afgerond op vijftigtallen en worden vermeld bij zes of meer (bewoonde) woningen per woningtype of type eigendom (huur- of koopwoning).

`gemiddeld_gasverbruik_totaal`: Gemiddeld aardgasverbruik totaal [m3]

Het gemiddeld aardgasverbruik voor alle woningtypen samen.

### Gasverbruik naar woningtype

De volgende typen worden onderscheiden: appartement, tussenwoning, hoekwoning, twee-onder-één-kap-woning en vrijstaande woning. De typering wordt bepaald door het Kadaster.

`gemiddeld_gasverbruik_appartement` : Appartement [m3]

Een geheel van bij elkaar horende vertrekken als afzonderlijke woongelegenheid binnen een grotere woning waarbij de opdeling van het gebouw heeft plaatsgevonden volgens het appartementsrecht. Een bovenwoning of flat die geen appartement is wordt niet meegenomen bij het berekenen van de verbruikscijfers.

`gemiddeld_gasverbruik_tussenwoning` : Tussenwoning [m3]

`gemiddeld_gasverbruik_hoekwoning` : Hoekwoning [m3]

`gemiddeld_gasverbruik_2_onder_1_kap_woning` : Twee-onder-één-kap-woning [m3]

`gemiddeld_gasverbruik_vrijstaande_woning` : Vrijstaande woning [m3]

### Gasverbruik naar eigendom

De volgende typen worden onderscheiden: huur- of koopwoning. Deze informatie wordt samengesteld uit een koppeling tussen de Basisregistratie Adressen en Gebouwen (BAG) en het WOZ-register met een aanvulling uit het woningbestand van het Kadaster.

`gemiddeld_gasverbruik_huurwoning` : Gasverbruik huurwoning [m3]

Het gemiddelde aardgasverbruik van woningen in eigendom van 'toegelaten instellingen' (woningcorporaties), van institutionele beleggers of van particulieren die de woning verhuren aan de bewoner.

`gemiddeld_gasverbruikkoopwoning`: Gasverbruik koopwoning [m3]

Het gemiddelde aardgasverbruik van Woningen die eigendom zijn of worden van de (toekomstige) bewoners.

### Gemiddeld elektriciteitsverbruik

Het gemiddeld jaarverbruik voor elektriciteit op individuele aansluitingen van particuliere woningen, berekend uit gegevens van de aansluitingenregisters van de energienetbedrijven. De eigen opwekking van elektriciteit, bijvoorbeeld met zonnepanelen, is niet bekend en dus ook niet inbegrepen in het gemiddelde jaarverbruik. Ook collectieve verbruiken van bijvoorbeeld liftinstallaties of hal-/galerijverlichting zijn niet meegeteld bij de berekening. De cijfers zijn afgerond op vijftigtallen en worden vermeld bij zes of meer (bewoonde) woningen per woningtype of type eigendom (huur- of koopwoning).

`gemiddeld_elektriciteitsverbruik_totaal` : Gemiddeld elektriciteitsverbruik totaal [kWh]

Het gemiddeld elektriciteitsverbruik voor alle woningtypen samen.

### Elektriciteitsverbruik naar woningtype

De volgende typen worden onderscheiden: appartement, tussenwoning, hoekwoning, twee-onder-één-kap-woning en vrijstaande woning.

De typering wordt bepaald door het Kadaster.

`gemiddeld_elektriciteitsverbruik_appartement` : Appartement [kWh]

Een geheel van bij elkaar horende vertrekken als afzonderlijke woongelegenheid binnen een grotere woning waarbij de opdeling van het gebouw heeft plaatsgevonden volgens het appartementsrecht. Een bovenwoning of flat die geen appartement is wordt niet meegenomen bij het berekenen van de verbruikscijfers.

`gemiddeld_elektriciteitsverbruik_tussenwoning` : Tussenwoning [kWh]

`gemiddeld_elektriciteitsverbruik_hoekwoning` : Hoekwoning [kWh]

`gem_elektriciteitsverbruik_2_onder_1_kap_woning` : Twee-onder-één-kap-woning [kWh]

`gem_elektriciteitsverbruik_vrijstaande_woning` : Vrijstaande woning [kWh]

### Elektriciteitsverbruik naar eigendom

De volgende typen worden onderscheiden: huur- of koopwoning. Deze informatie wordt samengesteld uit een oppeling tussen de Basisregistratie Adressen en Gebouwen (BAG) en het WOZ-register met een aanvulling uit het woningbestand van het Kadaster.

`gemiddeld_elektriciteitsverbruik_huurwoning` : Huurwoning [kWh]

Het gemiddeld elektriciteitsverbruik van woningen in eigendom van 'toegelaten instellingen' (woningcorporaties), van institutionele beleggers of van particulieren die de woning verhuren aan de bewoner.

`gemiddeld_elektriciteitsverbruikkoopwoning` : Koopwoning [kWh]

Het gemiddeld elektriciteitsverbruik van woningen die eigendom zijn of worden van de (toekomstige) bewoners.

`percentage_woningen_met_stadsverwarming` : Percentage woningen met stadsverwarming [%]

Het percentage woningen dat is aangesloten op stadsverwarming.

Stadsverwarming is een verwarmingssysteem waarbij de woningen in een wijk worden verwarmd via een ondergronds netwerk van warmwaterleidingen. In veel gevallen maakt stadsverwarming gebruik van restwarmte van bijvoorbeeld elektriciteitscentrales. Het aardgasverbruik van deze woningen is in veel gevallen zeer laag of zelfs nul. De hoeveelheid warmte die door aangesloten woningen in een jaar wordt afgenomen van de stadsverwarming is niet beschikbaar. Het percentage is vermeld bij tien of meer (bewoonde) woningen. Voor de gemeentes is een percentage van minder dan vijf of groter dan 95 afgerond op vijftallen.

## 5.6 ARBEID

Deze variabelen geven per gemeente, wijk en buurt inzicht in de nettoarbeidsparticipatie en het percentage werknemers en zelfstandigen.

De nettoarbeidsparticipatie is vermeld als percentage van het totaal aantal personen van 15 tot 75 jaar en vermeld bij minimaal 150 inwoners in een buurt. Het percentage werknemers en het percentage zelfstandigen zijn vermeld bij minimaal 150 werkenden (van 15 tot 75 jaar) in een buurt.

`netto_arbeidsparticipatie` :  Nettoarbeidsparticipatie  [%] 

Het aandeel van de werkzame beroepsbevolking in de bevolking (beroeps- en niet-beroepsbevolking).

Deze definitie heeft betrekking op personen die in Nederland wonen (exclusief de institutionele bevolking). De gegevens worden meestal gepresenteerd
voor de bevolking van 15 tot 75 jaar.

Het betreft voorlopige cijfers.

`percentage_werknemers` : Percentage werknemers [%]

Een persoon die in een arbeidsovereenkomst afspraken met een economische eenheid maakt om arbeid te verrichten waartegenover een financiële beloning staat.

Als een persoon meer dan één baan of werkkring heeft, dan wordt uitgegaan van de baan of werkkring waaraan de meeste tijd wordt besteed.

Het betreft voorlopige cijfers.

`percentage_zelfstandigen` : Percentage zelfstandigen [%]

Een persoon die voor eigen rekening of risico arbeid verricht

- in een eigen bedrijf of praktijk (zelfstandig ondernemer),
- als directeur-grootaandeelhouder (dga),
- in het bedrijf of de praktijk van een gezinslid (meewerkend gezinslid), of
- als overige zelfstandige.

Als een persoon meer dan één baan of werkkring heeft, dan wordt uitgegaan van de baan of werkkring waaraan de meeste tijd wordt besteed.

Het betreft voorlopige cijfers.

## 5.7   INKOMEN

### Inkomen

De cijfers geven informatie over het persoonlijk inkomen van personen in particuliere huishoudens waarvan het inkomen is waargenomen en het inkomen van particuliere huishoudens met een waargenomen inkomen. De gegevens komen uit de Integrale Inkomens- en Vermogensstatistiek (IIVS) met als populatie de bevolking van Nederland op 1 januari van het verslagjaar met het inkomen over het verslagjaar.

De Integrale Inkomens- en Vermogensstatistiek van het CBS is voornamelijk gebaseerd op registers afkomstig van het Ministerie van Financiën (de fiscale registers) en de bevolkingsregisters van de Nederlandse gemeenten (Basisregistratie personen). De Basisregistratie personen is een register waarin alle inwoners van een gemeente behoren te zijn ingeschreven. Uitgezonderd zijn:

- Inwoners van Nederland die gebruik maken van uitzonderingsregels die gelden met betrekking tot opneming in de bevolkingsregisters (niet-Nederlandse diplomaten en niet-Nederlandse NAVO militairen).
- Zij mogen zelf bepalen of zij in de bevolkingsregisters ingeschreven worden of niet.
- Asielzoekers die korter dan zes maanden in de centrale opvang verblijven en nog geen verblijfsvergunning hebben gekregen.

### Inkomen van personen

De doelpopulatie bestaat uit personen in particuliere huishoudens waarvan het inkomen is waargenomen.

De inkomensgegevens zijn gebaseerd op het persoonlijk inkomen. Dit omvat de volgende bestanddelen van het bruto-inkomen van een persoon:

- inkomen uit arbeid;
- inkomen uit eigen onderneming;
- uitkering inkomensverzekeringen;
- uitkering sociale voorzieningen (met uitzondering van kinderbijslag).

`aantal_inkomensontvangers` : Aantal inkomensontvangers [aantal]

Personen met persoonlijk inkomen in particuliere huishoudens. De cijfers zijn afgerond op honderdtallen.

`gemiddeld_inkomen_per_inkomensontvanger` : Gemiddeld inkomen per inkomensontvanger [x 1 000 euro]

Het rekenkundig gemiddeld persoonlijk inkomen per persoon op basis van personen met persoonlijk inkomen die deel uitmaken van particuliere huishoudens.

De waarde is vermeld bij minimaal 100 personen met persoonlijk inkomen in particuliere huishoudens per regio.

`gemiddeld_inkomen_per_inwoner` : Gemiddeld inkomen per inwoner [x 1 000 euro]

Het rekenkundig gemiddeld persoonlijk inkomen per persoon op basis van de totale bevolking in particuliere huishoudens.

De waarde is vermeld bij minimaal 100 inwoners per regio.

`percentage_personen_met_laag_inkomen` : Personen met laagste inkomen [%]

Aandeel personen in particuliere huishoudens die behoren tot de landelijke 40% met laagste persoonlijk inkomen.

Personen met persoonlijk inkomen in particuliere huishoudens zijn ingedeeld naar hoogte van het persoonlijk inkomen.

De indeling vindt plaats nadat alle personen landelijk zijn gerangschikt van laag naar hoog persoonlijk inkomen. Tot de laagste 40-procent- groep worden de veertig procent personen met het laagste persoonlijk inkomen gerekend.

Het persoonlijk inkomen omvat inkomen uit arbeid, inkomen uit eigen onderneming, uitkering inkomensverzekeringen en uitkering sociale voorzieningen (met uitzondering van kinderbijslag).

Het percentage is vermeld bij minimaal 100 personen met persoonlijk inkomen in particuliere huishoudens per regio.

`percentage_personen_met_hoog_inkomen` : Personen met hoogste inkomen [%]

Aandeel personen in particuliere huishoudens die behoren tot de landelijke 20% met hoogste persoonlijk inkomen.

Personen met persoonlijk inkomen in particuliere huishoudens zijn ingedeeld naar hoogte van het persoonlijk inkomen.

De indeling vindt plaats nadat alle personen landelijk zijn gerangschikt van laag naar hoog persoonlijk inkomen. Tot de hoogste 20-procent- groep worden de twintig procent personen met het hoogste persoonlijk inkomen gerekend.

Het persoonlijk inkomen omvat inkomen uit arbeid, inkomen uit eigen onderneming, uitkering inkomensverzekeringen en uitkering sociale voorzieningen (met uitzondering van kinderbijslag).

Het percentage is vermeld bij minimaal 100 personen met persoonlijk inkomen in particuliere huishoudens per regio.

### Inkomen van huishoudens

De doelpopulatie bestaat uit particuliere huishoudens waarvan het inkomen bekend is.

`percentage_huishoudens_met_laagste_inkomen` : Huishoudens met laagste inkomen [%]

Aandeel particuliere huishoudens die behoren tot de landelijke 40% huishoudens met laagste huishoudensinkomen.

Particuliere huishoudens zijn ingedeeld naar hoogte van het besteedbaar huishoudensinkomen.

De indeling vindt plaats nadat huishoudens landelijk zijn gerangschikt van laag naar hoog besteedbaar huishoudensinkomen. Tot de laagste 40-procent-groep worden de veertig procent huishoudens met het laagste besteedbaar inkomen gerekend.

Het percentage is vermeld bij minimaal 100 particuliere huishoudens per regio.

Het besteedbaar inkomen van particuliere huishoudens bestaat uit het bruto-inkomen verminderd met:

- betaalde inkomensoverdrachten, zoals alimentatie van de ex- echtgeno(o)t(e);
- premies inkomensverzekeringen zoals premies betaald voor sociale verzekeringen, volksverzekeringen en particuliere verzekeringen in verband met werkloosheid, arbeidsongeschiktheid en ouderdom en nabestaanden;
- premies ziektekostenverzekeringen;
- belastingen op inkomen en vermogen.

`percentage_huishoudens_met_hoog_inkomen` : Huishoudens met hoogste inkomen [%]

Aandeel particuliere huishoudens die behoren tot de landelijke 20% huishoudens met hoogste huishoudensinkomen.

Particuliere huishoudens zijn ingedeeld naar hoogte van het besteedbaar huishoudensinkomen.

De indeling vindt plaats nadat huishoudens landelijk zijn gerangschikt van laag naar hoog besteedbaar huishoudensinkomen. Tot de hoogste 20-procent-groep worden de twintig procent huishoudens met het hoogste besteedbaar inkomen gerekend.

Het percentage is vermeld bij minimaal 100 particuliere huishoudens per regio.

Het besteedbaar inkomen van particuliere huishoudens bestaat uit het bruto-inkomen verminderd met:

- betaalde inkomensoverdrachten, zoals alimentatie van de ex- echtgeno(o)t(e);
- premies inkomensverzekeringen zoals premies betaald voor sociale verzekeringen, volksverzekeringen en particuliere verzekeringen in verband met werkloosheid, arbeidsongeschiktheid en ouderdom en nabestaanden;
- premies ziektekostenverzekeringen;
- belastingen op inkomen en vermogen.

`percentage_huishoudens_met_laag_inkomen` : Huishoudens met een laag inkomen[%]

Bij de bepaling van laag inkomen is van de particuliere huishoudens een aantal groepen niet meegenomen. Dit betreft enerzijds studentenhuishoudens en anderzijds huishoudens met een onvolledig jaarinkomen.
De doelpopulatie bestaat dan ook uit particuliere huishoudens waarvan de hoofdkostwinner (of eventuele partner) het gehele jaar inkomen heeft en niet afhankelijk is van studiefinanciering.

Om te bepalen of een huishouden een laag inkomen heeft, wordt het inkomen van een huishouden omgerekend tot het gestandaardiseerde inkomen (exclusief eventueel ontvangen huurtoeslag). Vervolgens wordt dit gestandaardiseerde inkomen (met het prijsindexcijfer) herleid naar het prijspeil in 2000. Het resulterende gestandaardiseerde en gedefleerde inkomen is laag wanneer het minder is dan 9249 euro.

Deze grens komt ongeveer overeen met de koopkracht van een bijstandsuitkering voor een alleenstaande in 1979 toen deze op zijn hoogst was.

Het percentage is vermeld bij minimaal 100 particuliere huishoudens behorende tot de doelpopulatie per regio.

`percentage_huishoudens_onder_of_rond_sociaal_minimum` : Huishouden onder of rond sociaal minimum [%]

Huishoudens onder of rond het sociaal minimum.

Bij de bepaling van het sociaal minimum is van de particuliere huishoudens een aantal groepen niet meegenomen. Dit betreft enerzijds studentenhuishoudens en anderzijds huishoudens met een onvolledig jaarinkomen. De doelpopulatie bestaat dan ook uit particuliere huishoudens waarvan de hoofdkostwinner (of eventuele partner) het gehele jaar inkomen heeft en niet afhankelijk is van studiefinanciering.

Het sociaal minimum is het wettelijk bestaansminimum zoals dat in de politieke besluitvorming is vastgesteld. Om te kunnen beoordelen hoe het inkomen zich verhoudt tot het minimum, is aan de hand van de regelgeving vastgesteld welke norm voor het desbetreffende huishouden van toepassing is. De norm voor een (echt)paar met uitsluitend minderjarige kinderen is bijvoorbeeld gelijkgesteld aan de bijstandsuitkering van een echtpaar, aangevuld met de (leeftijdsafhankelijke) kinderbijslag. Bij 65-plussers is het bedrag aan AOW-pensioen als norm gekozen. Het waargenomen inkomen van huishoudens, die uitsluitend op een bijstandsuitkering zijn aangewezen, wijkt in veel gevallen in geringe mate af van de vastgestelde normbedragen. Zouden de normbedragen als inkomensgrens worden gehanteerd, dan valt een deel van deze huishoudens met hun inkomen net boven het sociale minimum. Daarom is niet 100%, maar 101% van het sociaal minimum als inkomensgrens gehanteerd.

Het percentage is vermeld bij minimaal 100 huishoudens behorende tot de doelpopulatie per regio.

`gemiddeld_gestandaardiseerd_inkomen_van_huishoudens` : Gem. gestandaardiseerd inkomen van huish [x 1 000 euro]

Het besteedbaar inkomen gecorrigeerd voor verschillen in grootte en samenstelling van het huishouden. Deze correctie vindt plaats met behulp van equivalentiefactoren. In de equivalentiefactor komen de schaalvoordelen tot uitdrukking die het gevolg zijn van het voeren van een gemeenschappelijke huishouding. Met behulp van de equivalentiefactoren worden alle inkomens herleid tot het inkomen van een eenpersoonshuishouden. Op deze wijze zijn de welvaartsniveaus van huishoudens onderling vergelijkbaar gemaakt. Het gestandaardiseerd inkomen is een maat voor de welvaart van (de leden van) een huishouden.

Het betreft voorlopige cijfers.

`huishoudens_tot_110_percent_van_sociaal_minimum` : Huishoudens tot 110% van sociaal minimum [%]

Het besteedbaar huishoudensinkomen exclusief gebonden uitkeringen is lager dan 110 procent van het sociaal minimum. Het sociaal minimum is het wettelijk bestaansminimum dat in de politieke besluitvorming is vastgesteld. Tot aan de pensioengerechtigde leeftijd is het sociaal minimum gelijk aan de hoogte van de bijstandsuitkering en vanaf de pensioengerechtigde leeftijd is het ontleend aan het AOW-pensioen.

Voor huishoudens met kinderen zijn de kinderbijslag en het kindgebonden budget aan het normbedrag toegevoegd.

Het betreft voorlopige cijfers.

`huishoudens_tot_120_percent_van_sociaal_minimum` : Huishoudens tot 120% van sociaal minimum [%]

Het besteedbaar huishoudensinkomen exclusief gebonden uitkeringen is lager dan 120 procent van het sociaal minimum. Het sociaal minimum is het wettelijk bestaansminimum dat in de politieke besluitvorming is vastgesteld. Tot aan de pensioengerechtigde leeftijd is het sociaal minimum gelijk aan de hoogte van de bijstandsuitkering en vanaf de pensioengerechtigde leeftijd is het ontleend aan het AOW-pensioen.

Voor huishoudens met kinderen zijn de kinderbijslag en het kindgebonden budget aan het normbedrag toegevoegd.

Het betreft voorlopige cijfers.

`mediaan_vermogen_van_particuliere_huish` : Mediaan vermogen van particuliere huish. [x 1 000 euro]

De mediaan is het middelste getal wanneer alle getallen van laag naar hoog worden gesorteerd. Vermogen is het saldo van bezittingen en schulden. Bezittingen worden gevormd door bank- en spaartegoeden,
effecten, de eigen woning, overig onroerend goed, ondernemingsvermogen, aanmerkelijk belang en de overige bezittingen. De schulden omvatten onder meer schulden ten behoeve van een eigen woning en consumptief krediet.

Het betreft voorlopige cijfers.

## 5.8 ZORG

Deze variabelen geven per gemeente, wijk en buurt inzicht in het aantal personen dat gebruik maakte van jeugdzorg in natura en/of een maatwerkarrangement in het kader van de Wet maatschappelijke ondersteuning.

De cijfers zijn afgerond op vijftallen. Om het risico op onthulling van individuen te voorkomen zijn de waarden 0 tot en met 7 weergegeven als geheim. Hierdoor kan het voorkomen, dat de som van de detailgegevens afwijkt van het totaal.

`aantal_jongeren_met_jeugdzorg_in_natura` : Jongeren met jeugdzorg in natura [aantal]

Personen tot 23 jaar die op enig moment in de verslagperiode gebruik gemaakt hebben van jeugdhulp in natura, jeugdbescherming of jeugdreclassering.

Jeugdhulp in natura wordt direct vergoed aan de zorgverlener zonder tussenkomst van de zorggebruiker. In het kader van de jeugdzorg betekent dit dat de hulp rechtstreeks door de gemeente wordt vergoed. Jeugdhulp bekostigd via PGB is hier dus van uitgesloten.

Persoonsgebonden budget (PGB) is een geldbedrag waarmee de zorggebruiker zelf zorg, begeleiding, hulp, hulpmiddelen of voorzieningen in kan kopen. Deze wordt verstrekt via de Sociale verzekeringsbank (SVB) maar is ook afkomstig van de gemeente.

Jeugdhulp is hulp en zorg zoals deze bedoeld en beschreven is in de Jeugdwet (2014). Het betreft hulp en zorg aan jongeren en hun ouders bij psychische, psychosociale en of gedragsproblemen, een verstandelijke beperking van de jongere, of opvoedingsproblemen van de ouders.

Jeugdhulp omvat zowel lichte jeugd- en opvoedhulp, jeugd geestelijke gezondheidszorg en zorg voor licht verstandelijk beperkte jongeren. Er zijn ambulante vormen van jeugdhulp (die door het wijkteam of door een jeugdhulpaanbieder kunnen worden geleverd) en vormen van jeugdhulp met verblijf (zoals pleegzorg, gesloten plaatsing en residentiële jeugdhulp). Jeugdhulp kan zowel gericht zijn op behandelen als op begeleiden.

Jeugdbescherming is een maatregel die de rechter dwingend oplegt. Het doel van de kinderbeschermingsmaatregelen is het opheffen van de bedreiging voor de veiligheid en ontwikkeling van het kind. Een kind of jongere wordt dan 'onder toezicht gesteld' of ‘onder voogdij geplaatst’.

Jeugdreclassering is een combinatie van begeleiding en controle voor jongeren vanaf 12 jaar, die voor hun 18e verjaardag met de politie of leerplichtambtenaar in aanraking zijn geweest en een proces-verbaal hebben gekregen. Indien de persoonlijkheid van de dader of de omstandigheden waaronder de overtreding of het misdrijf is begaan daartoe aanleiding geven, bijvoorbeeld bij jongvolwassenen met een verstandelijke beperking, kan het jeugdstrafrecht eveneens worden toegepast op jongvolwassenen in de leeftijd 18 tot en met 22 jaar. De jongere krijgt op maat gesneden begeleiding van een jeugdreclasseringswerker om te voorkomen dat hij of zij opnieuw de fout ingaat. Jeugdreclassering kan worden opgelegd door de kinderrechter of de officier van Justitie. Jeugdreclassering kan ook op initiatief van de Raad voor de Kinderbescherming in het vrijwillige kader worden opgestart.

### Indeling naar gemeente, wijk en buurt

De indeling naar gemeente en wijk is gebaseerd op het adres van de gezagsdrager van de jongere. Er is uitgegaan van het woonplaatsbeginsel zoals dat is toegepast in de Jeugdwet die vanaf 2015 in werking is getreden. Wanneer het adres gedurende de verslagperiode is gewijzigd krijgt de jongere in deze tabel het meest recente adres toegewezen.

Voor sommige jongeren is alleen de gemeente volgens woonplaatsbeginsel bekend, maar niet het specifieke adres. In deze gevallen wordt de jongere wel meegeteld in het totaal voor de gemeente, maar niet in één van de onderliggende wijken. Hierdoor kan het voorkomen dat de cijfers van de wijken binnen een gemeente niet optellen tot het totaal van de gemeente.

`percentage_jongeren_met_jeugdzorg_in_natura` : Percentage jongeren met jeugdzorg [%]

Percentage van personen tot 23 jaar die op enig moment in de verslagperiode gebruik gemaakt hebben van jeugdhulp, jeugdbescherming of jeugdreclassering.

`aantal_wmo_clienten` : Wmo-cliënten [aantal]

Aantal personen dat ten minste één maatwerkarrangement in het kader van de Wet maatschappelijke ondersteuning (Wmo) heeft gehad. Deze cijfers zijn samengesteld op basis van gegevens die gemeenten aan CBS hebben geleverd in het kader van de Gemeentelijke Monitor Sociaal Domein.

### Maatwerkarrangement

Ondersteuning binnen het kader van de Wmo2015 geleverd in de vorm van een product of dienst die is afgestemd op de wensen, persoonskenmerken mogelijkheden en behoeften van een individu.

### Wmo2015

Wet maatschappelijke ondersteuning zoals ingegaan op 1 januari 2015. Deze wet stelt gemeenten verantwoordelijk voor het ondersteunen van de zelfredzaamheid en participatie van mensen met een beperking, chronische psychische of psychosociale problemen.

### Regio

Alleen de gegevens van gemeenten die aangeleverd hebben en die toestemming hebben gegeven voor publicatie worden gepubliceerd. Gemeenten kunnen daarbij apart toestemming geven voor de basisvariabelen Wmo en de facultatieve variabelen Wmo. Als gemeenten herlevering doen over eerdere verslagperioden, is de toestemming voor publicatie zoals die bij de herlevering is gegeven, leidend.

De cijfers over het totaal aantal cliënten in Nederland zijn geschat met een regressiemodel op de data van de deelnemende gemeenten. Voor meer informatie over deze methode wordt verwezen naar de onderzoeksbeschrijving Gemeentelijke monitor sociaal domein, Wmo.

`aantal_wmo_clienten_per_1000_inwoners` : Wmo- cliënten relatief [per 1000 inwoners]

Het aantal Wmo-cliënten per 1000 inwoners dat ten minste één maatwerkarrangement in het kader van de Wet maatschappelijke ondersteuning (Wmo) heeft gehad. De relatieve cijfers zijn berekend na het afronden van de absolute cijfers.

## 5.9 SOCIALE ZEKERHEID

Deze tabel geeft per gemeente, wijk en buurt inzicht in het aantal personen dat een uitkering ontvangt op grond van arbeidsongeschiktheid, bijstand, werkloosheid en AOW.

Het is mogelijk dat een persoon aanspraak maakt op meer dan één uitkering. Dat kunnen uitkeringen zijn van eenzelfde soort (bijvoorbeeld twee uitkeringen op grond van de Wet op de arbeidsongeschiktheidsverzekering (WAO) of twee uitkeringen van verschillende soort (zoals een uitkering op grond van de Werkloosheidswet en een bijstandsuitkering). In het laatste geval wordt de persoon bij beide soorten uitkeringen meegeteld, in het eerste geval slechts één keer (bij de WAO).

Bij de categorie personen met een uitkering (totaal) wordt de persoon uiteraard ook maar één keer geteld.

### Uitkeringen Algemene bijstand (ABW/WWB/Participatiewet)

**Wet werk en bijstand (WWB)**

Wettelijke sociale voorziening die op 1 januari 2004 in werking is getreden ter vervanging van de Algemene bijstandswet (Abw), de Wet inschakeling werkzoekenden (WIW) en het Besluit In- en Doorstroombanen (ID-banen).

De WWB was tot 1 januari 2015 de wet die in Nederland de ondersteuning bij arbeidsinschakeling en bijstand regelde voor mensen die weinig of geen ander inkomen (waaronder andere uitkeringen) hebben en ook weinig of geen vermogen.

De wet is per 1 januari 2015 gewijzigd en heet sindsdien Participatiewet.

**Participatiewet**

De Participatiewet vervangt sinds 1 januari 2015 de Wet werk en bijstand (WWB), de Wet Sociale Werkvoorziening (WsW) en een groot deel van de Wet werk en arbeidsondersteuning jonggehandicapten (wet Wajong).

De wet regelt in Nederland de ondersteuning bij arbeidsinschakeling en het verlenen van bijstand door gemeenten voor mensen die weinig of geen ander inkomen (waaronder andere uitkeringen) hebben en ook weinig of geen vermogen.

Werk gaat voor inkomen: oogmerk van de wet is om mensen met of zonder arbeidsbeperking op de kortste weg naar betaald werk te kunnen zetten.

De gemeenten voeren de wet uit en bepalen, binnen de wettelijke grenzen, hun eigen beleid.

De AOW-leeftijd is de leeftijd waarop recht is ontstaan op het basispensioen van de Rijksoverheid op grond van de Algemene Ouderdomswet (AOW).

Tot 1 januari 2013 was de AOW-leeftijd 65 jaar. Vanaf die datum gaat de AOW-leeftijd jaarlijks met één of meerdere maanden omhoog. Zo was de AOW-leeftijd in 2013 65 jaar en één maand, in 2014 was die leeftijd 65 jaar en twee maanden.

De AOW-leeftijd wordt vanaf 2016 in stappen van 3 maanden verhoogd en vanaf 2018 in stappen van 4 maanden. Daarmee wordt de AOW- leeftijd 66 jaar in 2018 en 67 jaar in 2021. Vanaf 2022 wordt de AOW-leeftijd gekoppeld aan de levensverwachting.

`aantal_personen_met_een_alg_bijstandsuitkering_tot` : Algemene bijstandsuitkeringen totaal [absoluut]

Personen die een bijstandsuitkering op grond van de Wet werk en bijstand (WWB, tot 1 januari 2015) of de Participatiewet (vanaf 1 januari 2015) ontvangen.

Het gaat om algemeen periodieke uitkeringen aan thuiswonende personen tot de AOW-leeftijd.

`aantal_personen_met_een_aow_uitkering_totaal` : Personen met een AOW-uitkering totaal [aantal]

Personen die een basispensioen van de Rijksoverheid ontvangen op grond van de Algemene Ouderdomswet (AOW).

De AOW is een algemene, de gehele bevolking omvattende, verplichte verzekering die personen met de AOW-gerechtigde leeftijd een inkomen garandeert. In het Nederlandse sociale zekerheidsstelsel is dit een volksverzekering.

In principe is iedereen die nog niet de AOW-gerechtige leeftijd heeft bereikt en in Nederland woont, verzekerd voor de AOW.

Ook degenen die niet in Nederland wonen, maar in Nederland in dienstbetrekking arbeid verrichten waarover loonbelasting wordt betaald, zijn verzekerd.

Voor perioden die men in het buitenland woont, kan men zich verzekeren tegen verlies van aanspraak op een AOW-uitkering. Een uitkering kan, binnen het kader van de wet Beperking export uitkeringen (wet BEU), naar het buitenland worden overgemaakt.

De AOW-leeftijd is de leeftijd waarop recht is ontstaan op het basispensioen van de Rijksoverheid op grond van de Algemene Ouderdomswet (AOW).

Tot 1 januari 2013 was de AOW-leeftijd 65 jaar. Vanaf die datum gaat de AOW-leeftijd jaarlijks met één of meerdere maanden omhoog. Zo was de AOW-leeftijd in 2013 65 jaar en één maand, in 2014 was die leeftijd 65 jaar en twee maanden.

De AOW-leeftijd wordt vanaf 2016 in stappen van 3 maanden verhoogd en vanaf 2018 in stappen van 4 maanden. Daarmee wordt de AOW- leeftijd 66 jaar in 2018 en 67 jaar in 2021. Vanaf 2022 wordt de AOW-leeftijd gekoppeld aan de levensverwachting.

`aantal_personen_met_een_ao_uitkering_totaal` : AO- uitkeringen totaal [absoluut]

Personen die een arbeidsongeschiktheidsuitkering ontvangen op grond van de Wet op de arbeidsongeschiktheidsverzekering (WAO), de Wet arbeidsongeschiktheidsverzekering zelfstandigen (WAZ), de Wet werk en Inkomen naar arbeidsvermogen (WIA), de Wet arbeidsongeschiktheidsvoorziening jonggehandicapten (Wajong) en de Wet werk en arbeidsondersteuning jonggehandicapten (wet Wajong).

De wet op de arbeidsongeschiktheidsverzekering (WAO) heeft als doel om personen in loondienst te verzekeren van een loonvervangende uitkering bij langdurige arbeidsongeschiktheid.

De wet arbeidsongeschiktheidsverzekering zelfstandigen (WAZ) is een verplichte verzekering voor zelfstandigen, beroepsbeoefenaren, directeuren-grootaandeelhouders en meewerkende echtgenoten tegen de financiële gevolgen van langdurige arbeidsongeschiktheid.

De WAZ is met ingang van 1 augustus 2004 geblokkeerd.

De wet arbeidsongeschiktheidsvoorziening jonggehandicapten (Wajong) is een wettelijke voorziening in de financiële gevolgen van langdurige arbeidsongeschiktheid van mensen die geen aanspraak kunnen maken op de WAO/WIA omdat er geen arbeidsverleden is opgebouwd.

Dit zijn mensen die arbeidsongeschikt zijn voor de dag dat zij 17 jaar worden of na hun 17e jaar arbeidsongeschikt worden en een opleiding of studie volgen.

Met ingang van 1 januari 2010 is de Wet werk en arbeidsondersteuning jonggehandicapten (Wet Wajong) in werking getreden.

In tegenstelling tot de 'oude' Wajong hebben jongeren met een ziekte of handicap in de eerste plaats recht op hulp bij het vinden en houden van werk. Daaraan gekoppeld kunnen ze een inkomensondersteuning krijgen.

De 'oude' Wajong blijft gelden voor jongeren die voor 1 januari 2010 een uitkering hebben aangevraagd.

De werk en inkomen naar arbeidsvermogen (WIA) geeft werknemers die na een wachttijd van twee jaar nog minstens 35 procent arbeidsongeschikt zijn, recht op een uitkering. De wet is zo opgezet dat een persoon
gestimuleerd wordt om naar vermogen te werken. De WIA kent twee regelingen: de regeling inkomensvoorziening volledig

arbeidsongeschikten (IVA) en de regeling werkhervatting gedeeltelijk arbeidsgeschikten (WGA).

De IVA regelt een loonvervangende uitkering voor werknemers die volledig en duurzaam arbeidsongeschikt zijn.

De WGA regelt een aanvulling op het met arbeid verdiende inkomen of een minimumuitkering als men niet of onvoldoende werkt.

`aantal_personen_met_een_ww_uitkering_totaal` : WW- uitkeringen totaal [absoluut]

Personen die een uitkering ontvangen op grond van de Werkloosheidswet (WW).

De werkloosheidswet (WW) heeft tot doel werknemers te verzekeren tegen de financiële gevolgen van werkloosheid. De wet voorziet in een uitkering die gerelateerd is aan het laatstverdiende inkomen uit dienstbetrekking. De duur van de uitkering is afhankelijk van het arbeidsverleden van de verzekerde. Het Uitvoeringsinstituut Werknemersverzekeringen (UWV) beoordeelt of men voor een WW- uitkering in aanmerking komt.

## 5.10 MOTORVOERTUIGEN

De motorvoertuigen betreffen personenauto's, bedrijfsauto’s en motortweewielers, op 1 januari. Aanhangwagens en opleggers zijn niet meegerekend.

De gegevens zijn ontleend aan de Statistiek van de Motorvoertuigen. Deze gegevens zijn gebaseerd op de kentekenregistratie van de Rijksdienst voor het Wegverkeer (RDW). Met behulp van deze registratie zijn tellingen gemaakt van alle voertuigen met actuele, houderschapsplichtige kentekens die op 1 januari in het kentekenbestand voorkomen.

Het aantal geregistreerde motorvoertuigen is inclusief voertuigen van lease- en verhuurbedrijven. Deze motorvoertuigen staan geregistreerd op het adres van het lease- of verhuurbedrijf. De motorvoertuigen die staan ingeschreven op postbusadressen zijn niet meegeteld bij de aantallen van de wijken en buurten, maar wel in de gemeentelijke totalen. De wijken en buurten tellen daarom niet altijd op tot gemeenten. De gemeentelijke totalen komen overeen met de Regionale Kerncijfers Nederland.

`personenautos_totaal` : Personenauto’s totaal [absoluut]

**Personenauto**

Motorvoertuig voor personenvervoer over de weg, exclusief brom- en motorfietsen, met maximaal negen zitplaatsen (met inbegrip van de bestuurdersplaats).

Hieronder vallen personenauto's, bestelwagens ontworpen voor en voornamelijk gebruikt voor het vervoer van reizigers, taxi's, huurauto's, ziekenwagens en campers. Lichte wegvoertuigen voor goederenvervoer over de weg, touringcars, autobussen en minibussen vallen hier niet onder. Het begrip personenauto omvat ook taxi's en huurauto's met minder dan tien zitplaatsen. Vanaf 1 mei 2009 worden campers gekentekend als personenauto of als bus afhankelijk van het aantal zitplaatsen. Vóór die datum zijn campers geregistreerd als speciale voertuigen.

`personenautos_per_huishouden` : Personenauto's per huishouden [per huishouden]

Het aantal personenauto's per (particulier) huishouden op 1 januari. De personenauto's worden regionaal ingedeeld met behulp van de kentekenregistratie. Personenauto's die geregistreerd staan op het adres van het lease- of verhuurbedrijf vertekenen daarom de autodichtheid per huishouden.

Het aantal personenauto's per huishouden is vermeld bij minimaal 50 huishoudens en bij een waarde van maximaal 2,5 personenauto’s per huishouden.

`personenautos_per_km2`: Personenauto's naar oppervlakte [per km2]

Het aantal personenauto's per km² land op 1 januari. De personenauto's worden regionaal ingedeeld met behulp van de kentekenregistratie.

Personenauto's die geregistreerd staan op het adres van het lease- of verhuurbedrijf vertekenen daarom de autodichtheid per oppervlakte. Het aantal personenauto's naar oppervlakte is vermeld als ook het aantal personenauto's per huishouden is gepubliceerd. Dat is bij minimaal 50 huishoudens en bij een waarde van maximaal 2,5 personenauto's per huishouden.

`motortweewielers_totaal` : Motortweewielers totaal [absoluut]

**Motorfiets**

Voertuig voor het wegverkeer op twee, drie of vier wielen met een onbeladen gewicht van maximaal 400 kg. Dergelijke motorvoertuigen met een cilinderinhoud van meer dan 50 cm³ vallen hieronder, alsook motorvoertuigen met een cilinderinhoud van minder dan 50 cm³ die niet aan de definitie van bromfiets beantwoorden.

### Personenauto’s naar kenmerken

Twee kernmerken van de personenauto’s zijn opgenomen: de leeftijd van het voertuig en soort brandstof.

`aantal_personenautos_met_brandstof_benzine` : Personenauto’s; brandstof benzine [aantal]

Het aantal personenauto’s rijdend op benzine.

`aantal_personenautos_met_overige_brandstof` : Personenauto’s; overige brandstof [aantal]

Het aantal personenauto's met overige brandstof. Hieronder vallen: diesel, LPG, elektriciteit (incl. Hybride), waterstof, alcohol, LNG en CNG.

## 5.11 OPPERVLAKTE

Voor de bepaling van oppervlaktecijfers is voor de gemeentegrenzen gebruikgemaakt van het digitale gemeentegrenzenbestand van het Kadaster en voor de wijk- en buurtgrenzen binnen de gemeenten van het digitale wijk- en buurtgrenzenbestand van het CBS.

Met ingang van 2011 wordt het bestand Burgerlijke gemeentegrenzen van het Kadaster gebruikt als basis voor de gemeentegrenzen, in tegenstelling tot het bestand Topgrenzen, de gemeentegrenzen van de voormalige Topografische Dienst, wat in 2010 en voorgaande jaren is gebruikt.

Vanwege kleine grensverschillen tussen beide gemeentegrenzenbestanden zullen daarom kleine afwijkingen in oppervlakte voor bijna alle gemeenten gerapporteerd worden, ook voor gemeenten waarvan de gemeentegrenzen niet officieel gewijzigd zijn. Met totale oppervlakte per gemeente wordt de oppervlakte inclusief het gemeentelijk ingedeeld buitenwater bedoeld. Bij oppervlaktecijfers over wijken en buurten is de oppervlakte land en water opgenomen exclusief buitenwater. Door dit laatste kan de optelling van de wijken of buurten verschillen met de gepubliceerde totalen per gemeente. Deze verschillen doen zich vooral voor bij kustgemeenten.

`oppervlakte_totaal_in_ha` : Oppervlakte totaal [ha]

De totale oppervlakte is de som van de oppervlakten water en land in hele hectaren (ha.).

`oppervlakte_land_in_ha` : Oppervlakte land [ha]

De oppervlakte land is bepaald door het meest recente digitale bestand Bodemgebruik te combineren met het digitale bestand van gemeente-, wijk- en buurtgrenzen.

Voor de jaren 2020, 2021 en 2022 is uitgegaan van het bestand Bodemgebruik 2015.

De oppervlakte land wordt uitgedrukt in hele hectaren (ha.).

`oppervlakte_water_in_ha` : Oppervlakte water [ha]

Oppervlakte water omvat zowel binnen- als buitenwater. Tot binnenwater wordt gerekend alle water niet onderhevig aan getijden en breder dan 6 meter, zoals het IJsselmeer, Markermeer, Randmeren, sloten, rivieren, kanalen en dergelijke. Onder het buitenwater valt alle water onderhevig aan getijden, zoals de Waddenzee, Oosterschelde, Westerschelde en het gemeentelijk ingedeelde gedeelte van de Noordzee.

De oppervlakte water is bepaald door het meest recente digitale bestand Bodemgebruik te combineren met het digitale bestand van gemeente-, wijk- en buurtgrenzen.

Voor 2021, 2022 en 2023 is uitgegaan van het bestand Bodemgebruik 2017.

Het buitenwater is alleen op gemeenteniveau vermeld, water per wijk of buurt bestaat alleen uit binnenwater. De oppervlakte water wordt uitgedrukt in hele hectaren (ha.).

## 5.12 VOORZIENINGEN

Voorzieningen zijn locaties die bezocht kunnen worden door personen. De locatie sluit aan bij het gebruik in het dagelijks leven. Dit zijn onder andere instellingen van de gezondheidszorg, culturele instellingen, scholen en opritten van een hoofdverkeersweg.

De afstand tot een voorziening is berekend over verharde, door auto's te gebruiken wegen, dus niet over fiets- en voetpaden. Overtochten via veerboten zijn hierbij inbegrepen. Er wordt geen rekening gehouden met éénrichtingsverkeer en overige inrijverboden van toegangswegen tot rijks- of provinciale wegen.

De gemiddelde afstand is opgenomen wanneer van 90 procent of meer van de inwoners in de buurt de exacte ligging (x,y-coördinaat) van het adres kon worden vastgesteld. Daarnaast geldt dat het gemiddelde alleen is vermeld bij minimaal 10 inwoners per buurt.

`huisartsenpraktijk_gemiddelde_afstand_in_km` : Afstand tot huisartsenpraktijk [km]

Huisartsenpraktijk: Pand of ruimte waarin een of meer huisartsen (samen) werken.

Huisarts: De huisarts is verantwoordelijk voor de algemene medische zorg. Hij/zij geeft persoonlijke en continue zorg aan een vaste praktijkpopulatie.

De gemiddelde afstand van alle inwoners in een gebied tot de dichtstbijzijnde huisartsenpraktijk, berekend over de weg.

`huisartsenpraktijk_gemiddeld_aantal_binnen_1_km` : Aantal huisartsenpraktijken [absoluut]

Het gemiddeld aantal huisartsenpraktijken binnen 1 kilometer over de weg voor alle inwoners van een gebied.

`huisartsenpraktijk_gemiddeld_aantal_binnen_3_km` : Aantal huisartsenpraktijken [absoluut]

Het gemiddeld aantal huisartsenpraktijken binnen 3 kilometer over de weg voor alle inwoners van een gebied.

`huisartsenpraktijk_gemiddeld_aantal_binnen_5_km` : Aantal huisartsenpraktijken [absoluut]

Het gemiddeld aantal huisartsenpraktijken binnen 5 kilometer over de weg voor alle inwoners van een gebied.

`huisartsenpost_gemiddelde_afstand_in_km` : Aantal huisartsenposten [absoluut]

De gemiddelde afstand van alle inwoners in een gebied tot de dichtstbijzijnde huisartsenpost, berekend over de weg.

Huisartsenpost: plaats waar huisartsen uit de regio de avond-, nacht- en weekenddiensten verzorgen

`apotheek_gemiddelde_afstand_in_km` : Afstand tot apotheek [km]

De gemiddelde afstand van alle inwoners in een gebied tot de dichtstbijzijnde apotheek of apotheekhoudende huisarts, berekend over de weg.

`ziekenhuis_excl_buitenpolikliniek_gem_afst_in_km` : Afstand tot ziekenhuis excl. Buitenpolikliniek [km]

De gemiddelde afstand van alle inwoners in een gebied tot het dichtstbijzijnde ziekenhuis, berekend over de weg.

In een ziekenhuis kunnen patiënten voor meer dan 24 uur opgenomen worden en er kunnen grote operaties worden uitgevoerd. Een buitenpolikliniek is een locatie van een ziekenhuis waar niet bedlegerige patiënten worden behandeld of gecontroleerd. Patiënten worden er niet voor meer dan 24 uur opgenomen en er worden geen grote operaties uitgevoerd.

`ziekenhuis_excl_buitenpoli_gem_aantal_binnen_5_km` : Aantal ziekenhuizen excl. Buitenpolikliniek [absoluut]

Het gemiddeld aantal ziekenhuizen binnen 5 kilometer over de weg voor alle inwoners van een gebied.

In een ziekenhuis kunnen patiënten voor meer dan 24 uur opgenomen worden en er kunnen grote operaties worden uitgevoerd. Een buitenpolikliniek is een locatie van een ziekenhuis waar niet bedlegerige patiënten worden behandeld of gecontroleerd. Patiënten worden er niet voor meer dan 24 uur opgenomen en er worden geen grote operaties uitgevoerd.

`ziekenhuis_excl_buitenpoli_gem_aantal_binnen_10_km` : Aantal ziekenhuizen excl. Buitenpolikliniek [absoluut]

Het gemiddeld aantal ziekenhuizen binnen 10 kilometer over de weg voor alle inwoners van een gebied.

In een ziekenhuis kunnen patiënten voor meer dan 24 uur opgenomen worden en er kunnen grote operaties worden uitgevoerd. Een buitenpolikliniek is een locatie van een ziekenhuis waar niet bedlegerige patiënten worden behandeld of gecontroleerd. Patiënten worden er niet voor meer dan 24 uur opgenomen en er worden geen grote operaties uitgevoerd.

`ziekenhuis_excl_buitenpoli_gem_aantal_binnen_20_km` : Aantal ziekenhuizen excl. buitenpolikliniek [absoluut]

Het gemiddeld aantal ziekenhuizen binnen 20 kilometer over de weg voor alle inwoners van een gebied.

In een ziekenhuis kunnen patiënten voor meer dan 24 uur opgenomen worden en er kunnen grote operaties worden uitgevoerd. Een buitenpolikliniek is een locatie van een ziekenhuis waar niet bedlegerige patiënten worden behandeld of gecontroleerd. Patiënten worden er niet voor meer dan 24 uur opgenomen en er worden geen grote operaties uitgevoerd.

`ziekenhuis_incl_buitenpolikliniek_gem_afst_in_km` : Afstand tot ziekenhuis incl. buitenpolikliniek [km]

De gemiddelde afstand van alle inwoners in een gebied tot het dichtstbijzijnde ziekenhuis, berekend over de weg.

In een ziekenhuis kunnen patiënten voor meer dan 24 uur opgenomen worden en er kunnen grote operaties worden uitgevoerd. Een buitenpolikliniek is een locatie van een ziekenhuis waar niet bedlegerige patiënten worden behandeld of gecontroleerd. Patiënten worden er niet voor meer dan 24 uur opgenomen en er worden geen grote operaties uitgevoerd.

`ziekenhuis_incl_buitenpoli_gem_aantal_binnen_5_km` : Aantal ziekenhuizen incl. buitenpolikliniek [absoluut]

Het gemiddeld aantal ziekenhuizen binnen 5 kilometer over de weg voor alle inwoners van een gebied.

In een ziekenhuis kunnen patiënten voor meer dan 24 uur opgenomen worden en er kunnen grote operaties worden uitgevoerd. Een buitenpolikliniek is een locatie van een ziekenhuis waar niet bedlegerige patiënten worden behandeld of gecontroleerd. Patiënten worden er niet voor meer dan 24 uur opgenomen en er worden geen grote operaties uitgevoerd.

`ziekenhuis_incl_buitenpoli_gem_aantal_binnen_10_km` : Aantal ziekenhuizen incl. buitenpolikliniek [absoluut]

Het gemiddeld aantal ziekenhuizen binnen 10 kilometer over de weg voor alle inwoners van een gebied.

In een ziekenhuis kunnen patiënten voor meer dan 24 uur opgenomen worden en er kunnen grote operaties worden uitgevoerd. Een buitenpolikliniek is een locatie van een ziekenhuis waar niet bedlegerige patiënten worden behandeld of gecontroleerd. Patiënten worden er niet voor meer dan 24 uur opgenomen en er worden geen grote operaties uitgevoerd.

`ziekenhuis_incl_buitenpoli_gem_aantal_binnen_20_km` : Aantal ziekenhuizen incl. buitenpolikliniek [absoluut]

Het gemiddeld aantal ziekenhuizen binnen 20 kilometer over de weg voor alle inwoners van een gebied.

In een ziekenhuis kunnen patiënten voor meer dan 24 uur opgenomen worden en er kunnen grote operaties worden uitgevoerd. Een buitenpolikliniek is een locatie van een ziekenhuis waar niet bedlegerige patiënten worden behandeld of gecontroleerd. Patiënten worden er niet voor meer dan 24 uur opgenomen en er worden geen grote operaties uitgevoerd.

`grote_supermarkt_gemiddelde_afstand_in_km` : Afstand tot grote supermarkt [km]

De gemiddelde afstand van alle inwoners in een gebied tot de dichtstbijzijnde grote supermarkt, berekend over de weg.

Een grote supermarkt is een winkel met meerdere soorten dagelijkse artikelen en een minimale oppervlakte van 150 m2.

`grote_supermarkt_gemiddeld_aantal_binnen_1_km` : Aantal grote supermarkten [absoluut]

Het gemiddeld aantal grote supermarkten binnen 1 kilometer over de weg voor alle inwoners van een gebied.

Een grote supermarkt is een winkel met meerdere soorten dagelijkse artikelen en een minimale oppervlakte van 150 m2.

`grote_supermarkt_gemiddeld_aantal_binnen_3_km` : Aantal grote supermarkten [absoluut]

Het gemiddeld aantal grote supermarkten binnen 3 kilometer over de weg voor alle inwoners van een gebied.

Een grote supermarkt is een winkel met meerdere soorten dagelijkse artikelen en een minimale oppervlakte van 150 m2.

`grote_supermarkt_gemiddeld_aantal_binnen_5_km` : Aantal grote supermarkten [absoluut]

Het gemiddeld aantal grote supermarkten binnen 5 kilometer over de weg voor alle inwoners van een gebied.

Een grote supermarkt is een winkel met meerdere soorten dagelijkse artikelen en een minimale oppervlakte van 150 m2.

`winkels_ov_dagelijkse_levensm_gem_afst_in_km` : Afstand tot ov. dagel. levensmiddelen [km]

De gemiddelde afstand van alle inwoners in een gebied tot de dichtstbijzijnde overige winkels voor dagelijkse levensmiddelen, berekend over de weg.

Voorbeelden van overige winkels voor dagelijkse levensmiddelen zijn groenteboer, bakker, vlaaienwinkel, toko, chocoladewinkel, koffie/theewinkel, delicatessenwinkel, kaaswinkel, mini supermarkt, notenwinkel, poelier, reformwinkel, slagerij, slijterij, tabakswinkel, visboer, zoetwarenwinkel, nachtwinkel, wijnwinkel en ziekenhuiswinkel.

`winkels_ov_dagel_levensm_gem_aantal_binnen_1_km` : Aantal overige dagelijkse levensmiddelen [absoluut]

Het gemiddeld aantal overige winkels voor dagelijkse levensmiddelen binnen 1 kilometer over de weg voor alle inwoners van een gebied.

Voorbeelden van overige winkels voor dagelijkse levensmiddelen zijn groenteboer, bakker, vlaaienwinkel, toko, chocoladewinkel, koffie/theewinkel, delicatessenwinkel, kaaswinkel, mini supermarkt, notenwinkel, poelier, reformwinkel, slagerij, slijterij, tabakswinkel, visboer, zoetwarenwinkel, nachtwinkel, wijnwinkel en ziekenhuiswinkel.

`winkels_ov_dagel_levensm_gem_aantal_binnen_3_km` : Aantal overige dagelijkse levensmiddelen [absoluut]

Het gemiddeld aantal overige winkels voor dagelijkse levensmiddelen binnen 3 kilometer over de weg voor alle inwoners van een gebied.

Voorbeelden van overige winkels voor dagelijkse levensmiddelen zijn groenteboer, bakker, vlaaienwinkel, toko, chocoladewinkel, koffie/theewinkel, delicatessenwinkel, kaaswinkel, mini supermarkt, notenwinkel, poelier, reformwinkel, slagerij, slijterij, tabakswinkel, visboer, zoetwarenwinkel, nachtwinkel, wijnwinkel en ziekenhuiswinkel.

`winkels_ov_dagel_levensm_gem_aantal_binnen_5_km` : Aantal overige dagelijkse levensmiddelen [absoluut]

Het gemiddeld aantal overige winkels voor dagelijkse levensmiddelen binnen 5 kilometer over de weg voor alle inwoners van een gebied.

Voorbeelden van overige winkels voor dagelijkse levensmiddelen zijn groenteboer, bakker, vlaaienwinkel, toko, chocoladewinkel, koffie/theewinkel, delicatessenwinkel, kaaswinkel, mini supermarkt, notenwinkel, poelier, reformwinkel, slagerij, slijterij, tabakswinkel, visboer, zoetwarenwinkel, nachtwinkel, wijnwinkel en ziekenhuiswinkel.

`warenhuis_gemiddelde_afstand_in_km` : Afstand tot warenhuis [km]

De gemiddelde afstand van alle inwoners in een gebied tot de dichtstbijzijnde warenhuis, berekend over de weg.

`warenhuis_gemiddeld_aantal_binnen_5_km` : Aantal warenhuizen [absoluut]

Het gemiddeld aantal warenhuizen binnen 5 kilometer over de weg voor alle inwoners van een gebied.

`warenhuis_gemiddeld_aantal_binnen_10_km` : Aantal warenhuizen [absoluut]

Het gemiddeld aantal warenhuizen binnen 10 kilometer over de weg voor alle inwoners van een gebied.

`warenhuis_gemiddeld_aantal_binnen_20_km` : Aantal warenhuizen [absoluut]

Het gemiddeld aantal warenhuizen binnen 20 kilometer over de weg voor alle inwoners van een gebied.

`cafe_gemiddelde_afstand_in_km` : Afstand tot café [km]

De gemiddelde afstand van alle inwoners in een gebied tot het dichtstbijzijnde café, koffiehuis, coffeeshop, discotheek, seks/nachtclub of partycentrum, berekend over de weg.

`cafe_gemiddeld_aantal_binnen_1_km` : Aantal cafés [absoluut]

Het gemiddeld aantal cafés, koffiehuizen, coffeeshops, discotheken, seks/nachtclubs of partycentra, binnen 1 kilometer over de weg voor alle inwoners van een gebied.

`cafe_gemiddeld_aantal_binnen_3_km` : Aantal cafés [absoluut]

Het gemiddeld aantal cafés, koffiehuizen, coffeeshops, discotheken, seks/nachtclubs of partycentra, binnen 3 kilometer over de weg voor alle inwoners van een gebied.

`cafe_gemiddeld_aantal_binnen_5_km` : Aantal cafés [absoluut]

Het gemiddeld aantal cafés, koffiehuizen, coffeeshops, discotheken, seks/nachtclubs of partycentra, binnen 5 kilometer over de weg voor alle inwoners van een gebied.

`cafetaria_gemiddelde_afstand_in_km` : Afstand tot cafetaria [km]

De gemiddelde afstand van alle inwoners in een gebied tot het dichtstbijzijnde cafetaria, fastfoodrestaurant, grillroom/shoarmazaak, lunchroom, pannenkoekenhuis of ijssalon, berekend over de weg.

`cafetaria_gemiddeld_aantal_binnen_1_km` : Aantal cafetaria's [absoluut]

Het gemiddeld aantal cafetaria’s, fastfoodrestaurants, grillrooms/shoarmazaken, lunchrooms, pannenkoekenhuizen of ijssalons, binnen 1 kilometer over de weg voor alle inwoners van een gebied.

`cafetaria_gemiddeld_aantal_binnen_3_km` : Aantal cafetaria's [absoluut]

Het gemiddeld aantal cafetaria’s, fastfoodrestaurants, grillrooms/shoarmazaken, lunchrooms, pannenkoekenhuizen of ijssalons, binnen 3 kilometer over de weg voor alle inwoners van een gebied.

`cafetaria_gemiddeld_aantal_binnen_5_km` : Aantal cafetaria's [absoluut]

Het gemiddeld aantal cafetaria’s, fastfoodrestaurants, grillrooms/shoarmazaken, lunchrooms, pannenkoekenhuizen of ijssalons, binnen 5 kilometer over de weg voor alle inwoners van een gebied.

`restaurant_gemiddelde_afstand_in_km` : Afstand tot restaurant [km]

De gemiddelde afstand van alle inwoners in een gebied tot de dichtstbijzijnde restaurant, café-restaurant of afhaal/thuisbezorging, berekend over de weg.

`restaurant_gemiddeld_aantal_binnen_1_km` : Aantal restaurants [absoluut]

Het gemiddeld aantal restaurants, café-restaurants of afhaal/thuisbezorging, binnen 1 kilometer over de weg voor alle inwoners van een gebied.

`restaurant_gemiddeld_aantal_binnen_3_km` : Aantal restaurants [absoluut]

Het gemiddeld aantal restaurants, café-restaurants of afhaal/thuisbezorging, binnen 3 kilometer over de weg voor alle inwoners van een gebied.

`restaurant_gemiddeld_aantal_binnen_5_km` : Aantal restaurants [absoluut]

Het gemiddeld aantal restaurants, café-restaurants of afhaal/thuisbezorging, binnen 5 kilometer over de weg voor alle inwoners van een gebied.

`hotel_gemiddelde_afstand_in_km` : Afstand tot hotel [km]

De gemiddelde afstand van alle inwoners in een gebied tot het dichtstbijzijnde hotel, berekend over de weg.

`hotel_gemiddeld_aantal_binnen_5_km` : Aantal hotels [absoluut]

Het gemiddeld aantal hotels binnen 5 kilometer over de weg voor alle inwoners van een gebied.

`hotel_gemiddeld_aantal_binnen_10_km` : Aantal hotels [absoluut]

Het gemiddeld aantal hotels binnen 10 kilometer over de weg voor alle inwoners van een gebied.

`hotel_gemiddeld_aantal_binnen_20_km` : Aantal hotels [absoluut]

Het gemiddeld aantal hotels binnen 20 kilometer over de weg voor alle inwoners van een gebied.

`kinderdagverblijf_gemiddelde_afstand_in_km` : Afstand tot kinderdagverblijf [km]

De gemiddelde afstand van alle inwoners in een gebied tot het dichtstbijzijnde kinderdagverblijf, berekend over de weg.

Op het kinderdagverblijf kunnen kinderen van 0 tot 4 jaar gedurende één of meer dagdelen per week het hele jaar door worden opgevangen. Er kan voor meer dan 5 uur per dag van het kinderdagverblijf gebruik gemaakt worden en voor maximaal 10 dagdelen per week.

`kinderdagverblijf_gemiddeld_aantal_binnen_1_km` : Aantal kinderdagverbijven [absoluut]

Het gemiddeld aantal kinderdagverblijven binnen 1 kilometer over de weg voor alle inwoners van een gebied.

Op het kinderdagverblijf kunnen kinderen van 0 tot 4 jaar gedurende één of meer dagdelen per week het hele jaar door worden opgevangen. Er kan voor meer dan 5 uur per dag van het kinderdagverblijf gebruik gemaakt worden en voor maximaal 10 dagdelen per week.

`kinderdagverblijf_gemiddeld_aantal_binnen_3_km` : Aantal kinderdagverbijven [absoluut]

Het gemiddeld aantal kinderdagverblijven binnen 3 kilometer over de weg voor alle inwoners van een gebied.

Op het kinderdagverblijf kunnen kinderen van 0 tot 4 jaar gedurende één of meer dagdelen per week het hele jaar door worden opgevangen. Er kan voor meer dan 5 uur per dag van het kinderdagverblijf gebruik gemaakt worden en voor maximaal 10 dagdelen per week.

`kinderdagverblijf_gemiddeld_aantal_binnen_5_km` : Aantal kinderdagverbijven [absoluut]

Het gemiddeld aantal kinderdagverblijven binnen 5 kilometer over de weg voor alle inwoners van een gebied.

Op het kinderdagverblijf kunnen kinderen van 0 tot 4 jaar gedurende één of meer dagdelen per week het hele jaar door worden opgevangen. Er kan voor meer dan 5 uur per dag van het kinderdagverblijf gebruik gemaakt worden en voor maximaal 10 dagdelen per week.

`buitenschoolse_opvang_gem_afstand_in_km` : Afstand tot buitenschoolse opvang [km]

De gemiddelde afstand van alle inwoners in een gebied tot de dichtstbijzijnde buitenschoolse opvang, berekend over de weg. Hier worden kinderen in de basisschoolleeftijd voor en/of na schooltijd, tijdens studie- en adv-dagen van leraren en in de vakanties opgevangen.

`buitenschoolse_opvang_gemiddeld_aantal_binnen_1_km` : Aantal buitenschoolse opvang [absoluut]

Het gemiddeld aantal locaties van buitenschoolse opvang binnen 1 kilometer over de weg voor alle inwoners van een gebied. Hier worden kinderen in de basisschoolleeftijd voor en/of na schooltijd, tijdens studie- en adv-dagen van leraren en in de vakanties opgevangen.

`buitenschoolse_opvang_gemiddeld_aantal_binnen_3_km` : Aantal buitenschoolse opvang [absoluut]

Het gemiddeld aantal locaties van buitenschoolse opvang binnen 3 kilometer over de weg voor alle inwoners van een gebied. Hier worden kinderen in de basisschoolleeftijd voor en/of na schooltijd, tijdens studie- en adv-dagen van leraren en in de vakanties opgevangen.

`buitenschoolse_opvang_gemiddeld_aantal_binnen_5_km` : Aantal buitenschoolse opvang [absoluut]

Het gemiddeld aantal locaties van buitenschoolse opvang binnen 5 kilometer over de weg voor alle inwoners van een gebied. Hier worden kinderen in de basisschoolleeftijd voor en/of na schooltijd, tijdens studie- en adv-dagen van leraren en in de vakanties opgevangen.

### Basisonderwijs

Het basisonderwijs omvat naast de reguliere basisscholen ook de scholen voor kinderen van mensen zonder vaste woon- of verblijfplaats, de zogenaamde rijdende scholen en de ligplaatsscholen voor varende kleuters. Het speciaal basisonderwijs en de speciale scholen zijn niet meegenomen.

In Nederland zijn er ongeveer 10 rijdende scholen. Deze scholen hebben allen als officiële vestigingsgemeente Geldermalsen. Het aantal basisscholen in Geldermalsen is hierdoor hoog, vooral in het oostelijke deel. Ook in buurten van de omliggende gemeenten Buren, Culemborg en Neerijnen is het effect van deze scholen nog zichtbaar.

De cijfers vermeld bij het betreffende jaar, gaan over het jaar daarvoor. De cijfers zijn gebaseerd op het adressenbestand van het Ministerie van Onderwijs, Cultuur en Wetenschap met vestigingen van basisscholen. Als bekend is dat er onderwijs gevolgd kan worden op een dependance en dit een effect heeft van meer dan 500 meter op de berekende gemiddelde afstand, zijn deze gegevens van de buurten en wijken aanvullend geheim gemaakt.

`basisonderwijs_gemiddelde_afstand_in_km` : Afstand tot basisschool [km]

De gemiddelde afstand van alle inwoners in een gebied tot de dichtstbijzijnde basisschool, berekend over de weg.

`basisonderwijs_gemiddeld_aantal_binnen_1_km` : Aantal basisscholen [absoluut]

Het gemiddeld aantal basisscholen binnen 1 kilometer over de weg voor alle inwoners van een gebied.

`basisonderwijs_gemiddeld_aantal_binnen_3_km` : Aantal basisscholen [absoluut]

Het gemiddeld aantal basisscholen binnen 3 kilometer over de weg voor alle inwoners van een gebied.

`basisonderwijs_gemiddeld_aantal_binnen_5_km` : Aantal basisscholen [absoluut]

Het gemiddeld aantal basisscholen binnen 5 kilometer over de weg voor alle inwoners van een gebied.

`voortgezet_onderwijs_gem_afstand_in_km` : Afstand tot voortgezet onderwijs [km]

De gemiddelde afstand van alle inwoners in een gebied tot de dichtstbijzijnde VMBO, HAVO of VWO school, berekend over de weg. Dit zijn scholen waar leerlingen door de overheid bekostigde voltijd voortgezet onderwijs kunnen volgen. Praktijkonderwijsscholen en speciale scholen zijn niet meegenomen.

`voortgezet_onderwijs_gemiddeld_aantal_binnen_3_km` : Aantal scholen voortgezet onderwijs [absoluut]

Het gemiddeld aantal VMBO, HAVO en VWO-scholen binnen 3 kilometer over de weg voor alle inwoners van een gebied.

Dit zijn scholen waar leerlingen door de overheid bekostigde voltijd voortgezet onderwijs kunnen volgen. Praktijkonderwijsscholen en speciale scholen zijn niet meegenomen.

`voortgezet_onderwijs_gemiddeld_aantal_binnen_5_km` : Aantal scholen voortgezet onderwijs [absoluut]

Het gemiddeld aantal VMBO, HAVO en VWO-scholen binnen 5 kilometer over de weg voor alle inwoners van een gebied.

Dit zijn scholen waar leerlingen door de overheid bekostigde voltijd voortgezet onderwijs kunnen volgen. Praktijkonderwijsscholen en speciale scholen zijn niet meegenomen.

`voortgezet_onderwijs_gemiddeld_aantal_binnen_10_km` : Aantal scholen voortgezet onderwijs [absoluut]

Het gemiddeld aantal VMBO, HAVO en VWO-scholen binnen 10 kilometer over de weg voor alle inwoners van een gebied.

Dit zijn scholen waar leerlingen door de overheid bekostigde voltijd voortgezet onderwijs kunnen volgen. Praktijkonderwijsscholen en speciale scholen zijn niet meegenomen.

`vmbo_gemiddelde_afstand_in_km` : Afstand tot scholen VMBO [km]

De gemiddelde afstand van alle inwoners in een gebied tot de dichtstbijzijnde VMBO school, berekend over de weg.

Dit zijn scholen waar leerlingen door de overheid bekostigde voltijd voortgezet onderwijs kunnen volgen als voorbereidend middelbaar beroepsonderwijs (VMBO). Praktijkonderwijsscholen en speciale scholen zijn niet meegenomen.

`vmbo_gemiddeld_aantal_binnen_3_km` : Aantal scholen VMBO [absoluut]

Het gemiddeld aantal VMBO-scholen binnen 3 kilometer over de weg voor alle inwoners van een gebied.

Dit zijn scholen waar leerlingen door de overheid bekostigde voltijd voortgezet onderwijs kunnen volgen als voorbereidend middelbaar beroepsonderwijs (VMBO). Praktijkonderwijsscholen en speciale scholen zijn niet meegenomen.

`vmbo_gemiddeld_aantal_binnen_5_km` : Aantal scholen VMBO [absoluut]

Het gemiddeld aantal VMBO-scholen binnen 5 kilometer over de weg voor alle inwoners van een gebied.

Dit zijn scholen waar leerlingen door de overheid bekostigde voltijd voortgezet onderwijs kunnen volgen als voorbereidend middelbaar beroepsonderwijs (VMBO). Praktijkonderwijsscholen en speciale scholen zijn niet meegenomen.

`vmbo_gemiddeld_aantal_binnen_10_km` : Aantal scholen VMBO [absoluut]

Het gemiddeld aantal VMBO-scholen binnen 10 kilometer over de weg voor alle inwoners van een gebied.

Dit zijn scholen waar leerlingen door de overheid bekostigde voltijd voortgezet onderwijs kunnen volgen als voorbereidend middelbaar beroepsonderwijs (VMBO). Praktijkonderwijsscholen en speciale scholen zijn niet meegenomen.

`havo_vwo_gemiddelde_afstand_in_km` : Afstand tot scholen HAVO/VWO [km]

De gemiddelde afstand van alle inwoners in een gebied tot de dichtstbijzijnde HAVO/VWO school, berekend over de weg.

Dit zijn scholen waar leerlingen door de overheid bekostigde voltijd voortgezet onderwijs kunnen volgen als hoger algemeen voortgezet onderwijs of voorbereidend wetenschappelijk onderwijs (HAVO/VWO).

`havo_vwo_gemiddeld_aantal_binnen_3_km` : Aantal scholen HAVO/VWO [absoluut]

Het gemiddeld aantal HAVO/VWO-scholen binnen 3 kilometer over de weg voor alle inwoners van een gebied.

Dit zijn scholen waar leerlingen door de overheid bekostigde voltijd voortgezet onderwijs kunnen volgen als hoger algemeen voortgezet onderwijs of voorbereidend wetenschappelijk onderwijs (HAVO/VWO).

`havo_vwo_gemiddeld_aantal_binnen_5_km` : Aantal scholen HAVO/VWO [absoluut]

Het gemiddeld aantal HAVO/VWO-scholen binnen 5 kilometer over de weg voor alle inwoners van een gebied.

Dit zijn scholen waar leerlingen door de overheid bekostigde voltijd voortgezet onderwijs kunnen volgen als hoger algemeen voortgezet onderwijs of voorbereidend wetenschappelijk onderwijs (HAVO/VWO).

`havo_vwo_gemiddeld_aantal_binnen_10_km` : Aantal scholen HAVO/VWO [absoluut]

Het gemiddeld aantal HAVO/VWO-scholen binnen 10 kilometer over de weg voor alle inwoners van een gebied.

Dit zijn scholen waar leerlingen door de overheid bekostigde voltijd voortgezet onderwijs kunnen volgen als hoger algemeen voortgezet onderwijs of voorbereidend wetenschappelijk onderwijs (HAVO/VWO).

`oprit_hoofdverkeersweg_gemiddelde_afstand_in_km` : Afstand tot oprit hoofdverkeersweg [km]

De gemiddelde afstand van alle inwoners in een gebied tot de dichtstbijzijnde oprit van een rijks- of provinciale weg, berekend over de weg.

Toegang tot een rijks- of provinciale weg. Als uitgangspunt voor de opritten is het Nationale Wegenbestand (een product van Adviesdienst Verkeer en Vervoer van het Ministerie van Infrastructuur en Milieu) gebruikt.

`treinstation_gemiddelde_afstand_in_km` : Afstand tot treinstation [km]

De gemiddelde afstand van alle inwoners in een gebied tot het dichtstbijzijnde treinstation, berekend over de weg.

`overstapstation_gemiddelde_afstand_in_km` : Afstand tot belangrijk overstapstation [km]

De gemiddelde afstand van alle inwoners in een gebied tot het dichtstbijzijnde belangrijke overstapstation, berekend over de weg.

`bibliotheek_gemiddelde_afstand_in_km` : Afstand tot bibliotheek [km]

De gemiddelde afstand van alle inwoners in een gebied tot de dichtstbijzijnde bibliotheek, berekend over de weg.

Bibliotheken en hun vestigingen zoals deze zijn opgenomen in de database G!DS. Opgenomen zijn de vestigingen en de servicepunten. De miniservicepunten, zelfbedieningsbibliotheken en de bibliobussen zijn niet opgenomen.

Een vestiging voldoet aan de volgende criteria: minimaal 15 uur per week open, digitale toegang tot de gehele collectie en activiteitenaanbod, vraagbemiddeling, culturele/literaire activiteiten, aanbod voor scholieren/instellingen passend bij de keuzes die gemaakt zijn in het spreidings- en- marketingbeleid en studiemogelijkheden.

Een servicepunt biedt minimaal het volgende dienstverleningsniveau: is minimaal 4 uur per week open, biedt digitale toegang tot het totale activiteitenaanbod en voorziet in vraagbemiddeling (zowel persoonlijk als via internet).

`zwembad_gemiddelde_afstand_in_km` : Afstand tot zwembad [km]

De gemiddelde afstand van alle inwoners in een gebied tot het dichtstbijzijnde zwembad, berekend over de weg.

Het zwembad moet voldoen aan de volgende criteria: er is een gebouw aanwezig, de activiteiten zijn commercieel opgezet, en het is het hele jaar openbaar toegankelijk voor minimaal drie dagen per week.

`kunstijsbaan_gemiddelde_afstand_in_km` : Afstand tot kunstijsbaan [km]

De gemiddelde afstand van alle inwoners in een gebied tot de dichtstbijzijnde schaatsbaan van kunstijs, geopend tijdens het winterseizoen, berekend over de weg.

`theater_gemiddelde_afstand_in_km` : Afstand tot podiumkunsten totaal [km]

De gemiddelde afstand van alle inwoners in een gebied tot de dichtstbijzijnde locaties van schouwburgen, concertgebouwen, buurtcentra of poppodia, berekend over de weg. Festivals en locaties met podiumkunsten als nevenactiviteit worden hierbij niet opgenomen.

`theater_gemiddeld_aantal_binnen_5_km` : Aantal podiumkunsten totaal [absoluut]

Het gemiddeld aantal locaties van schouwburgen, concertgebouwen, buurtcentra of poppodia binnen 5 kilometer over de weg voor alle inwoners van een gebied. Festivals en locaties met podiumkunsten als nevenactiviteit worden hierbij niet opgenomen.

`theater_gemiddeld_aantal_binnen_10_km` : Aantal podiumkunsten totaal [absoluut]

Het gemiddeld aantal locaties van schouwburgen, concertgebouwen, buurtcentra of poppodia binnen 10 kilometer over de weg voor alle inwoners van een gebied. Festivals en locaties met podiumkunsten als nevenactiviteit worden hierbij niet opgenomen.

`theater_gemiddeld_aantal_binnen_20_km` : Aantal podiumkunsten totaal [absoluut]

Het gemiddeld aantal locaties van schouwburgen, concertgebouwen, buurtcentra of poppodia binnen 20 kilometer over de weg voor alle inwoners van een gebied. Festivals en locaties met podiumkunsten als nevenactiviteit worden hierbij niet opgenomen.

`poppodium_gemiddelde_afstand_in_km` : Afstand tot poppodium [km]

De gemiddelde afstand van alle inwoners in een gebied tot het dichtstbijzijnde poppodium, berekend over de weg. Festivals en locaties met podiumkunsten als nevenactiviteit worden hierbij niet opgenomen.

`bioscoop_gemiddelde_afstand_in_km` : Afstand tot bioscoop [km]

De gemiddelde afstand van alle inwoners in een gebied tot de dichtstbijzijnde bioscoop, berekend over de weg.

`bioscoop_gemiddeld_aantal_binnen_5_km` : Aantal bioscopen [absoluut]

Het gemiddeld aantal bioscopen binnen 5 kilometer over de weg voor alle inwoners van een gebied.

`bioscoop_gemiddeld_aantal_binnen_10_km` : Aantal bioscopen [absoluut]

Het gemiddeld aantal bioscopen binnen 10 kilometer over de weg voor alle inwoners van een gebied.

`bioscoop_gemiddeld_aantal_binnen_20_km` : Aantal bioscopen [absoluut]

Het gemiddeld aantal bioscopen binnen 20 kilometer over de weg voor alle inwoners van een gebied.

`sauna_gemiddelde_afstand_in_km` : Afstand tot sauna [km]

De gemiddelde afstand van alle inwoners in een gebied tot de dichtstbijzijnde sauna, berekend over de weg.

`zonnebank_gemiddelde_afstand_in_km` : Afstand tot zonnebank [km]

De gemiddelde afstand van alle inwoners in een gebied tot de dichtstbijzijnde zonnebank, berekend over de weg.

`attractiepark_gemiddelde_afstand_in_km` : Afstand tot attractie [km]

De gemiddelde afstand van alle inwoners in een gebied tot de dichtstbijzijnde pretpark, dierentuin of binnenspeeltuin, berekend over de weg.

`attractiepark_gemiddeld_aantal_binnen_10_km` : Aantal attracties [absoluut]

Het gemiddeld aantal pretparken, dierentuinen en binnenspeeltuinen binnen 10 kilometer over de weg voor alle inwoners van een gebied.

`attractiepark_gemiddeld_aantal_binnen_20_km` : Aantal attracties [absoluut]

Het gemiddeld aantal pretparken, dierentuinen en binnenspeeltuinen binnen 20 kilometer over de weg voor alle inwoners van een gebied.

`attractiepark_gemiddeld_aantal_binnen_50_km` : Aantal attracties [absoluut]

Het gemiddeld aantal pretparken, dierentuinen en binnenspeeltuinen binnen 50 kilometer over de weg voor alle inwoners van een gebied.

`brandweerkazerne_gemiddelde_afstand_in_km` : Afstand tot brandweerkazerne [km]

De gemiddelde afstand van alle inwoners in een gebied tot de dichtstbijzijnde brandweerkazerne, berekend over de weg. Exclusief locaties van blusboten.

`gemiddelde_afstand_tot_museum` : Afstand tot museum [km]

De gemiddelde afstand van alle inwoners in een gebied tot de dichtstbijzijnde museum, berekend over de weg.

`gemiddeld_aantal_musea_binnen_5_km` : Aantal musea [absoluut]

Het gemiddeld aantal musea binnen 5 kilometer over de weg voor alle inwoners van een gebied.

`gemiddeld_aantal_musea_binnen_10_km` : Aantal musea [absoluut]

Het gemiddeld aantal musea binnen 10 kilometer over de weg voor alle inwoners van een gebied.

`gemiddeld_aantal_musea_binnen_20_km` : Aantal musea [absoluut]

Het gemiddeld aantal musea binnen 20 kilometer over de weg voor alle inwoners van een gebied.

`afstand_tot_openbaar_groen_totaal` [km]
`afstand_tot_park_of_plantsoen` [km]
`afstand_tot_dagrcreatief_terrein` [km]
`afstand_tot_bos` [km]
`afstand_tot_open_natuur_terrein_totaal` [km]
`afstand_tot_open_droog_natuur_terrein` [km]
`afstand_tot_open_nat_natuurlijk_terrein` [km]
`afstand_tot_semiopenbaar_groen_totaal` [km]
`afstand_tot_sportterrein` [km]
`afstand_tot_volkstuin` [km]
`afstand_tot_verblijfsrecreatief_terrein` [km]
`afstand_tot_recreatief_binnenwater` [km]
`afstand_tot_begraafplaats` [km]

*2)*                  *Zie bijlage 1 voorkomen variabelen per jaar.*

# 6. Koppelingen naar relevante tabellen en artikelen

[Korte onderzoeksbeschrijving Kerncijfers wijken en buurten](https://www.cbs.nl/nl-nl/onze-diensten/methoden/onderzoeksomschrijvingen/korte-onderzoeksbeschrijvingen/kerncijfers-wijken-en-buurten).

[Korte onderzoeksbeschrijving nabijheidsstatistiek](https://www.cbs.nl/nl-nl/onze-diensten/methoden/onderzoeksomschrijvingen/korte-onderzoeksbeschrijvingen/nabijheidsstatistiek).

[Kerncijfers wijken en buurten 2024](https://opendata.cbs.nl/statline/CBS/nl/dataset/85984NED/table?ts=1727857599802).

[Kerncijfers wijken en buurten 2023](https://opendata.cbs.nl/statline/CBS/nl/dataset/85618NED/table?ts=1695292138054).

[Kerncijfers wijken en buurten 2022](https://opendata.cbs.nl/statline/CBS/nl/dataset/85318NED/table?ts=1664441075329).

[Kerncijfers wijken en buurten 2021](https://opendata.cbs.nl/statline/CBS/nl/dataset/85039NED/table?ts=1632408323557).

[Kerncijfers wijken en buurten 2020](https://opendata.cbs.nl/statline/CBS/nl/dataset/84799NED/table?ts=1601291977403).

[Kerncijfers wijken en buurten 2019](https://opendata.cbs.nl/statline/CBS/nl/dataset/84583NED/table).

[Kerncijfers wijken en buurten 2018](https://opendata.cbs.nl/statline/CBS/nl/dataset/84286NED/table).

[Kerncijfers wijken en buurten 2017](https://opendata.cbs.nl/statline/CBS/nl/dataset/83765NED/table?dl=C3D2).

[Kerncijfers wijken en buurten 2016](https://opendata.cbs.nl/statline/CBS/nl/dataset/83487NED/table?dl=3E45).

[Kerncijfers wijken en buurten 2015](https://opendata.cbs.nl/statline/CBS/nl/dataset/83220NED/table?dl=4A5F).

[Kerncijfers wijken en buurten 2014](https://opendata.cbs.nl/statline/CBS/nl/dataset/82931NED/table?dl=5F5A).

[Kerncijfers wijken en buurten 2013](https://opendata.cbs.nl/statline/CBS/nl/dataset/82339NED/table?dl=5F5B).

[Kerncijfers wijken en buurten 2009-2012](https://opendata.cbs.nl/statline/CBS/nl/dataset/70904ned/table?dl=5F5D).

[Digitale wijk- en buurtkaart 2003 t/m 2023](https://www.cbs.nl/nl-nl/dossier/nederland-regionaal/geografische-data).

[Kerncijfers Postcodegebieden 2004](https://www.cbs.nl/nl-nl/publicatie/2006/08/kerncijfers-postcodegebieden-2004/).

[Regionale Kerncijfers Nederland](https://opendata.cbs.nl/statline/CBS/nl/dataset/70072ned/table?dl=ED88).

[Cijfers op de Kaart](https://www.cbs.nl/nl-nl/visualisaties/cijfers-op-de-kaart).

[Pdok.nl](https://www.pdok.nl/).

# 7. Voorwaarden gebruik

De gebruiker van de Wijk- en Buurtkaart is gehouden aan de volgende rechten en verplichtingen:

1.   Alle rechten op de Wijk- en Buurtkaart blijven te allen tijde berusten bij het Centraal Bureau voor de Statistiek en het Kadaster;

2.   Bij de gegevensvermelding op basis van de Wijk- en Buurtkaart is bronvermelding verplicht;

3.   Bij visualisering van grenzen of bij visualisering van gegevens met behulp van dit digitale bestand dient te worden vermeld: © Kadaster / Centraal Bureau voor de Statistiek, 2024

4.   Het gebruik van geometrie van buurtgrenzen en buurtcijfers van het CBS als toevoeging aan het bestand burgerlijke gemeentegrenzen is zonder kosten;

5.   Bij publicatie van cijfers is bronvermelding verplicht, verveelvoudiging voor eigen gebruik of intern gebruik is toegestaan;

Copyright: (c) Centraal Bureau voor de Statistiek, Den Haag/Heerlen, 2023

# 8. Bijlage

[Beschikbaarheid variabelen per jaar](https://www.cbs.nl/-/media/_excel/2024/44/voorkomenvariabele-pub-2024.xlsx).
