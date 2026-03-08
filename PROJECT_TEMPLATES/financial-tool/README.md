# Financial Tool Template

**Purpose:** Template for building financial tools (invoicing, accounting, expense tracking, tax tools, etc.)

**Inherits:** All 12 patterns from `PATTERNS_DISCOVERED.md` + machine-first architecture

**Examples:** Invoice generators, expense trackers, accounting software, tax calculators, payment processors

---

## Quick Start

### 1. Copy Template to Your Business

```bash
# From workspace root
cp -r _template/PROJECT_TEMPLATES/financial-tool/ businesses/your-tool-name/

cd businesses/your-tool-name/
```

### 2. Initialize Git Repository

```bash
git init
git remote add origin https://github.com/yourusername/your-tool-name.git
```

### 3. Customize CLAUDE.md

Edit `CLAUDE.md` with your business context:
- What financial problem does your tool solve?
- Who are your users? (freelancers, small businesses, enterprises?)
- What regulations apply? (tax laws, accounting standards)
- What's your business model?

### 4. Link to Template Rules

```bash
# Copy rules from template
cp -r ../../_template/.claude/rules/ .claude/rules/
```

### 5. Customize Modules

Rename/modify modules based on your tool:

**Example (Invoice Generator):**
- `calculation-engine/` → `invoice-calculator/`, `tax-calculator/`, `discount-engine/`

**Example (Expense Tracker):**
- `calculation-engine/` → `expense-categorizer/`, `report-generator/`, `budget-analyzer/`

**Example (Accounting Software):**
- `calculation-engine/` → `ledger-manager/`, `reconciliation-engine/`, `financial-reporter/`

### 6. Start Building

```bash
# Create first module
cd invoice-calculator/

# Read knowledge.md for module guidance
cat knowledge.md

# Start coding!
```

---

## Folder Structure

```
businesses/your-tool-name/
├── CLAUDE.md                    # Business context (customize this!)
├── README.md                    # This file (customize for your tool)
├── SPRINT_LOG.md                # Track development progress
├── LEARNINGS.md                 # Document patterns you discover
├── .gitignore                   # Financial-specific gitignore
│
├── .claude/
│   ├── rules/                   # Architecture rules (copied from template)
│   ├── commands/                # Custom slash commands
│   └── agents/                  # Agent configurations
│
├── calculation-engine/          # Core calculation logic
│   ├── README.md                # Module purpose
│   ├── knowledge.md             # Formulas, tax rates, algorithms
│   ├── role.md                  # Module identity/role
│   └── history.md               # Learning history
│
├── document-generator/          # PDF/Excel/CSV generation
│   ├── README.md
│   ├── knowledge.md             # Template formats, styling
│   ├── role.md
│   └── history.md
│
├── data-manager/                # Data storage and retrieval
│   ├── README.md
│   ├── knowledge.md             # Database schemas, queries
│   ├── role.md
│   └── history.md
│
├── _shared/                     # Cross-module shared knowledge
│   ├── README.md
│   ├── tax-rates.md             # Country/region tax rates
│   ├── accounting-standards.md # GAAP, IFRS, etc.
│   ├── currency-data.md         # Exchange rates, formatting
│   └── regulations.md           # Legal compliance requirements
│
├── _meta/                       # Self-improvement intelligence
│   ├── knowledge-graph.md       # Concept relationships
│   ├── validation-rules.md     # Business rule validations
│   └── optimization-log.md      # Performance optimizations
│
├── pipelines/
│   ├── intake/                  # Zero-friction automation
│   │   ├── README.md
│   │   ├── inbox/               # Drop receipts, invoices here
│   │   ├── outbox/              # Processed documents
│   │   └── process-receipts.py  # Automation script
│   │
│   └── export/                  # Export to accounting software
│       ├── README.md
│       └── export-to-quickbooks.py
│
├── archive/
│   ├── trash-can/               # Reversible deletions
│   ├── backups/                 # Quick snapshots
│   └── deprecated/              # Old code
│
├── decisions/                   # Architectural Decision Records
│   ├── 000-template.md
│   └── 001-tax-calculation-strategy.md
│
├── knowledge/                   # Persistent memory
│   ├── MEMORY.md                # Current state (multi-machine continuity)
│   └── patterns.md              # Accumulated learnings
│
└── templates/                   # Document templates
    ├── invoice-template.html
    ├── receipt-template.html
    └── report-template.html
```

