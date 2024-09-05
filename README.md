## Meaningful Bites

An open-source project to bring transparency to the food system.

## Database Schema

Our database schema is documented in [SCHEMA.md](./SCHEMA.md). This file provides a detailed overview of all tables, columns, and relationships in our database.

## Data Overview

For a snapshot of our current data state, including table record counts and last update times, see [DATA_SNAPSHOT.md](./docs/DATA_SNAPSHOT.md).

## Automated Data Updates

We have implemented an automated system to keep our public data snapshot up-to-date:
- Changes in our Supabase database trigger a webhook to our GitHub repository.
- A GitHub Action then fetches the latest data and updates the public snapshot.
- This ensures that the data in this repository is always current and reflects the latest information in our database.

## Contributing

We welcome contributions to our dataset. Please see [CONTRIBUTING.md](./docs/CONTRIBUTING.md) for guidelines on how to propose and make data updates.

## Licensing
The dataset is licensed under the [Creative Commons Attribution 4.0 International License](LICENSE-DATA).