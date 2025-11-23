# MyCask - Project Roadmap

## Project Overview

MyCask is a mobile-first Progressive Web App (PWA) for whiskey enthusiasts to manage their collection, discover new bottles, and track tasting notes with intelligent recommendations.

---

## Phase 0: Foundation & Setup (Week 1-2)

**Goal:** Set up development environment, learn key technologies, establish project structure

### Task 0.1: Technology Research & Setup (3-5 days)

- [x] Install Node.js (v18+) and Python (3.10+)
- [x] Set up code editor (VS Code recommended) with extensions:
  - ESLint, Prettier, Python, Tailwind IntelliSense
- [x] Create GitHub repository with README
- [x] Research and document PWA basics (manifests, service workers)
- [ ] Read FastAPI documentation quick start
- [ ] Read React documentation (especially Hooks)

**Documentation to Create:**

- `SETUP.md` - Development environment setup guide
- `TECH_STACK.md` - Chosen technologies with rationale

### Task 0.2: Project Initialization (2-3 days)

- [ ] Initialize React app with Vite: `npm create vite@latest mycask-frontend -- --template react`
- [ ] Set up Tailwind CSS
- [ ] Initialize FastAPI project structure
- [ ] Set up PostgreSQL locally (or use Docker)
- [ ] Create `.gitignore` for both frontend and backend
- [ ] Set up basic folder structure:
  ```
  /mycask
    /frontend
      /src
        /components
        /pages
        /services
        /hooks
        /utils
    /backend
      /app
        /api
        /models
        /schemas
        /services
        /db
  ```

**Documentation to Create:**

- `PROJECT_STRUCTURE.md` - Folder organization and conventions
- `CONTRIBUTING.md` - Code style, commit conventions, PR process

### Task 0.3: Development Workflow Setup (1-2 days)

- [ ] Set up ESLint and Prettier for code formatting
- [ ] Create development scripts in `package.json`
- [ ] Set up hot-reload for both frontend and backend
- [ ] Configure CORS for local development
- [ ] Test that frontend can call backend API (simple health check endpoint)

**Deliverable:** Working development environment where you can run both frontend and backend simultaneously

---

## Phase 1: Core Infrastructure (Week 3-4)

**Goal:** Build authentication, database foundation, and basic UI shell

### Task 1.1: Database Design & Setup (3-4 days)

- [ ] Design database schema (see schema section below)
- [ ] Create SQLAlchemy models for:
  - Users
  - Bottles
  - Collections
  - Tastings
  - Flavor Profiles
- [ ] Write and test database migrations (Alembic)
- [ ] Create seed data script for testing (10-20 sample bottles)
- [ ] Write database helper functions (CRUD operations)

**Documentation to Create:**

- `DATABASE_SCHEMA.md` - Entity relationship diagram and table definitions
- `MIGRATION_GUIDE.md` - How to run migrations

**Learning Resources:**

- SQLAlchemy ORM tutorial
- Alembic migrations documentation

### Task 1.2: Authentication System (3-4 days)

- [ ] Implement user registration endpoint
- [ ] Implement login endpoint with JWT tokens
- [ ] Create password hashing utilities (bcrypt)
- [ ] Build token refresh mechanism
- [ ] Add authentication middleware to protect routes
- [ ] Write tests for auth endpoints

**Frontend:**

- [ ] Create login/register forms
- [ ] Implement auth context/state management
- [ ] Store JWT in localStorage (or httpOnly cookies)
- [ ] Create protected route wrapper
- [ ] Build basic profile page

**Documentation to Create:**

- `API.md` - Start documenting all API endpoints (auth section)
- `SECURITY.md` - Security considerations and best practices

### Task 1.3: Basic UI Shell (2-3 days)

- [ ] Create navigation component (bottom nav for mobile)
- [ ] Build page layout template
- [ ] Create basic pages (Home, Collection, Search, Profile)
- [ ] Implement responsive design (mobile-first)
- [ ] Add loading states and error boundaries
- [ ] Set up routing (React Router)

