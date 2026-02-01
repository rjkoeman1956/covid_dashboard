## Bestandsnaam

`COVID-19_aantallen_gemeente_per_dag_tm_03102021.csv`

`COVID-19_aantallen_gemeente_per_dag.csv`

## Dataset

`Covid-19 aantallen per gemeente per publicatiedatum`

## Bron

https://data.overheid.nl/dataset/12900-covid-19-aantallen-per-gemeente-per-publicatiedatum#reuse

## Beschrijving

Nederland heeft voor het SARS-CoV-2 virus (coronavirus) een endemische fase bereikt en de GGD teststraten zijn per 17 maart 2023 gesloten. Daardoor wordt de data vanaf 1 april 2023 niet meer bijgewerkt.

Dit bestand bevat de volgende aantallen:

- aantal nieuw gemelde positief geteste personen naar gemeente, per datum waarop de gegevens zijn gepubliceerd door het RIVM
- aantal nieuw gemelde sterfgevallen naar gemeente, per datum waarop de gegevens zijn gepubliceerd door het RIVM weergegeven tot 1 januari 2023. De aantallen betreffen Covid-19 meldingen sinds de eerste melding in Nederland (27/02/2020).

Het bestand is als volgt opgebouwd:

- Een set records per publicatiedatum met voor elke publicatiedatum: Een record voor elke gemeente van Nederland, ook als voor de betreffende gemeente geen meldingen zijn. De aantallen zijn dan 0 (nul). Een record voor elke GGD, voor de aantallen meldingen waarbij de gemeente niet bekend is. Ook deze records worden altijd toegevoegd, dus ook als de aantallen 0 (nul) zijn. Ook zijn kolommen voor diverse regionale indelingen toegevoegd. In de beschrijving van de variabelen hieronder wordt per regio beschreven hoe deze zijn bepaald.

## Beschrijving van de variabelen

