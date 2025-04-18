# Boilerplate Collection

A curated collection of reusable boilerplate templates for various development tasks, designed to save time and ensure consistency.

## Overview

This repository serves as a central place for various boilerplate files and template structures commonly used in software development and project setup. The goal is to provide ready-to-use starting points for files like script headers, configuration files, documentation structures, and more, helping you jumpstart your work and maintain standard practices across projects.

## Motivation

-   **Save Time:** Avoid rewriting common files or structures from scratch.
-   **Ensure Consistency:** Promote standardized formats and essential information within files.
-   **Best Practices:** Offer templates incorporating good practices (e.g., comprehensive script headers, standard `.gitignore` files).
-   **Easy Access:** Provide a single location to find and retrieve common boilerplate code and documentation.

## Repository Contents

This collection aims to include templates for various categories, such as:

*   **Scripting:**
    *   Bash Script Headers
    *   Python Script Templates
    *   PowerShell Script Templates
*   **Configuration Files:**
    *   `.gitignore` (for various project types)
    *   `Dockerfile` examples
    *   CI/CD Pipeline configurations (e.g., GitHub Actions, GitLab CI)
    *   Linter/Formatter configurations (e.g., `.eslintrc`, `.prettierrc`)
*   **Documentation:**
    *   README templates (like this one!)
    *   `CONTRIBUTING.md` guidelines
    *   `CODE_OF_CONDUCT.md`
    *   `LICENSE` placeholders
*   **Project Structures:**
    *   Basic web application layouts
    *   Standard library/package structures

*(Feel free to browse the directories to see the currently available templates.)*

## Folder Structure

```
boilerplate-collection/
│
├── .gitignore             # Base .gitignore for this repository
├── LICENSE                # The license under which the collection is distributed
├── README.md              # This README file providing guidance
│
├── config/                # Templates for configuration files
│   ├── ci-cd/             # --> e.g., GitHub Actions workflows, GitLab CI templates
│   ├── docker/            # --> e.g., Dockerfile examples, docker-compose setups
│   ├── git/               # --> e.g., .gitignore templates for various languages/frameworks, .gitattributes
│   └── linters-formatters/ # --> e.g., .eslintrc, .prettierrc, .flake8, editorconfig
│
├── docs/                  # Templates for project documentation
│   ├── ISSUE_TEMPLATE/    # --> GitHub issue templates (bug report, feature request)
│   ├── CONTRIBUTING.md    # --> Template for contribution guidelines
│   ├── CODE_OF_CONDUCT.md # --> Template for a code of conduct
│   └── PULL_REQUEST_TEMPLATE.md # --> Template for GitHub pull requests
│
├── project-structures/    # Boilerplate directory layouts for new projects
│   ├── node-module/       # --> Standard layout for a Node.js package
│   ├── python-package/    # --> Standard layout for a Python package
│   └── web-app-basic/     # --> Basic structure for a generic web application
│
└── scripts/               # Templates related to scripting
    ├── headers/           # --> Reusable script headers
    ├── bash/              # --> Full bash script templates or common snippets
    ├── python/            # --> Python script templates or common snippets
    └── powershell/        # --> PowerShell script templates or common snippets
```
Explanation of Directories:

- **Root Files**: Contains the essential README.md, LICENSE, and potentially a base .gitignore for the collection repository itself.
- `/config`: Houses templates for various configuration needs, categorized by tool or purpose (CI/CD, Docker, Git, Linters/Formatters).
- `/docs`: Contains standard documentation file templates commonly found in software repositories. Includes GitHub-specific templates like issue and PR templates.
- `/project-structures`: Provides complete directory skeletons for different types of projects to quickly scaffold a new repository.
- `/scripts`: Focuses on scripting templates, separating reusable headers from language-specific script bodies or snippets.

## How to Use

There are several ways to use the templates in this collection:

1.  **Copy & Paste:**
    *   Navigate to the template file you need within the repository on GitHub.
    *   Click the "Raw" button to view the raw file content.
    *   Copy the content and paste it into a new file in your own project.
    *   **Important:** Remember to fill in any placeholders with your specific project details.

2.  **Download Files:**
    *   Use tools like `curl` or `wget` to download specific files directly. Replace `[path/to/template.ext]` with the actual path in the repository.
      ```
      # Example using curl
      curl -O https://raw.githubusercontent.com/0xbaha/boilerplate-collection/main/[path/to/template.ext]

      # Example using wget
      wget https://raw.githubusercontent.com/0xbaha/boilerplate-collection/main/[path/to/template.ext]
      ```
    *   Remember to replace `0xbaha` with your actual GitHub username if you fork this repository, or the original owner's username if using theirs.

3.  **Use as a GitHub Template Repository:**
    *   If enabled (repository maintainer can do this in settings), you can click the "Use this template" button near the top of the repository page on GitHub.
    *   This will create a new repository in your account, pre-populated with all the files from this collection, which you can then modify as needed.

## Contributing

Contributions are welcome! If you have a useful boilerplate template that could benefit others, please consider adding it.

1.  **Fork** the repository.
2.  **Create a new branch** for your template (`git checkout -b add-my-cool-template`).
3.  **Add your template** file to an appropriate directory. If a suitable category doesn't exist, feel free to suggest one or create a new directory.
4.  **Ensure your template is well-documented or commented**, explaining its purpose and usage. Remove any sensitive or personal information.
5.  **Commit your changes** (`git commit -m 'Add [Template Name] template'`).
6.  **Push** to the branch (`git push origin add-my-cool-template`).
7.  **Open a Pull Request** explaining the purpose and benefits of your template.

You can also contribute by suggesting new template ideas or improvements by opening an issue.

## License

This collection is distributed under the **MIT** License. Please see the `LICENSE` file in the root of the repository for the full text.

Copyright (c) 2025 Baha

## Support & Contact

If you encounter issues with specific templates, have suggestions for improvements, or want to request a new type of template, please **open an issue** in this repository's issue tracker on GitHub.
