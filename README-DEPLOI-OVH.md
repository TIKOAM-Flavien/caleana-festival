## Dossier `www/` (prêt pour OVH)

Copiez **tout le contenu** de ce dossier `www/` vers le répertoire web OVH (souvent `www/` via FTP).

### Contenu
- `index.html`
- `style.css`
- `img/` (toutes les images)
- `favicon.png`
- `robots.txt`
- `sitemap.xml`
- `.htaccess` (redirections HTTPS / non-www)

### Déploiement FTP (OVH)
- Envoyer **les fichiers + dossiers** en conservant la structure.
- Une fois en ligne, tester :
  - Page d’accueil
  - Affichage des images (`/img/...`)
  - Favicon (vider le cache du navigateur si besoin)
  - `https://votre-domaine/robots.txt` et `https://votre-domaine/sitemap.xml`

### Notes
- Si vous voyez encore des erreurs CORS Google Sheets : la solution la plus robuste est d’exporter les CSV en fichiers locaux et de les servir depuis `www/data/`.

