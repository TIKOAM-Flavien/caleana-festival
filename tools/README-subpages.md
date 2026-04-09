## Mettre à jour le texte de toutes les subpages

Le contenu texte des subpages est centralisé dans :

- `content/subpages.fr.json`

Puis régénéré dans les pages statiques via :

- `tools/generate_subpages.py`

### Modifier un texte

1. Ouvrir `content/subpages.fr.json`
2. Modifier la page dans `pages[]` (champs `title`, `meta_description`, `h1`, `blocks`…)

### Régénérer toutes les pages

Depuis la racine du site :

```bash
python tools/generate_subpages.py
```

Le script recrée/écrase automatiquement :

- `*/index.html` pour chaque `slug` déclaré.

### Ajouter une nouvelle page

1. Ajouter une entrée dans `pages[]` avec un `slug` unique (sans accents)
2. Relancer le script
3. (Optionnel) Ajouter l’URL dans `sitemap.xml` si tu veux l’indexation explicite

