---
title: Discontinued Git version control for canvas apps (experimental)
description: Retired status for Git version control feature.
author: gregli-msft
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 10/30/2024
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType:
  - maker
contributors:
  - mduelae
  - gregli-msft
  - mkaur-msft
  - gesnaaggarwal
  - angela21k
---

# Discontinued: Git version control for canvas apps (experimental)

> [!IMPORTANT]
>
> - This experimental feature has been retired on October 30, 2024. To improve the team development experience, a future release of source control integration will replace this feature. [Learn more](/power-platform/release-plan/2024wave2/data-platform/source-code-integration).
> - Experimental features aren’t meant for production use and have restricted functionality. Learn more about feature roll out stages [here](/power-platform/release-plan/2024wave2/data-platform/planned-features). 

## Overview

The [Git](https://git-scm.com/) version control feature allowed multiple users to edit a canvas app simultaneously by connecting to a Git repository such as GitHub or Azure DevOps. While connected, changes made in Power Apps Studio would be merged and stored in Git. Due to this feature’s limitations and user needs for more advanced source management techniques, this git version control for canvas apps has been phased out. 
- **Discontinued status**: All new Git connections are disabled for canvas apps.
-	**Alternative options**: Users are encouraged to use two new features in Power Apps Studio to collaborate in real-time with other makers on canvas apps: copresence and coauthoring. [Learn more](/power-apps/maker/canvas-apps/copresence-power-apps-studio).

## Suggested Next Steps
Existing connections will continue to function. However, to avoid disruption we recommend that all users disconnect your existing apps from Git repositories.

:::image type="content" source="media/git-version-control/git-disconnect.jpg" alt-text="Button to disconnect Git connection.":::

While Git version control is no longer enabled for new canvas apps, Power Apps provides alternative ways to manage app changes. You may continue to publish and share apps as before, export versions as backups, and use built-in collaboration features. Additionally, tools for app lifecycle management within the Power Platform are available to support structured version tracking.

## Existing Git connected canvas apps

### Authenticate with Git

> [!NOTE]
>
> - Before you begin, ensure you read [known limitations](#known-limitations) of this feature. Use of Git is evolving and may change how this feature works. 
> - Git version control is managed on a per-app basis. Each app must be individually added to Git version control.
> - Once Git version control is enabled, your app's autosave will be disabled. You will have to manually save or sync your changes.


Power Apps requires you to use a personal access token instead of your version control provider account password. A personal access token is not the same as your password, either for Power Apps or for your Git provider. You must create a personal access token to use this feature. 

Different version control providers have different methods to generate personal access tokens. Follow below instructions to obtain personal access token.

- **GitHub** - [Creating a personal access token](https://docs.github.com/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- **Azure DevOps** - [Use personal access tokens](/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate)
- **Other version control providers**: Any Git provider can be used with Git version control. Check your provider's documentation to learn about how to create a personal access token.

While editing apps connected to Git, you're prompted for username and password. Enter your **username** and the **access token** in the dialog to authenticate with Git.

Git credentials are not stored by Power Apps between sessions. If you want, you can use browser settings to save form information for reuse to avoid entering credentials frequently.

### Make changes to the app

After an app is connected to Git, all you have to do is authenticate with Git credentials to open and edit the app. You don't need to go through Git concepts when using this feature to load, edit, save, publish, and share the app.

Use the new synchronize button at the top of the Studio screen (between the **App Checker** and **Undo** buttons) to merge any current changes with what's in Git, and to bring the result into Studio for further editing.

:::image type="content" source="media/git-version-control/sync.png" alt-text="Button to synchronize changes with the Git repo.":::

> [!NOTE]
> The app will need to be loaded each time there is a merge. If the app is large, this load could take some time.

After being connected to Git, changes are stored in Git rather than in Power Apps. Unpublished versions won't appear in the Power Apps maker portal.

### Merge results

There's no option to resolve merge conflicts currently. Studio will attempt to merge and fix conflicts automatically through semantic knowledge of the app (for example, the types of objects and other app changes). Since all changes are still stored in Git, you can always retrieve the app changes to reapply if automatic merge doesn't meet your business requirement.

### Publish the app

Apps connected to Git continue to work normally for publishing and user experience with no changes to this process. When you publish an app, the app version is stored in Power Apps since Power Apps needs a runnable copy of the app to share with users.

### Pull requests, viewing history, blaming, and other Git features

Working with pull requests or any other Git operations must be done through other Git tools, including the Git provider's website. There's no option available to perform such Git operations to pull or push commits.

Each save or synchronize that includes changes will result in a commit in Git. If other changes occurred in Git, for example by other makers, then there will be additional commits made in order to merge the results of all the changes. No changes will be lost, even if a merge would override an edit. Changes by each maker are stored in Git through commits.

## Known limitations

Since this feature is experimental, we welcome your feedback. The following lists known limitations.

- This feature isn't compatible with [code components](../../developer/component-framework/create-custom-controls-using-pcf.md). Don't use this feature with apps that make of use of code components.
- This feature isn't compatible with on-premises Git repositories. The Git repo must be hosted on the web and accessible with username and personal access token.
- Edits to the same property on the same control aren't merged. The last edit made will win.
- You can't restore a canvas app to a previous version using the steps described in [Restore an app](restore-an-app.md) article. Instead, you'll have to use Git for restoring the app to a previous version. For more information, see the following resources:
  - [git-revert](https://git-scm.com/docs/git-revert)
  - [Reverting a commit](https://docs.github.com/desktop/contributing-and-collaborating-using-github-desktop/managing-commits/reverting-a-commit)
  - [Undo changes](/azure/devops/repos/git/undo?view=azure-devops&tabs=command-line&preserve-view=true)
- Connecting multiple apps to the same git directory may cause problems. This includes making copies of your app and exporting and importing them.
- Any existing files in the repository with names exceeding 180 characters in length may cause problems when connecting. We recommend using a dedicated repository for Git connected apps.
- Selecting **Close** on the **File** menu may appear to delete your customizations in the app. However, customizations are not deleted. Refresh the page to see all customizations again.
- If you open a non git connected app (for example, **App A**) from within a git connected app (for example, **App B**) (File > Open) and try to connect **App A** to a repository, **App A**'s git version control parameters will be the same as **App B**. When this happens, refresh your page and then try connecting **App A** to the repository again.
- This feature does not support renaming of custom components.
- If you see a message about the app being open for editing by another user, ask the referenced user to refresh the app. Afterwards, refresh your app to remove the lock.
- This feature is not compatible with [Test Studio tests](test-studio.md) and [custom pages for model-driven apps](../model-driven-apps/model-app-page-overview.md)
- This feature does not support the use of personal access tokens that are authorized for use with SAML single sign-on.

## Feedback to the community forum

For questions or additional support, visit the [Power Apps community forum](https://powerusers.microsoft.com/t5/Power-Apps-Community/ct-p/PowerApps1).
