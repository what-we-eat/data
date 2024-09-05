# Database Schema

This document provides a detailed overview of the database schema for the Meaningful Bites project.
Note: This schema documentation is automatically updated to reflect any changes in the database structure. Last updated: 2024-09-03

## brand_categories

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id | bigint | NO |  | |
| name | text | NO |  | |

## brands

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id | uuid | NO | gen_random_uuid() | |
| created_at | timestamp with time zone | NO | now() | |
| name | text | YES |  | |
| desc | character varying | YES |  | |
| url | character varying | YES |  | |
| logoURL | uuid | YES |  | |

## certifications

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id | uuid | NO | gen_random_uuid() | |
| created_at | timestamp with time zone | NO | now() | |
| name | text | NO |  | |
| url | character varying | NO |  | |
| regenerative | boolean | NO | FALSE | |
| logoURL | uuid | YES |  | |

## producer_categories

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id | bigint | NO |  | |
| name | text | NO |  | |

## producers

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id | uuid | NO | gen_random_uuid() | |
| created_at | timestamp with time zone | NO | now() | |
| url | character varying | YES |  | |
| location_simple | text | YES |  | |
| desc | character varying | YES |  | |
| name | text | YES |  | |

## rel_brands_categories

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| brand_id | uuid | NO |  | |
| category_id | bigint | NO |  | |

## rel_brands_certifications

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| brand_id | uuid | NO |  | |
| certification_id | uuid | NO |  | |

## rel_producers_categories

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| producer_id | uuid | NO |  | |
| category_id | bigint | NO |  | |

## rel_producers_certifications

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| producer_id | uuid | NO |  | |
| certification_id | uuid | NO |  | |

