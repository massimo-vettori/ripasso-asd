# Ripasso AsD (Modulo 2)

Ho creato questa repository per raccogliere tutti gli algoritmi su grafi che abbiamo fatto durante il secondo modulo di AsD.

Dentro trovate la libreria, composta da una classe per creare e gestire grafi, i vari algoritmi per la ricerca di MST e di percorsi minimi e delle funzioni
per "disegnare" i grafi tramite la libreria `matplotlib`.

### Note:
> Le dimostrazioni degli algoritmi sono all'interno del file `main.ipynb`.

> Potete trovare alcuni esempi di come usare la libreria dentro lo stesso file, (`main.ipynb`).

> La rappresentazione di grafi con archi con pesi negativi puo' essere un po' strana, se ci sono tanti nodi, non viene visualizzato in maniera ottimale. Per questo devo indagare un
> po di piu' su come gestire questo problema.

> Lo stesso problema di visualizzazione si presenta quando uno o piu' nodi sono scollegati da qualsiasi altro nodo.

### Uso:
Per utilizzare il file principale, ovvero `main.ipynb`, bisogna prima di tutto impostare l'ambiente virtuale

```sh
python -m venv ./venv
pip install -r requirements.txt
```

Una volta fatto questo ho notato che il modo piu' affidabile e' tramite VS Code, aprendo il notebook e' possibile eseguirlo sceglendo come kernel `venv`, in modo da usare l'ambiente virtuale appena creato.

### Problemi:
Per qualsiasi problema, non esitate a contattarmi, tuttavia preferisco se prima create una issue su questa repository o direttamente una pull-request se avete qualche cambiamento che vorreste apportare.
