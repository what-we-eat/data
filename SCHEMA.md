# Database Schema

This document provides a detailed overview of the database schema for the Meaningful Bites project.
Last updated: 2024-09-13

## brand_attributes

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id | uuid | NO | gen_random_uuid() | |
| attribute | character varying | YES |  | |

## brand_certifications

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id | uuid | NO | uuid_generate_v4() | |
| brand_id | uuid | YES |  | |
| certification_level_id | uuid | YES |  | |
| status | USER-DEFINED | NO | 'active'::certification_status | |
| certification_date | date | YES |  | |
| expiration_date | date | YES |  | |

## brands

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

## certification_bodies

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id | uuid | NO | uuid_generate_v4() | |
| name | character varying | NO |  | |
| website_url | character varying | YES |  | |
| logoURL | uuid | YES |  | |

## certification_criteria

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id | uuid | NO | uuid_generate_v4() | |
| certification_standard_id | uuid | YES |  | |
| name | character varying | NO |  | |
| description | text | YES |  | |
| markdown_references | jsonb | YES |  | |
| parent_id | uuid | YES |  | |
| criteria_code | character varying | YES |  | |

## certification_levels

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id | uuid | NO | uuid_generate_v4() | |
| certification_standard_id | uuid | YES |  | |
| name | character varying | NO |  | |
| producer_description | text | YES |  | |
| level_order | integer | NO |  | |
| logoURL | uuid | YES |  | |

## certification_standards

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id | uuid | NO | uuid_generate_v4() | |
| certification_body_id | uuid | YES |  | |
| name | character varying | NO |  | |
| description | text | YES |  | |
| markdown_file_path | character varying | YES |  | |
| markdown_file_version | character varying | YES |  | |

## certifications

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id | uuid | NO | gen_random_uuid() | |
| created_at | timestamp with time zone | NO | now() | |
| name | text | NO |  | |
| url | character varying | NO |  | |
| regenerative | boolean | NO | false | |
| logoURL | uuid | YES |  | |

## producer_categories

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| name | text | NO |  | |
| description | text | YES |  | |
| id | uuid | NO | gen_random_uuid() | |

## producer_certifications

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id | uuid | NO | uuid_generate_v4() | |
| producer_id | uuid | YES |  | |
| certification_level_id | uuid | YES |  | |
| status | USER-DEFINED | NO | 'active'::certification_status | |
| certification_date | date | YES |  | |
| expiration_date | date | YES |  | |

## producers

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id | uuid | NO | gen_random_uuid() | |
| created_at | timestamp with time zone | NO | now() | |
| url | character varying | YES |  | |
| location_simple | text | YES |  | |
| desc | character varying | YES |  | |
| name | text | YES |  | |
| status | USER-DEFINED | NO | 'active'::producer_status | |

## product_categories

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| name | character varying | NO |  | |
| description | text | YES |  | |
| id | uuid | NO | gen_random_uuid() | |

## product_certification_claims

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id | uuid | NO | uuid_generate_v4() | |
| claim_requirements | text | NO |  | |
| claim_text | text | YES |  | |
| minimum_ingredient_percentage | integer | YES |  | |
| maximum_ingredient_percentage | integer | YES |  | |
| certification_standards_id | uuid | YES |  | |

## product_certifications

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id | uuid | NO | uuid_generate_v4() | |
| product_id | uuid | YES |  | |
| certification_level_id | uuid | YES |  | |
| status | USER-DEFINED | NO | 'active'::certification_status | |
| certification_date | date | YES |  | |
| expiration_date | date | YES |  | |
| claim_id | uuid | YES |  | |

## products

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id | uuid | NO | uuid_generate_v4() | |
| brand_id | uuid | YES |  | |
| name | character varying | NO |  | |
| description | text | YES |  | |
| status | USER-DEFINED | NO | 'active'::product_status | |
| url | text | YES |  | |