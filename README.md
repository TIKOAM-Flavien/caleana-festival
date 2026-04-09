# Caleana Festival — site statique

Site **statique** (HTML/CSS/JS) prêt à déployer (OVH/FTP).  
Le contenu des pages “SEO” (subpages) est centralisé dans un JSON puis régénéré en HTML.

## Structure

- **Accueil**: `index.html`
- **Styles**: `style.css`, `subpages.css`
- **Images**: `img/`
- **Sous-pages (générées)**:
  - `festival-musique-mulhouse/index.html`
  - `festival-electro-alsace/index.html`
  - `que-faire-mulhouse-weekend/index.html`
- **Contenu subpages**: `content/subpages.fr.json`
- **Générateur subpages**: `tools/generate_subpages.py`
- **SEO**: `robots.txt`, `sitemap.xml`
- **Redirects**: `.htaccess`

## Modifier les subpages (pages génériques)

1. Éditer `content/subpages.fr.json`
   - `common.nav_items`: liens du menu des subpages
   - `pages[]`: contenu des pages (title/meta/h1/blocks)
2. Régénérer les HTML:

```bash
python tools/generate_subpages.py
```

Le script écrase automatiquement `*/index.html` pour chaque `slug`.

## Favicon (Google / navigateurs)

Les icônes sont servies depuis la racine :

- `favicon.ico`
- `favicon-32x32.png`
- `favicon-192x192.png`
- `apple-touch-icon.png`

Les balises favicon sont présentes dans `index.html` et dans les subpages (via le générateur).

## Déploiement

Voir `README-DEPLOI-OVH.md`.

## Notes “production”

- Après modification des subpages, penser à **mettre à jour** `sitemap.xml` si vous ajoutez/supprimez des slugs.
- Google peut mettre un certain temps à refléter les changements (favicon / snippets).

