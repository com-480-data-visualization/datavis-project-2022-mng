OpenData: Energie Reporter -- Reporter Energie -- Reporter Energetico
===========================================================================

Der Energie Reporter zeigt die Entwicklungen der Energiewende in den 
Gemeinden der Schweiz. Hier erfahren Sie den aktuellen Fortschritt in den 
ausgewählten Bereichen Elektroautos, Produktion Solarstrom und erneuerbar 
heizen für jede Gemeinde.

Le ReporterEnergie montre les développements du tournant énergétique dans 
les communes de Suisse. Vous y découvrirez les progrès actuels dans les
domaines choisis, à savoir les voitures électriques, la production 
d'électricité solaire et le chauffage renouvelable pour chaque commune.
-- Version française voir ci-dessous. --

Il ReporterEnergetico mostra gli sviluppi della transizione energetica nei 
comuni della Svizzera. Qui potete scoprire i progressi attuali nelle aree 
selezionate di auto elettriche, produzione di energia solare e riscaldamento 
rinnovabile per ogni comune.
-- Versione italiana vedi sotto. --



-- (DE) -- 
===========================================================================

Lizenz und Nutzungsbedingungen
---------------------------------------------------------------------------
Diese Daten sind unter der Creative Commons Lizenz CC BY 4.0 veröffentlicht. 
Sie können frei verwendet und weitergegeben werden. 
Bei einer Veröffentlichung müssen der Name "Energie Reporter" als Quelle
sowie "geoimpact", "WWF Schweiz" und "EnergieSchweiz" als Mitwirkende 
angegeben werden.
Bei Online-Inhalten ist zudem der Link zu Energie Reporter
(https://www.reporterenergie.ch) anzugeben.

Kontakte
---------------------------------------------------------------------------
### Medienkontakt
Myriam Planzer, Projektleiterin Energiewende
+41 44 297 23 59
myriam.planzer@wwf.ch
WWF Schweiz
Hohlstrasse 110, 8010 Zürich
www.wwf.ch

### Daten, Inhalte & Umsetzung
Alexander Thommen, Communications & Business Development
+41 41 560 09 85
alexander.thommen@geoimpact.ch
geoimpact AG
Gutenbergstrasse 14, 3011 Bern
www.geoimpact.ch

### Mit Unterstützung von EnergieSchweiz
Bundesamt für Energie BFE
Geschäftsstelle EnergieSchweiz
Pulverstrasse 13, 3063 Ittigen
www.energieschweiz.ch


Rechtliche Hinweise
---------------------------------------------------------------------------
Die Inhalte auf Energie Reporter dienen ausschliesslich Informationszwecken 
und wurden mit grösstmöglicher Sorgfalt erstellt. Die geoimpact übernimmt 
jedoch keine Gewähr für die Richtigkeit und Aktualität der bereitgestellten 
Inhalte. Die Werte werden auf der Grundlage bestehender Datenquellen 
automatisiert berechnet. Die geoimpact hat keinen Einfluss auf die 
Datenlage und somit auf die Aktualität und Qualität der Ursprungsdaten.
Berechnungen können zudem Annahmen beinhalten. Trotz Qualitätsprüfung sind 
Fehler in den eigenen Daten und in Daten Dritter sowie in der Software 
nicht auszuschliessen. Die geoimpact lehnt explizit jede Haftung für 
direkten, indirekten und/oder Folgeschaden irgendwelcher Art ab.


energyreporter_latest.zip
---------------------------------------------------------------------------
Der aktuelle Datensatz enthält die aktuellen Daten der Energie 
Reporter-Applikation zum Zeitpunkt des Downloads.

Er enthält drei CSV-Dateien:
* energyreporter_municipality_latest.csv: Energie Reporter-Indikatoren aller Gemeinden der Schweiz.
* energyreporter_canton_latest.csv: Energie Reporter-Indikatoren aller Kantone der Schweiz.
* energyreporter_national_latest.csv: Energie Reporter-Indikatoren der gesamten Schweiz.

WICHTIGER HINWEIS:
Für die Berechnung der Indikatoren auf Kantons- und nationaler Ebene dürfen
nicht einfach die Werte der Gemeinden gemittelt werden, da diese Werte auf
aggregierten Daten beruhen. Die Indikatoren müssen entweder direkt auf Basis
der Daten berechnet werden, welche der Aggregation zugrunde liegen, oder die
Werte der Gemeinden müssen anhand der Anzahl Objekte in einer Gemeinde
(z.B. Anzahl Autos) gewichtet werden. Der Einfachheit halber stellen wir
in diesem Download bereits für alle Ebene vorberechnete Indikatoren zur
Verfügung (Gemeinde, Kanton, Schweiz).

energyreporter_historized.zip
---------------------------------------------------------------------------
Der historisierte Datensatz enthält monatliche Zeitschnitte seit dem 
Bestehen des Energie Reporters (1. März 2021) mit dem Fortschritt aller
Gemeinden und Kantone sowie der Schweiz.

Er enthält drei CSV-Dateien:
* energyreporter_municipality_historized.csv: Energie Reporter-Indikatoren aller Gemeinden der Schweiz pro Monat.
* energyreporter_canton_historized.csv: Energie Reporter-Indikatoren aller Kantone der Schweiz pro Monat.
* energyreporter_national_historized.csv: Energie Reporter-Indikatoren der gesamten Schweiz pro Monat.


Beschreibung Attribute
---------------------------------------------------------------------------
| Attribut                            | Typ                | Einheit      | Beschreibung
|-------------------------------------|--------------------|--------------|---------------------------------------------------------------------------------------
| bfs_nr                              | Integer            |              | Offizielle Gemeinde-ID des Bundesamtes für Statistik (nur für Gemeindedaten)
| municipality                        | Text               |              | Gemeindename (nur für Gemeindedaten)
| canton                              | Text               |              | Kantonskürzel (nur für Gemeinde- und Kantonsdaten)
| energyreporter_date                 | Datum (YYYY-MM-DD) |              | Datenstand der Energie Reporter-Applikation (nur für historisierte Daten)
| electric_car_share                  | Zahl               | Dezimalbruch | Indikator: Elektroautos (Details siehe unten)
| electric_car_share_last_change      | Datum (YYYY-MM-DD) |              | Datenstand der primären Datenquelle (ASTRA)
| solar_potential_usage               | Zahl               | Dezimalbruch | Indikator: Produktion Solarstrom (Details siehe unten)
| solar_potential_usage_last_change   | Datum (YYYY-MM-DD) |              | Letzte Änderung der primären Datenquelle (Produktionsanlagen, Solarpotenzial)
| renewable_heating_share             | Zahl               | Dezimalbruch | Indikator: Erneuerbar heizen (Details siehe unten)
| renewable_heating_share_coverage    | Zahl               | Dezimalbruch | Abdeckung der Heizungsdaten zur Qualitätsabschätzung des Indikators Erneuerbar heizen
| renewable_heating_share_last_change | Datum (YYYY-MM-DD) |              | Letzte Änderung der primären Datenquelle (Heizungen aus dem GWR)


Indikator: Elektroautos
---------------------------------------------------------------------------
Der Wert Elektroautos zeigt auf, wie gross der Anteil elektrisch 
angetriebener Fahrzeuge im Strassenverkehr in Prozent ist.

Für die Erhebung werden alle Personenwagen und Lieferwagen berücksichtigt, 
welche sich aktuell im Verkehr befinden. Die Fahrzeuge werden über die 
Postleitzahl und Ortsbezeichnung der Halteradressen einer Gemeinde zugeordnet.

Als Elektroautos gelten alle Fahrzeuge mit einem elektrischen Antrieb, 
einem elektrischen Antrieb mit Range Extender oder einem 
Wasserstoff/elektrischen Antrieb. Als Personenwagen sind Fahrzeuge 
klassifiziert, welche dem Personen-Transport dienen und über höchstens 
neun Sitzplätze inklusive Fahrerin oder Fahrer verfügen.
Lieferwagen sind für den Sachentransport konzipiert und haben höchstens ein 
Gesamtgewicht von 3.5 Tonnen.

Die Daten werden monatlich aktualisiert.

Datenquellen: ASTRA (https://www.astra.admin.ch/astra/de/home.html), 
swisstopo (https://www.swisstopo.admin.ch/)


Indikator: Produktion Solarstrom
---------------------------------------------------------------------------
Der Wert Produktion Solarstrom zeigt auf, wie viel Prozent des 
realisierbaren Solar-Potenzials auf Dachflächen bereits für die 
Stromproduktion mit Photovoltaik (PV) Anlagen genutzt wird.

Der Wert gibt die installierte PV-Leistung im Verhältnis zum wirtschaftlich 
sowie technisch realisierbaren Potenzial auf Dachflächen in Prozent an.

Die installierte Leistung setzt sich aus allen bestehenden PV-Anlagen 
zusammen, die im von der Pronovo AG betriebenen schweizerischen 
Herkunftsnachweissystem registriert sind.
Die grosse Mehrheit aller PV-Anlagen in der Schweiz ist im 
Herkunftsnachweissystem registriert.
Über nicht registrierte Anlagen kann keine Aussage getroffen werden.
Die PV-Anlagen werden anhand der im Herkunftsnachweissystem registrierten 
Adresse einer Gemeinde zugewiesen.

Für die Berechnung des wirtschaftlich sowie technisch realisierbaren 
Potenzials werden die für Solarstrom geeigneten Dachflächen aller Gebäude 
innerhalb eines Gemeindegebiets verwendet.
Fassadenflächen werden nicht berücksichtigt. Gebäude, die in mehr als einem 
Gemeindegebiet liegen, werden anhand der im Gebäude liegenden Adressen den 
Gemeinden zugeordnet.
Geeignete Dachflächen sind grösser als 10 Quadratmeter und für die 
Solarstrom-Produktion mindestens "gut" geeignet, das heisst sie verfügen 
über eine mittlere jährliche Sonneneinstrahlung von über 1’000 Kilowattstunden 
pro Quadratmeter. Für die Dachflächen wird ein Belegungsgrad von 70% angenommen 
(Anteil der Dachfläche, welche mit PV-Modulen belegt werden kann). Es wird 
weiter ein Modulwirkungsgrad von 17% für die Produktion von PV-Strom verwendet.

Die Daten werden monatlich aktualisiert.

Datenquellen: UVEK (https://www.uvek-gis.admin.ch/BFE/storymaps/EE_Elektrizitaetsproduktionsanlagen/), 
swisstopo (https://www.swisstopo.admin.ch/)


Indikator: Erneuerbar heizen
---------------------------------------------------------------------------
Der Wert erneuerbar heizen gibt an, wie viel Prozent der Gebäude ein 
erneuerbares Heizsystem installiert haben.

Für die Erhebung werden alle Gebäude in einer Gemeinde berücksichtigt, 
welche über ein installiertes Heizsystem mit Wärme versorgt werden.
Die Gesamtanzahl der Heizsyssteme setzt sich aus allen registrierten 
primären Systemen für die Wärmeerzeugung zusammen. Gebäude ohne Heizsystem 
oder mit einem nicht definierten Heizsystem werden nicht berücksichtigt.

Die Heizsysteme werden anhand der verwendeten Energie-/Wärmequelle sowie 
des Wärmeerzeugers in erneuerbare und nicht erneuerbare Heizsysteme 
eingeteilt. 
Als erneuerbare Heizsysteme gelten Heizungen mit einer erneuerbaren 
Energie-/Wärmequelle (Luft, Erdwärme, Wasser, Abwärme, Holz oder Sonne).
Als nicht erneuerbar gelten Heizungen mit einer nicht erneuerbaren 
Energie-/Wärmequelle (Gas, Heizöl) und elektrische Heizsysteme (bei einer 
elektrischen Heizung kann die Energiequelle nicht eruiert werden).
Heizungen, welche an einen Wärmeverbund angeschlossen sind, werden aufgrund 
der primären Energiequelle der Heizzentrale als erneuerbar oder nicht 
erneuerbar deklariert.

In einzelnen Gemeinden ist bei weniger als 80 % der Gebäude ein Heizsystem 
dokumentiert (siehe Attribut renewable_heating_share_coverage).
Die Datenlage für die Erhebung der Heizsysteme ist in diesen Gemeinden 
unzureichend und in der Energie Reporter-Applikation wird kein Wert 
ausgewiesen. In diesem Datensatz sind die Daten zu diesen Gemeinden aber 
trotzdem enthalten.

Die Daten werden monatlich aktualisiert.
Die Aktualität der Originärdatenquelle der Heizsysteme kann hier eingesehen werden: https://www.housing-stat.ch/monitoringnrj/.

Datenquellen: BFE (https://www.bfe.admin.ch/bfe/de/home.html), BFS (https://www.bfs.admin.ch/bfs/de/home.html), swisstopo (https://www.swisstopo.admin.ch/)




-- (FR) -- 
===========================================================================

Conditions d'utilisation
---------------------------------------------------------------------------
Ces données sont publiées sous la licence Creative Commons CC BY 4.0
(https://creativecommons.org/licenses/by/4.0/deed.fr).
Ils peuvent être librement utilisés et transmis.
En cas de publication, le nom "Energie Reporter" doit être indiqué comme
source et "geoimpact", "WWF Suisse" et "SuisseEnergie" comme contributeurs.
Dans le cas d'un contenu en ligne, le lien vers Energie Reporter
(https://www.energiereporter.ch) doit également être indiqué.


Avis juridique
---------------------------------------------------------------------------
Le contenu de "Reporter Energie" est uniquement fourni à titre d'information
et a été élaboré avec le plus grand soin. Toutefois, geoimpact ne garantit
pas l’exactitude et le caractère actuel du contenu fourni. Les valeurs sont
calculées automatiquement sur la base des sources de données existantes.
La geoimpact n'a aucune influence sur l'actualité et la qualité des données
originales. Les calculs peuvent également contenir des hypothèses. Malgré le
contrôle de qualité, des erreurs dans ses propres données et dans les données
de tiers ainsi que dans les logiciels ne peuvent être exclues. La geoimpact
décline explicitement toute responsabilité pour les dommages directs,
indirects et/ou consécutifs de toute nature.


Contacts
---------------------------------------------------------------------------
### Contact médias
Myriam Planzer, chef de projet Transition énergétique
+41 44 297 23 59
myriam.planzer@wwf.ch
WWF Suisse
Hohlstrasse 110, 8010 Zurich
www.wwf.ch

### Données, contenu et réalisation
Alexander Thommen, Communications et développement commercial
+41 41 560 09 85
alexander.thommen@geoimpact.ch
geoimpact AG
Gutenbergstrasse 14, 3011 Bern
www.geoimpact.ch

### Avec le soutien de SuisseEnergie
SuisseEnergie
Office fédéral de l’énergie (OFEN)
Pulverstrasse 13, 3063 Ittigen
www.suisseenergie.ch


energyreporter_latest.zip
---------------------------------------------------------------------------
L'ensemble de données actuel contient les données actuelles de
l'application Reporter Energie au moment du téléchargement.

Il contient trois fichiers CSV :
* energyreporter_municipality_latest.csv : Indicateurs du Reporter Energie de toutes les communes de Suisse.
* energyreporter_canton_latest.csv : Indicateurs du Reporter Energie de toutes les cantons de Suisse.
* energyreporter_national_latest.csv : Indicateurs du Reporter Energie de toute la Suisse.

REMARQUE IMPORTANTE :
Pour le calcul des indicateurs au niveau cantonal et national, il ne faut
pas simplement faire la moyenne des valeurs des communes, car ces
valeurs sont basées sur des données déjà agrégées. Les indicateurs doivent
être calculés directement sur la base de données sur laquelle se fonde
l'agrégation, ou les valeurs des communes doivent être pondérées en
fonction du nombre d'objets dans une commune (p. ex. nombre de voitures).
Par souci de simplicité, nous mettons à disposition dans ce téléchargement
des indicateurs déjà précalculés pour tous les niveaux (commune, canton,
Suisse).


energyreporter_historized.zip
---------------------------------------------------------------------------
Cet ensemble de données contient une série temporelle mensuelle depuis
l'existence d'Energie Reporter (1. Mars 2021) avec l'évolution de toutes
les communes et cantons ainsi que de la Suisse.

Il contient trois fichiers CSV :
* energyreporter_municipality_historized.csv : Indicateurs du Reporter Energie de toutes les communes de Suisse par mois.
* energyreporter_canton_historized.csv : Indicateurs du Reporter Energie de toutes les cantons de Suisse par mois.
* energyreporter_national_historized.csv : Indicateurs du Reporter Energie de toute la Suisse par mois.


Description des attributs
---------------------------------------------------------------------------
| Attribut                            | Type              | Unité             | Description
|-------------------------------------|-------------------|-------------------|---------------------------------------------------------------------------------------
| bfs_nr                              | Entier            |                   | ID officiel de la commune de l'Office fédéral de la statistique (uniquement pour les données communales)
| municipality                        | Texte             |                   | Nom de la commune (uniquement pour les données communales)
| canton                              | Texte             |                   | Abréviation du canton (uniquement pour les données communales et cantonales)
| energyreporter_date                 | Date (YYYY-MM-DD) |                   | État des données de l'application Reporter Energie (uniquement pour les données historisées)
| electric_car_share                  | Nombre            | Fraction décimale | Indicateur : voitures électriques (voir détails ci-dessous)
| electric_car_share_last_change      | Date (YYYY-MM-DD) |                   | État des données de la source de données primaire (OFROU)
| solar_potential_usage               | Nombre            | Fraction décimale | Indicateur : production d'énergie solaire (voir détails ci-dessous)
| solar_potential_usage_last_change   | Date (YYYY-MM-DD) |                   | Dernière modification de la source de données primaire (installations de production, potentiel solaire)
| renewable_heating_share             | Nombre            | Fraction décimale | Indicateur : chauffage renouvelable (voir détails ci-dessous)
| renewable_heating_share_coverage    | Nombre            | Fraction décimale | Couverture des données de chauffage pour l'estimation de la qualité de l'indicateur Chauffage renouvelable
| renewable_heating_share_last_change | Date (YYYY-MM-DD) |                   | Dernière modification de la source de données primaire (chauffages issus du RegBL)


Indicateur : voitures électriques
---------------------------------------------------------------------------
La quantité de voitures électriques correspond au pourcentage de véhicules
à propulsion électrique dans le trafic routier.

L’enquête prend en compte l’ensemble des voitures personnelles et
camionnettes actuellement en circulation. Les véhicules sont affectés à une
commune sur la base du code postal et de l’adresse des propriétaires.

Tous les véhicules à propulsion électrique, à propulsion électrique avec
extension d’autonomie ou à propulsion hydrogène/électrique sont classés
comme des voitures électriques.

Les véhicules sont classés comme véhicules de tourisme s’ils sont utilisés
pour le transport de passagers et comptent un maximum de neuf sièges,
conducteur compris. Les camionnettes sont conçues pour le transport de
marchandises et ont un poids total maximum de 3,5 tonnes.

Les données sont mises à jour mensuellement.

Sources de données: OFROU (https://www.astra.admin.ch/astra/fr/home.html),
swisstopo (https://www.swisstopo.admin.ch/)


Indicateur : production d'énergie solaire
---------------------------------------------------------------------------
La quantité d’électricité solaire indique quel pourcentage du potentiel
solaire réalisable sur les surfaces de toiture est déjà utilisé pour la
production d’électricité au moyen de systèmes photovoltaïques (PV).

Cette valeur indique le pourcentage de capacité photovoltaïque installée
par rapport au potentiel économiquement et techniquement réalisable sur
les surfaces de toitures.

La puissance installée se compose de toutes les installations PV existantes
enregistrées dans le système suisse de garantie d'origine géré par Pronovo AG.
La grande majorité des systèmes photovoltaïques en Suisse sont
enregistrées dans le système de garantie d'origine.
Par rapport des installations non enregistrée ne peut pas être faites aucune
déclaration. Les systèmes photovoltaïques sont attribués à une commune
sur la base de l'adresse enregistrée dans le système des garanties d'origine.

Les surfaces des toitures de l’ensemble des bâtiments d’une commune qui
sont adaptées à l’électricité solaire sont utilisées pour calculer le
potentiel réalisable d’un point de vue économique et technique. Les surfaces
des façades ne sont pas pris en considération. Les bâtiments situés dans plus
d’un territoire municipal sont attribués sur la base des adresses
correspondant au bâtiment de ces communes. Les surfaces de toiture
appropriées sont supérieures à 10 mètres carrés et au minimum « bien »
adaptées à la production d’électricité solaire, c’est-à-dire qu’elles ont une
irradiation solaire annuelle moyenne de plus de 1 000 kilowattheures par mètre
carré. On suppose un taux d’occupation de 70 % pour les surfaces de toit
(proportion de la surface de toit pouvant être couverte par des modules PV).
Un rendement de 17 % est également appliqué à la production d’électricité
photovoltaïque.

Les données sont mises à jour mensuellement.

Sources de données: UVEK (https://www.uvek-gis.admin.ch/BFE/storymaps/EE_Elektrizitaetsproduktionsanlagen/?lang=fr),
swisstopo (https://www.swisstopo.admin.ch/)


Indikator : chauffage renouvelable
---------------------------------------------------------------------------
Pour l’enquête, tous les bâtiments d’une commune qui sont alimentés en
électricité par un système de chauffage installé sont pris en compte. Le
nombre total de systèmes de chauffage comprend tous les systèmes primaires
enregistrés pour la production de chaleur. Ne sont pas pris en compte, les
bâtiments sans système de chauffage ou avec un système de chauffage non
défini.

Les systèmes de chauffage sont classés en systèmes de chauffage
renouvelables et non renouvelables selon la source d’énergie/chaleur
utilisée et le générateur de chaleur. Les systèmes de chauffage
renouvelables sont ceux utilisant une source d’énergie/de chaleur
renouvelable (air, géothermie, eau, chaleur résiduelle, bois ou solaire).
Les systèmes de chauffage non renouvelables sont des systèmes utilisant une
source d’énergie/de chaleur non renouvelable (gaz, mazout) et les systèmes de
chauffage électrique (dans le cas du chauffage électrique, la source d’énergie
ne peut être déterminée) sont considérés comme non renouvelables. Les systèmes
de chauffage qui sont connectés à un réseau de chauffage sont désignés comme
renouvelables ou non renouvelables en fonction de la source d’énergie primaire
du système de chauffage.

Dans certaines communes, un système de chauffage est renseigné pour moins de
80 % des bâtiments. La situation des données pour l’enquête sur les systèmes
de chauffage est insuffisante dans ces communes et aucune valeur n’est
indiquée.

Les données sont mises à jour mensuellement. L'actualité de la source de
données originale des systèmes de chauffage peut être consultée ici.:
https://www.housing-stat.ch/monitoringnrj/.

Sources de données: BFE (https://www.bfe.admin.ch/bfe/fr/home.html),
BFS (https://www.bfs.admin.ch/bfs/fr/home.html),
swisstopo (https://www.swisstopo.admin.ch/)




-- (IT) -- 
===========================================================================

Termini di utilizzo
---------------------------------------------------------------------------
Questi dati sono pubblicati sotto la licenza Creative Commons CC BY 4.0.
(https://creativecommons.org/licenses/by/4.0/deed.it)
Possono essere liberamente utilizzati e trasmessi.

In caso di pubblicazione, deve essere indicato il nome "Reporter Energetico"
come fonte e "geoimpact", "WWF Svizzera" e "SvizzeraEnergia" come
contributori. Nel caso di contenuti online deve essere fornito anche il link
a Reporter Energetico.


Avviso legale
---------------------------------------------------------------------------
Il contenuto della piattaforma "Reporter Energetico" è reso disponibile
solo a scopo informativo ed è stato realizzato con la massima cura
possibile. Tuttavia, la geoimpact AG non fornisce garanzie sull'accuratezza
e lo stato d'attualità dei contenuti. I valori messi in evidenza sono
frutto di elaborazioni automatizzate basate su dati preesistenti, pertanto
la geoimpact AG non ha alcuna influenza sullo stato e l'attualità dei dati
di base. Ai fini dell'analisi possono essere state applicati valori
ipotetici e/o approssimati. La geoimpact AG declina esplicitamente ogni
responsabilità per danni diretti, indiretti e di qualsiasi altra natura che
possano essere ricondotti all'utilizzo della piattaforma e dei dati forniti.


Contatti
---------------------------------------------------------------------------
### Contatto con i media
Myriam Planzer, responsabile della transizione energetica
+41 44 297 23 59
myriam.planzer@wwf.ch
WWF Svizzera
Hohlstrasse 110, 8010 Zürich
www.wwf.ch

### Dati, contenuti e realizzazione
Alexander Thommen, comunicazione e business development
+41 41 560 09 85
alexander.thommen@geoimpact.ch
geoimpact AG
Gutenbergstrasse 14, 3011 Bern
www.geoimpact.ch

### Con il sostegno di SvizzeraEneregia
SvizzeraEneregia
Ufficio Federeale dell'Energia (BFE)
Pulverstrasse 13, 3063 Ittigen
www.energieschweiz.ch


energyreporter_latest.zip
---------------------------------------------------------------------------
Quanto segue è l'andamento attuale di tutti i comuni, i cantoni e della
Svizzera intera. Il seguente archivio contiene dati dell'applicazione
"Reporter Energetico" aggiornati all'istante del download.

Questo archivio contiene 3 file CSV:
* energyreporter_municipality_latest.csv: metriche del Reporter Energetico di tutti i comuni della Svizzera.
* energyreporter_canton_latest.csv: metriche del Reporter Energetico su tutti i cantoni della Svizzera.
* energyreporter_national_latest.csv: metriche del Reporter Energetico di tutta la Svizzera.

NOTE IMPORTANTI:
Per il calcolo del valore medio non è possibile avvalesi della
somma dei singoli indici a livello cantonale o nazionale poiché questi
ultimi si basano su dati aggregati. Gli indici devono essere direttamente
calcolati sulle fonti che sono alla base del calcolo aggregato oppure devono
essere ponderati con il numero degli Oggetti presenti nel comune (e.g. il
numero delle Auto). Al fine di ridurre la complessità sono stati già calcolati
indici di comuni, cantoni e di tutta la svizzera e messi a disposizione
tramite link di download.


energyreporter_historized.zip
---------------------------------------------------------------------------
I seguenti sono i dati ad intervalli mensili a partire dalla data di
pubblicazione del Reporter Energetico (1. Marzo 2021) con l'andamento di
tutti i comuni e cantoni, nonché della Svizzera.

Questo archivio contiene 3 file CSV:
* energyreporter_municipality_historized.csv: metriche mensili del Reporter Energetico di tutti i comuni della Svizzera.
* energyreporter_canton_historized.csv: metriche mensili del Reporter Energetico di tutti i cantoni della Svizzera.
* energyreporter_national_historized.csv: metriche mensili del Reporter Energetico di tutta la Svizzera.


Descrizione degli attributi
------------------------------------------------------------------------------------------------------------------------
| Attributo                           | Tipo               | Unità              | Descrizione
|-------------------------------------|--------------------|--------------------|---------------------------------------
| bfs_nr                              | Integer            |                    | Identificatore ufficiale del comune attribuito dall'ufficio federale di statistica (per i comuni)
| municipality                        | Testo              |                    | Nome del comune (per i comuni)
| canton                              | Testo              |                    | Abbreviazione del comune (per i comuni e cantoni)
| energyreporter_date                 | Data (YYYY-MM-DD)  |                    | Data dello stato del Reporter Energetico (solo per dati storicizzati)
| electric_car_share                  | Numero             | Frazione decimale  | Indice: auto elettriche (vedi dettagli a seguire)
| electric_car_share_last_change      | Data (YYYY-MM-DD)  |                    | Data dello stato delle fonti primarie (ASTRA)
| solar_potential_usage               | Numero             | Frazione decimale  | Indice: produzione di energia fotovoltaica (vedi dettagli a seguire)
| solar_potential_usage_last_change   | Data (YYYY-MM-DD)  |                    | Ultimo cambiamento della fonte primaria (impianti fotovoltaici, potenziale fotovoltaico)
| renewable_heating_share             | Numero             | Frazione decimale  | Indice: riscaldamento da fonti rinnovabili (vedi dettagli a seguire)
| renewable_heating_share_coverage    | Numero             | Frazione decimale  | Copertura dei dati relativi all'indice riscaldamento rinnovabile per la stima di qualità dello stesso.
| renewable_heating_share_last_change | Data (YYYY-MM-DD)  |                    | Ultimo cambiamento della fonte primaria dei dati (impianti di riscaldamento del REA)


Indicatore: Mobilità elettrica
---------------------------------------------------------------------------
Il valore "Mobilità elettrica" mostra la percentuale di veicoli alimentati
elettricamente nel traffico stradale.

Per l'analisi sono state prese in considerazione tutte le autovetture e
mezzi di trasporto attualmente in circolazione. I veicoli vengono assegnati
ad un'area comunale prendendo in considerazione il codice di avviamento
postale dei proprietari del veicolo.

Tutti i veicoli aventi motore elettrico, motore elettrico con range extender
o un motore ad idrogeno/elettrico sono classificati come veicoli elettrici.

I veicoli sono classificati come autovetture se sono utilizzati per il
trasporto di passeggeri e hanno un massimo di nove posti, incluso il
conducente. Gli altri mezzi di trasporto presi in considerazione, progettati
per il trasporto merci, hanno un peso massimo di 3,5 tonnellate.

I dati sono aggiornati mensilmente.

Fonte dei dati: ASTRA (https://www.astra.admin.ch/astra/it/home.html),
swisstopo (https://www.swisstopo.admin.ch/)


Indicatore: Produzione fotovoltaica
---------------------------------------------------------------------------
Il valore "Utilizzo fotovoltaico" mostra in percentuale il potenziale
solare delle superfici dei tetti che viene già utilizzato per la produzione
di elettricità con sistemi fotovoltaici.

Il valore indica la capacità fotovoltaica installata in relazione al
potenziale economicamente e tecnicamente fattibile sulle superfici dei
tetti espresso in percentuale.

La capacità installata è costituita da tutti gli impianti fotovoltaici
esistenti, che sono stati registrati per il sostegno del governo federale
nell'ambito del sistema di tariffe di cessione in rete o per la tariffa
unica. Quasi tutti gli impianti fotovoltaici in Svizzera sono registrati
in una di queste due banche dati. Sugli impianti non registrati non è
possibile condurre alcuna analisi. Gli impianti fotovoltaici sono assegnati
a un comune in base all'indirizzo registrato nel sistema di garanzia
d'origine.

Per calcolare il potenziale economicamente e tecnicamente fattibile,
vengono prese in considerazione tutte le superfici dei tetti di tutti
gli edifici all'interno di un comune. Le facciate degli edifici non sono
prese in considerazine.Gli edifici situati in più di una zona comunale
sono assegnati ai comuni in base agli indirizzi interni all'edificio. Le
dimensioni minime per un tetto sono di almeno 10 metri quadrati e devono
essere classificati come "idonei", ovvero devono avere un'irradiazióne
solare media annuale di più di 1.000 chilowattora per metro quadrato. Si
assume che si possa al massimo ricoprire il 70% della superficie del tetto
con dei moduli fotovoltaici. L'efficienza del modulo fotovoltaico è
approssimativa e viene assunto un valore del 17%.

I dati sono aggiornati mensilmente.

Fonte dei dati: UVEK (https://www.uvek-gis.admin.ch/BFE/storymaps/EE_Elektrizitaetsproduktionsanlagen/?lang=it),
swisstopo (https://www.swisstopo.admin.ch/)


Indicatore: Riscaldamento rinnovabile
---------------------------------------------------------------------------
Il valore "Riscaldamento rinnovabile" indica la percentuale di edifici che
hanno un sistema di riscaldamento rinnovabile installato.

Per l'indagine, vengono presi in considerazione tutti gli edifici con un
impianto di riscaldamento installato. Il numero totale di sistemi di
riscaldamento è dato dall'insieme dei sistemi primari di riscaldamento
registrati. Gli edifici senza impianti di riscaldamento o con un impianto
di riscaldamento non classificato non vengono presi in considerazione.

Gli impianti di riscaldamento sono classificati in impianti di riscaldamento
rinnovabili e non rinnovabili in base alla fonte di energia/calore utilizzata
e/o al combustibile di cui fanno uso. Gli impianti considerati rinnovabili
sono quelli con una fonte di energia/calore rinnovabile (aria, geotermica,
acqua, legno o solare). Gli impianti non rinnovabili sono sistemi di
riscaldamento con una fonte di energia/calore non rinnovabile come gas, olio
combustibile e sistemi di riscaldamento elettrici (nel caso del riscaldamento
elettrico, la fonte di energia non può essere determinata). Gli impianti di
riscaldamento che sono collegati a una rete di riscaldamento sono dichiarati
rinnovabili o non rinnovabili in base alla fonte di energia primaria del
sistema di riscaldamento.

In alcuni comuni, la copertura dei dati circa gli impianti di riscaldamento
negli edifici è inferiore all'80%. In tal caso la base dei dati è
insufficiente e per tali comuni non viene mostrato alcun valore.

I dati sono aggiornati su base mensile. Lo stato di aggiornamento dei dati
sui sistemi di riscaldamento possono essere approfondito qui:
https://www.housing-stat.ch/monitoringnrj/.

Fonte dei dati: BFE (https://www.bfe.admin.ch/bfe/it/home.html),
BFS (https://www.bfs.admin.ch/bfs/it/home.html),
swisstopo (https://www.swisstopo.admin.ch/)

