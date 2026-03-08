# SaaS Platform Template

**Purpose:** Template for building multi-tenant SaaS platforms (ride-sharing, marketplaces, booking systems, etc.)

**Inherits:** All 12 patterns from `PATTERNS_DISCOVERED.md` + machine-first architecture

**Examples:** CarPooling platform, marketplace apps, booking systems, on-demand services

---

## Quick Start

### 1. Copy Template to Your Business

```bash
# From workspace root
cp -r _template/PROJECT_TEMPLATES/saas-platform/ businesses/your-platform-name/

cd businesses/your-platform-name/
```

### 2. Initialize Git Repository

```bash
git init
git remote add origin https://github.com/yourusername/your-platform-name.git
```

### 3. Customize CLAUDE.md

Edit `CLAUDE.md` with your business context:
- What problem does your platform solve?
- Who are your users?
- What's your business model?
- What's your tech stack?

### 4. Link to Template Rules

```bash
# Copy rules from template (or symlink if on Unix)
cp -r ../../_template/.claude/rules/ .claude/rules/
```

### 5. Customize Modules

Rename/modify modules based on your business:

**Example (Ride-Sharing Platform):**
- `core-service/` → `route-optimizer/`, `user-matching/`, `payment-processing/`

**Example (Marketplace):**
- `core-service/` → `listing-manager/`, `search-engine/`, `transaction-processor/`

**Example (Booking System):**
- `core-service/` → `availability-manager/`, `booking-engine/`, `notification-service/`

### 6. Start Building

```bash
# Create first module
cd route-optimizer/

# Read knowledge.md for module guidance
cat knowledge.md

# Start coding!
```

---

## Folder Structure

```
businesses/your-platform-name/
├── CLAUDE.md                    # Business context (customize this!)
├── README.md                    # This file (customize for your platform)
├── SPRINT_LOG.md                # Track development progress
├── LEARNINGS.md                 # Document patterns you discover
├── .gitignore                   # Standard gitignore
│
├── .claude/
│   ├── rules/                   # Architecture rules (copied from template)
│   ├── commands/                # Custom slash commands
│   └── agents/                  # Agent configurations
│
├── core-service/                # Main business logic module
│   ├── README.md                # Module purpose
│   ├── knowledge.md             # Domain knowledge for this module
│   ├── role.md                  # Module identity/role
│   └── history.md               # Learning history
│
├── api-gateway/                 # API layer module
│   ├── README.md
│   ├── knowledge.md
│   ├── role.md
│   └── history.md
│
├── user-interface/              # Frontend module
│   ├── README.md
│   ├── knowledge.md
│   ├── role.md
│   └── history.md
│
├── _shared/                     # Cross-module shared knowledge
│   ├── README.md
│   ├── data-models.md           # Shared data structures
│   ├── api-contracts.md         # API specifications
│   └── deployment-config.md     # Deployment configurations
│
├── _meta/                       # Self-improvement intelligence
│   ├── knowledge-graph.md       # Concept relationships
│   ├── routing-rules.md         # Module routing logic
│   └── optimization-log.md      # Performance optimizations
│
├── pipelines/
│   ├── intake/                  # Zero-friction automation
│   │   ├── README.md
│   │   ├── inbox/               # Drop files here
│   │   ├── outbox/              # Results appear here
│   │   └── process-inbox.py     # Automation script
│   │
│   └── deployment/              # CI/CD pipelines
│       ├── README.md
│       └── deploy.sh
│
├── archive/
│   ├── trash-can/               # Reversible deletions
│   ├── backups/                 # Quick snapshots
│   └── deprecated/              # Old code
│
├── decisions/                   # Architectural Decision Records
│   ├── 000-template.md
│   └── 001-initial-architecture.md
│
└── knowledge/                   # Persistent memory
    ├── MEMORY.md                # Current state (multi-machine continuity)
    └── patterns.md              # Accumulated learnings
```

---

## Module Templates

### Core Service Module (Main Business Logic)

**Example: route-optimizer/ for ride-sharing platform**

`route-optimizer/README.md`:
```markdown
# Route Optimizer

**Purpose:** Calculates optimal routes for matching riders with drivers.

**Responsibilities:**
- Calculates shortest/fastest routes using geospatial data
- Considers real-time traffic conditions
- Optimizes for cost, time, or carbon footprint
- Caches frequent routes for performance

**Dependencies:**
- Google Maps API (or OpenStreetMap)
- Redis (route caching)
- PostgreSQL with PostGIS (geospatial queries)

**Key Algorithms:**
- Dijkstra's algorithm for route calculation
- K-nearest neighbors for driver matching
- Cache invalidation after 15 minutes
```

