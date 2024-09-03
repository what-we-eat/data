# Database Schema

Last updated: [Current Date]

## Table: [Table Name 1]

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id          | UUID      | NO       | uuid_generate_v4() | Primary key |
| name        | TEXT      | NO       | NULL    | Name of the item |
| created_at  | TIMESTAMP | NO       | now()   | Creation timestamp |
...

## Table: [Table Name 2]

| Column Name | Data Type | Nullable | Default | Description |
|-------------|-----------|----------|---------|-------------|
| id          | UUID      | NO       | uuid_generate_v4() | Primary key |
| [Table1]_id | UUID      | NO       | NULL    | Foreign key to [Table Name 1] |
| value       | INTEGER   | YES      | NULL    | Some value |
...

## Relationships

- `[Table Name 2].[Table1]_id` references `[Table Name 1].id`

## Indexes

- `[Table Name 1]_name_idx` on `[Table Name 1] (name)`

## Notes

- Add any additional notes about the schema here
- Include information about any triggers, functions, or special constraints