---

## Module Templates

### Calculation Engine Module

**Example: invoice-calculator/ for invoice generator**

`invoice-calculator/README.md`:
```markdown
# Invoice Calculator

**Purpose:** Calculates invoice totals including taxes, discounts, and fees.

**Responsibilities:**
- Calculate subtotal from line items
- Apply discounts (percentage or fixed amount)
- Calculate taxes (VAT, sales tax, GST) based on location
- Calculate fees (payment processing, late fees)
- Compute final total

**Dependencies:**
- `_shared/tax-rates.md` — Tax rates by country/region
- `_shared/currency-data.md` — Currency formatting

**Key Algorithms:**
- Tax calculation: `tax = subtotal × tax_rate`
- Discount: `discount = subtotal × discount_percentage` or `fixed_amount`
- Total: `total = subtotal - discount + tax + fees`
```

`invoice-calculator/knowledge.md`:
```markdown
# Invoice Calculator Knowledge Base

## Tax Calculation Rules

### United States
- **Sales Tax:** Varies by state (0% - 10.25%)
- **Calculated on:** Subtotal after discounts
- **Special rules:** Some states exempt services

### European Union
- **VAT:** Standard rate 15% - 27% (varies by country)
- **Calculated on:** Subtotal after discounts
- **Special rules:** Reverse charge for B2B cross-border

### Costa Rica
- **IVA (VAT):** 13%
- **Calculated on:** Subtotal before discounts
- **Special rules:** Basic goods exempt

## Discount Calculation

### Percentage Discount
```python
discount_amount = subtotal * (discount_percentage / 100)
```

### Fixed Amount Discount
```python
discount_amount = min(discount_fixed, subtotal)  # Can't exceed subtotal
```

### Stacked Discounts
Apply sequentially, not cumulatively:
```python
# Wrong: subtotal * (discount1 + discount2)
# Right:
price_after_d1 = subtotal * (1 - discount1)
final_price = price_after_d1 * (1 - discount2)
```

## Currency Handling

### Rounding
- Round to 2 decimal places for most currencies
- Round to 0 decimal places for JPY, KRW (no cents)

### Formatting
- USD: $1,234.56
- EUR: €1.234,56
- GBP: £1,234.56
- CRC: ₡1.234,56
```

---

### Document Generator Module

**Example: document-generator/ for any financial tool**

`document-generator/README.md`:
```markdown
# Document Generator

**Purpose:** Generates professional PDF, Excel, and CSV documents.

**Responsibilities:**
- Render invoices, receipts, reports to PDF
- Export data to Excel for analysis
- Generate CSV for import to other tools
- Apply branding (logos, colors, fonts)

**Tech Stack:**
- Python: ReportLab (PDF), openpyxl (Excel), csv (CSV)
- OR Node.js: Puppeteer (PDF), ExcelJS (Excel)

**Templates:**
- `templates/invoice-template.html`
- `templates/receipt-template.html`
- `templates/report-template.html`
```

`document-generator/knowledge.md`:
```markdown
# Document Generator Knowledge Base

## PDF Generation Best Practices

### Layout
- Page size: A4 (210mm × 297mm) or US Letter (8.5" × 11")
- Margins: 20mm all sides
- Font: Professional (Arial, Helvetica, Times)
- Font size: 10-12pt for body, 16-20pt for headings

### Required Elements (Invoice)
- Company logo and details
- Client details
- Invoice number and date
- Due date
- Line items table
- Subtotal, tax, discount, total
- Payment terms
- Legal disclaimers (if required)

### Branding
- Use company colors (hex codes in config)
- Position logo in header
- Include company slogan/tagline

## Multi-Format Export Pattern

```python
class DocumentExporter:
    def __init__(self, data):
        self.data = data

    def to_pdf(self):
        # Generate PDF
        pass

    def to_excel(self):
        # Generate Excel
        pass

    def to_csv(self):
        # Generate CSV
        pass

    def export(self, format):
        exporters = {
            'pdf': self.to_pdf,
            'excel': self.to_excel,
            'csv': self.to_csv,
        }
        return exporters[format]()
