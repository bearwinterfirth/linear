# linear

### G-uppgiften
G-uppgiften (deluppgifterna c-f) finns i filen __sort.py__. Här läses de 600 punkterna från filen __unlabelled_data.csv__ in, och kategoriseras genom att undersöka om varje punkt ligger ovanför eller under linjen $y=-1.5x+0.2$ (denna linje har valts genom en okulär undersökning av en plot av samtliga punkter).

Varje punkt får ett tillägg i form av siffran 0 (under/vänster om linjen) eller 1 (över/höger om linjen). Dessa data skrivs sedan till filen __labelled_data.csv__.

Vi plottar också samtliga punkter tillsammans med den föreslagna linjen, så att man kan få en uppfattning om den verkar rimlig. Punkterna har färg efter sin kategori. För att förenkla plottandet har punkterna delats upp i separata listor, efter klasstillhörighet. 

### VG-uppgiften
VG-uppgiften återfinns i notebooken __sort_alternative.ipynb__. (_OBS! Viktigt att köra python-fönstren uppifrån och ned, då vissa variabelnamn definierats i tidigare fönster!_) Här undersöks några alternativ till den föreslagna linjen från G-uppgiften, och modellernas rimlighet diskuteras.

Alla linjer plottas först i samma fönster, tillsammans med punkterna (ännu oklassificerade), för att man enklast ska kunna jämföra dem. Därefter följer en fyrfaldig klassificering av punkterna, baserat på var och en av de fyra linjerna. All klassificering (klass 0 resp. klass 1) sparas i fyra separata listor, tillsammans med de ursprungliga punkterna, för eventuell framtida referens. (Däremot skrivs inga data till någon ny fil.)

För var och en av linjerna räknas anatalet punkter i klass 0 respektive klass 1. Det visar sig bli mycket jämna uppdelningar, dock aldrig 300-300. Separata plottar för var och en av de fyra linjerna (nu med olikfärgade klassificerade punkter) ritas upp och jämförs i den sammanfattande diskussionen.