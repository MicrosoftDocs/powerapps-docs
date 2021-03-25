---
title: "Tutorial: Use Power Apps CLI with Power Apps portals for CI/CD | MicrosoftDocs"
description: "Learn about how to use Power Apps CLI with Power Apps portals for CI/CD ."
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 03/29/2021
ms.author: nenandw
ms.reviewer: tapanm
---

# Tutorial: Use Power Apps CLI with portals

[This article is pre-release documentation and is subject to change.]

In this tutorial example, you’ll see how to get started with Power Apps CLI
to update sample portals configuration.

> [!NOTE]
> This tutorial focuses on the required Power Apps CLI commands for
Power Apps portals use. For more information about commands used in Power Apps
CLI, read [common
commands](../../developer/data-platform/powerapps-cli.md#common-commands).

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]

## Download and instal Visual Studio Code

To connect to Power Apps portals, and to use Power Apps CLI commands, use
[Visual Studio Code](https://code.visualstudio.com/docs) and the [integrated
terminal](https://code.visualstudio.com/docs/editor/integrated-terminal). The
integrated terminal makes it easy to connect to the Dataverse environment and to
download/change/upload the portals configuration. You can also use Windows
PowerShell instead.

## Step 1: Authenticate

Before you connect, list, download or upload any changes for a Power Apps
portal, you must authenticate to the Dataverse environment first. For more
information about authentication using Power Apps CLI, go to [Power Apps CLI –
Auth](../../developer/data-platform/powerapps-cli.md#auth).

To authenticate, open Windows PowerShell, and run the following command using
your Dataverse environment URL.

`pac auth create -u [Dataverse URL]`

**Example**

`pac auth create -u https://contoso-org.crm.dynamics.com`

Follow the prompts of authentication to sign into the environment.

![Example of how to authenticate to a Dataverse environment using Power Apps CLI](media/power-apps-cli/auth-create.png "Example of how to authenticate to a Dataverse environment using Power Apps CLI")

## Step 2: List available portals

Use the **list** command to list the available Power Apps portals in the
Dataverse environment you connected to using the previous step.

`pac paportal list`

![Example list of portals](media/power-apps-cli/paportal-list.png "Example list of portals")

## Step 3: Download portals content

Download portal website content from the connected Dataverse environment.

`pac paportal download --path [PATH] -id [WebSiteId-GUID]`

**Example**

`pac paportal download --path c:\pac-portals\downloads -id
d44574f9-acc3-4ccc-8d8d-85cf5b7ad141`

For the **id** parameter, use the **WebSiteId** returned from the output of the
previous step.

![Example of downloading portals content](media/power-apps-cli/paportal-download.png "Example of downloading portals content")

## Step 4: Change portals content

Change the configuration using Visual Studio Code and save your changes.

> [!NOTE]
> Ensure you update only the supported entities for use with Power Apps
CLI. More information: [Supported entities](power-apps-cli.md#supported-entities)

For example, the default portal page shows the text such as this:

![Sample portals page text](media/power-apps-cli/sample-page.png "Sample portals page text")

This text is visible from the web page html:

![Visual Studio Code with text highlighted for change](media/power-apps-cli/vs-code-page.png "Visual Studio Code with text highlighted for change")

You can change this text, and save the changes:

![Updated text using Visual Studio Code](media/power-apps-cli/page-updated.png "Updated text using Visual Studio Code")

> [!TIP]
> You can change the location of the folder path in PowerShell/integrated
terminal to the downloaded location, and enter “*code .”* to open the folder
directly in Visual Studio Code.

## Step 5: Upload the changes

After making the required changes, upload them using the following command.

`pac paportal --path [Folder-location]`

**Example**

`pac paportal upload --path C:\pac-portals\downloads\custom-portal\`

![Starting upload](media/power-apps-cli/upload.png "Starting upload")

> [!NOTE]
> Ensure the path for the portals content you entered is correct. By
default, a folder named by the portal (friendly name) is created with downloaded
portals content. For example, if the portal’s friendly name is *custom-portal,*
the path for the above command (--path) should be
*C:\\pac-portals\\downloads\\custom-portal*.

The upload only happens for content that has changed. In this example, since the
change is made to a web page, content is uploaded only for the adx_webpage
entity.

![Upload completed only for changed content](media/power-apps-cli/upload-completed.png "Upload completed only for changed content")

## Step 6: Confirm the changes

To confirm the changes made to the portal webpage:

1.  Clear the [server-side
    cache](admin/clear-server-side-cache.md),
    or use [Sync
    Configuration](portal-designer-anatomy.md)
    by using Power Apps portals Studio.

2.  Browse to the portal webpage to see the change.

    ![View updated page content](media/power-apps-cli/changed-page.png "View updated page content")

This concludes the tutorial. You can repeat the above steps and change the
portals content for other [supported entities](power-apps-cli.md#supported-entities).

## Next steps

[Overview of portals support for Power Apps CLI](power-apps-cli-tutorial.md)

### See also

[Power Apps CLI](../../developer/data-platform/powerapps-cli.md)
