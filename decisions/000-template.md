# Decision {NUMBER}: {TITLE}

**Date:** YYYY-MM-DD
**Status:** [Proposed | Accepted | Deprecated | Superseded]
**Deciders:** [Names or roles]

---

## Context

[Describe the situation, problem, or opportunity that requires a decision]

[Include relevant background information:]
- What problem are we trying to solve?
- What constraints do we have?
- What business or technical needs drive this?
- What's the current situation?

---

## Decision

[Clear, concise statement of the decision made]

[Explain what will be done and what won't be done]

---

## Consequences

### Positive

- ✅ [Benefit 1]
- ✅ [Benefit 2]
- ✅ [Benefit 3]

### Negative

- ❌ [Tradeoff 1]
- ❌ [Tradeoff 2]
- ❌ [Limitation 1]

### Neutral

- ℹ️ [Interesting note 1]
- ℹ️ [Side effect that's neither good nor bad]

---

## Alternatives Considered

### Option A: {NAME}

**Description:** [What was this alternative?]

**Pros:**
- [Advantage 1]
- [Advantage 2]

**Cons:**
- [Disadvantage 1]
- [Disadvantage 2]

**Rejected because:** [Specific reason]

---

### Option B: {NAME}

**Description:** [What was this alternative?]

**Pros:**
- [Advantage 1]
- [Advantage 2]

**Cons:**
- [Disadvantage 1]
- [Disadvantage 2]

**Rejected because:** [Specific reason]

---

## Implementation Notes

[How will this decision be implemented?]

[What are the next steps?]

[What files, code, or systems will change?]

---

## References

- [Link to relevant discussion or issue]
- [Related ADRs]
- [External documentation]
- [Research or articles that influenced this decision]

---

## Revision History

| Date | Change | Author |
|------|--------|--------|
| YYYY-MM-DD | Initial decision | [Name] |

---

## Notes

**How to use this template:**

1. Copy this file to `decisions/{NUMBER}-{slug}.md`
2. Replace `{NUMBER}` with next sequential number (e.g., 001, 002, 003)
3. Replace `{TITLE}` and `{slug}` with your decision title
4. Fill in all sections (delete this Notes section when done)
5. Update **Status** as decision evolves (Proposed → Accepted → Deprecated)
6. Commit with message: `docs: ADR-{NUMBER} - {TITLE}`

**Tips:**
- Be specific and concrete, avoid vague language
- Explain the "why" not just the "what"
- Document alternatives to show you considered options
- Keep it concise (1-2 pages maximum)
- Update status if decision changes later
- Reference this ADR in code comments where relevant
