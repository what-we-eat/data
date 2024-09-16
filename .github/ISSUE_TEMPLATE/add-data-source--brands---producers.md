---
name: 'Add Data Source: Brands & Producers'
about: Add basic source data for brands/producers.
title: "[Data Source]"
labels: add data
assignees: ''

---

**Certifying Body:**
**Standard:**
**URL:**

**Schema: Brands**

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id | uuid | NO | gen_random_uuid() | |
| created_at | timestamp with time zone | NO | now() | |
| name | text | YES |  | |
| desc | character varying | YES |  | |
| url | character varying | YES |  | |
| logoURL | uuid | YES |  | |
| status | USER-DEFINED | NO | 'active'::brand_status | |
| parent_co | text | YES |  | |

**Schema: Producers**
| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id | uuid | NO | gen_random_uuid() | |
| created_at | timestamp with time zone | NO | now() | |
| url | character varying | YES |  | |
| location_simple | text | YES |  | |
| desc | character varying | YES |  | |
| name | text | YES |  | |
| status | USER-DEFINED | NO | 'active'::producer_status | |
