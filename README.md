# GitHub Enterprise Migration Scripts

## Overview

This repository contains a collection of scripts designed for migrating from GitHub Enterprise Cloud to Enterprise Managed Users. These scripts aim to streamline the migration process, making it more efficient and error-free.

## Features

- **Automated Migration:** Simplifies the transition from GitHub Enterprise Cloud to Enterprise Managed Users.
- **Error Handling:** Robust error checking to ensure a smooth migration process.
- **Customization:** Scripts can be modified to fit specific migration needs.

## Getting Started

### Prerequisites

- GitHub Enterprise Cloud account
- GitHub Enterprise Managed Users account
- Basic knowledge of GitHub operations

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ferjosem777/GitHub.git


### Usage
Modify the scripts as needed for your specific migration scenario.
Execute the scripts in your local environment.

### How it Works
Each of the scripts provide a self explanation by name on how they work in two different scenarios:

- Organization Migration as a whole: Creating migration file, locking repos to migrate, populating metadata, and control for migration (logs)
- User migration: Control for metadata and lock users before migration (right after creating the migration file)
- Error handling is provided for every script

### Contributing
To contribute, please use python 3.9 and follow the API calls and instructions from https://docs.github.com/en/rest/migrations?apiVersion=2022-11-28 to interact with the GitHub's REST API

### License
This project is licensed under the MIT License - see the [LICENSE] file for details.


### Contact
This was originally created by Jose Miguel Fernandez Santos-Casas (josemiguel.fernandezsantoscasas@sky.uk)

### Acknowledgements
Special thanks to Paul Crossan and his team, who made this possible.



