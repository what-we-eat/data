# Database Schema

Last updated: 2024-09-03

## Table: brand_categories

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id | bigint | NO |  | |
| name | text | NO |  | |

## Table: brands

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id | uuid | NO | gen_random_uuid() | |
| created_at | timestamp with time zone | NO | now() | |
| name | text | YES |  | |
| desc | character varying | YES |  | |
| url | character varying | YES |  | |
| logoURL | uuid | YES |  | |

## Table: certifications

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id | uuid | NO | gen_random_uuid() | |
| created_at | timestamp with time zone | NO | now() | |
| name | text | NO |  | |
| url | character varying | NO |  | |
| regenerative | boolean | NO | FALSE | |
| logoURL | uuid | YES |  | |

## Table: producer_categories

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id | bigint | NO |  | |
| name | text | NO |  | |

## Table: producers

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id | uuid | NO | gen_random_uuid() | |
| created_at | timestamp with time zone | NO | now() | |
| url | character varying | YES |  | |
| location_simple | text | YES |  | |
| desc | character varying | YES |  | |
| name | text | YES |  | |

## Table: rel_brands_categories

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| brand_id | uuid | NO |  | |
| category_id | bigint | NO |  | |

## Table: rel_brands_certifications

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| brand_id | uuid | NO |  | |
| certification_id | uuid | NO |  | |

## Table: rel_producers_categories

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| producer_id | uuid | NO |  | |
| category_id | bigint | NO |  | |

## Table: rel_producers_certifications

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| producer_id | uuid | NO |  | |
| certification_id | uuid | NO |  | |

