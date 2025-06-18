✅ Stack actuelle fonctionnelle

📝 Éditeur (CKEditor 5)
• Édition riche de contenu (titres, listes, tableaux, images…)
• Rendu HTML enregistré dans Supabase (html)
• JSON optionnel (content) pour structure future (non obligatoire pour l’affichage)
• Images uploadées automatiquement dans Supabase Storage (via SupabaseUploadAdapter)

💾 Supabase
• Table DzawTable1 avec colonnes : id, title, slug, html, content, author
• Policies RLS configurées :
• ✅ allow anon insert
• ✅ allow public read

⚙️ FastAPI
• API /articles pour lire
• API /article pour insérer
• CORS configuré pour accepter les requêtes depuis localhost:5500

🌐 Frontend HTML/JS
• editor.html pour écrire
• articles.html pour lire les articles
• CSS et navigation propres

⸻

✅ Tu peux maintenant :
• Ajouter un champ auteur dynamique (au lieu de moi)
• Améliorer la gestion des slugs
• Ajouter une page de prévisualisation par article (/article/:slug)
• Ajouter l’upload image via CKEditor (ça marche déjà si tu ajoutes supabaseClient.js)