**Deliverable:** Users can register, login, and navigate between empty pages

---

## Phase 2: Collection Management (Week 5-7)

**Goal:** Enable users to manually add bottles and view their collection

### Task 2.1: Bottle Data Structure & API (3-4 days)

- [ ] Research and document bottle attributes (name, distillery, type, ABV, age, etc.)
- [ ] Create bottle schema/validation (Pydantic)
- [ ] Build bottle CRUD endpoints:
  - GET /bottles (list with filters)
  - GET /bottles/{id} (details)
  - POST /bottles (admin/community add)
  - PUT /bottles/{id}
  - DELETE /bottles/{id}
- [ ] Implement search functionality (by name, distillery, type)
- [ ] Add pagination for bottle lists
- [ ] Write API tests

**Documentation to Create:**

- Update `API.md` with bottle endpoints
- `BOTTLE_ATTRIBUTES.md` - Standard fields and data sources

### Task 2.2: User Collection Management (4-5 days)

- [ ] Create user_collections table (many-to-many with bottles)
- [ ] Build collection endpoints:
  - GET /my-collection
  - POST /my-collection (add bottle)
  - DELETE /my-collection/{bottle_id}
  - PUT /my-collection/{bottle_id} (update notes, quantity)
- [ ] Add image upload for bottles (S3 or Cloudflare R2)
- [ ] Implement collection filtering and sorting
- [ ] Build collection statistics endpoint (count, total value, etc.)

**Frontend:**

- [ ] Create "Add Bottle" form (manual entry)
- [ ] Build collection list view (card/grid layout)
- [ ] Implement search/filter UI
- [ ] Create bottle detail modal/page
- [ ] Add image upload component
- [ ] Show collection statistics dashboard

**Documentation to Create:**

- `IMAGE_HANDLING.md` - Image upload, storage, and optimization

**Deliverable:** Users can manually add bottles to their collection, view them, and manage their inventory

---

## Phase 3: Barcode Scanner (Week 8-9)

**Goal:** Implement barcode scanning for quick bottle addition

### Task 3.1: Barcode Scanner Research & Setup (2-3 days)

- [ ] Research barcode scanning libraries:
  - `html5-qrcode`
  - `react-zxing`
  - `quagga2`
- [ ] Test libraries with sample barcodes
- [ ] Choose best option for UPC-A/EAN-13 (standard bottle barcodes)
- [ ] Set up camera permissions handling
- [ ] Create reusable scanner component

**Learning Resources:**

- Barcode format documentation
- Web Camera API
- Chosen library documentation

### Task 3.2: Barcode Lookup Integration (3-4 days)

- [ ] Research barcode lookup APIs:
  - UPC Database API
  - Barcodelookup.com
  - Open Product Data
- [ ] Create backend service for barcode lookup
- [ ] Build fallback mechanism if API fails
- [ ] Implement caching for barcode results
- [ ] Create "bottle not found" flow for user to add manually
- [ ] Map API data to your bottle schema

**Documentation to Create:**

- `BARCODE_INTEGRATION.md` - How barcode lookup works, API keys, rate limits

### Task 3.3: Scanner UI Integration (2-3 days)

- [ ] Build scanner page/modal with camera view
- [ ] Add barcode detection feedback (visual indicators)
- [ ] Create "bottle found" confirmation screen
- [ ] Implement "add to collection" from scanner
- [ ] Add error handling for camera access denied
- [ ] Test on multiple devices (iOS Safari, Android Chrome)

**Frontend Polish:**

