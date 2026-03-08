# Core Service — Knowledge Base

**Module Purpose:** [Describe what this module does — main business logic]

**Example (Ride-Sharing):** Calculates optimal routes and matches riders with drivers

**Example (Marketplace):** Manages product listings and search functionality

---

## Domain Knowledge

### [Topic 1]
[Add domain-specific knowledge here]

**Example (Ride-Sharing — Geospatial Calculations):**
- Use Haversine formula for distance calculation
- Earth radius: 6371 km
- 1 degree latitude ≈ 111 km

### [Topic 2]
[Add more domain knowledge]

**Example (Ride-Sharing — Traffic Patterns):**
- Rush hour: 7-9 AM, 5-7 PM (higher congestion)
- Off-peak: 10 AM - 4 PM (faster routes)
- Weekend: Different patterns

---

## Learned Patterns

### Pattern 1: [Pattern Name] ([Date])
**Problem:** [What was the challenge?]

**Solution:** [How did you solve it?]

**Code:**
```[language]
[Example code]
```

**Result:** [What improved? Metrics?]

---

## Common Issues

### Issue 1: [Issue Name]
**Problem:** [Description]

**Solution:** [How to fix]

**Prevention:** [How to avoid in future]

---

## External Dependencies

### [API/Service Name]
**Purpose:** [What it's used for]

**Configuration:** [Where is config/key stored?]

**Rate Limits:** [Any limitations?]

**Example (Google Maps API):**
- Purpose: Route calculation, geocoding
- Configuration: API key in .env (GOOGLE_MAPS_API_KEY)
- Rate Limits: 40,000 requests/day (free tier)

---

## Formulas & Algorithms

### [Formula/Algorithm Name]
[Description and formula]

**Example (Haversine Distance):**
```
d = 2r × arcsin(√(sin²((lat₂-lat₁)/2) + cos(lat₁)×cos(lat₂)×sin²((lon₂-lon₁)/2)))

where:
  r = Earth radius (6371 km)
  lat₁, lon₁ = Origin coordinates
  lat₂, lon₂ = Destination coordinates
```

---

## Data Models

See `_shared/data-models.md` for complete data model definitions.

**Key models used by this module:**
- [Model 1]
- [Model 2]
- [Model 3]

---

## Testing Notes

### Test Data
[Where to find test data for this module]

### Edge Cases
- [Edge case 1]
- [Edge case 2]
- [Edge case 3]

---

🧠 **This knowledge base grows with every problem solved.**
