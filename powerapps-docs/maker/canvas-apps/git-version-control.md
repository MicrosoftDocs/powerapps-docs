---
title: Co-authoring in canvas apps (experimental)
description: Learn how to enable co-authoring in Power Apps Studio for canvas apps (experimental).
author: gregli-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 11/01/2021
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - gregli-msft
---

# Co-authoring in canvas apps (experimental)

[This article is pre-release documentation and is subject to change.]

> [!IMPORTANT]
> - This is an experimental feature.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]

You can now use Git version control to enable more than one person to edit a canvas app at the same time. With this feature, others won't get locked out of the app while one person is editing it. As changes are made and synchronized, they're automatically merged with other changes, and made available to all others editing the app. This is a first step towards the Microsoft Office style of co-authoring experience.

[Git](https://git-scm.com/) is used as the backing store for this feature. After the initial setup with the connection to Git, any user can use this feature without any additional configuration steps except to authenticate with Git.

Any Git provider can be used with Power Apps Studio&mdash;such as [GitHub](https://github.com/) or [Azure DevOps](https://azure.microsoft.com/services/devops/). Use existing Git tools to see version history, create and manage pull requests, and perform other version control tasks.

> [!NOTE]
> - Before you begin, ensure you read [known limitations](#known-limitations) of this feature. Use of Git is evolving and may change how this feature works. For updates and to share your feedback about this feature, go to [Collaborative authoring](https://powerusers.microsoft.com/t5/Error-Handling/bd-p/PA_Error_Handling).
> - Git version control is managed on a per-app basis. Each app must be individually added to Git version control.

## Enable Git version control

Follow these steps to enable Git version control in your app.

1. Create a new app or open an existing app that you would like to add to Git version control.
1. Open the **Settings** for this app.
1. Select **Upcoming features**.
1. Select **Experimental**.
1. Scroll down to **Show the Git version control setting** and enable the switch below it.
1. You'll see a new **Git version control** item on the left-hand side of the settings.

    :::image type="content" source="media/git-version-control/enable-git.png" alt-text="Swtich to enable Git version control.":::

    > [!TIP]
    > If you don't see the **Show the Git version control setting** experimental feature, your tenant may not have been properly enabled for this feature. In this case, send an email to [PAGit@microsoft.com](mailto:PAGit@microsoft.com) to get this feature listed on your tenant. For any other problem with this feature, go to [Collaborative authoring](https://powerusers.microsoft.com/t5/Error-Handling/bd-p/PA_Error_Handling).

## Connect an app to Git

Follow these steps to connect your app to Git.

1. Select **Git version control** in settings:

    :::image type="content" source="media/git-version-control/connect-git.png" alt-text="Button to start a connection to git for this app.":::

1. Select **Connect** to fill in Git connection information for this app.

    :::image type="content" source="media/git-version-control/connect-info.png" alt-text="Text input boxes to provide git connection information.":::

    - **Git Repository URL**: The URL you would normally use with Git tools. For Azure DevOps, be sure to include the **_git/repo** portion of the URL, such as `https://contoso.visualstudio.com/_git/repo`.  
    - **Branch**: The branch name to use.
    - **Directory**: The directory within the branch to use. You can't store a canvas app at the root of the branch.

    If the branch or directory doesn't exist, you'll be prompted to create them. If the branch and directory already contain a canvas app, the current app will be closed and the existing app loaded from Git.

    Once connected, the connection information will be displayed.

    > [!NOTE]
    > Once connected, the app can't be disconnected from Git currently. The option to disconnect is coming soon.

## Authenticate with Git

Power Apps requires you to use a personal access token instead of your version control provider account password.

Different version control providers have different methods to generate personal access tokens. Follow below instructions to obtain personal access token.

- **GitHub** - [Creating a personal access token](https://docs.github.com/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- **Azure DevOps** - [Use personal access tokens](/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate)
- **Other version control providers**: Any Git provider can be used with Git version control. Check your provider's help for how to create a personal access token.

While editing apps connected to Git, you're prompted for username and password. Enter your **username** and the **access token** in this dialog to authenticate with Git.

:::image type="content" source="media/git-version-control/credentials.png" alt-text="Dialog asks for Git username and access token (as password).":::

> [!NOTE]
> Git credentials are not stored by Power Apps between sessions. If you want, you can use browser settings to save form information for reuse to avoid entering credentials frequently.

## Make changes to the app

After an app is connected to Git, all you have to do is authenticate with Git credentials to open and edit the app. You don't need to go through Git concepts when using this feature to load, edit, save, publish, and share the app.

Use the new synchronize button at the top of the Studio screen (between the **App Checker** and **Undo** buttons) to merge any current changes with what's in Git, and to bring the result into the Studio for further editing.

:::image type="content" source="media/git-version-control/sync.png" alt-text="Button to synchronize changes with the Git repo.":::

> [!IMPORTANT]
> The app will need to be loaded each time there is a merge. If the app is large, this load could take some time.

After being connected to Git, changes are stored in Git rather than in Power Apps. Additional versions won't appear in the Power Apps maker portal.

## Merge results

There's no option to resolve merge conflicts currently. Studio will attempt to merge and fix conflicts automatically through semantic knowledge of the app (for example, the types of objects and other app changes. Since all changes are still stored in Git, you can always retrieve the app changes to reapply if automatic merge doesn't meet your business requirement.

## Publish the app

Apps connected to Git continue to work normally for publishing and user experience with no changes to this process. However, when you publish an app, the app version is stored in Power Apps since Power Apps needs a runnable copy of the app to share with users.

## Pull requests, viewing history, blaming, and other Git features

Working with pull requests or any other Git operations must be done through other Git tools, including the Git provider's website. There's no option available to perform such Git operations to pull or push commits.

Each save or synchronize that includes changes will result in a commit in Git. If other changes occurred in Git, for example by other makers, then there will be additional commits made in order to merge the result of all the changes. No changes will be lost, even if a merge would override an edit. Changes by each maker are stored in Git through commits.

## Known limitations

Since this feature is experimental, we welcome your feedback. Here's a list of known limitations. We plan to remove most of these limitations in future versions.

1. This feature isn't compatible with [code components](../../developer/component-framework/create-custom-controls-using-pcf.md). Don't use this feature with apps that make of use of code components.
1. This feature doesn't work with public Git repository. Use a private repo instead.
1. This feature doesn't work with on-premises Git repositories. The Git repo must be hosted on the web and accessible with username and personal access token.
1. Edits to the same property on the same control aren't merged. The last edit made will win.

## Feedback to the community forum

**Let us know what you think!**  This feature is a first step in a long journey to enable a great team development experience. Visit the [Collaborative authoring](https://powerusers.microsoft.com/t5/Error-Handling/bd-p/PA_Error_Handling) section of the Power Apps community forum for updates and to provide us feedback.