- [ ] Add scanning animations
- [ ] Create helpful instructions for first-time users
- [ ] Add manual barcode entry option (if camera doesn't work)

**Deliverable:** Users can scan bottle barcodes to quickly add them to their collection

---

## Phase 4: Tasting Notes & Ratings (Week 10-11)

**Goal:** Allow users to record tasting experiences and rate bottles

### Task 4.1: Tasting Notes System (3-4 days)

- [ ] Design tasting notes schema (date, rating, notes, flavor tags)
- [ ] Create flavor profile taxonomy (smoky, sweet, spicy, fruity, etc.)
- [ ] Build tasting CRUD endpoints:
  - GET /tastings (user's all tastings)
  - GET /bottles/{id}/tastings
  - POST /tastings
  - PUT /tastings/{id}
  - DELETE /tastings/{id}
- [ ] Implement flavor profile aggregation (user's taste preferences)
- [ ] Add rating calculation (average per bottle)

**Frontend:**

- [ ] Create tasting note form with:
  - Rating (1-5 stars)
  - Text notes
  - Flavor tag selection
  - Date picker
- [ ] Build tasting history view (timeline/list)
- [ ] Show average ratings on bottle cards
- [ ] Create flavor profile visualization (radar chart or tag cloud)

**Documentation to Create:**

- `FLAVOR_PROFILES.md` - Flavor taxonomy and tagging system

### Task 4.2: User Taste Profile (2-3 days)

- [ ] Calculate user's flavor preferences from ratings
- [ ] Create taste profile endpoint (aggregated data)
- [ ] Build taste profile visualization page
- [ ] Show "You tend to enjoy..." insights

**Deliverable:** Users can log tasting notes, rate bottles, and see their taste preferences

---

## Phase 5: Recommendations Engine (Week 12-13)

**Goal:** Provide personalized bottle recommendations

### Task 5.1: Rule-Based Recommendation Logic (4-5 days)

- [ ] Define recommendation rules:
  - Bottles similar to high-rated ones
  - Same distillery/region as favorites
  - Matching flavor profiles
  - Price range preferences
- [ ] Implement similarity scoring algorithm
- [ ] Build recommendation endpoint
- [ ] Create "Why we recommend this" explanations
- [ ] Add diversity to recommendations (don't just show same type)
- [ ] Implement recommendation filtering (exclude already owned)

**Frontend:**

- [ ] Create recommendations page/section
- [ ] Show recommendation cards with reasoning
- [ ] Add "I'm interested" / "Not for me" feedback
- [ ] Implement wishlist functionality

**Documentation to Create:**

- `RECOMMENDATIONS_ALGORITHM.md` - How recommendations work (v1)

### Task 5.2: Recommendation Refinement (2-3 days)

- [ ] Use user feedback to improve recommendations
- [ ] Add explicit preference settings (e.g., "I prefer bourbon")
- [ ] Create "Discovery Mode" for different bottle styles
- [ ] A/B test different recommendation strategies

**Deliverable:** Users receive personalized bottle recommendations based on their taste profile

---

## Phase 6: Pricing Intelligence (Week 14-15)

**Goal:** Show MSRP, typical market price, and value indicators

### Task 6.1: Pricing Data Integration (3-4 days)

- [ ] Research pricing data sources:
  - Wine-Searcher API (paid)
  - Web scraping from major retailers
  - Community pricing data
- [ ] Build price scraper/aggregator service
- [ ] Create pricing database table (bottle_id, source, price, date)
- [ ] Implement price history tracking
- [ ] Calculate typical market price (median/average)
- [ ] Add MSRP data (manual entry initially)

**Documentation to Create:**

- `PRICING_DATA.md` - Data sources, update frequency, accuracy

### Task 6.2: Price Display & Alerts (2-3 days)

- [ ] Show MSRP vs current market price on bottle pages
- [ ] Add "Good Deal" indicator (below typical price)
- [ ] Create price history chart
- [ ] Implement wishlist price alerts (notify when price drops)
- [ ] Add "What did you pay?" to collection entry

**Frontend:**

- [ ] Design price comparison UI
- [ ] Build price history visualization (line chart)
- [ ] Create alert preferences page

**Deliverable:** Users can see if a bottle is fairly priced and get alerts on wishlist items

---

## Phase 7: Polish & PWA Features (Week 16-17)

**Goal:** Make app installable and production-ready

### Task 7.1: PWA Implementation (3-4 days)

- [ ] Create PWA manifest.json
- [ ] Design app icons (multiple sizes)
- [ ] Implement service worker for offline support
- [ ] Add "Add to Home Screen" prompt
- [ ] Test offline functionality
- [ ] Optimize bundle size and loading times
- [ ] Add splash screen

**Documentation to Create:**

- `PWA_SETUP.md` - How PWA features work

### Task 7.2: Performance Optimization (2-3 days)

- [ ] Implement lazy loading for images
- [ ] Add code splitting (route-based)
- [ ] Optimize API calls (caching, batching)
- [ ] Add loading skeletons for better UX
- [ ] Run Lighthouse audits and fix issues
- [ ] Compress images

### Task 7.3: Testing & Bug Fixes (2-3 days)

- [ ] Write integration tests (key user flows)
- [ ] Test on multiple devices and browsers
- [ ] Fix responsive design issues
- [ ] Add error tracking (Sentry or similar)
- [ ] Implement analytics (privacy-focused)
- [ ] Create user feedback mechanism

**Deliverable:** Production-ready PWA that works offline and performs well

---

## Phase 8: Deployment & Launch (Week 18)

**Goal:** Deploy to production and prepare for users

### Task 8.1: Production Setup (2-3 days)

- [ ] Set up production database (managed PostgreSQL)
- [ ] Configure production environment variables
- [ ] Deploy backend to Railway/Render/Fly.io
- [ ] Deploy frontend to Vercel/Netlify
- [ ] Set up custom domain (optional)
- [ ] Configure SSL certificates
- [ ] Set up backup strategy for database

**Documentation to Create:**

- `DEPLOYMENT.md` - How to deploy updates
- `ENVIRONMENT_VARIABLES.md` - Required env vars for production

### Task 8.2: Pre-Launch Checklist (1-2 days)

- [ ] Create privacy policy
- [ ] Create terms of service
- [ ] Set up user support email
- [ ] Write onboarding tutorial
- [ ] Create demo/marketing page
- [ ] Final security audit
- [ ] Load testing

### Task 8.3: Soft Launch (1-2 days)

- [ ] Invite 5-10 beta testers
- [ ] Gather feedback
- [ ] Fix critical bugs
- [ ] Iterate on UX issues
- [ ] Monitor server performance

**Deliverable:** Live app accessible to users!

---

## Future Phases (Post-Launch)

### Phase 9: Local Inventory Tracking

- Scrape/monitor local liquor store websites
- Instagram integration for store drops
- Store location mapping
- Rare bottle alerts

### Phase 10: Machine Learning Recommendations

- Collect more user data
- Train collaborative filtering model
- Implement content-based filtering
- A/B test ML vs rule-based

### Phase 11: Social Features

- Follow friends
- Share collections
- Comments on tastings
- Public profiles

### Phase 12: Advanced Features

- Investment tracking
- Cellar management
- Event planning
- Insurance export

---

## Database Schema (Reference)

```sql
-- Users
users (
  id SERIAL PRIMARY KEY,
  email VARCHAR UNIQUE NOT NULL,
  password_hash VARCHAR NOT NULL,
  username VARCHAR UNIQUE,
  created_at TIMESTAMP DEFAULT NOW()
)

-- Bottles (master list)
bottles (
  id SERIAL PRIMARY KEY,
  name VARCHAR NOT NULL,
  distillery VARCHAR,
  type VARCHAR (bourbon, scotch, rye, etc.),
  region VARCHAR,
  age_years INTEGER,
  abv DECIMAL,
  msrp DECIMAL,
  barcode VARCHAR UNIQUE,
  description TEXT,
  image_url VARCHAR,
  created_at TIMESTAMP DEFAULT NOW()
)

-- User Collections (bottles owned)
user_collections (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  bottle_id INTEGER REFERENCES bottles(id),
  quantity INTEGER DEFAULT 1,
  purchase_date DATE,
  purchase_price DECIMAL,
  purchase_location VARCHAR,
  notes TEXT,
  added_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(user_id, bottle_id)
)

-- Tastings (tasting notes)
tastings (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  bottle_id INTEGER REFERENCES bottles(id),
  rating INTEGER CHECK (rating >= 1 AND rating <= 5),
  notes TEXT,
  tasting_date DATE,
  created_at TIMESTAMP DEFAULT NOW()
)

-- Flavor Profiles
flavor_tags (
  id SERIAL PRIMARY KEY,
  name VARCHAR UNIQUE (smoky, sweet, spicy, etc.)
)

-- Tasting Flavors (many-to-many)
tasting_flavors (
  tasting_id INTEGER REFERENCES tastings(id),
  flavor_tag_id INTEGER REFERENCES flavor_tags(id),
  intensity INTEGER CHECK (intensity >= 1 AND intensity <= 5),
  PRIMARY KEY (tasting_id, flavor_tag_id)
)

-- Pricing History
bottle_prices (
  id SERIAL PRIMARY KEY,
  bottle_id INTEGER REFERENCES bottles(id),
  price DECIMAL,
  source VARCHAR (retailer name or 'market'),
  recorded_at TIMESTAMP DEFAULT NOW()
)

-- Wishlist
wishlists (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  bottle_id INTEGER REFERENCES bottles(id),
  target_price DECIMAL,
  notify_on_drop BOOLEAN DEFAULT FALSE,
  added_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(user_id, bottle_id)
)
```

---

## Learning Resources by Phase

### Phase 0-1 (Foundations):

- [React Official Tutorial](https://react.dev/learn)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [PWA Documentation](https://web.dev/progressive-web-apps/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)

### Phase 2-3 (Core Features):

- [SQLAlchemy ORM Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)
- [Web Camera API](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia)
- [File Upload Best Practices](https://web.dev/file-upload/)

### Phase 4-5 (Advanced Features):

- [Recommendation Systems Basics](https://developers.google.com/machine-learning/recommendation)
- [Data Visualization with Recharts](https://recharts.org/en-US/)

### Phase 6-7 (Polish):

- [Web Scraping with Python](https://realpython.com/python-web-scraping-practical-introduction/)
- [Service Workers Guide](https://web.dev/service-workers-cache-storage/)
- [Web Performance Optimization](https://web.dev/fast/)

---

## Time Estimates Summary

| Phase                          | Duration  | Cumulative |
| ------------------------------ | --------- | ---------- |
| Phase 0: Foundation            | 1-2 weeks | 2 weeks    |
| Phase 1: Infrastructure        | 1-2 weeks | 4 weeks    |
| Phase 2: Collection Management | 2-3 weeks | 7 weeks    |
| Phase 3: Barcode Scanner       | 2 weeks   | 9 weeks    |
| Phase 4: Tasting Notes         | 2 weeks   | 11 weeks   |
| Phase 5: Recommendations       | 2 weeks   | 13 weeks   |
| Phase 6: Pricing               | 2 weeks   | 15 weeks   |
| Phase 7: PWA & Polish          | 2 weeks   | 17 weeks   |
| Phase 8: Deployment            | 1 week    | 18 weeks   |

**Total MVP Timeline: ~4-5 months** (accounting for learning, debugging, and iteration)

---

## Quality Checklist (Use Throughout)

For each feature/phase:

- [ ] Code is documented with comments
- [ ] API endpoints are documented in `API.md`
- [ ] Database changes have migrations
- [ ] Tests are written (where applicable)
- [ ] Mobile responsive design tested
- [ ] Error handling implemented
- [ ] Loading states implemented
- [ ] User feedback collected
- [ ] Git commits are descriptive
- [ ] Code reviewed (self-review at minimum)

---

## Notes

- **Adjust timeline as needed** - These are estimates. Some phases may take longer as you learn.
- **Document as you go** - Don't save documentation for the end. Update docs when you build features.
- **Ship early, iterate often** - Don't wait for perfection. Get Phase 2-3 working and start using it yourself.
- **Ask for help** - Join developer communities (Reddit, Discord) when stuck.
- **Take breaks** - This is a marathon, not a sprint. Burnout helps no one.

Good luck! 🥃
