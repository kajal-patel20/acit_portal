# 📋 Deployment Checklist

Use this checklist to track your deployment progress.

---

## Pre-Deployment ✅

- [x] Project code complete
- [x] requirements.txt created
- [x] build.sh created
- [x] render.yaml created
- [x] .gitignore created
- [x] settings.py updated for production
- [x] Documentation written

---

## GitHub Setup

- [ ] Create GitHub account (if needed)
- [ ] Install Git on computer
- [ ] Initialize Git repository (`git init`)
- [ ] Add all files (`git add .`)
- [ ] Commit files (`git commit -m "Initial commit"`)
- [ ] Create new repository on GitHub
- [ ] Connect local repo to GitHub
- [ ] Push code to GitHub (`git push -u origin main`)

---

## Render Setup

- [ ] Create Render account at render.com
- [ ] Link GitHub account to Render
- [ ] Create PostgreSQL database
  - [ ] Name: acit-portal-db
  - [ ] Copy Internal Database URL
- [ ] Create Web Service
  - [ ] Connect GitHub repository
  - [ ] Set build command: `./build.sh`
  - [ ] Set start command: `gunicorn acit_portal.wsgi:application`
  - [ ] Choose Free plan
- [ ] Add Environment Variables:
  - [ ] SECRET_KEY (generate)
  - [ ] DEBUG = False
  - [ ] ALLOWED_HOSTS = your-app-name.onrender.com
  - [ ] DATABASE_URL = [paste from PostgreSQL]
- [ ] Click "Create Web Service"
- [ ] Wait for first build to complete

---

## Post-Deployment

- [ ] Open Render Shell
- [ ] Create superuser (`python manage.py createsuperuser`)
- [ ] Test user portal (https://your-app-name.onrender.com/)
- [ ] Test admin portal (https://your-app-name.onrender.com/admin/)
- [ ] Create test HOD user in admin
- [ ] Submit test asset request as HOD
- [ ] Approve/reject test request as admin
- [ ] Verify all features work correctly

---

## Optional Enhancements

- [ ] Set up custom domain
- [ ] Upgrade to paid database (for persistence beyond 90 days)
- [ ] Set up email notifications
- [ ] Add monitoring/analytics
- [ ] Configure automated backups
- [ ] Add HTTPS enforcement
- [ ] Set up CI/CD pipeline

---

## Troubleshooting

If something goes wrong, check:

- [ ] Build logs in Render dashboard
- [ ] All environment variables set correctly
- [ ] DATABASE_URL is Internal URL (not External)
- [ ] ALLOWED_HOSTS includes your Render domain
- [ ] All files committed and pushed to GitHub
- [ ] build.sh has correct permissions

---

## Notes

Write down your important details:

**GitHub Repository URL:**
_______________________________________________

**Render App URL:**
_______________________________________________

**Database Name:**
_______________________________________________

**Admin Username:**
_______________________________________________

**Admin Password:**
_______________________________________________ (keep secure!)

---

## Success Criteria ✨

Your deployment is successful when:

- ✅ Site loads without errors
- ✅ Can log in as HOD
- ✅ Can submit requests
- ✅ Can log into admin panel
- ✅ Can approve/reject requests
- ✅ Static files (CSS) load correctly
- ✅ Logo appears in admin
- ✅ Database saves data

---

**When all items are checked, you're live! 🎉**

Share your live URL:
https://_____________________.onrender.com
