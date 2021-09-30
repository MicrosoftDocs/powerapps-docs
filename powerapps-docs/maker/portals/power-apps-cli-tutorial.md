---
title: Tutorial on how to use Power Apps CLI with portals
description: This page provides a walk-through with examples for how to use Power Apps CLI with Power Apps portals for CI/CD (Continuous Integration/Continuous Deployment).
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 05/27/2021
ms.subservice: portals
ms.author: nenandw
ms.reviewer: tapanm
contributors:
    - neerajnandwana-msft
    - tapanm-msft
---

# Tutorial: Use Microsoft Power Platform CLI with portals

[This article is pre-release documentation and is subject to change.]

In this tutorial example, you’ll see how to get started with Microsoft Power Platform CLI to update sample portals configuration.

> [!NOTE]
> This tutorial focuses on the required Microsoft Power Platform CLI commands for
Power Apps portals use. For more information about commands used in Power Apps
CLI, read [Common
commands](../../developer/data-platform/powerapps-cli.md#common-commands).

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]

## Download and install Visual Studio Code

To connect to Power Apps portals, and to use Microsoft Power Platform CLI commands, use
[Visual Studio Code](https://code.visualstudio.com/docs) and the [integrated
terminal](https://code.visualstudio.com/docs/editor/integrated-terminal). The
integrated terminal makes it easy to connect to the Dataverse environment and to
download, change, and upload the portals configuration. You can also use Windows
PowerShell instead.

## Step 1: Authenticate

Before you connect, list, download, or upload any changes for a Power Apps
portal, you must authenticate to the Dataverse environment first. For more
information about authentication using Microsoft Power Platform CLI, go to [Microsoft Power Platform CLI –
Auth](../../developer/data-platform/cli/reference/auth-command.md).

To authenticate, open Windows PowerShell and run the following command using
your Dataverse environment URL:

`pac auth create -u [Dataverse URL]`

**Example**

`pac auth create -u https://contoso-org.crm.dynamics.com`

Follow the prompts of authentication to sign in to the environment.

![Example of how to authenticate to a Dataverse environment using Microsoft Power Platform CLI.](media/power-apps-cli/auth-create.png "Example of how to authenticate to a Dataverse environment using Microsoft Power Platform CLI")

## Step 2: List available portals

Use the **list** command to list the available Power Apps portals in the
Dataverse environment you connected to in the previous step.

`pac paportal list`

![Example list of portals.](media/power-apps-cli/paportal-list.png "Example list of portals")

## Step 3: Download portals content

Download portal website content from the connected Dataverse environment.

`pac paportal download --path [PATH] -id [WebSiteId-GUID]`

**Example**

`pac paportal download --path c:\pac-portals\downloads -id
d44574f9-acc3-4ccc-8d8d-85cf5b7ad141`

For the **id** parameter, use the **WebSiteId** returned from the output of the
previous step.

![Example of downloading portals content.](media/power-apps-cli/paportal-download.png "Example of downloading portals content")

## Step 4: Change portals content

Change the configuration using Visual Studio Code and save your changes.

> [!NOTE]
> Ensure you update only the supported tables for use with Power Apps
CLI. For more information, see [Supported tables](power-apps-cli.md#supported-tables).

For example, the default portal page shows text such as this:

![Sample portals page text.](media/power-apps-cli/sample-page.png "Sample portals page text")

This text is visible from the webpage html:

![Visual Studio Code with text highlighted for change.](media/power-apps-cli/vs-code-page.png "Visual Studio Code with text highlighted for change")

You can alter this text and save the changes:

![Updated text using Visual Studio Code.](media/power-apps-cli/page-updated.png "Updated text using Visual Studio Code")

> [!TIP]
> You can change the location of the folder path in PowerShell/integrated
terminal to the downloaded location, and enter “*code .”* to open the folder
directly in Visual Studio Code.

## Step 5: Upload the changes

After making the required changes, upload them using the following command:

`pac paportal --path [Folder-location]`

**Example**

`pac paportal upload --path C:\pac-portals\downloads\custom-portal\`

![Starting upload.](media/power-apps-cli/upload.png "Starting upload")

> [!NOTE]
> Ensure the path for the portals content you entered is correct. By
default, a folder named by the portal (friendly name) is created with downloaded
portals content. For example, if the portal’s friendly name is *custom-portal,*
the path for the above command (--path) should be
*C:\\pac-portals\\downloads\\custom-portal*.

The upload only happens for content that's been changed. In this example, since the
change is made to a webpage, content is uploaded only for the adx_webpage
table.

![Upload completed only for changed content.](media/power-apps-cli/upload-completed.png "Upload completed only for changed content")

## Step 6: Confirm the changes

To confirm the changes made to the portal webpage:

1.  Clear the [server-side
    cache](admin/clear-server-side-cache.md),
    or use [Sync
    Configuration](portal-designer-anatomy.md)
    by using Power Apps portals Studio.

2.  Browse to the portal webpage to see the change.

    ![View updated page content.](media/power-apps-cli/changed-page.png "View updated page content")

This concludes the tutorial. You can repeat the above steps and change the
portals content for other [supported tables](power-apps-cli.md#supported-tables).

## Next steps

[Overview of portals support for Microsoft Power Platform CLI](power-apps-cli-tutorial.md)

### See also

- [Microsoft Power Platform CLI](../../developer/data-platform/powerapps-cli.md)
- [Use the Visual Studio Code extension (preview)](vs-code-extension.md)

