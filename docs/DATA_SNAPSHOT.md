# Data Snapshot

This file provides an overview of the current state of data in the Meaningful Bites project database. Last updated: 2024-09-03 15:28:36

## Table Summaries

### Producers
- Total Records: 1
- Fields: id, created_at, url, location_simple, desc, name
- Sample Data (first 5 rows):

| id | created_at | url | location_simple | desc | name |
|---|---|---|---|---|---|
| c27bb743-cb54-4bc9-a775-27594b94edcc | 2024-08-29T18:58:10.034858+00:00 | https://tablascreek.com/ | Paso Robles, California | Tablas Creek is a pioneer of California's Rhone movement, and the world's first Regenerative Organic Certified™ vineyard. | Tablas Creek Vineyard |

### Brands
- Total Records: 1
- Fields: id, created_at, name, desc, url, logoURL
- Sample Data (first 5 rows):

| id | created_at | name | desc | url | logoURL |
|---|---|---|---|---|---|
| 70356494-cbc2-4f76-b3ef-424bcfb9453b | 2024-08-29T20:23:27.452881+00:00 | Ancient Nutrition | What began as a mission to create high-quality supplements has grown into a steadfast commitment to transform the way we grow our food. | https://ancientnutrition.com/ | 1921cdda-bc22-4bae-9f8a-d479cbe57c3a |

### Certifications
- Total Records: 13
- Fields: id, created_at, name, url, regenerative, logoURL
- Sample Data (first 5 rows):

| id | created_at | name | url | regenerative | logoURL |
|---|---|---|---|---|---|
| 3953085d-fb84-4799-8126-34f6d543c316 | 2024-08-29T17:36:08.700737+00:00 | Regenerative Organic Alliance | https://regenorganic.org/ | True | 67ddc528-daa0-44b1-9224-e3462fa9e40a |
| 18866dec-4291-48e0-96a5-d2925398a49e | 2024-08-29T17:36:46.228076+00:00 | Regenefied | https://regenified.com/ | True | 91efea90-3e73-48bc-860f-3cad40fbbbb8 |
| 610e0081-0f97-488e-a621-4de64ca9bcfe | 2024-08-29T17:37:18.676901+00:00 | Certified Regenerative by AGW | https://agreenerworld.org/certifications/certified-regenerative/ | True | d9bd6abf-262b-44eb-bef6-1e0797c846fa |
| c638100a-5f15-4894-824e-0c18435b50a8 | 2024-08-29T17:44:29.024245+00:00 | 1% For The Planet | https://www.onepercentfortheplanet.org/ | False | None |
| 106ce2a7-0ffe-4dec-9148-7cb780c3cb79 | 2024-08-29T17:44:29.024245+00:00 | Audubon Certified | https://www.audubon.org/news/for-consumers-and-conservationists-faqs-conservation-ranching | False | da7434b0-078d-498a-97a1-6e6d188d6439 |

## Notes
- This snapshot represents a sample of the data. For full data access, please refer to the Supabase database.
- Data is subject to change. Regular updates to this snapshot are recommended.
