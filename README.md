# Portfolio Website - HTML, CSS & JavaScript

A modern, responsive portfolio website built with pure HTML, CSS, and JavaScript. No backend required!

## 📁 Project Structure
{{ url_for('static', filename='css/styles.css') }}
```
/portfolio
  index.html              # Home page
  about.html              # About page with skills
  services.html           # Services offered
  journey.html            # Experience timeline
  projects.html           # Project showcase
  blog.html               # Blog/articles listing
  testimonials.html       # Client testimonials
  contact.html            # Contact form
  /static
    /css
      style.css           # Main stylesheet
    /js
      main.js             # JavaScript functionality
    /images               # Place your images here (optional)
  README.md               # This file
```

## 🚀 Getting Started

### No Installation Required!

This is a static website that runs directly in your browser. Simply:

1. **Download or clone this project**

2. **Open `index.html` in your browser**
   - Double-click `index.html`, or
   - Right-click → Open with → Your browser

3. **That's it!** The website is ready to use.

### Optional: Use a Local Server

For better development experience, you can use a local server:

**Python:**
```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```

**Node.js (with http-server):**
```bash
npx http-server
```

**VS Code:**
- Install "Live Server" extension
- Right-click on `index.html` → "Open with Live Server"

Then visit: `http://localhost:8000`

## 🎨 Customization

### 1. Update Personal Information

Edit each HTML file to replace:
- "John Doe" with your name
- Contact information (email, phone, location)
- Project descriptions and links
- Blog posts and articles
- Testimonials

### 2. Customize Colors

Edit `/static/css/style.css` and modify the CSS variables:

```css
:root {
    --color-primary: #2563eb;      /* Main brand color */
    --color-secondary: #7c3aed;    /* Secondary color */
    --color-accent-yellow: #eab308;
    --color-accent-green: #10b981;
    /* ... other colors ... */
}
```

### 3. Add Your Images

- Place your images in `/static/images/` folder
- Update image sources in HTML files
- Replace Unsplash URLs with your own images:
  ```html
  <img src="static/images/your-image.jpg" alt="Description">
  ```

### 4. Customize Content

Each page is self-contained and easy to edit:

- **index.html** - Hero section, quick intro
- **about.html** - Biography, skills with progress bars
- **services.html** - Services you offer, work process
- **journey.html** - Career timeline, achievements
- **projects.html** - Portfolio showcase
- **blog.html** - Articles and blog posts
- **testimonials.html** - Client reviews, statistics
- **contact.html** - Contact form and information

## 📱 Features

- ✅ Fully responsive design (mobile, tablet, desktop)
- ✅ Smooth scrolling navigation
- ✅ Mobile-friendly hamburger menu
- ✅ Animated skill progress bars
- ✅ Project showcase grid
- ✅ Blog section
- ✅ Testimonials with ratings
- ✅ Contact form (frontend only)
- ✅ Timeline for experience
- ✅ Social media links
- ✅ Modern gradient design
- ✅ Smooth animations and transitions

## 📄 Pages Overview

### 1. Home (`index.html`)
- Hero section with call-to-action
- Quick introduction
- Featured services overview

### 2. About (`about.html`)
- Personal bio and story
- Technical skills with animated bars
- Three categories: Frontend, Backend, Tools

### 3. Services (`services.html`)
- 6 service offerings
- Feature lists for each service
- 5-step work process

### 4. Journey (`journey.html`)
- Career timeline with dates
- Educational background
- Achievements and certifications

### 5. Projects (`projects.html`)
- 6 project showcases
- Technology tags
- GitHub and demo links

### 6. Blog (`blog.html`)
- 6 article cards
- Categories and reading time
- Publication dates

### 7. Testimonials (`testimonials.html`)
- 6 client testimonials
- Star ratings
- Statistics section (clients, projects, experience, satisfaction)

### 8. Contact (`contact.html`)
- Contact form
- Email, phone, location
- Social media links

## 🔧 Contact Form Setup

The contact form is frontend-only. To make it functional, you can:

### Option 1: Formspree (Free & Easy)
```html
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
  <!-- form fields -->
</form>
```

### Option 2: EmailJS
Add EmailJS script and configure in `/static/js/main.js`

### Option 3: Backend Integration
Connect to your own backend API (PHP, Node.js, Python, etc.)

### Option 4: Netlify Forms
If hosted on Netlify, add `netlify` attribute:
```html
<form netlify>
  <!-- form fields -->
</form>
```

## 🎨 Color Scheme

The default design uses:
- **Primary:** Blue (#2563eb)
- **Secondary:** Purple (#7c3aed)
- **Accents:** Yellow (#eab308), Green (#10b981)

All colors are defined as CSS variables for easy customization.

## 🌐 Deployment

### GitHub Pages
1. Create a GitHub repository
2. Push your files
3. Go to Settings → Pages
4. Select branch and save
5. Your site will be live at `https://yourusername.github.io/repository-name`

### Netlify
1. Drag and drop your folder to [Netlify](https://netlify.com)
2. Site deployed instantly!

### Vercel
1. Push to GitHub
2. Import project on [Vercel](https://vercel.com)
3. Deploy with one click

### Traditional Hosting
Upload all files via FTP to your web host.

## 🛠️ Technologies Used

- **HTML5** - Structure
- **CSS3** - Styling with CSS Grid, Flexbox, Variables
- **JavaScript** - Interactivity and animations
- **Font Awesome 6** - Icons

## 📱 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## 📝 Customization Tips

1. **Navigation:** Update links in all HTML files to match your structure
2. **Footer:** Same footer appears on all pages - edit once, copy to all
3. **Colors:** Use CSS variables for consistent theming
4. **Images:** Optimize images before adding (use tools like TinyPNG)
5. **SEO:** Update `<title>` and add meta descriptions to each page

## 🎯 Performance Tips

- Compress images
- Minify CSS and JS for production
- Use CDN for Font Awesome (already implemented)
- Enable browser caching if using web server

## 📄 License

This project is open source and available for personal and commercial use.

## 🤝 Credits

- Icons: [Font Awesome](https://fontawesome.com)
- Images: [Unsplash](https://unsplash.com) (replace with your own)

---

**Made with ❤️ - Ready to customize and deploy!**

For questions or support, feel free to reach out or create an issue.