```

## Legal Requirements

### Invoice Requirements (Costa Rica)
- Company name and tax ID (Cédula Jurídica)
- Client name and tax ID
- Invoice number (sequential)
- Date
- Description of goods/services
- Subtotal, IVA (13%), total

### Invoice Requirements (EU)
- VAT number
- Reverse charge notation (if applicable)
- Payment terms
```

---

## Shared Knowledge Layer (`_shared/`)

### tax-rates.md
```markdown
# Tax Rates by Country/Region

## North America

### United States (Sales Tax)
- Alabama: 4.0%
- Alaska: 0.0% (local taxes may apply)
- Arizona: 5.6%
- Arkansas: 6.5%
- California: 7.25%
- ...

### Canada (GST/HST)
- GST (Federal): 5.0%
- HST (Harmonized): 13-15% (varies by province)

### Mexico (IVA)
- Standard: 16%

## Europe (VAT)

- Austria: 20%
- Belgium: 21%
- France: 20%
- Germany: 19%
- Italy: 22%
- Spain: 21%
- UK: 20%

## Latin America

### Costa Rica
- IVA: 13%

### Colombia
- IVA: 19%

## Asia

### Japan
- Consumption Tax: 10%

### Singapore
- GST: 8%

---

**Last Updated:** [Date]
**Source:** [Government websites, reliable references]
```

### currency-data.md
```markdown
# Currency Data

## Formatting Rules

| Currency | Code | Symbol | Decimal Places | Thousands Sep | Decimal Sep |
|----------|------|--------|----------------|---------------|-------------|
| US Dollar | USD | $ | 2 | , | . |
| Euro | EUR | € | 2 | . | , |
| British Pound | GBP | £ | 2 | , | . |
| Japanese Yen | JPY | ¥ | 0 | , | - |
| Costa Rican Colón | CRC | ₡ | 2 | . | , |

## Exchange Rates (Updated Daily)

```python
# Use live API for production (e.g., exchangerate-api.com)
EXCHANGE_RATES = {
    'USD': 1.0,  # Base currency
    'EUR': 0.92,
    'GBP': 0.79,
    'JPY': 149.50,
    'CRC': 520.00,
}
```

## Currency Conversion

```python
def convert_currency(amount, from_currency, to_currency):
    # Convert to USD first
    amount_in_usd = amount / EXCHANGE_RATES[from_currency]

    # Convert to target currency
    amount_in_target = amount_in_usd * EXCHANGE_RATES[to_currency]

    return round(amount_in_target, 2)
```
```

---

## Zero-Friction Automation

### Receipt Processing (Inbox Pattern)

