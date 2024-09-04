---
title: Use Git version control to edit canvas apps (experimental)
description: Learn how to connect to a Git repository and allow multiple users to work on the app at the same time (experimental).
author: gregli-msft
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 09/03/2024
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType:
  - maker
contributors:
  - mduelae
  - gregli-msft
  - mkaur-msft
  - gesnaaggarwal
---

# Use Git version control to edit canvas apps (experimental)

[This article is pre-release documentation and is subject to change.]

> [!IMPORTANT]
>
> - This experimental feature is discontinued and will be replaced with the source control integration feature. More information: [Source code integration](/power-platform/release-plan/2024wave1/data-platform/source-code-integration)
> - This feature is being rolled out and depending on your region, it may not be available for your tenant yet. Check the experimental switch described in [Enable Git version control](#enable-git-version-control) to know if the feature is available in your tenant.
> - This is an experimental feature. It is disabled by default and must be [enabled](#enable-git-version-control) before use.
> - Experimental features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

You can use the experimental Git version control feature to enable more than one person to edit a canvas app at the same time. With this feature, others won't get locked out of the app while one person is editing it. As changes are made and synchronized, they're automatically merged with other changes, and made available to all others editing the app. 


[Git](https://git-scm.com/) is used as the backing store for this feature. After the initial setup with the connection to Git, any user can use this feature without any extra configuration steps except to authenticate with Git.

Any Git provider can be used with Power Apps Studio&mdash;such as [GitHub](https://github.com/) or [Azure DevOps](https://azure.microsoft.com/services/devops/). Use existing Git tools to see version history, create and manage pull requests, and do other version control tasks.

> [!NOTE]
>
> - Before you begin, ensure you read [known limitations](#known-limitations) of this feature. Use of Git is evolving and may change how this feature works. For updates and to share your feedback about this feature, vist the [Power Apps community forum](https://powerusers.microsoft.com/t5/Power-Apps-Community/ct-p/PowerApps1).
> - Git version control is managed on a per-app basis. Each app must be individually added to Git version control.
> - Once git version control is enabled, your app's autosave will be disabled. You will have to manually save or sync your changes.

## Enable Git version control

Follow these steps to enable Git version control in your app.

1. Create a new app or open an existing app that you would like to add to Git version control.
1. Select **Settings** in Power Apps Studio.
1. Select **Upcoming features**.
1. Select **Experimental**.
1. Scroll down to **Show the Git version control setting** and turn it to **On**.
1. You'll see a new **Git version control** item on the left-hand side of the settings pane.

   :::image type="content" source="media/git-version-control/enable-git.png" alt-text="Swtich to enable Git version control.":::

   > [!TIP]
   > For any other problem with this feature, visit the [Power Apps community forum](https://powerusers.microsoft.com/t5/Power-Apps-Community/ct-p/PowerApps1).

## Connect an app to Git

Follow these steps to connect your app to Git.

1. Select **Settings** in Power Apps Studio.

1. Select **Git version control**.

   :::image type="content" source="media/git-version-control/connect-git.png" alt-text="Button to start a connection to git for this app.":::

1. Select **Connect**, and fill-in Git connection information for this app.

   :::image type="content" source="media/git-version-control/connect-info.png" alt-text="Text input boxes to provide git connection information.":::

   - **Git Repository URL**: The URL you would normally use with Git tools. For Azure DevOps, be sure to include the **/\_git/repo** portion of the URL, such as `https://contoso.visualstudio.com/_git/repo`.
   - **Branch**: The branch name to use.
   - **Directory**: The directory within the branch to use. You can't store a canvas app at the root of the branch.

   You'll be prompted to create the branch or directory if it doesn't exist. If the branch and directory already contains a canvas app, the current app will be closed and the existing app will be loaded from Git.

   Once connected, the connection information will be displayed.

## Authenticate with Git

Power Apps requires you to use a personal access token instead of your version control provider account password.

> [!NOTE]
> A personal access token is not the same as your password, either for Power Apps or for your Git provider. You must create a personal access token to use this feature.

Different version control providers have different methods to generate personal access tokens. Follow below instructions to obtain personal access token.

- **GitHub** - [Creating a personal access token](https://docs.github.com/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- **Azure DevOps** - [Use personal access tokens](/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate)
- **Other version control providers**: Any Git provider can be used with Git version control. Check your provider's documentation to learn about how to create a personal access token.

While editing apps connected to Git, you're prompted for username and password. Enter your **username** and the **access token** in this dialog to authenticate with Git.

:::image type="content" source="media/git-version-control/credentials.png" alt-text="Dialog asks for Git username and access token (as password).":::

> [!NOTE]
> Git credentials are not stored by Power Apps between sessions. If you want, you can use browser settings to save form information for reuse to avoid entering credentials frequently.

## Make changes to the app

After an app is connected to Git, all you have to do is authenticate with Git credentials to open and edit the app. You don't need to go through Git concepts when using this feature to load, edit, save, publish, and share the app.

Use the new synchronize button at the top of the Studio screen (between the **App Checker** and **Undo** buttons) to merge any current changes with what's in Git, and to bring the result into Studio for further editing.

:::image type="content" source="media/git-version-control/sync.png" alt-text="Button to synchronize changes with the Git repo.":::

> [!IMPORTANT]
> The app will need to be loaded each time there is a merge. If the app is large, this load could take some time.

After being connected to Git, changes are stored in Git rather than in Power Apps. Unpublished versions won't appear in the Power Apps maker portal.

## Merge results

There's no option to resolve merge conflicts currently. Studio will attempt to merge and fix conflicts automatically through semantic knowledge of the app (for example, the types of objects and other app changes). Since all changes are still stored in Git, you can always retrieve the app changes to reapply if automatic merge doesn't meet your business requirement.

## Publish the app

Apps connected to Git continue to work normally for publishing and user experience with no changes to this process. When you publish an app, the app version is stored in Power Apps since Power Apps needs a runnable copy of the app to share with users.

## Pull requests, viewing history, blaming, and other Git features

Working with pull requests or any other Git operations must be done through other Git tools, including the Git provider's website. There's no option available to perform such Git operations to pull or push commits.

Each save or synchronize that includes changes will result in a commit in Git. If other changes occurred in Git, for example by other makers, then there will be additional commits made in order to merge the results of all the changes. No changes will be lost, even if a merge would override an edit. Changes by each maker are stored in Git through commits.

## Known limitations

Since this feature is experimental, we welcome your feedback. The following lists known limitations. We plan to remove most of these limitations in future versions.

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

**Let us know what you think!** This feature is a first step in a long journey to enable a great team development experience. Visit the [Power Apps community forum](https://powerusers.microsoft.com/t5/Power-Apps-Community/ct-p/PowerApps1) for updates and to provide feedback.
