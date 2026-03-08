# Learnings & Patterns Discovered

**Business:** [Your Platform Name]
**Started:** [Date]
**Last Updated:** [Date]

---

## Purpose

This file documents patterns, solutions, and learnings discovered while building this platform.

**When to document a learning:**
- Solved a non-trivial problem (>1 hour to figure out)
- Solution is generalizable to other businesses
- Has measurable evidence of success
- You'd want this pattern in your next project

**What happens to learnings:**
- Periodically, run `python ../../_template/sync-learnings.py`
- Script extracts HIGH/MEDIUM value patterns
- Adds to `_template/PATTERNS_DISCOVERED.md`
- Syncs to all other businesses
- Future businesses inherit your discoveries

---

## Template for New Patterns

```markdown
## Pattern: [Descriptive Name]
**Category:** [Architecture / Automation / Intelligence / Operations / Safety / Performance / Integration / Testing / Deployment / Monitoring]
**Date Discovered:** [YYYY-MM-DD]
**Problem:** [What problem did this solve? Be specific.]

**Solution:**
[How did you solve it? Include code snippets, diagrams, or step-by-step explanation.]

**Implementation:**
```[language]
[Code example or pseudocode]
```

**Evidence:**
[Proof it works. Metrics, test results, before/after comparisons.]

**Generalizability:** [HIGH / MEDIUM / LOW]
- HIGH: Universal benefit, solves major pain point
- MEDIUM: Useful for many businesses
- LOW: Specific to this business (don't extract)

**Notes:**
[Any additional context, trade-offs, or future improvements.]
```

---

## Patterns Discovered

### Example Pattern (DELETE THIS AFTER FIRST REAL PATTERN)

## Pattern: Real-Time WebSocket Connection Management
**Category:** Performance
**Date Discovered:** 2026-03-08
**Problem:** WebSocket connections dropping during high load, users experiencing lag.

**Solution:**
Implement connection pooling with automatic reconnection and heartbeat monitoring.

**Implementation:**
```python
# websocket_manager.py
import asyncio
from datetime import datetime

class WebSocketManager:
    def __init__(self, max_connections=1000):
        self.connections = {}
        self.max_connections = max_connections
        self.heartbeat_interval = 30  # seconds

    async def add_connection(self, user_id, websocket):
        if len(self.connections) >= self.max_connections:
            raise Exception("Max connections reached")

        self.connections[user_id] = {
            'socket': websocket,
            'last_heartbeat': datetime.now(),
        }

        # Start heartbeat monitor
        asyncio.create_task(self.monitor_heartbeat(user_id))

    async def monitor_heartbeat(self, user_id):
        while user_id in self.connections:
            try:
                # Send ping
                await self.connections[user_id]['socket'].ping()
                self.connections[user_id]['last_heartbeat'] = datetime.now()
            except Exception as e:
                # Connection lost, remove
                self.remove_connection(user_id)
                break

            await asyncio.sleep(self.heartbeat_interval)

    def remove_connection(self, user_id):
        if user_id in self.connections:
            del self.connections[user_id]
```

**Evidence:**
- Connection drop rate: 15% → 2% (87% improvement)
- Average latency: 450ms → 180ms (60% improvement)
- Tested with 5,000 concurrent connections (load test)

**Generalizability:** HIGH
- Any platform with real-time features (chat, notifications, live updates)
- Academic ghostwriting: Real-time collaboration on documents
- Invoice tool: Live invoice status updates

**Notes:**
- Could optimize further with Redis pub/sub for horizontal scaling
- Consider adding exponential backoff for reconnection attempts

---

## Pattern Categories

Track patterns by category to identify strengths and gaps:

- **Architecture:** 0 patterns
- **Automation:** 0 patterns
- **Intelligence:** 0 patterns
- **Operations:** 0 patterns
- **Safety:** 0 patterns
- **Performance:** 1 pattern (example above)
- **Integration:** 0 patterns
- **Testing:** 0 patterns
- **Deployment:** 0 patterns
- **Monitoring:** 0 patterns

---

## Cross-Business Opportunities

Patterns from other businesses that might apply here:

### From academic-ghostwriting:
- **Two-PC Continuity System** — Could use for multi-device development
- **Sprint Log Pattern** — Already using (SPRINT_LOG.md)
- **Trash-Can Pattern** — Could use for reversible deletions

### From other platforms (when discovered):
- [Patterns will appear here after sync]

---

## Anti-Patterns (What NOT to Extract)

### ❌ Business-Specific Logic
Example: Pricing formula for ride-sharing ($2 base + $0.50/km)
Reason: Only applies to this business

### ❌ Trivial Solutions
Example: "Use async/await for asynchronous code"
Reason: Common knowledge, not a discovery

### ❌ Unproven Patterns
Example: "Experimental caching strategy (not tested)"
Reason: Only extract patterns with evidence

---

## Next Sync

**Last sync:** [Date or "Never"]
**Patterns extracted:** [Count]
**Next sync:** [Date or "Run manually when you discover 3+ HIGH value patterns"]

**To run sync:**
```bash
cd ../../_template
python sync-learnings.py --verbose
```

---

🌱 **Document your discoveries. They'll help all businesses in the ecosystem.**
