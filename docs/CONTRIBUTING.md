# Contributing to Meaningful Bites

We're excited that you're interested in contributing to Meaningful Bites! This document outlines the process for contributing to our project, especially regarding data updates and maintenance.

## Table of Contents
1. [Getting Started](#getting-started)
2. [Data Contribution Process](#data-contribution-process)
3. [Proposing Data Updates](#proposing-data-updates)
4. [Submitting Changes](#submitting-changes)
5. [Review Process](#review-process)
6. [Data Quality Guidelines](#data-quality-guidelines)
7. [Setting Up Local Environment](#setting-up-local-environment)
8. [Code of Conduct](#code-of-conduct)

## Getting Started

- Make sure you have a [GitHub account](https://github.com/signup/free)
- Familiarize yourself with our [database schema](./SCHEMA.md)
- Review our [current data snapshot](./DATA_SNAPSHOT.md)

## Data Contribution Process

1. Identify the data you wish to add or update
2. Open an issue describing the proposed changes
3. Fork the repository on GitHub
4. Make the changes in your fork
5. Submit a pull request with your changes

## Proposing Data Updates

When proposing data updates, please:

1. Clearly describe the data you're adding or changing
2. Explain the source of the data
3. Provide context on why this update is valuable
4. Indicate which tables and columns will be affected

## Submitting Changes

1. Create a new branch for your changes: `git checkout -b data-update-description`
2. Make your changes in the appropriate files
3. Commit your changes with a clear commit message
4. Push to your fork and submit a pull request

## Review Process

1. A project maintainer will review your pull request
2. They may ask for additional information or request changes
3. Once approved, your changes will be merged into the main branch

## Data Quality Guidelines

- Ensure data accuracy and reliability
- Provide sources for all new data
- Follow the existing data format and structure
- Update the DATA_SNAPSHOT.md file if you're adding substantial new data

## Setting Up Local Environment

1. Clone the repository: `git clone https://github.com/MeaningfulBites/data.git`
2. Install required dependencies (list any specific requirements)
3. Set up a local Supabase instance for testing (provide instructions or link to them)

## Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

Thank you for contributing to Meaningful Bites!