`Version`: Versienummer van de dataset. Wanneer de inhoud van de dataset structureel wordt gewijzigd (dus niet de dagelijkse update of een correctie op record niveau), zal het versienummer aangepast worden (+1) en ook de corresponderende metadata in RIVMdata (https://data.rivm.nl). Versie 1 correctie update (16 juli 2021)

- Door een correctie in de verwerking door het RIVM heeft een kleine set meldingen een herziene ziekenhuisopname publicatiedatum en overlijdens publicatiedatum gekregen per 16-07-2021 (betreft kolommen: Hospital_admission per Date_of_publication en Deceased per Date_of_publication). Versie 2 update (18 januari 2022)

- In versie 2 van deze dataset is de variabele ‘hospital_admission’  niet meer beschikbaar. Voor het aantal ziekenhuisopnames wordt verwezen naar de geregistreerde ziekenhuisopnames van Stichting NICE (https://data.rivm.nl/covid-19/COVID-19_ziekenhuisopnames.html). Versie 3 update (20 januari 2022)

- In versie 3 van deze dataset zijn records samengesteld volgens de gemeente herindeling van 1 januari 2022. Zie beschrijving van de variabele Municipality_code voor meer informatie. Versie 4 update (8 februari 2022)

- Vanaf 8 februari 2022 worden de positieve SARS-CoV-2 testuitslagen rechtstreeks vanuit CoronIT aan het RIVM gemeld. Ook worden de testuitslagen van andere testaanbieders (zoals Testen voor Toegang) en zorginstellingen (zoals ziekenhuizen, verpleeghuizen en huisartsen) die hun positieve SARS-CoV-2 testuitslagen via het Meldportaal van GGD GHOR invoeren rechtstreeks aan het RIVM gemeld. Meldingen die onderdeel zijn van de bron- en contactonderzoek steekproef en positieve SARS-CoV-2 testuitslagen van zorginstellingen die via zorgmail aan de GGD worden gemeld worden wel via HPZone aan het RIVM gemeld. Versie 5 update (24 maart 2022)

- In versie 5 van deze dataset zijn records samengesteld volgens de gemeente herindeling van 24 maart 2022. Zie beschrijving van de variabele Municipality_code voor meer informatie. Versie 6 update (1 september 2022)

- Vanaf 1 september 2022 wordt de data niet meer iedere werkdag geüpdatet, maar op dinsdagen en vrijdagen. De data wordt op deze dagen met terugwerkende kracht bijgewerkt voor de andere dagen. Vanaf 1 september 2022 is deze dataset opgesplitst in twee delen. Het eerste deel bevat de data vanaf het begin van de pandemie tot en met 3 oktober 2021 (week 39) en bevat ‘tm’ in de bestandsnaam. Deze data wordt niet meer geüpdatet. Het tweede deel bevat de data vanaf 4 oktober 2021 (week 40) en wordt iedere dinsdag en vrijdag geüpdatet. Versie 7 update (3 januari 2023)

- In versie 7 van deze dataset zijn records samengesteld volgens de gemeente herindeling van 1 januari 2023. Deze gemeente herindeling is ook toegepast in het eerste deel van deze dataset dat ‘tm’ bevat in de bestandsnaam en de data bevat vanaf het begin van de pandemie tot en met 3 oktober 2021 (week 39). Zie beschrijving van de variabele Municipality_code voor meer informatie.

- Per 1 januari 2023 verzamelt het RIVM geen aanvullende informatie meer. Dit heeft als gevolg dat we vanaf 1 januari 2023 geen overlijdens meer rapporteren en wordt en wordt de kolom [Deceased] op 9999 gezet.

`Date_of_report`: Datum en tijd waarop het databestand is aangemaakt door het RIVM.

`Date_of_publication`: Dit betreft per dag het aantal meldingen dat nieuw binnengekomen is bij het RIVM. De tijdsperiode waarin de melding is doorgegeven loopt van 10.01 uur gisteren tot 10.00 uur vandaag. De publicatiedatum kan afwijken van de datum van de positieve testuitslag. Dit kan gebeuren als een melding van een positieve SARS-CoV-2 test later is doorgeven door een GGD aan het RIVM. Dit bestand bevat de meest actuele meldingen op basis van het bronbestand Osiris. Als er in Osiris correcties worden gedaan, dan worden deze correcties ook verwerkt in dit bestand.

`Municipality_code`: Gemeentecode. Gemeentelijke indeling gebaseerd op postcode van de woonplaats van de SARS-CoV-2 positief geteste persoon, gecodeerd volgens CBS. Sinds de eerste publicatiedatum van 13 maart 2020 tot de versie 3 update van 20 januari 2022, hebben 2 gemeentelijke herindelingen plaatsgevonden. Tot 7 januari 2021 is dit bestand volgens de gemeente indeling van 2020. Vanaf 7 januari 2021 t/m 19 januari 2022 is dit bestand samengesteld volgens de gemeente indeling van 1 januari 2021: Gemeenten Appingedam, Delfzijl en Loppersum zijn samengevoegd tot de nieuwe gemeente Eemsdelta Gr. De gemeente Haaren is opgegaan in de gemeenten Oisterwijk, Tilburg, Vught en Boxtel. Met de opdeling van Haaren is de veiligheidsregio Midden- en West-Brabant iets groter geworden, ten koste van veiligheidsregio Brabant-Noord. Vanaf 20 januari 2022 t/m 23 maart 2022 is dit bestand samengesteld volgens de gemeente indeling van 1 januari 2022. Gemeente Beemster is opgegaan in gemeente Purmerend. De gemeenten Heerhugowaard en Langedijk zijn samengevoegd tot gemeente Dijk en Waard. Gemeente Landerd is met gemeente Uden samengevoegd tot gemeente Maashorst. De gemeenten Boxmeer, Cuijk, Grave, Mill en Sint Hubert en Sint Anthonis zijn samengevoegd tot de gemeente Land van Cuijk. Vanaf 24 maart 2022 t/m 31 december 2022 is dit bestand samengesteld volgens de gemeente indeling van 24 maart 2022. Gemeente Weesp is opgegaan in gemeente Amsterdam. Met deze indeling is de veiligheidsregio Gooi- en Vechtstreek kleiner geworden en de veiligheidsregio Amsterdam-Amstelland groter; GGD Amsterdam is groter geworden en GGD Gooi- en Vechtstreek is kleiner geworden. Vanaf 1 januari 2023 is dit bestand samengesteld volgens de gemeente indeling van 1 januari 2023. De gemeenten Brielle, Hellevoetsluis en Westvoorne zijn samen opgegaan in de nieuwe gemeente Voorne aan Zee (Gemeentelijke indeling op 1 januari 2023.

`Municipality_name`: Naam van de gemeente.

`Province`: Naam van de provincie. Indien gemeente niet bekend is, is de provincie afgeleid van de meldende GGD zodat provincie voor elk record gevuld is.

`Security_region_code`: Veiligheidsregiocode. Veiligheidsregio gebaseerd op de woonplaats van de patiënt. Indien de woonplaats niet bekend is, wordt Veiligheidsregio gebaseerd op de GGD die de melding heeft gedaan, behalve voor Veiligheidsregio Midden- en West-Brabant en Brabant-Noord aangezien voor deze regio’s GGD en Veiligheidsregio niet vergelijkbaar zijn.

`Security_region_name`: Naam van de veiligheidsregio. Dit is de naam van de veiligheidregios zoals tot dusver gebruikt in diverse rapportages en verslagen van het RIVM, en kan iets afwijken van de naamgeving zoals aangegeven in de codelijst van CBS (zie link hierboven bij variabele Security_region_code). Zie ook: https://www.rijksoverheid.nl/onderwerpen/veiligheidsregios-en-crisisbeheersing/veiligheidsregios

`Municipal_health_service`: Naam van de GGD. GGD op basis van gemeente (woonplaats van de patiënt). Indien deze niet bekend is wordt hier de GGD die de melding heeft gedaan ingevuld. Zie ook: https://www.ggd.nl

`ROAZ_region`: Naam van de ROAZ-regio. ROAZ-regio op basis van de woonplaats van de patiënt. Indien de woonplaats niet bekend is op basis van meldende GGD (alleen wanneer een GGD geografisch kan worden gematched met een ROAZ-regio). Zie ook: https://www.lnaz.nl/acute-zorg

`Total_reported`: Het aantal nieuwe aan de GGD gemelde personen die positief zijn getest voor SARS-CoV-2 dat op [Date_of_publication] is gepubliceerd door het RIVM. Sinds het begin van de COVID-19 epidemie in Nederland is het testbeleid gelijdelijk veranderd. Het huidige testbeleid is hier te vinden (https://www.rijksoverheid.nl/onderwerpen/coronavirus-covid-19/testen/testbeleid/wijzigingen-testen-vanaf-11-april-2022).

Niet alle met SARS-CoV-2 besmette personen worden getest. De werkelijke aantallen in Nederland zijn daarom hoger dan de aantallen die hier genoemd worden.

`Deceased`: Het aantal aan de GGD’en gemelde overleden personen die positief zijn getest voor SARS-CoV-2 en op [Date_of_publication] is gepubliceerd door het RIVM. Het werkelijke aantal overleden personen positief voor SARS-CoV-2 is hoger dan het aantal meldingen in de surveillance, omdat niet alle overleden personen getest worden. Dit komt doordat er geen meldingsplicht geldt voor overlijden van personen met een positieve SARS-CoV-2 testuitslag. Vanaf 1 januari 2023 is deze kolom op 9999 gezet.

Correcties die in meldingen in het bronsysteem OSIRIS worden gedaan kunnen ook leiden tot correcties in dit databestand. Aantallen die in het verleden door het RIVM zijn gepubliceerd kunnen in dat geval afwijken van de aantallen in dit databestand. Dit bestand bevat dus altijd het aantal nieuwe, door RIVM gerapporteerde meldingen per dag, op basis van de meest actuele gegevens in het bronsysteem OSIRIS.