`route-optimizer/knowledge.md`:
```markdown
# Route Optimizer Knowledge Base

## Domain Knowledge

### Geospatial Calculations
- Use Haversine formula for distance: `d = 2r * arcsin(sqrt(sin²((lat2-lat1)/2) + cos(lat1)*cos(lat2)*sin²((lon2-lon1)/2)))`
- Earth radius: 6371 km
- 1 degree latitude ≈ 111 km

### Traffic Patterns
- Rush hour: 7-9 AM, 5-7 PM (higher congestion)
- Off-peak: 10 AM - 4 PM (faster routes)
- Weekend: Different patterns (less congestion)

### Optimization Strategies
- **Shortest route:** Minimize distance (good for cost)
- **Fastest route:** Minimize time (good for urgency)
- **Eco route:** Minimize carbon (good for environment)

## Learned Patterns

### Pattern 1: Route Caching (2026-03-08)
Cache routes with composite key: (origin, destination, time_of_day)
- Reduces calculation time: 450ms → 12ms
- Invalidate after 15 minutes (traffic changes)

### Pattern 2: Batch Processing (2026-03-09)
Process multiple route requests in parallel
- Use asyncio for concurrent API calls
- 10x faster for batch requests

## Common Issues

### Issue 1: API Rate Limits
**Problem:** Google Maps API limits requests
**Solution:** Implement exponential backoff, cache aggressively

### Issue 2: Outdated Cache
**Problem:** Traffic changes, cached route is slow
**Solution:** TTL of 15 minutes, invalidate on major incidents
```

---

### API Gateway Module

**Example: api-gateway/ for any SaaS platform**

`api-gateway/README.md`:
```markdown
# API Gateway

**Purpose:** Central entry point for all API requests. Handles authentication, rate limiting, routing.

**Responsibilities:**
- Authenticate API requests (JWT tokens)
- Rate limiting (prevent abuse)
- Route to correct microservice
- Log all requests

**Tech Stack:**
- Node.js + Express (or FastAPI for Python)
- Redis (rate limiting, session storage)
- JWT for authentication

**Endpoints:**
- POST /auth/login
- POST /auth/register
- GET /api/v1/{resource}
- POST /api/v1/{resource}
```

---

### User Interface Module

**Example: user-interface/ for any SaaS platform**

`user-interface/README.md`:
```markdown
# User Interface

**Purpose:** Frontend application for end users.

**Responsibilities:**
- Render UI components
- Handle user interactions
- Communicate with API gateway
- Manage client-side state

**Tech Stack:**
- React (or Vue, Svelte, etc.)
- TypeScript
- Tailwind CSS
- React Query (API state management)

**Key Features:**
- Responsive design (mobile-first)
- Accessibility (WCAG 2.1 AA)
- Offline support (PWA)
```

---

## Shared Knowledge Layer (`_shared/`)

### data-models.md
```markdown
# Shared Data Models

## User Model
```json
{
  "id": "uuid",
  "email": "string",
  "name": "string",
  "role": "rider | driver | admin",
  "created_at": "timestamp",
  "verified": "boolean"
}
```

## Route Model
```json
{
  "id": "uuid",
  "origin": {"lat": "float", "lon": "float"},
  "destination": {"lat": "float", "lon": "float"},
  "distance_km": "float",
  "duration_minutes": "float",
  "cost_usd": "float",
  "created_at": "timestamp"
}
```
```

### api-contracts.md
```markdown
# API Contracts

## Authentication

### POST /auth/login
**Request:**
```json
{
  "email": "user@example.com",
  "password": "secure_password"
}
```

**Response:**
```json
{
  "token": "jwt_token_here",
  "user": { /* User object */ }
}
```

## Routes

### POST /api/v1/routes/calculate
**Request:**
```json
{
  "origin": {"lat": 9.9281, "lon": -84.0907},
  "destination": {"lat": 9.9326, "lon": -84.0787},
  "optimization": "fastest | shortest | eco"
}
```

**Response:**
```json
{
  "route_id": "uuid",
  "distance_km": 5.2,
  "duration_minutes": 12,
  "cost_usd": 8.50,
  "polyline": "encoded_polyline_string"
}
```
```

---

## Zero-Friction Automation

### Inbox Pattern (for User Feedback Processing)

