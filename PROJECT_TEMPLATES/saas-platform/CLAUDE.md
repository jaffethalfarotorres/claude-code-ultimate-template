# [Your Platform Name] — Business Context

**Version:** 1.0.0
**Last Updated:** [Date]
**Business Type:** SaaS Platform
**Status:** [Planning / Development / Production]

---

## What We Do

### Problem Statement
**[Describe the problem your platform solves]**

Example (Ride-Sharing):
> Commuters waste money on individual rides. Drivers have empty seats. No efficient way to match riders with drivers going the same route.

Example (Marketplace):
> Buyers can't find quality handmade goods. Artisans can't reach customers. Traditional marketplaces charge 30%+ fees.

### Our Solution
**[Describe how your platform solves it]**

Example (Ride-Sharing):
> Platform that matches riders with drivers in real-time. Riders save 60% vs taxis. Drivers earn money from empty seats. Win-win.

Example (Marketplace):
> Direct connection between artisans and buyers. Only 10% fee. Quality verification. Fair pricing.

---

## Business Model

### Revenue Streams
- [ ] **Commission:** [X%] per transaction
- [ ] **Subscription:** $[X]/month for premium features
- [ ] **Freemium:** Free tier + paid upgrades
- [ ] **Ads:** Sponsored listings/placements
- [ ] **Other:** [Specify]

### Target Customers
- **Primary:** [Who are your main users?]
- **Secondary:** [Who else benefits?]

Example (Ride-Sharing):
- Primary: Daily commuters (9-5 workers)
- Secondary: Occasional riders (airport trips, events)

### Geographic Focus
- [ ] Local (city-specific)
- [ ] Regional (country/state)
- [ ] Global

**Initial Launch:** [City/Region]

---

## Technical Architecture

### Tech Stack
**Backend:**
- Language: [Python / Node.js / Go / etc.]
- Framework: [FastAPI / Express / Django / etc.]
- Database: [PostgreSQL / MongoDB / etc.]

**Frontend:**
- Framework: [React / Vue / Svelte / etc.]
- Language: [TypeScript / JavaScript]
- Styling: [Tailwind / CSS Modules / etc.]

**Infrastructure:**
- Hosting: [AWS / GCP / Azure / Vercel / etc.]
- CI/CD: [GitHub Actions / GitLab CI / etc.]
- Monitoring: [Sentry / DataDog / etc.]

### Core Modules
1. **[module-name]/** — [What it does]
2. **[module-name]/** — [What it does]
3. **[module-name]/** — [What it does]

Example (Ride-Sharing):
1. **route-optimizer/** — Calculates optimal routes
2. **user-matching/** — Matches riders with drivers
3. **payment-processing/** — Handles transactions
4. **notification-service/** — Sends alerts
5. **user-interface/** — Frontend app

---

## Development Guidelines

### Architecture Principles (Inherited from Template)

✅ **Machine-First:**
- Purpose-driven naming (`route-optimizer` not `services`)
- Flat structure (max 2 levels)
- English-only, ASCII paths
- Predictable patterns

✅ **Zero-Friction:**
- Inbox automation (user feedback → auto-process)
- Background file watchers
- 3-second rule (automate if >3 seconds)

✅ **Self-Improving:**
- Learning loop (extract patterns from usage)
- LEARNINGS.md (document discoveries)
- Cross-business pattern sharing

### Code Style
- **Language:** [Specify: Python PEP 8, JavaScript Standard, etc.]
- **Linting:** [ESLint, Pylint, etc.]
- **Formatting:** [Prettier, Black, etc.]
- **Testing:** [Jest, Pytest, etc.]

### Git Workflow
- **Branch strategy:** [Git Flow / GitHub Flow / Trunk-Based]
- **Commit format:** [Conventional Commits / Custom]
- **PR requirements:** [Tests pass, code review, etc.]

---

## Current State

### What Works
- [ ] Authentication (login/register)
- [ ] Core service (basic functionality)
- [ ] API endpoints (documented)
- [ ] Frontend (MVP)
- [ ] Deployment (staging)

### In Progress
- [ ] [Feature/module name]
- [ ] [Feature/module name]
- [ ] [Feature/module name]

### Backlog
- [ ] [Future feature]
- [ ] [Future feature]
- [ ] [Future feature]

---

## Key Metrics

### Business Metrics
- **Users:** [Current count]
- **Transactions:** [Per day/week/month]
- **Revenue:** $[Amount] [per month]
- **Growth:** [X]% month-over-month

### Technical Metrics
- **Uptime:** [X]%
- **Response time:** [X]ms average
- **Error rate:** [X]%
- **Test coverage:** [X]%

---

## Team

### Roles
- **Developer:** [Name or "Solo founder"]
- **Designer:** [Name or "DIY"]
- **Marketing:** [Name or "TBD"]

---

## External Resources

### APIs & Services
- **[Service name]:** [What it's used for, API key location]
- **[Service name]:** [What it's used for, API key location]

Example:
- **Google Maps API:** Route calculation, geocoding (key in .env)
- **Stripe:** Payment processing (key in .env)
- **SendGrid:** Email notifications (key in .env)

### Documentation
- [Link to external docs]
- [Link to design files]
- [Link to product roadmap]

---

## Security & Compliance

### Data Privacy
- [ ] GDPR compliant (if EU users)
- [ ] CCPA compliant (if California users)
- [ ] Privacy policy published
- [ ] Data retention policy defined

### Security Measures
- [ ] HTTPS everywhere
- [ ] JWT token authentication
- [ ] Rate limiting
- [ ] SQL injection prevention
- [ ] XSS protection
- [ ] CSRF protection

### Secrets Management
- [ ] `.env` file (gitignored)
- [ ] Environment variables in production
- [ ] No secrets in code

---

## Contact

**Primary Contact:** [Your name]
**Email:** [Your email]
**Repository:** [GitHub URL]
**Live Site:** [URL if deployed]

---

## Version History

### v1.0.0 (Initial Release)
- [Date]
- Initial business context document
- Template structure set up
- Architecture defined

---

**Instructions for Claude Code:**

This file provides the business context for the platform. When working on this project:

1. **Follow architecture principles** defined in `.claude/rules/`
2. **Document learnings** in `LEARNINGS.md`
3. **Update SPRINT_LOG.md** after completing tasks
4. **Create ADRs** for major architectural decisions
5. **Use inbox automation** for processing user feedback
6. **Run sync-learnings.py** periodically to share patterns with other businesses

**Remember:** This platform is part of a larger ecosystem. Patterns you discover here will help all other businesses. Patterns discovered elsewhere are available to you.

🌱 Build independently. Learn collectively.
