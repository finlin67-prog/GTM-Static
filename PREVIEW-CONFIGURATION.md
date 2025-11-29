# GTMstack.pro Preview Configuration

## ✅ Preview Successfully Configured

The project preview is now serving the static HTML website with the complete brand system applied.

---

## Configuration Details

### **Preview URL Structure**
- **Main Site:** `https://[your-preview-url].preview.emergentagent.com/`
- **Port:** 3000 (internal)
- **Server:** Nginx serving static files from `/app/`

### **Services Status**
```
✅ gtmstack-static  - RUNNING (Nginx serving static site on port 3000)
✅ backend           - RUNNING (FastAPI on port 8001)
✅ mongodb           - RUNNING  
✅ nginx-code-proxy  - RUNNING
❌ frontend          - STOPPED (React app replaced with static site)
```

---

## Files Served

### **Root Level**
- `index.html` - Homepage with brand system applied
- `404.html` - Error page
- `brand-system.css` - Master brand stylesheet
- All image assets (*.jpg, *.png, *.svg)

### **Content Directories**
- `/about/` - About page
- `/contact/` - Contact page
- `/resume/` - Resume page
- `/expertise/` - 16 expertise pages
- `/industries/` - 6 industry pages
- `/projects/` - 9 project case studies

### **Static Assets**
- `/_next/static/` - Next.js build artifacts (fonts, CSS, JS)

---

## Nginx Configuration

**Config File:** `/etc/nginx/gtmstack-preview.conf`

**Key Settings:**
- Serves files from `/app/` directory
- Default file: `index.html`
- Cache headers for static assets (1 year)
- Security headers enabled
- Custom 404 error page

**Supervisor Config:** `/etc/supervisor/conf.d/gtmstack-static.conf`

---

## Brand System Applied

The following brand elements are active:

### **Visual Changes:**
- ✅ Deep Navy (#0A0F1F) hero sections
- ✅ Electric Blue → Purple gradients
- ✅ Topographic background patterns
- ✅ Grid overlay patterns
- ✅ Route line patterns
- ✅ White text on navy backgrounds
- ✅ Premium button styling
- ✅ Navy footer with white text

### **CSS File Loaded:**
All pages include: `<link rel="stylesheet" href="/brand-system.css"/>`

---

## How to Verify

1. **Open Preview URL** in your browser
2. **Check Hero Section** - Should have navy background
3. **Inspect Elements** - Look for `.hero-navy` class
4. **View CSS** - Visit `/brand-system.css` directly
5. **Test Navigation** - All internal links should work

---

## Management Commands

### **Restart Static Site Server:**
```bash
sudo supervisorctl restart gtmstack-static
```

### **View Logs:**
```bash
tail -f /var/log/supervisor/gtmstack-static.*.log
```

### **Check Status:**
```bash
sudo supervisorctl status gtmstack-static
```

### **Test Locally:**
```bash
curl http://localhost:3000/
```

---

## Technical Details

**Nginx Process:**
- Command: `/usr/sbin/nginx -g "daemon off;" -c /etc/nginx/gtmstack-preview.conf`
- User: root
- Priority: 100

**Static File Handling:**
- HTML: Direct serve with fallback to index.html
- CSS/JS: 1-year cache headers
- Images: 1-year cache headers, immutable
- Fonts: 1-year cache headers, immutable

**Security Headers:**
- `X-Frame-Options: SAMEORIGIN`
- `X-Content-Type-Options: nosniff`
- `X-XSS-Protection: 1; mode=block`

---

## Troubleshooting

### **If preview shows old React app:**
1. Clear browser cache
2. Hard refresh (Ctrl+Shift+R or Cmd+Shift+R)
3. Check service status: `sudo supervisorctl status`

### **If CSS not loading:**
1. Verify file exists: `ls -la /app/brand-system.css`
2. Check nginx logs: `tail -f /var/log/supervisor/gtmstack-static.err.log`
3. Test CSS directly: `curl http://localhost:3000/brand-system.css`

### **If 404 errors:**
1. Check nginx config: `sudo nginx -t -c /etc/nginx/gtmstack-preview.conf`
2. Verify file paths are correct
3. Check nginx error logs

---

## Notes

- The React frontend app has been stopped and replaced with static HTML
- Backend API still runs on port 8001 (not used by static site)
- All 42 HTML pages have the brand system applied
- Changes to HTML/CSS files are immediately reflected (no build step needed)

---

**Status:** ✅ FULLY OPERATIONAL  
**Last Updated:** 2025-11-29  
**Configuration:** Production-ready static site with GTMstack.pro brand system
