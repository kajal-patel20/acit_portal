# 🚀 Deploying ACIT Portal to Render

This guide will walk you through deploying your Django ACIT Portal project to Render (a free hosting platform).

---

## 📋 Prerequisites

1. **GitHub Account** - You'll need to push your code to GitHub
2. **Render Account** - Sign up at [render.com](https://render.com) (free tier available)
3. **Git installed** on your computer

---

## 🔧 Step 1: Prepare Your Project (Already Done!)

The following files have been created for deployment:

✅ `requirements.txt` - Python dependencies  
✅ `build.sh` - Build script for Render  
✅ `render.yaml` - Render configuration  
✅ `.gitignore` - Files to exclude from Git  
✅ `settings.py` - Updated for production

---

## 📤 Step 2: Push to GitHub

### 2.1 Initialize Git Repository (if not already done)

Open PowerShell in your project directory and run:

```powershell
cd "c:\Users\Kajal Patel\OneDrive\Desktop\kajal\vs code files\SMG(Training)\acit_portal"
git init
```

### 2.2 Add All Files

```powershell
git add .
```

### 2.3 Commit Your Changes

```powershell
git commit -m "Initial commit - ACIT Portal ready for deployment"
```

### 2.4 Create GitHub Repository

1. Go to [github.com](https://github.com) and log in
2. Click the **+** icon (top right) → **New repository**
3. Name it: `acit-portal` (or any name you prefer)
4. **Do NOT** initialize with README (your project already has files)
5. Click **Create repository**

### 2.5 Connect and Push to GitHub

GitHub will show commands. Copy and run them (they'll look like this):

```powershell
git remote add origin https://github.com/YOUR_USERNAME/acit-portal.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

---

## 🌐 Step 3: Deploy on Render

### 3.1 Create Render Account

1. Go to [render.com](https://render.com)
2. Click **Get Started for Free**
3. Sign up with GitHub (recommended) or email

### 3.2 Create PostgreSQL Database

1. From Render Dashboard, click **New +** → **PostgreSQL**
2. Fill in:
   - **Name:** `acit-portal-db`
   - **Database:** `acit_portal_db`
   - **User:** `acit_portal_user`
   - **Region:** Select closest to you
   - **Plan:** Free
3. Click **Create Database**
4. Wait for it to provision (1-2 minutes)
5. **IMPORTANT:** Copy the **Internal Database URL** (you'll need this later)

### 3.3 Create Web Service

1. From Render Dashboard, click **New +** → **Web Service**
2. Click **Connect account** to link your GitHub
3. Select your `acit-portal` repository
4. Fill in the form:
   - **Name:** `acit-portal` (this will be your URL subdomain)
   - **Region:** Same as database
   - **Branch:** `main`
   - **Root Directory:** Leave blank
   - **Runtime:** Python 3
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn acit_portal.wsgi:application`
   - **Plan:** Free

### 3.4 Add Environment Variables

Scroll down to **Environment Variables** and add:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | Click "Generate" button |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `acit-portal.onrender.com` (replace with YOUR actual Render URL) |
| `DATABASE_URL` | Paste the **Internal Database URL** you copied earlier |

**Important:** Replace `acit-portal.onrender.com` with your actual Render app URL (it will be shown after you create the service).

### 3.5 Deploy

1. Click **Create Web Service**
2. Render will start building your app (takes 5-10 minutes on first deploy)
3. Watch the logs in real-time
4. When you see "Build successful", your app is deployed!

---

## ✅ Step 4: Create Superuser (Admin Account)

After deployment, you need to create an admin account.

### 4.1 Open Render Shell

1. Go to your web service dashboard on Render
2. Click **Shell** tab (top right)
3. Wait for shell to connect

### 4.2 Create Superuser

In the shell, run:

```bash
python manage.py createsuperuser
```

Follow the prompts:
- **Username:** admin (or your choice)
- **Email:** your-email@example.com
- **Password:** (enter a strong password)
- **Password (again):** (confirm)

---

## 🎉 Step 5: Access Your Application

Your app is now live!

### User Portal (HOD Login)
```
https://your-app-name.onrender.com/
```

### Admin Portal
```
https://your-app-name.onrender.com/admin/
```

Login with the superuser credentials you just created.

---

## 🔄 Updating Your Application

When you make changes to your code:

### 1. Commit and Push to GitHub

```powershell
git add .
git commit -m "Description of your changes"
git push
```

### 2. Render Auto-Deploys

Render will automatically detect the push and redeploy your app!  
Watch the logs in your Render dashboard.

---

## ⚠️ Important Notes

### Free Tier Limitations

- **Database:** 1 GB storage, expires after 90 days (save your data before expiry!)
- **Web Service:** Spins down after 15 minutes of inactivity
- **First Request:** May take 30-60 seconds to wake up
- **Build Time:** 512 MB RAM (may be slow on first build)

### Database Expiry Warning

Free PostgreSQL databases expire after 90 days. Options:

1. **Upgrade to paid plan** ($7/month for persistence)
2. **Backup data regularly** with:
   ```bash
   python manage.py dumpdata > backup.json
   ```
3. **Create new free database** and migrate data every 90 days

### Custom Domain (Optional)

To use your own domain:

1. Go to Settings in Render dashboard
2. Add custom domain
3. Update DNS settings with your domain provider
4. Update `ALLOWED_HOSTS` environment variable

---

## 🐛 Troubleshooting

### Build Fails

**Check:**
- All files committed to Git
- `build.sh` has execute permissions
- Requirements.txt is valid

**Solution:**
```powershell
# Make build.sh executable (if on Linux/Mac)
chmod +x build.sh
git add build.sh
git commit -m "Make build.sh executable"
git push
```

### Static Files Not Loading

**Check:**
- `STATIC_ROOT` is set correctly
- WhiteNoise is in MIDDLEWARE
- Ran `collectstatic` in build.sh

**Solution:** Redeploy or run manual deploy

### Database Connection Error

**Check:**
- `DATABASE_URL` environment variable is set correctly
- Database is running (check Render dashboard)
- Internal Database URL is used (not External)

---

## 📞 Support

### Render Documentation
- [Render Docs](https://render.com/docs)
- [Django on Render Guide](https://render.com/docs/deploy-django)

### Django Documentation
- [Django Deployment Checklist](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/)

---

## 🎓 Summary

You've successfully deployed your ACIT Portal to Render! 🎉

**Your deployment includes:**
- ✅ Live web application
- ✅ PostgreSQL database
- ✅ Automatic deployments from GitHub
- ✅ SSL certificate (HTTPS)
- ✅ Professional admin portal with custom branding

**Next Steps:**
1. Test all features on live site
2. Create test HOD users in admin
3. Submit test asset requests
4. Share URL with stakeholders

---

**Deployed by:** Kajal Patel  
**Project:** ACIT Portal - Asset Request Management System  
**Date:** October 2025
