## Bestandsnaam

`COVID-19_ziekenhuisopnames_tm_03102021.csv`

`COVID-19_ziekenhuisopnames.csv`

## Dataset

`Covid-19 ziekenhuisopnames (volgens NICE registratie) per gemeente per ziekenhuisopnamedatum en meldingsdatum`

## Bron

https://data.overheid.nl/dataset/56934-covid-19-ziekenhuisopnames--volgens-nice-registratie--per-gemeente-per-ziekenhuisopnamedatum-e

## Beschrijving

- het aantal Covid-19 ziekenhuisopnames naar gemeente gebaseerd op gemeente van inschrijving van de patiënt, per datum van ziekenhuisopname en per datum waarop de gegevens zijn gemeld aan de NICE registratie (https://www.stichting-nice.nl). De aantallen betreffen Covid-19 ziekenhuisopnames sinds de eerste melding in Nederland (27/02/2020) tot 1 april 2024.

Per 1 april 2024 is de NICE COVID-19 klinische registratie gestopt. Daardoor wordt de data vanaf 17 april 2024 niet meer bijgewerkt. Informatie over het aantal COVID-19 ziekenhuisopnames en de bedbezetting wordt nog gerapporteerd door het LCPS (https://lcps.nu/datafeed/). Het aantal ziekenhuisopnames in de NICE COVID-19 registratie werd tussen april 2023 en april 2024 steeds minder compleet, vergeleken met het aantal ziekenhuisopnames gerapporteerd door het LCPS.

Het bestand is als volgt opgebouwd:

- Een record per datum van statistiek, per gemeente van Nederland, ook als voor de betreffende gemeente geen opname of meldingen zijn. De aantallen zijn dan 0 (nul).
- De genoemde datum voor statistiek kan betrekking hebben op een ziekenhuisopnamedatum of de datum dat het ziekenhuis een opname heeft gemeld aan de NICE registratie.

## Beschrijving van de variabelen

`Version`: Versienummer van de dataset. Wanneer de inhoud van de dataset structureel wordt gewijzigd (dus niet de dagelijkse update of een correctie op record niveau), zal het versienummer aangepast worden (+1) en ook de corresponderende metadata in RIVMdata (https://data.rivm.nl). Versie 2 update (25 maart 2021):

- In versie 2 van deze open data file worden meldingen met een registratiedatum na 27/02/2020, maar een ziekenhuisopnamedatum voor 27/02/2020 niet meer meegenomen. Versie 3 update (20 januari 2022):
- In versie 3 van dit bestand zijn records samengesteld volgens de gemeente herindeling van 1 januari 2022. Zie beschrijving van de variabele Municipality_code voor meer informatie. Versie 4 update (24 maart 2022):
- In versie 4 van deze dataset zijn records samengesteld volgens de gemeente herindeling van 24 maart 2022. Zie beschrijving van de variabele Municipality_code voor meer informatie. Versie 5 update (9 augustus 2022):
- Vanaf 9 augustus 2022 zijn nieuwe opnames van personen met een SARS-CoV-2 besmetting die tijdens een eerdere COVID-19 episode ook opgenomen zijn geweest, toegevoegd aan dit open databestand. Om deze reden valt het aantal opnames met terugwerkende kracht hoger uit dan in onze voorgaande bestanden. De onderschatting van het aantal opnames sinds het begin van de pandemie tot 9 augustus 2022 is minder dan 1%. Een opname wordt geteld als een nieuwe opname wanneer een persoon met een SARS-CoV-2 besmetting een opname datum heeft die meer dan 90 dagen na de voorgaande opname. Versie 6 update (1 september 2022):
- Vanaf 1 september 2022 wordt de data niet meer iedere werkdag geüpdatet, maar op dinsdagen en vrijdagen. De data wordt op deze dagen met terugwerkende kracht bijgewerkt voor de andere dagen.
- Vanaf 1 september 2022 is deze dataset opgesplitst in twee delen. Het eerste deel bevat de data vanaf het begin van de pandemie tot en met 3 oktober 2021 (week 39) en bevat ‘tm’ in de bestandsnaam. Deze data wordt niet meer geüpdatet. Het tweede deel bevat de data vanaf 4 oktober 2021 (week 40) en wordt iedere dinsdag en vrijdag geüpdatet. Versie 7 update (3 januari 2023):
- In versie 7 van dit bestand zijn records samengesteld volgens de gemeente herindeling van 1 januari 2023. Deze gemeente herindeling is ook toegepast in het eerste deel van deze dataset dat ‘tm’ bevat in de bestandsnaam en de data bevat vanaf het begin van de pandemie tot en met 3 oktober 2021 (week 39). Zie beschrijving van de variabele Municipality_code voor meer informatie. Versie 8 update (4 april 2023):
- Vanaf 4 april 2023 zal dit bestand wekelijks op dinsdag worden geüpdatet. De data wordt met terugwerkende kracht bijgewerkt voor de andere dagen.

Vanaf 6 september 2023 wordt dit bestand wekelijks op woensdag geüpdatet. De data wordt met terugwerkende kracht bijgewerkt voor de andere dagen.

`Date_of_report`: Datum en tijd waarop het databestand is aangemaakt door het RIVM.

`Date_of_statistics`: Datum van ziekenhuisopname (variabele Hospital_admission) of de datum waarop de ziekenhuisopname is gemeld aan de NICE registratie (variabele Hospital_admission_notification).

`Municipality_code`: Gemeentecode. Gemeentelijke indeling gebaseerd op postcode van de woonplaats van de SARS-CoV-2 positief geteste persoon, gecodeerd volgens CBS. Sinds de eerste publicatiedatum van 13 maart 2020 tot de versie 3 update van 20 januari 2022, hebben 2 gemeentelijke herindelingen plaatsgevonden. Tot 7 januari 2021 is dit bestand volgens de gemeente indeling van 2020. Vanaf 7 januari 2021 t/m 19 januari 2022 is dit bestand samengesteld volgens de gemeente indeling van 1 januari 2021: Gemeenten Appingedam, Delfzijl en Loppersum zijn samengevoegd tot de nieuwe gemeente Eemsdelta Gr. De gemeente Haaren is opgegaan in de gemeenten Oisterwijk, Tilburg, Vught en Boxtel (https://www.cbs.nl/nl-nl/onze-diensten/methoden/classificaties/overig/gemeentelijke-indelingen-per-jaar/indeling-per-jaar/gemeentelijke-indeling-op-1-januari-2021). Met de opdeling van Haaren is de veiligheidsregio Midden- en West-Brabant iets groter geworden, ten koste van veiligheidsregio Brabant-Noord. Vanaf 20 januari 2022 t/m 23 maart 2022 is dit bestand samengesteld volgens de gemeente indeling van 1 januari 2022. Gemeente Beemster is opgegaan in gemeente Purmerend. De gemeenten Heerhugowaard en Langedijk zijn samengevoegd tot gemeente Dijk en Waard. Gemeente Landerd is met gemeente Uden samengevoegd tot gemeente Maashorst. De gemeenten Boxmeer, Cuijk, Grave, Mill en Sint Hubert en Sint Anthonis zijn samengevoegd tot de gemeente Land van Cuijk (https://www.cbs.nl/nl-nl/onze-diensten/methoden/classificaties/overig/gemeentelijke-indelingen-per-jaar/indeling-per-jaar/gemeentelijke-indeling-op-1-januari-2022). Vanaf 24 maart 2022 t/m 31 december 2022 is dit bestand samengesteld volgens de gemeente indeling van 24 maart 2022. Gemeente Weesp is opgegaan in gemeente Amsterdam. Met deze indeling is de veiligheidsregio Gooi- en Vechtstreek kleiner geworden en de veiligheidsregio Amsterdam-Amstelland groter; GGD Amsterdam is groter geworden en GGD Gooi- en Vechtstreek is kleiner geworden (( https://www.cbs.nl/nl-nl/onze-diensten/methoden/classificaties/overig/gemeentelijke-indelingen-per-jaar/indeling-per-jaar/gemeentelijke-indeling-op-1-januari-2022) Vanaf 1 januari 2023 is dit bestand samengesteld volgens de gemeente indeling van 1 januari 2023. De gemeenten Brielle, Hellevoetsluis en Westvoorne zijn samen opgegaan in de nieuwe gemeente Voorne aan Zee (Gemeentelijke indeling op 1 januari 2023 (https://www.cbs.nl/nl-nl/onze-diensten/methoden/classificaties/overig/gemeentelijke-indelingen-per-jaar/indeling-per-jaar/gemeentelijke-indeling-op-1-januari-2023)).

`Municipality_name`: Naam van de gemeente.

`Security_region_code`: Veiligheidsregiocode.

`Security_region_name`: Naam van de veiligheidsregio. De veiligheidsregio is gebaseerd op de woonplaats van de patiënt. Dit is de naam van de veiligheidsregio’s zoals tot dusver gebruikt in diverse rapportages en verslagen van het RIVM, en kan iets afwijken van de naamgeving zoals aangegeven in de codelijst van CBS (zie link hierboven bij variabele Security_region_code). Zie ook: https://www.rijksoverheid.nl/onderwerpen/veiligheidsregios-en-crisisbeheersing/veiligheidsregios

`Hospital_admission_notification`: Het aantal nieuwe, bij de NICE registratie gemelde, COVID-19 patiënten dat in het ziekenhuis is opgenomen per datum waarop de ziekenhuisopname is gemeld [Date_of_statistics].

`Hospital_admission`: Het aantal nieuwe, bij de NICE registratie gemelde, COVID-19 patiënten dat in het ziekenhuis is opgenomen per ziekenhuisopnamedatum [Date_of_statistics]. Een patiënt kan meerdere keren in een ziekenhuis worden opgenomen.
Ondanks dat aan ziekenhuizen wordt gevraagd meerdere malen per week de COVID-19 patiënten te registeren, kan de registratie van het aantal patiënten achterlopen. Dit heeft als gevolg dat de aantallen van de afgelopen dagen nog onvolledig kunnen zijn (https://www.stichting-nice.nl).

Correcties die in meldingen in het bronsysteem van de NICE registratie worden gedaan door medewerkers van ziekenhuizen kunnen ook leiden tot correcties in dit databestand. Aantallen die in het verleden door het RIVM zijn gepubliceerd kunnen in dat geval afwijken van de aantallen in dit databestand. Dit bestand bevat op het moment van aanmaken en publicatie dus altijd de meest actuele gegevens volgens het bronsysteem van de NICE registratie.
