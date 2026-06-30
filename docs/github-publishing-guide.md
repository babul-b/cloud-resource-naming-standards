# GitHub Publishing Guide

Use this guide after your Medium story is ready.

## 1. Create a public GitHub repository

Create a repository, not a GitHub Project.

A repository is used for code, documentation, examples, and revision history. A GitHub Project is used for planning and tracking tasks.

Suggested repository name:

```text
cloud-resource-naming-standards
```

Suggested description:

```text
Generic cloud resource naming standards with examples, Terraform templates, and validation script.
```

Recommended visibility:

```text
Public
```

## 2. Upload this code

Use either GitHub web upload or Git command line.

### GitHub web upload

1. Open your new GitHub repository.
2. Click **Add file**.
3. Click **Upload files**.
4. Upload all files from this folder.
5. Click **Commit changes**.

### Git command line

```bash
git init
git add .
git commit -m "Initial cloud naming standards sample"
git branch -M main
git remote add origin https://github.com/<your-github-username>/cloud-resource-naming-standards.git
git push -u origin main
```

## 3. Add GitHub link to Medium story

After the repository is public, copy the GitHub URL and add this section to your Medium story:

```markdown
## Source Code

The complete anonymized code and examples for this article are available on GitHub:

https://github.com/<your-github-username>/cloud-resource-naming-standards
```

## 4. Add Medium story link to GitHub repo

After publishing the Medium story, edit `README.md` and replace:

```text
Medium article: `<PASTE_YOUR_MEDIUM_STORY_LINK_HERE>`
```

with your real Medium story link.

Also update `docs/medium-story.md` if you want to keep the published article link there.
