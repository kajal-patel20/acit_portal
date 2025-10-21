# Quick Deployment Commands

## Push to GitHub

```powershell
# Navigate to project
cd "c:\Users\Kajal Patel\OneDrive\Desktop\kajal\vs code files\SMG(Training)\acit_portal"

# Initialize Git (if not done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Ready for deployment"

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/acit-portal.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Environment Variables for Render

Add these in Render Dashboard → Environment Variables:

```
SECRET_KEY = [Click "Generate"]
DEBUG = False
ALLOWED_HOSTS = your-app-name.onrender.com
DATABASE_URL = [Paste Internal Database URL from PostgreSQL service]
```

## Create Superuser (Run in Render Shell)

```bash
python manage.py createsuperuser
```

## Future Updates

```powershell
# After making changes
git add .
git commit -m "Description of changes"
git push
```

Render will auto-deploy!

## URLs After Deployment

- **User Portal:** https://your-app-name.onrender.com/
- **Admin Portal:** https://your-app-name.onrender.com/admin/

## Files Created for Deployment

✅ requirements.txt - Python dependencies
✅ build.sh - Build script
✅ render.yaml - Render config
✅ .gitignore - Git exclusions
✅ settings.py - Updated for production
✅ DEPLOYMENT.md - Full documentation
