## Bestandsnaam

`COVID-19_rioolwaterdata.csv`

## Dataset

`Covid-19 Nationale SARS-CoV-2 Afvalwatersurveillance`

## Bron

https://data.overheid.nl/dataset/46040-covid-19-nationale-sars-cov-2-afvalwatersurveillance#panel-description

## Beschrijving

Dit bestand bevat, naast een kolom met het versienummer en een kolom met de datum van aanmaken van het bestand, de volgende karakteristieken per bemonsterde rioolwaterzuiveringsinstallatie (RWZI) in Nederland: Datum van monster, RWZI code, RWZI naam, Virusvracht per 100,000 inwoners

Het bestand is als volgt opgebouwd: Per zuiveringsinstallatie wordt er 24 uur lang een monster genomen van het rioolwater. Deze monsters worden door onderzoekers van het RIVM geanalyseerd op het aantal aanwezige virusdeeltjes. Een record bevat voor elke bemonsterde afval-/rioolwaterzuiveringsinstallatie (AWZI/RWZI) het gemiddelde aantal virusdeeltjes in het rioolwater, gecorrigeerd voor de dagelijkse hoeveelheid rioolwater (debiet) en weergegeven per 100.000 inwoners. Het bestand wordt van maandag tot en met vrijdag ververst (voor 14:00 uur). De informatie over inwonersaantallen per RWZI kunt u vinden in een omzet-tabel, die wordt aangeleverd door het Centraal Bureau voor de Statistiek (CBS). (De versie voor 2021:) (https://www.cbs.nl/nl-nl/maatwerk/2021/06/inwoners-per-rioolwaterzuiveringsinstallatie-1-1-2021) (De versie voor 2022:) (https://www.cbs.nl/nl-nl/maatwerk/2022/42/inwoners-per-rioolwaterzuiveringsinstallatie-1-1-2022)

Per 4 maart 2021 zijn een aantal wijzigingen doorgevoerd voor onderstaande RWZI’s.

- Per 8 oktober 2020 is RWZI Aalst opgeheven. Het bijbehorende verzorgingsgebied is toegevoegd aan dat van RWZI Zaltbommel. De waarden voor de RNA_flow_per_100000 voor Zaltbommel zijn in het databestand vanaf 4 maart 2021 met terugwerkende kracht gewijzigd tot aan de bovengenoemde opheffingsdatum. Voor de waarden die voor de opheffingsdatum zijn gerapporteerd, zijn voor RWZI Aalst en RWZI Zaltbommel de individuele inwonersaantallen gebruikt die golden voor de opheffing van RWZI Aalst.
- Per 9 december 2020 is RWZI Lienden opgeheven. Het bijbehorende verzorgingsgebied is toegevoegd aan dat van RWZI Tiel. De waarden voor RNA_flow_per_100000 voor RWZI Tiel zijn in het databestand vanaf 4 maart 2021 met terugwerkende kracht gewijzigd tot aan de bovengenoemde opheffingsdatum. Voor de waarden die voor de opheffingsdatum zijn gerapporteerd, zijn voor RWZI Lienden en RWZI Tiel de individuele inwonersaantallen gebruikt die golden voor de opheffing van RWZI Lienden. Wijzigingen vanaf 1 januari 2021 zijn verwerkt in de CBS omzet-tabel. Vanaf 30 september 2021 worden wijzigingen in de CBS omzet-tabel verwerkt, zodra ze bekend worden. Vanaf 30 september is de kolom RNA_per_ml uit het open data bestand verwijderd. Waarden die in deze kolom vermeld stonden, zijn omgerekend naar RNA_flow_per_100000 en in die kolom vermeld, voor zover dat mogelijk was. Daarnaast zijn alle waarden van 2021 én 2020 op 30 september 2021 met terugwerkende kracht herberekend met de inwonersaantallen in de CBS tabel die op 30 september 2021 is gepubliceerd. Alle waarden van 2022 zijn op 30 december 2022 met terugwerkende kracht herberekend met de CBS tabel die op 19 oktober 2022 is gepubliceerd.

## Beschrijving van de variabelen

`Version`: Versienummer van de dataset. Wanneer de inhoud van de dataset structureel word gewijzigd (dus niet de dagelijkse update of een correctie op record niveau) , zal het versienummer aangepast worden (+1) en ook de corresponderende metadata in RIVMdata (data.rivm.nl).

`Date_of_report`: Datum waarop het bestand aangemaakt is. (formaat: jjjj-mm-dd)

`Date_measurement`: Datum waarop de monstername van het 24-uurs influent (ongezuiverd afval-/rioolwater) monster is gestart (formaat: jjjj-mm-dd).

`RWZI_AWZI_code`: Code van rioolwaterzuiveringsinstallatie (RWZI) of afvalwaterzuiveringsinstallatie (AWZI).

`RWZI_AWZI_name`: Naam van rioolwaterzuiveringsinstallatie (RWZI) of afvalwaterzuiveringsinstallatie (AWZI).

`RNA_flow_per_100000`: De gemiddelde concentratie SARS-CoV-2 RNA, omgerekend naar dagelijkse hoeveelheid rioolwater (debiet) en weergegeven per 100.000 inwoners.