`pipelines/intake/process-inbox.py`:
```python
#!/usr/bin/env python3
"""
Process user feedback, bug reports, feature requests from inbox.

Files dropped in inbox/ are automatically classified and routed.
"""

import os
from pathlib import Path
from datetime import datetime

INBOX = Path("pipelines/intake/inbox")
OUTBOX = Path("pipelines/intake/outbox")
PROCESSED = Path("pipelines/intake/processed")

KEYWORDS_TO_CATEGORY = {
    "bug": "bugs",
    "error": "bugs",
    "crash": "bugs",
    "feature": "features",
    "request": "features",
    "feedback": "feedback",
    "suggestion": "feedback",
}

def classify_file(filename, content):
    """Classify file based on keywords."""
    filename_lower = filename.lower()
    content_lower = content.lower()

    for keyword, category in KEYWORDS_TO_CATEGORY.items():
        if keyword in filename_lower or keyword in content_lower:
            return category

    return "general"

def process_inbox():
    """Process all files in inbox."""
    for file_path in INBOX.glob("*"):
        if not file_path.is_file():
            continue

        print(f"Processing: {file_path.name}")

        # Read file
        content = file_path.read_text(encoding='utf-8', errors='ignore')

        # Classify
        category = classify_file(file_path.name, content)
        print(f"  Category: {category}")

        # Archive processed file
        archive_dir = PROCESSED / datetime.now().strftime("%Y-%m-%d")
        archive_dir.mkdir(parents=True, exist_ok=True)
        archive_path = archive_dir / file_path.name
        file_path.rename(archive_path)

        print(f"  Archived: {archive_path}")

if __name__ == "__main__":
    process_inbox()
```

---

## Customization Examples

### Example 1: Ride-Sharing Platform (CarPooling)

**Modules:**
- `route-optimizer/` — Calculate routes
- `user-matching/` — Match riders with drivers
- `payment-processing/` — Handle transactions
- `notification-service/` — Send alerts
- `user-interface/` — Frontend app

**_shared/data-models.md:**
- User, Driver, Rider, Route, Trip, Payment

**Learnings to discover:**
- Real-time matching algorithms
- Dynamic pricing strategies
- Surge pricing during peak hours

---

### Example 2: Marketplace Platform

**Modules:**
- `listing-manager/` — Create/edit listings
- `search-engine/` — Find products
- `transaction-processor/` — Handle purchases
- `review-system/` — User reviews
- `user-interface/` — Frontend app

**_shared/data-models.md:**
- Product, Seller, Buyer, Order, Review

**Learnings to discover:**
- Search ranking algorithms
- Fraud detection patterns
- Reputation scoring

---

### Example 3: Booking System

**Modules:**
- `availability-manager/` — Track availability
- `booking-engine/` — Create bookings
- `payment-processing/` — Handle payments
- `notification-service/` — Confirmations, reminders
- `user-interface/` — Frontend app

**_shared/data-models.md:**
- Resource, Booking, Customer, Payment

**Learnings to discover:**
- Overbooking strategies
- Cancellation policies
- No-show prediction

---

## Growth Path

### Phase 1: MVP (Weeks 1-4)
- [ ] Set up core-service module
- [ ] Implement basic API gateway
- [ ] Build minimal user-interface
- [ ] Deploy to staging

### Phase 2: Learning (Weeks 5-8)
- [ ] Process real user feedback (inbox automation)
- [ ] Extract patterns to LEARNINGS.md
- [ ] Optimize based on usage data
- [ ] Document in SPRINT_LOG.md

### Phase 3: Scale (Weeks 9-12)
- [ ] Add caching layer (Pattern 9: Route Optimization Caching)
- [ ] Implement backup strategy (Pattern 9: Backup/Rollback)
- [ ] Create ADRs for major decisions (Pattern 10: ADRs)
- [ ] Prepare for production launch

### Phase 4: Contribution (Ongoing)
- [ ] Run `python ../../_template/sync-learnings.py`
- [ ] Share discovered patterns with all businesses
- [ ] Benefit from patterns discovered in other businesses
- [ ] Compound learning across ecosystem

---

## Inherited Patterns (Automatic)

This template includes all 12 patterns from `PATTERNS_DISCOVERED.md`:

✅ **Architecture Patterns:**
- Linked Documentation System (every folder has README.md)
- Root Hygiene Rules (clean root folder)

✅ **Automation Patterns:**
- Zero-friction inbox (drop files → auto-process)

✅ **Intelligence Patterns:**
- Sprint Log (track progress)
- Chronicle (document journey)
- ADRs (document decisions)

✅ **Operations Patterns:**
- Two-PC Continuity (work from multiple machines)
- Backup/Rollback Strategy (quick snapshots)

✅ **Safety Patterns:**
- Autonomous Decision Framework (clear boundaries)
- Trash-Can Pattern (reversible operations)

---

## Next Steps

1. **Copy this template** to `businesses/your-platform-name/`
2. **Customize CLAUDE.md** with your business context
3. **Rename modules** based on your business needs
4. **Start building** your first module
5. **Document learnings** in LEARNINGS.md
6. **Run sync** to share patterns with all businesses

---

🚀 **Build fast. Learn continuously. Share generously.**

Your platform benefits from all previous businesses. Future businesses will benefit from yours.
