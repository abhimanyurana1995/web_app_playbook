# Web App Playbook
### The decision guide for every AI-coded web app you build

> **How to use this:** Don't read top to bottom. Jump to the layer giving you trouble.
> Each section answers one question: *what do I pick and why?*

---

## Table of Contents

- [Layer 1 — UI / Frontend](#layer-1--ui--frontend)
- [Layer 2 — Backend / Logic](#layer-2--backend--logic)
- [Layer 3 — Data / Infra](#layer-3--data--infra)
- [Cross-Layer Decision Trees](#cross-layer-decision-trees)
- [The Stack Selector](#the-stack-selector)

---

---

# Layer 1 — UI / Frontend

> *The part users see and touch.*

---

## 1.1 Rendering Approach — The Foundational Choice

Before picking a framework, pick how your pages are built:

| Approach | What it means | Best for |
|---|---|---|
| **Static HTML** | Pages pre-written, same for everyone | Landing pages, docs, portfolios |
| **Server-rendered** | Server builds the page on each request | Dashboards, logged-in apps |
| **Client-rendered (SPA)** | Browser builds the page from JavaScript | Highly interactive apps, real-time UIs |
| **Hybrid** | Some pages static, some dynamic | Most modern production apps |

### Decision: Which rendering approach?

```
Does the page content change per user or per action?
   ├── No  → Static HTML (fastest, cheapest, zero JS needed)
   └── Yes → Does it change WITHOUT a page reload?
                ├── No  → Server-rendered (simpler, SEO-friendly)
                └── Yes → Client-rendered SPA (React/Vue/Svelte)
```

---

## 1.2 Frontend Frameworks

### Vanilla HTML/CSS/JS
**Use when:** You're building something simple, a single-page tool, or you want zero dependencies.
**Your project uses this.** `static/index.html` + `static/app.js` + `static/style.css`.

Strengths:
- Nothing to install or learn beyond the basics
- Every AI tool can write it perfectly
- Loads instantly, works everywhere

Weaknesses:
- Gets messy past ~500 lines of JS
- No built-in component system (you repeat yourself)

**Rule:** If your app has fewer than 5 distinct "screens" and no complex state, stick with vanilla.

---

### React
**Use when:** Multiple reusable UI pieces, state that changes frequently, team already knows it.

Core concept: Everything is a **component** (a self-contained piece of UI with its own logic).

```
Is the same UI element repeated 3+ times with different data?
   └── Yes → Make it a React component
```

Strengths:
- Massive ecosystem, AI writes it extremely well
- Component reuse saves time on large apps

Weaknesses:
- Overkill for simple apps
- Requires Node.js build step

---

### Vue
**Use when:** You want React-like components but simpler syntax. Good middle ground.

Strengths:
- Easier to learn than React
- Can be dropped into existing HTML (no build step required for Vue 3 CDN)

---

### HTMX
**Use when:** You have a Python/Go/Ruby backend and want interactivity WITHOUT writing JavaScript.

Core concept: HTML attributes that make elements do server requests.

```html
<!-- This button fetches /results and puts the response inside #output -->
<button hx-get="/results" hx-target="#output">Run Analysis</button>
```

**Best pairing:** Flask + HTMX. Your current project could use this instead of `app.js` for simpler interactions.

---

### Svelte
**Use when:** Performance matters and you want the simplest framework syntax.

Strengths:
- Compiles to pure JS (no framework runtime in browser)
- Cleanest syntax of all frameworks

---

## 1.3 Styling — Making It Look Good

| Tool | What it is | Use when |
|---|---|---|
| **Plain CSS** | You write all styles yourself | Full control, small projects |
| **Tailwind CSS** | Utility classes applied directly in HTML | Fastest to build with AI, consistent design |
| **Bootstrap** | Pre-built components (buttons, cards, modals) | Need professional look fast, not custom |
| **Pico CSS** | Minimal CSS that styles plain HTML automatically | Prototypes, internal tools |
| **DaisyUI** | Tailwind + pre-built components | Best of both worlds |

### Decision: Which styling tool?

```
Building for customers who care about design?
   ├── Yes → Are you building fast with AI?
   │            ├── Yes → Tailwind CSS (AI writes it perfectly, consistent)
   │            └── No  → Hire a designer or use a component library (MUI, Shadcn)
   └── No  → Internal tool / prototype?
                ├── Yes → Bootstrap or Pico CSS (looks fine, zero effort)
                └── No  → Plain CSS (you control everything)
```

---

## 1.4 Navigation — When Does a Screen Need What?

### When does a screen need a **Back button**?
- The user arrived via a deliberate action (clicked something, submitted a form)
- There is a meaningful "previous state" to return to
- The user might have made a mistake getting here

**Don't add a Back button when:** The page is a top-level destination (Home, Dashboard). Use menu/nav instead.

### When does an app need a **sidebar**?
- 5+ distinct sections that users switch between frequently
- Users need to see where they are at all times
- Content is deep (many sub-pages per section)

**Use a top navbar instead when:** Fewer than 5 sections, or mobile-first.

### When does something need a **modal** (popup) vs its own page?
```
Is the action quick (< 10 seconds, < 5 fields)?
   ├── Yes → Modal is fine
   └── No  → Give it its own page

Does the user need to see the background content while doing it?
   ├── Yes → Modal or side panel
   └── No  → Own page

Would the user want to bookmark or share this state?
   ├── Yes → Own page (has its own URL)
   └── No  → Modal is fine
```

### When does something need **real-time updates** (no page refresh)?
- Live chat, notifications
- Progress bars for long operations
- Collaborative editing
- Dashboards that auto-refresh

**How to do it:**
- **Polling** (simplest): JS checks `/status` every few seconds → good for progress bars
- **Server-Sent Events** (what your app uses): Server pushes updates → good for streaming text
- **WebSockets**: Two-way real-time → good for chat, collaboration

---

## 1.5 Frontend State — Where Does Data Live?

| Location | What it is | Use for |
|---|---|---|
| **URL params** | `?filter=active&sort=date` | Shareable, bookmarkable state |
| **Browser localStorage** | Persists after tab close | User preferences, remembered settings |
| **JS variables** | Lives only while page is open | Temporary UI state (open/closed menus) |
| **Backend (server)** | Fetched from API | The real data source of truth |

**Golden rule:** The server is always the source of truth. Frontend state is just a *copy* for display.

```
Does this data need to survive a page refresh?
   ├── No  → JS variable
   └── Yes → Does it need to survive browser close?
                ├── No  → sessionStorage
                └── Yes → localStorage OR save to server
```

---

---

# Layer 2 — Backend / Logic

> *The part that makes decisions, enforces rules, and talks to the database.*

---

## 2.1 Do You Even Need a Backend?

```
Does your app:
  - Store data that persists between users?    → Need backend
  - Keep secrets (API keys, passwords)?        → Need backend
  - Do processing too heavy for a browser?     → Need backend
  - Serve different content to different users?→ Need backend

None of the above?
  → Static site. No backend needed. Deploy to Netlify/Vercel for free.
```

---

## 2.2 Backend Frameworks

### Flask (Python) — *What your project uses*
**Use when:** Python is your language, app is moderate complexity, you want simplicity.

```python
@app.route("/hello")          # A route = a URL the app responds to
def hello():
    return "Hello World"
```

- Simple, readable, AI writes it extremely well
- Great for: data tools, AI apps, APIs, internal tools
- Not great for: very high traffic (millions of requests/day)

---

### FastAPI (Python)
**Use when:** You need Flask but with automatic documentation and better performance.

**Upgrade from Flask when:**
- You're building an API that other apps/teams will consume
- You want automatic type validation on inputs
- You need async performance

---

### Django (Python)
**Use when:** You need a full system fast — user accounts, admin panel, database, all included.

**Choose Django over Flask when:**
- You need user login/registration out of the box
- You need an admin dashboard to manage data
- The app has many models (10+ database tables)

**Stick with Flask when:**
- Simpler app with fewer models
- You want full control over the structure

---

### Express (JavaScript/Node.js)
**Use when:** Your frontend is React/Vue/Next.js and you want one language (JS) everywhere.

---

### Next.js (JavaScript)
**Use when:** You want React frontend AND backend in one project, with server-side rendering.

**The all-in-one choice** for modern web apps if you're using JavaScript.

---

### No-Code Backends (Supabase, Firebase, Appwrite)
**Use when:** You need user auth, database, and storage but don't want to write backend code.

```
Do you want to write zero backend code?
   └── Yes → Supabase (open source, PostgreSQL) or Firebase (Google, proprietary)

Tradeoffs:
   - Faster to start
   - Less control
   - Monthly cost as you scale
   - Vendor lock-in
```

---

## 2.3 Where Should Logic Live? — The Most Important Decision

This is the question that causes the most bugs and mess.

### The Principle: Push logic toward the backend

| Logic type | Where it lives | Why |
|---|---|---|
| **Validation** (is this email valid?) | Both — frontend for UX, backend for security | Frontend is fakeable; backend is authoritative |
| **Authorization** (can this user see this?) | **Backend only** | Never trust the frontend for security |
| **Calculations** (sum, average, totals) | Backend | Keep frontend dumb and fast |
| **Display formatting** (show date as "Jan 5") | Frontend | Backend shouldn't care about display |
| **Business rules** ("orders over $100 get free shipping") | **Backend only** | Rules must be enforced server-side |
| **Animations, transitions** | Frontend only | Backend doesn't know about pixels |

### Decision tree: Frontend or backend?

```
Would a malicious user breaking this rule cause damage?
   └── Yes → Backend. Always. No exceptions.

Is this purely about how something looks or feels?
   └── Yes → Frontend.

Does this require data from the database?
   └── Yes → Backend (or fetch and process on frontend if read-only display).

Is this a calculation the user triggers?
   └── Put in backend route, call it from frontend via fetch().
```

---

## 2.4 APIs — How Frontend Talks to Backend

### REST (what your app uses)
URLs represent resources. HTTP verbs (GET/POST/PUT/DELETE) represent actions.

| Verb | Meaning | Example |
|---|---|---|
| GET | Read data | `GET /files` → list all files |
| POST | Create something | `POST /upload` → upload a file |
| PUT/PATCH | Update something | `PUT /files/123` → update file |
| DELETE | Remove something | `DELETE /files/123` → delete file |

**Name routes after nouns, not verbs:**
- ✓ `GET /orders` 
- ✗ `GET /getOrders`

### When to stream vs return all at once
```
Will the response take > 1 second?
   └── Yes → Can you return partial results as they're ready?
                ├── Yes → Stream (Server-Sent Events, like your app's /chat/stream)
                └── No  → Background job + polling for status
```

---

## 2.5 Authentication — User Login

| Solution | Use when | Complexity |
|---|---|---|
| **No auth** | Internal tool, single user | None |
| **HTTP Basic Auth** | Internal tool, simple password gate | Minimal |
| **Session-based** (Flask-Login) | Traditional web app | Low |
| **JWT tokens** | API consumed by mobile/frontend separately | Medium |
| **OAuth** (Google/GitHub login) | "Sign in with Google" | Medium |
| **Auth services** (Auth0, Clerk, Supabase Auth) | Don't want to manage this yourself | Low effort, costs money |

**Decision:**
```
Is this a public app with multiple users?
   ├── No  → No auth or Basic Auth
   └── Yes → Do you want "Sign in with Google"?
                ├── Yes → OAuth or Auth0/Clerk
                └── No  → Flask-Login (session-based) for simplicity
```

---

---

# Layer 3 — Data / Infra

> *Where data lives and how the app runs.*

---

## 3.1 Database Selection

### The Big Question First

```
Is your data structured (rows + columns, like a spreadsheet)?
   ├── Yes → Relational database (SQL)
   └── No  → Is it documents/JSON (flexible schema)?
                ├── Yes → Document database (MongoDB)
                └── Is it key-value pairs (settings, cache)?
                        └── Yes → Redis or simple file storage
```

---

### SQLite
**What it is:** A database that's a single file on your disk. No server needed.

**Use when:**
- App runs on one machine
- Less than ~100,000 rows
- Prototype, personal tool, or single-user app
- You want zero setup

**Don't use when:**
- Multiple servers need to access the same database
- More than one user writes at the exact same time

---

### PostgreSQL
**What it is:** Full-featured relational database. Industry standard for production.

**Use when:**
- Public app with real users
- Data needs to persist reliably
- You'll deploy to cloud (Railway, Fly.io, Heroku)
- You need complex queries, joins, or transactions

**Always choose Postgres over SQLite when deploying to production.**

---

### MongoDB
**What it is:** Stores data as JSON documents. No fixed schema.

**Use when:**
- Data structure varies per record (different fields for different items)
- You're storing logs, events, or AI outputs
- Rapid prototyping where schema changes often

---

### Redis
**What it is:** Extremely fast key-value store. Runs in memory.

**Use when:**
- Caching (store expensive query results temporarily)
- Session storage
- Rate limiting
- Real-time leaderboards/counters

**Rule:** Redis is almost always used *alongside* a main database, not instead of it.

---

## 3.2 File Storage

| Solution | Use when | Cost |
|---|---|---|
| **Local disk** (what your app uses) | Single server, files are temp/user-specific | Free |
| **AWS S3 / Cloudflare R2** | Production app, files must persist, multiple servers | Pay per GB |
| **Supabase Storage** | Already using Supabase | Included in plan |
| **Vercel Blob** | Already deploying on Vercel | Included |

**Decision:**
```
Will the app run on more than one server?
   └── Yes → You MUST use cloud storage (S3/R2). Local disk won't work.

Do files need to persist forever?
   └── Yes → Cloud storage. Local disk is risky (servers get wiped).

Single server, temporary uploads?
   └── Local disk is fine (like your current app).
```

---

## 3.3 Deployment — Where the App Lives

### Local Only (what your app currently does)
Runs on your own machine. Users must be on the same network or use a tunnel.

**Use when:** Personal tool, dev/testing, demos.

---

### Railway
**Best for:** Python/Flask apps. What your app is already configured for (`railway.toml`).

- Connect GitHub repo → auto-deploys on every push
- Add PostgreSQL with one click
- Free tier available, ~$5-20/month for small apps

---

### Render
**Best for:** Similar to Railway. Good free tier for small apps.

- Free tier sleeps after 15 min inactivity (cold starts)
- Paid tier from ~$7/month

---

### Fly.io
**Best for:** Apps that need to run in specific regions or need Docker control.

---

### Vercel
**Best for:** Next.js apps, static sites, JavaScript frontends.

- Excellent free tier for static/serverless
- Less suited for Python Flask apps

---

### VPS (DigitalOcean, Hetzner, Linode)
**Best for:** Full control, custom config, cost efficiency at scale.

- You manage the server yourself (or use a tool like Coolify)
- Cheapest per performance
- Most work to set up

**Decision:**
```
Is this a personal/demo app?
   └── Railway free tier or Render free tier

Is this a small production app (< 1000 users/day)?
   └── Railway or Render paid (~$7-20/month)

Do you need full control or cost efficiency at scale?
   └── VPS (DigitalOcean Droplet + Coolify for easy management)

Is your app purely frontend (no backend)?
   └── Vercel or Netlify (free)
```

---

## 3.4 Environment Variables — Secrets Management

**The rule:** Never put API keys, passwords, or secrets in your code files.

Instead, use environment variables:

```bash
# In your terminal or deployment platform:
GEMINI_API_KEY=abc123
DATABASE_URL=postgresql://...
```

```python
# In your code:
import os
api_key = os.environ.get("GEMINI_API_KEY")
```

**Where to set them:**
| Environment | Where to put secrets |
|---|---|
| Local dev | `.env` file (in `.gitignore`!) |
| Railway | Dashboard → Variables tab |
| Render | Dashboard → Environment tab |
| Vercel | Dashboard → Settings → Environment Variables |

---

## 3.5 Scaling — When Your App Gets Popular

You don't need to think about this early, but know the progression:

```
1 user      → Local SQLite, local disk, 1 server
10 users    → Same stack is fine
100 users   → PostgreSQL instead of SQLite
1,000 users → Add Redis for caching, cloud file storage
10,000 users→ Multiple servers, load balancer, CDN for static files
100,000+    → You now have budget to hire someone who knows this
```

---

---

# Cross-Layer Decision Trees

## "What's the right architecture for my app?"

```
What kind of app is it?

├── CONTENT SITE (blog, portfolio, docs)
│     Frontend: Static HTML or Next.js
│     Backend:  None (or CMS like Contentful)
│     Data:     Files / CMS
│     Deploy:   Vercel / Netlify (free)

├── INTERNAL TOOL (team dashboard, data viewer)
│     Frontend: Bootstrap + vanilla JS or HTMX
│     Backend:  Flask or FastAPI
│     Data:     SQLite or PostgreSQL
│     Deploy:   Railway or local

├── AI / DATA APP (like your MyAnalyst)
│     Frontend: Vanilla JS or HTMX
│     Backend:  Flask or FastAPI
│     Data:     Local files + session state
│     Deploy:   Railway

├── SAAS / MULTI-USER APP
│     Frontend: React or Next.js
│     Backend:  Next.js API or FastAPI
│     Data:     PostgreSQL + Redis
│     Auth:     Clerk or Auth0
│     Deploy:   Railway / Render / Fly.io

└── MOBILE-FIRST APP
      Frontend: React (or React Native for actual mobile)
      Backend:  FastAPI or Supabase
      Data:     PostgreSQL
      Deploy:   Vercel (frontend) + Railway (backend)
```

---

## "Where is the bug probably hiding?"

```
Something LOOKS wrong (wrong color, element missing, layout broken)
   → frontend: HTML or CSS

Something SHOWS wrong data but the data exists
   → frontend: JavaScript (wrong fetch, wrong display logic)

Data never arrives from server
   → Check the API route in app.py + network tab in browser DevTools

Data arrives but is wrong
   → Backend logic in the route or engine

App crashes on startup
   → config.yaml, requirements.txt, or missing environment variable

App works locally but not deployed
   → Missing environment variable on deployment platform
   → Database URL not set
   → File path that works on Windows but not Linux
```

---

## "Should I add this feature to the frontend or backend?"

```
The feature involves:

DISPLAY / ANIMATION / LAYOUT     → Frontend
USER INPUT / FORM                 → Frontend for UX, Backend for validation
CALCULATION WITH USER'S DATA      → Backend (call API from frontend)
READING FROM DATABASE             → Backend (never expose DB to frontend)
SENDING EMAIL / SMS               → Backend (secrets must stay server-side)
CALLING EXTERNAL API              → Backend (protect your API key)
ENFORCING BUSINESS RULES          → Backend (always)
FORMATTING DATES/CURRENCY         → Frontend (display concern)
```

---

---

# The Stack Selector

## Fastest to Build (with AI)
```
Flask + Bootstrap + SQLite + Railway
```
- Every AI writes this perfectly
- Zero decisions to make
- Good for 90% of personal/small-business tools

---

## Best for Public SaaS Products
```
Next.js + Tailwind + PostgreSQL + Clerk (auth) + Vercel + Railway
```
- Modern, scalable
- Auth handled for you
- Strong AI support

---

## Best for AI / Data Tools
```
Flask + HTMX or vanilla JS + SQLite/PostgreSQL + Railway
```
- Python ecosystem (pandas, scikit-learn, LLMs all native)
- Simple frontend, powerful backend
- What your current app uses

---

## Best for Zero-Code Backend
```
Next.js + Tailwind + Supabase + Vercel
```
- No backend code to write
- Database, auth, storage all included
- Good if you want to avoid Python

---

## Most Boring (Best Compliment in Engineering)
```
Django + Bootstrap + PostgreSQL + Railway
```
- Everything batteries-included
- Boring = reliable = fewer surprises
- Admin panel for free

---

---

*Last updated: April 2026*
*Project this was built for: MyAnalyst (E:\1st project)*