`pipelines/intake/process-receipts.py`:
```python
#!/usr/bin/env python3
"""
Process receipts dropped in inbox (images, PDFs, emails).

OCR text → Extract amounts, dates, vendors → Create expense record → Archive
"""

import os
from pathlib import Path
from datetime import datetime
import pytesseract  # OCR library
from PIL import Image

INBOX = Path("pipelines/intake/inbox")
OUTBOX = Path("pipelines/intake/outbox")
PROCESSED = Path("pipelines/intake/processed")

def extract_text_from_image(image_path):
    """Extract text from receipt image using OCR."""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def parse_receipt(text):
    """Parse receipt text to extract structured data."""
    # Simple pattern matching (improve with ML in future)
    import re

    # Find amounts (e.g., $12.34, €45,67)
    amounts = re.findall(r'[\$€£]\s?\d+[.,]\d{2}', text)

    # Find dates (e.g., 2026-03-08, 03/08/2026)
    dates = re.findall(r'\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}', text)

    # Find vendor (heuristic: first line in uppercase)
    lines = text.split('\n')
    vendor = next((line for line in lines if line.isupper()), "Unknown Vendor")

    return {
        'vendor': vendor,
        'amount': amounts[-1] if amounts else "Unknown",  # Last amount is usually total
        'date': dates[0] if dates else datetime.now().strftime("%Y-%m-%d"),
        'raw_text': text,
    }

def process_inbox():
    """Process all receipts in inbox."""
    for file_path in INBOX.glob("*"):
        if not file_path.is_file():
            continue

        print(f"Processing: {file_path.name}")

        # Extract text (OCR for images, read for text files)
        if file_path.suffix.lower() in ['.jpg', '.jpeg', '.png']:
            text = extract_text_from_image(file_path)
        elif file_path.suffix.lower() == '.txt':
            text = file_path.read_text(encoding='utf-8')
        else:
            print(f"  Unsupported format: {file_path.suffix}")
            continue

        # Parse receipt
        data = parse_receipt(text)
        print(f"  Vendor: {data['vendor']}")
        print(f"  Amount: {data['amount']}")
        print(f"  Date: {data['date']}")

        # Save structured data
        output_file = OUTBOX / f"{file_path.stem}_data.json"
        import json
        output_file.write_text(json.dumps(data, indent=2))

        # Archive original
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

### Example 1: Invoice Generator

**Modules:**
- `invoice-calculator/` — Calculate totals
- `document-generator/` — Generate PDF invoices
- `client-manager/` — Store client details
- `payment-tracker/` — Track payments
- `reminder-service/` — Send payment reminders

**_shared/ knowledge:**
- `tax-rates.md` — Tax rates by country
- `invoice-templates.md` — HTML templates
- `legal-requirements.md` — Required fields per country

**Learnings to discover:**
- Multi-currency handling
- Recurring invoice patterns
- Late fee calculations

---

### Example 2: Expense Tracker

**Modules:**
- `expense-categorizer/` — Categorize expenses automatically
- `receipt-scanner/` — OCR receipt images
- `report-generator/` — Monthly/yearly reports
- `budget-analyzer/` — Compare actual vs budget
- `tax-calculator/` — Calculate deductible expenses

**_shared/ knowledge:**
- `expense-categories.md` — Standard categories
- `tax-deductions.md` — Deductible expense rules
- `exchange-rates.md` — Currency conversion

**Learnings to discover:**
- Automated categorization (ML)
- Duplicate detection
- Split transaction handling

---

### Example 3: Accounting Software

**Modules:**
- `ledger-manager/` — Double-entry bookkeeping
- `reconciliation-engine/` — Bank reconciliation
- `financial-reporter/` — Balance sheet, P&L, cash flow
- `tax-calculator/` — Tax liability calculations
- `audit-logger/` — Compliance audit trail

**_shared/ knowledge:**
- `chart-of-accounts.md` — Standard accounts
- `accounting-standards.md` — GAAP, IFRS
- `tax-regulations.md` — Tax compliance rules

**Learnings to discover:**
- Automated reconciliation algorithms
- Multi-entity consolidation
- Real-time financial reporting

---

## Growth Path

### Phase 1: MVP (Weeks 1-4)
- [ ] Set up calculation-engine module
- [ ] Implement basic document-generator
- [ ] Create invoice/receipt templates
- [ ] Test with sample data

### Phase 2: Learning (Weeks 5-8)
- [ ] Add receipt OCR (inbox automation)
- [ ] Extract patterns to LEARNINGS.md
- [ ] Optimize calculations (caching)
- [ ] Document edge cases

### Phase 3: Scale (Weeks 9-12)
- [ ] Add multi-currency support
- [ ] Implement tax compliance for multiple countries
- [ ] Create backup strategy (Pattern 9)
- [ ] Add ADRs for tax calculation decisions (Pattern 10)

### Phase 4: Contribution (Ongoing)
- [ ] Run `python ../../_template/sync-learnings.py`
- [ ] Share financial patterns with ecosystem
- [ ] Benefit from patterns from other businesses
- [ ] Compound learning

---

## Inherited Patterns (Automatic)

This template includes all 12 patterns from `PATTERNS_DISCOVERED.md`:

✅ **Operations:** Two-PC Continuity, Backup/Rollback Strategy
✅ **Safety:** Autonomous Decisions, Trash-Can Pattern
✅ **Intelligence:** Sprint Log, Chronicle, ADRs
✅ **Architecture:** Linked Documentation, Root Hygiene

---

## Next Steps

1. **Copy this template** to `businesses/your-tool-name/`
2. **Customize CLAUDE.md** with your financial tool context
3. **Update `_shared/tax-rates.md`** with relevant tax rates
4. **Rename modules** based on your tool's purpose
5. **Start building** your first module
6. **Document learnings** in LEARNINGS.md
7. **Run sync** to share patterns with all businesses

---

💰 **Build financial tools that are compliant, accurate, and automated.**

Your tool benefits from all previous businesses. Future businesses will benefit from yours.
