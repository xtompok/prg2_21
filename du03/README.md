# Hledání volných ploch a svahů

## Zadání
Implementujte program, který za pomoci digitálního modelu terénu a digitálního modelu povrchu nalezne nezastavěné plochy a určí na nich sklon.

Program načte 2 vstupní soubory - digitální model terénu, zadaný parametrem `--terrain <jmeno_souboru>` a digitální model povrchu, zadaný parametrem `--surface <jmeno_souboru>`. Následně spočítá rozdíl mezi těmito rastry a hledá místa, kde jsou rastry shodné, tedy terén odpovídá povrchu. Přesné určení limitu pro shodnost je součástí zadání, tento limit by měl být definován jako konstanta v programu.

Místa bez zástavby a vegetace z předchozí části pak program použije jako masku na terénní model a spočítá na těchto místech sklon z digitálního modelu terénu a výsledný rastr uloží. Tento rastr má jako hodnoty jednotlivých pixelů sklony svahu v daném místě.

Masku ukládejte jako `mask.tiff`, výstup jako `slopes.tiff`.

### Dokumentace
K aplikaci dodejte stručnou uživatelskou a vývojářskou dokumentaci obsahující nejen návod na použití programu, ale i popis výpočtu a zvolené konstanty. 

## Doporučení
Data si stáhněte z [Geoportálu](https://www.geoportalpraha.cz/cs/data/otevrena-data/seznam##category-3d-model). Protože DMP a DMT nejsou shodné, bude potřeba výpočty počítat tam, kde jsou oba definované. Jak na to se zeptejte na [StackExchange](https://gis.stackexchange.com/questions/337213/adding-raster-layers-of-different-shape-using-rasterio). 

Pro testování si vyřízněte menší oblasti, ať můžete rychle testovat. Pro zpracování používejte bloky, ať se vám data vejdou do RAM. O tom, jak vyrábět vlastní bloky se můžete dočíst třeba na [GISMentors](https://training.gismentors.eu/geopython-zacatecnik/rastrova_data/rasterio/windows.html#bloky).

Pro výpočet sklonu se vám může hodit funkce [`gradient`](https://numpy.org/doc/stable/reference/generated/numpy.gradient.html) z NumPy. Když znáte gradient v obou osách, snadno z něj můžete spočítat úhel.

Zkuste si postup otestovat v GISu a porovnejte výsledky.

Pokud se vám něco nebude dařit, zkonzultujte to s ostatními ve skupině, pokud si
stále nebudete vědět rady, nebojte se ozvat, rád vám pomohu.

## Odevzdání
Odevzdávat budete zdrojové soubory a soubor(y) s dokumentací. Vstupní ani
výstupní rastry nejsou součástí odevzdání.  Odevzdávejte ideálně přes GitHub
nebo podobnou službu, případně je možné poslat i vše zabalené v zipu.

Deadline na odevzdání je týden před tím, než chcete zápočet, o prázdninách 2
týdny.  Každému, kdo mi pošle úkol, odpovím, že jsem ho přijal a že se mi
podařilo zip rozbalit. Pokud neodpovím, urgujte.

### Předčasné odevzdání
Pokud odevzdáte úkol dopředu, zkusím se na něj podívat a napsat vám případné
nedostatky. Tato možnost není garantovaná, ale budu se snažit odbavovat úkoly co
nejrychleji. Zaručuji vám pouze to, že na úkoly se budu dívat v tom pořadí, v
jakém mi budou doručeny. Rovněž nezaručuji, že najdu v programu všechny chyby
napoprvé, tudíž pokud si nějaké nevšimnu, není to garance, že máte program
správně, závazné je pouze hodnocení po deadlinu. Pokud budete odevzdávat přes
GitHub, chyby vám vystavím jako Issue.

## Bodování
  * 3 b za vytvoření masky
  * 3 b za výpočet sklonu
  * 2 b za kvalitu kódu
  * 2 b za dokumentaci

## Bonusové body

### Uložení oblastí vektorově (1--2 body)
Program uloží nalezené oblasti jako vektory do GeoJSONu. Minimální velikost oblasti, kterou ještě vektorizovat, bude určena jako parametr `--min-area <pocet_pixelu>` programu. Soubor se bude jmenovat `slopes.geojson` (1 bod). Každý prvek bude mít atribut `avg_slope` obsahující průměrný sklon oblasti a `stdev` obsahující směrodatnou odchylku sklonu pro danou oblast (2 body).

### Pouze louky (3 body)
Program navíc načte NDIR snímky z leteckého mapování (nebo alespoň 1 vybraný), spočítá z nich NDVI index a z nalezených oblastí v základní verzi programu vybere pouze ty, co obsahují zeleň.
