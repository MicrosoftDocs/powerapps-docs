---
title: Use the Visual Studio Code extension (preview)
description: Learn about how to use the Visual Studio Code extension for portals and integrate with Microsoft Power Platform CLI for CI/CD.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/01/2021
ms.subservice: portals
ms.author: nenandw
ms.reviewer: tapanm
contributors:
    - neerajnandwana-msft
    - tapanm-msft
---

# Use the Visual Studio Code extension (preview)

[This article is pre-release documentation and is subject to change.]

## Overview

Visual Studio Code (VS Code) is a lightweight but powerful source code editor that runs on your desktop and is available for Windows, macOS, and Linux. It
comes with built-in support for JavaScript, TypeScript, and Node.js and has a
rich ecosystem of extensions for other languages (such as C++, C\#, Java,
Python, PHP, and Go) and runtimes (such as .NET and Unity). For more information, see [Get
started with VS Code](https://code.visualstudio.com/docs/getstarted/introvideos).

VS Code allows you to extend your capability through
[extensions](https://code.visualstudio.com/docs/introvideos/extend). VS Code
extensions can add more features to the overall experience. With the release of
this feature, you can now use the VS Code extension to work with Power Apps
portals.

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]

### VS Code extension for portals

The **Power Platform Tools** adds the capability to configure portals using
VS Code, and use the built-in Liquid language
[IntelliSense](https://code.visualstudio.com/docs/editor/intellisense) enabling
help with code completion, assistance, and hinting while customizing portals
interface using VS Code. Using the VS Code extension, you can also configure portals through the [portals
support for Microsoft Power Platform CLI](power-apps-cli.md).

![Animation that explains how to install and set Power Platform Tools with file icon theme.](media/vs-code-extension/install-set-icon-theme.gif "Animation that explains how to install and set Power Platform Tools with file icon theme")

## Prerequisites

Before using the VS Code extension for Power Apps portals, you must:

-   Download, install, and configure Visual Studio Code. More information:
    [Download Visual Studio Code](https://code.visualstudio.com/Download)

-   Configure your environment and system for Power Apps portals CI/CD support
    using CLI. More information: [Portals support for Microsoft Power Platform CLI (preview)](power-apps-cli.md)

## Install VS Code extension

After you install Visual Studio Code, you need to install the extension for the
Power Apps portals plug-in for VS Code. 

To install the VS Code extension:

1.  Open Visual Studio Code.

2.  Select ![Extensions icon.](media/vs-code-extension/extensions-symbol.png "Extensions icon") (Extensions) from the left pane.

    ![Select extensions.](media/vs-code-extension/extensions.png "Select extensions")

3.  Select ![Settings icon.](media/vs-code-extension/settings-symbol.png "Settings icon") from the top-right on the extensions pane.

4.  Search for and select **Power Platform Tools**.

    ![Select Power Platform Tools.](media/vs-code-extension/vs-code-extension.png "Select Power Platform Tools")

5.  Select **Install**.

6.  Verify the extension is installed successfully from the status messages.

## Download portals content

To authenticate against a Microsoft Dataverse environment, and to download
portals content, refer to the tutorial [Use Microsoft Power Platform CLI with portals - download portals content](power-apps-cli-tutorial.md#step-3-download-portals-content).

> [!TIP]
> The Power Platform Tools Extension automatically enables using Microsoft Power Platform CLI commands from within VS Code through [Visual Studio Integrated Terminal](https://code.visualstudio.com/docs/editor/integrated-terminal).

## Snippet support

When customizing downloaded content using VS Code, you can now use IntelliSense
for Power Apps portals
[Liquid tags](liquid/liquid-tags.md).

![Snippet with an example of entity liquid tag completion.](media/vs-code-extension/liquid-tag-completion.png "Snippet with an example of entity Liquid tag completio")

## File icons

The VS Code extension for portals automatically identifies and shows icons for
files and folders inside the downloaded portals content.

![List of files in a starter portal with portals-specific file icon theme.](media/vs-code-extension/file-icons.png "List of files in a starter portal with portals-specific file icon theme")

VS Code uses the default [file icon
theme](https://code.visualstudio.com/docs/getstarted/themes#_file-icon-themes)
which doesn’t show portals-specific icons. To view file icons specific
to your portals, you’ll have to update the VS Code instance to use the
portals-specific file icon theme.

To enable a portals-specific file-icon theme:

1.  Open VS Code.

2.  Go to **File** > **Preferences** > **File Icon Theme**

3.  Select the theme for Power Apps Portals Icons.

    ![Select the theme for Power Apps portals icons.](media/vs-code-extension/select-theme-icons.png "Select the theme for Power Apps Portals Icons")

## Live preview

The VS Code extension enables a live preview option to view the portals content page
inside the Visual Studio Code interface during the development
experience.

To see the preview, select ![Preview button.](media/vs-code-extension/preview-symbol.png "Preview button") from the top-right when having an HTML file open in edit mode.

![Page preview.](media/vs-code-extension/page-preview.png "Page preview")

The preview pane opens on the right side of the page being edited.

![A screen with file list, open file in VS Code editor, and a preview on the right-side.](media/vs-code-extension/preview-studio.png "A screen with file list, open file in VS Code editor, and a preview on the right-side")

The preview feature requires that the other files are also open in the same VS Code
session that make up the HTML markup for the preview to show. For example, if
only the HTML file is opened without the folder structure opened using VS Code,
you’ll see the following message.

![Running the contributed command: 'microsoft-powerapps-portals.preview-show' failed.](media/vs-code-extension/preview-failed.png "Error - Running the contributed command: 'microsoft-powerapps-portals.preview-show' failed")

When this problem occurs, open the folder using **File > Open folder** and
select the downloaded portal content folder to open before you try to preview
again.

## Autocomplete

The autocomplete capability in the VS Code extension shows the current context
being edited, and the relevant autocomplete elements through IntelliSense.

![An example of autocomplete for the page template ID.](media/vs-code-extension/auto-complete.png "An example of autocomplete for the page template ID")

## Limitations

The following limitations currently apply to the Power Platform Tools for portals:

- [Snippet support](#snippet-support) and [autocomplete](#autocomplete) features only support limited functionality.
- [Live preview](#live-preview) doesn't support custom themes or Liquid objects.

### See also

[Portals support for Microsoft Power Platform CLI (preview)](power-apps-cli.md)
