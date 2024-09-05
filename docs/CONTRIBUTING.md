# Contributing to Meaningful Bites

We're excited that you're interested in contributing to Meaningful Bites! This document outlines the process for contributing to our project, especially regarding data updates and maintenance.

## Table of Contents
1. [Getting Started](#getting-started)
2. [Data Contribution Process](#data-contribution-process)
3. [Proposing Data Updates](#proposing-data-updates)
4. [Submitting Changes](#submitting-changes)
5. [Review Process](#review-process)
6. [Data Quality Guidelines](#data-quality-guidelines)
7. [Understanding the Automated Update Process](#understanding-the-automated-update-process)
8. [Code of Conduct](#code-of-conduct)

## Getting Started

- Make sure you have a [GitHub account](https://github.com/signup/free)
- Familiarize yourself with our [database schema](./SCHEMA.md)
- Review our [current data snapshot](./DATA_SNAPSHOT.md)

## Data Contribution Process

1. Identify the data you wish to add or update
2. Open an issue describing the proposed changes
3. If approved, a project maintainer will make the changes in the Supabase database
4. The automated system will update the public snapshot in this repository

## Proposing Data Updates

When proposing data updates, please:

1. Clearly describe the data you're adding or changing
2. Explain the source of the data
3. Provide context on why this update is valuable
4. Indicate which tables and columns will be affected

## Submitting Changes

As we now use an automated system to update the public snapshot, direct changes to the repository are not accepted. Instead:

1. Open an issue with your proposed changes
2. Discuss the changes with the project maintainers
3. If approved, a maintainer will implement the changes in the Supabase database

## Review Process

1. A project maintainer will review your proposed changes
2. They may ask for additional information or clarification
3. Once approved, the changes will be made in the Supabase database
4. The automated system will update the public snapshot in this repository

## Data Quality Guidelines

- Ensure data accuracy and reliability
- Provide sources for all new data
- Follow the existing data format and structure
- The DATA_SNAPSHOT.md file will be automatically updated when changes are made

## Understanding the Automated Update Process

Our project uses an automated system to keep the public data snapshot up-to-date:

1. Changes in the Supabase database trigger a webhook to this GitHub repository
2. A GitHub Action is triggered, which fetches the latest data from Supabase
3. The Action updates the files in the `public_data/snapshots/latest/` directory
4. These changes are automatically committed and pushed to the repository

This system ensures that the public snapshot always reflects the current state of our database.

## Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

Thank you for contributing to Meaningful Bites!