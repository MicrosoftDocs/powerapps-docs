---
title: Use Visual Studio Code extension (Preview)
description: Learn about how to use the Visual Studio Code extension for portals and integrate with Power Apps CLI for CI/CD.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 05/27/2021
ms.author: nenandw
ms.reviewer: tapanm
contributors:
    - neerajnandwana-msft
    - tapanm-msft
---

# Use Visual Studio Code extension (Preview)

[This article is pre-release documentation and is subject to change.]

Visual Studio Code (VS Code) is a lightweight but powerful source code editor
which runs on your desktop and is available for Windows, macOS and Linux. It
comes with built-in support for JavaScript, TypeScript and Node.js and has a
rich ecosystem of extensions for other languages (such as C++, C\#, Java,
Python, PHP, Go) and runtimes (such as .NET and Unity). More information: [Get
started with VS Code](https://code.visualstudio.com/docs/getstarted/introvideos)

VS Code allows extending the capability through
[extensions](https://code.visualstudio.com/docs/introvideos/extend). VS Code
extensions can add more features to the overall experience. With the release of
this feature, you can now use the VS Code extension to work with Power Apps
portals.

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]

Benefits

The VS Code extension for portals adds the capability to configure portals using
VS Code, and utilize the built-in Liquid language
[IntelliSense](https://code.visualstudio.com/docs/editor/intellisense) enabling
help with code completion, assistance and hinting while customizing portals
interface using VS Code.

Using the VS Code extension, you can also configure portals through the portals
support for Power Apps CLI. For more information about how to use Power Apps CLI
commands, refer to the supplementary private preview documentation for Power
Apps portals CI/CD support using CLI.

Prerequisites
=============

Before using VS Code extension for Power Apps portals, you must:

-   Download, install and configure Visual Studio Code. More information:
    [Download Visual Studio Code](https://code.visualstudio.com/Download)

-   Configure your environment and system for Power Apps portals CI/CD support
    using CLI. Refer to the supplementary documentation for more information.

Install VS Code extension
=========================

After you install Visual Studio Code, you need to install the extension for
Power Apps portals plugin for VS Code. More information: [Install extensions
from VSIX
file](https://code.visualstudio.com/docs/editor/extension-gallery#_install-from-a-vsix)

To install VS code extension:

1.  Open Visual Studio Code.

2.  Select

    ![Extensions](media/vs-code-extension/6201ef948a1ac2a3f43a0d4fa1594c94.png)

    (Extensions) from the left pane.

    ![Select extensions](media/vs-code-extension/63adb8d05208ebf041ddd10697e6d349.png)

3.  Select

    ![Settings](media/vs-code-extension/1a39a892203164a43d5d0307c39d2dbd.png)

    from the top-right on the extensions pane.

4.  Select **Install from VSIX**.

    ![Install from VSIX option](media/vs-code-extension/96a16f3e07ad86cf9cd581018deb8297.png)

5.  Select the VSIX file.

6.  Verify the extension is installed successfully from the status messages.

    ![Status message for installation of extension: Completed installing Power Platform VS Code Extension.](media/vs-code-extension/8df3620116af7b235afbd296f0d46be8.png)

Download portals content
========================

To authenticate against a Microsoft Dataverse environment, and to download
portals content, refer to the supplementary private preview documentation for
Power Apps portals CI/CD support using CLI.

Snippet support
===============

When customizing downloaded content using VS Code, you can now use IntelliSense
for Power Apps portals
[liquid](https://docs.microsoft.com/powerapps/maker/portals/liquid/liquid-tags)
tags.

![Snippet with an example of entity liquid tag completion.](media/vs-code-extension/d10cd282d55d64fe78a3cdbadbe0cc2c.png)

File icons
==========

The VS Code extension for portals automatically identifies and shows icons for
files and folders inside the downloaded portals content.

![List of files in a starter portal with portals-specific file icon theme.](media/vs-code-extension/3b8cf3c9415298f6ff9cd5182e71a4e4.png)

VS Code uses default [file icon
theme](https://code.visualstudio.com/docs/getstarted/themes#_file-icon-themes)
that by default doesn’t show portals-specific icons. To view file icons specific
to portals, you’ll have to update the VS Code instance to use the
portals-specific file icon theme.

To enable portals-specific file-icon theme:

1.  Open VS Code.

2.  Go to **File** -\> **Preferences** -\> **File Icon Theme**

3.  Select the theme for Power Apps portals icons.

    ![Select the theme for Power Apps portals icons.](media/vs-code-extension/dcb22407219f3c985f514100049f124b.png)

Live preview
============

VS Code extension enables a live preview option to view the portals content page
inside the Visual Studio Code interface as preview during the development
experience.

To see the preview, select

![Preview](media/vs-code-extension/d11cda53e9b3bf49ca433fd728d74a31.png)

from the top-right when having an HTML file open in edit mode.

![Select preview](media/vs-code-extension/9161b2d578954da43f5127fdc69290c2.png)

The preview pane opens on the right side of the page being edited using VS Code.

![A screen with file list, open file in VS Code editor, and a preview on the right-side.](media/vs-code-extension/214645315999e1a69a110a935ce64726.png)

Preview feature requires that have the other files also open in the same VS Code
session that make up the HTML markup for the preview to show. For example, if
only the HTML file is opened without the folder structure opened using VS Code,
you’ll see the following message.

![Running the contributed command: 'microsoft-powerapps-portals.preview-show' failed.](media/vs-code-extension/5ed5bca0a674351ebba7b2942eea17bf.png)

When this happens, open the folder using **File -\> Open folder** in VS Code and
select the downloaded portal content folder to open before you try to preview
again.

Autocomplete
============

The autocomplete capability in the VS Code extension shows the current context
being edited, and the relevant autocomplete elements through IntelliSense.

![An example of autocomplete for the page template ID.](media/vs-code-extension/3267e433850aab6f71fe916b6a33bbb4.png)

Walkthrough
===========

In this example walkthrough, you’ll see how to use VS Code extension for Power
Apps portals to customize portals content.

**NOTE:** The steps to use Power Apps CLI commands for Power Apps portals are
also available in the supplementary documentation.

Visual Studio Code
------------------

To connect to Power Apps portals, and to use Power Apps CLI commands, use
[Visual Studio Code](https://code.visualstudio.com/docs) and the [integrated
terminal](https://code.visualstudio.com/docs/editor/integrated-terminal). The
integrated terminal makes it easy to connect to the Dataverse environment and to
download/change/upload the portals configuration. You can also use Windows
PowerShell instead.

Step 1: Authenticate
--------------------

Before you connect, list, download or upload any changes for a Power Apps
portal, you must authenticate to the Dataverse environment first. For more
information about authentication using Power Apps CLI, read [Power Apps CLI –
Auth](https://docs.microsoft.com/powerapps/developer/data-platform/powerapps-cli#auth).

To authenticate, open Windows PowerShell, and run the following command using
your Dataverse environment URL.

*pac auth create -u [Dataverse URL]*

Example:

*pac auth create -u* <https://contoso-org.crm.dynamics.com>

Follow the prompts of authentication to sign into the environment.

![pac auth create -u ORG-URL](media/vs-code-extension/cdec47c7899bff8395807cc34813668b.png)

Step 2: List available portals
------------------------------

Use the **list** command to list the available Power Apps portals in the
Dataverse environment you connected to using the previous step.

*pac paportal list*

![pac paportal list](media/vs-code-extension/ad4f2864afc933b378a7d93f272973bd.png)

Step 3: Download portals content
--------------------------------

Download portal website content from the connected Dataverse environment.

*pac paportal download --path [PATH] -id [WebSiteId-GUID]*

Example:

*pac paportal download --path c:\\pac-portals\\downloads -id
d44574f9-acc3-4ccc-8d8d-85cf5b7ad141*

For the **id** parameter, use the **WebSiteId** returned from the output of the
previous step.

![pac paportal download --path PATH -id WebSiteId](media/vs-code-extension/728a95c7a58cb14cf7817e877df32d8d.png)

Step 4: Change portals content
------------------------------

Change the configuration using Visual Studio Code and save your changes.

**NOTE:** Ensure you update only the supported entities for use with Power Apps
CLI. More information: [Supported entities](#_Supported_entities)

For example, the default portal page shows the text such as this:

![Sample data preview](media/vs-code-extension/17aa326b8aefb8d05c0a0e10f3920de5.png)

This text is visible from the web page html:

![Highlighted content in HTML format that needs to be edited](media/vs-code-extension/a72eae67d404bc5ac8050e9287bcee4f.png)

You can change this text, and save the changes. Use the preview capability to
preview your changes:

![Edited content in VS Code with a preview on the right-side](media/vs-code-extension/0ce754d2f0e86ba79bbeb6040b65d245.png)

**TIP:** You can change the location of the folder path in PowerShell/integrated
terminal to the downloaded location, and enter “*code .”* to open the folder
directly in Visual Studio Code.

Before you upload your changes, try and use the IntelliSense capability using
liquid tags, and configuration fields/IDs.

Step 5: Upload the changes
--------------------------

After making the required changes, upload them using the following command.

*pac paportal --path [Folder-location]*

Example*:*

*pac paportal upload --path C:\\pac-portals\\downloads\\custom-portal\\*

![pac paportal upload --path PATH](media/vs-code-extension/9aa93277e790c0a6f7e0dd57b919ada5.png)

**NOTE:** Ensure the path for the portals content you entered is correct. By
default, a folder named by the portal (friendly name) is created with downloaded
portals content. For example, if the portal’s friendly name is *custom-portal,*
the path for the above command (--path) should be
*C:\\pac-portals\\downloads\\custom-portal*.

The upload only happens for content that has changed. In this example, since the
change is made to a web page, content is uploaded only for the adx_webpage
entity.

![Upload completed for entity: adx_webpage](media/vs-code-extension/1498e083e14b686c46981d573a6682b9.png)

Step 6: Confirm the changes
---------------------------

To confirm the changes made to the portal webpage:

1.  Clear the [server-side
    cache](https://docs.microsoft.com/powerapps/maker/portals/admin/clear-server-side-cache),
    or use [Sync
    Configuration](https://docs.microsoft.com/powerapps/maker/portals/portal-designer-anatomy)
    by using Power Apps portals Studio.

2.  Browse to the portal webpage to see the change.

![](media/vs-code-extension/46d5ad1e16cb352d2751ff7861078198.png)

>   Highlighted change in text as seen on the portal after browsing the webpage
>   post upload of the changes.

>   This concludes the walkthrough. You can repeat the above steps and change
>   the portals content for other supported entities.

Preview disclaimer
==================

Preview features are features that aren’t complete but are made available on a
“preview” basis so customers can get early access and provide feedback. Preview
features are not supported by Microsoft Support, may have limited or restricted
functionality, aren’t meant for production use, and may be available only in
selected geographic areas.

Copyright
=========

This document is provided "as-is". Information and views expressed in this
document, including URL and other Internet web site references, may change
without notice.

Some examples depicted herein are provided for illustration only and are
fictitious. No real association or connection is intended or should be inferred.

This document does not provide you with any legal rights to any intellectual
property in any Microsoft product. You may copy and use this document for your
internal, reference purposes. This document is confidential and proprietary to
Microsoft. It is disclosed and can be used only pursuant to a non-disclosure
agreement.

© 2021 Microsoft. All rights reserved.

Microsoft is trademark of the Microsoft group of companies. All other trademarks
are property of their respective owners.
