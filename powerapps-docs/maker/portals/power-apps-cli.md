---
title: Portals support for Power Platform CLI
description: Learn how to work with Power Platform CLI for CI/CD (Continuous Integration/Continuous Deployment) improvements of a portal.
author: neerajnandwana-msft

ms.topic: conceptual
ms.custom: 
ms.date: 07/27/2022
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - neerajnandwana-msft
    - nickdoelman
---

# Portals support for Microsoft Power Platform CLI

Microsoft Power Platform CLI(Command Line Interface) is a simple, single-stop
developer command-line interface that empowers developers and app makers to
create code components.

Microsoft Power Platform CLI tooling is the first step toward a comprehensive application
life-cycle management (ALM) story where the enterprise developers and ISVs can
create, build, debug, and publish their extensions and customizations quickly
and efficiently. For more information, see [What is Microsoft Power Platform CLI?](../../developer/data-platform/powerapps-cli.md)

With this feature, Microsoft Power Apps portals
supports Microsoft Power Platform CLI to enable CI/CD (Continuous Integration/Continuous
Deployment) of portal configuration. You can now check in the portal
configuration to source control and move portal configuration to any environment
using Microsoft Power Platform CLI.

> [!NOTE]
> This feature is generally available starting with Power Platform CLI version 1.9.8. To learn about installing the latest version, see [Install Microsoft Power Platform CLI](../../developer/data-platform/powerapps-cli.md#standalone-power-platform-cli).

### Why use Microsoft Power Platform CLI for portals development?

With portals support for Microsoft Power Platform CLI, you can now use offline-like capability
for portals customization by making changes to the portals content. And once all
customizations or changes are saved, upload them to the portal. When you
download portals content using Microsoft Power Platform CLI, the content is structured in YAML
and HTML formats making it easy to customize, enabling a pro-development
experience.

Here's a list of features and capabilities that portals benefits from with the
support for Microsoft Power Platform CLI:

#### Ease of use

-   Support for download/upload of portal data to/from the local file system

-   Build on existing Microsoft Power Platform CLI tool.

#### Application lifecycle management (ALM)

-   Track changes to portal configuration within an organization

-   Move configuration files across organizations or tenants

#### Pro-dev and enterprise support

-   Helps integrate seamlessly with any source control tools, such as “git”

-   Easily set up CI/CD pipelines

## Prerequisites

Before using Microsoft Power Platform CLI commands for portals, ensure your portal is
configured to enable support for this feature.

## Install Microsoft Power Platform CLI

For step-by-step instructions, refer to [Install Microsoft Power Platform CLI](../../developer/data-platform/powerapps-cli.md#install-microsoft-power-platform-cli).

## Supported tables

Portals support for Microsoft Power Platform CLI is limited to the tables listed below.

:::row:::
   :::column span="":::
      adx_ad
   :::column-end:::
   :::column span="":::
      adx_adplacement
   :::column-end:::
   :::column span="":::
      adx_blog
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      adx_blogpost
   :::column-end:::
   :::column span="":::
      adx_botconsumer
   :::column-end:::
   :::column span="":::
      adx_communityforum
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      adx_communityforumaccesspermission
   :::column-end:::
   :::column span="":::
      adx_contentsnippet
   :::column-end:::
   :::column span="":::
      adx_entityform
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      adx_entityformmetadata
   :::column-end:::
   :::column span="":::
      adx_entitylist
   :::column-end:::
   :::column span="":::
      adx_entitypermission
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      adx_forumthreadtype
   :::column-end:::
   :::column span="":::
      adx_pagetemplate
   :::column-end:::
   :::column span="":::
      adx_poll
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      adx_polloption
   :::column-end:::
   :::column span="":::
      adx_pollplacement
   :::column-end:::
   :::column span="":::
      adx_portallanguage
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      adx_publishingstate
   :::column-end:::
   :::column span="":::
      adx_redirect
   :::column-end:::
   :::column span="":::
      adx_shortcut
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      adx_sitemarker
   :::column-end:::
   :::column span="":::
      adx_sitesetting
   :::column-end:::
   :::column span="":::
      adx_tag
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      adx_urlhistory
   :::column-end:::
   :::column span="":::
      adx_webfile
   :::column-end:::
   :::column span="":::
      adx_webform
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      adx_webformmetadata
   :::column-end:::
   :::column span="":::
      adx_webformstep
   :::column-end:::
   :::column span="":::
      adx_weblink
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      adx_weblinkset
   :::column-end:::
   :::column span="":::
      adx_webpage
   :::column-end:::
   :::column span="":::
      adx_webpageaccesscontrolrule
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      adx_webrole
   :::column-end:::
   :::column span="":::
      adx_website
   :::column-end:::
   :::column span="":::
      adx_websiteaccess
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      adx_websitebinding (only download)
   :::column-end:::
   :::column span="":::
      adx_websitelanguage
   :::column-end:::
   :::column span="":::
      adx_webtemplate
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      annotation
   :::column-end:::
   :::column span="":::
   :::column-end:::
   :::column span="":::
   :::column-end:::
:::row-end:::

> [!IMPORTANT]
> Custom tables and portal template-specific tables (such as
blog, community, or ideas portal) are not supported for customization using
Microsoft Power Platform CLI .

## Install and verify Microsoft Power Platform CLI for portals

To learn about installing Microsoft Power Platform CLI, go to [Install Microsoft Power Platform CLI](../../developer/data-platform/powerapps-cli.md).

After installing Microsoft Power Platform CLI, open a command-prompt and run *pac* to verify that the output contains “paportal” - the command for
    Power Apps portals.

![Confirm paportal command in Microsoft Power Platform CLI.](media/power-apps-cli/confirm-paportal.png "Confirm paportal command in Microsoft Power Platform CLI")

## Microsoft Power Platform CLI commands for portals

Microsoft Power Platform CLI command for portals is “*paportal”*.

The following sections provide more details about different properties of the “*paportal”* command.

#### Parameters

|Property Name|Description|Example|
|-------------|-----------|-------|
|list|Lists all portal websites from the current Dataverse environment. |`pac paportal list`|
|download|Download portal website content from the current Dataverse environment. It has the following parameters: <br/> - *path*: Path where the website content will be downloaded (alias: -p)<br/> - *webSiteId*: Portal website ID to download (alias: -id)<br/> - *overwrite*: (Optional) true - to overwrite existing content; false - to fail if the folder already has website content (alias: -o)|`pac paportal download --path "C:\portals" --webSiteId f88b70cc-580b-4f1a-87c3-41debefeb902`|
|upload|Upload portal website content to the current Dataverse environment. It has the following parameter: <br/> - *path*: Path where the website content is stored (alias: -p) <br/> -*deploymentProfile*: Upload portal data with environment details defined through [profile variables](#use-deployment-profile) in *deployment-profiles/[profile-name].deployment.yaml* file  |`pac paportal upload --path "C:\portals\starter-portal" --deploymentProfile "profile-name"`|

##### Use deployment profile

The **deploymentProfile** switch allows you to define a set of variables for the environment in YAML format. For example, you can have different deployment profiles (such as dev, test, prod) that have different schema details defined in the profile.

If you're creating test profile, you can create file under **deployment-profiles** with the name "test.deployment.yml" (that is, \<profileTag\>.deployment.yml). And you can run command with tag (\<profileTag\>) to use this profile:

`pac paportal upload --path "C:\portals\starter-portal" --deploymentProfile test`

In this file, you can have the table (entity) name with table ID, list of attributes, and the values that you want to override while uploading the portal configuration using the `deploymentProfile` parameter.

Additionally, you can use the `OS` variable to access the operating system's environment variables.

Here's an example of this "test.deployment.yml"  profile YAML file that has unique schema details:

```yml
adx_sitesetting:
    - adx_sitesettingid: 4ad86900-b5d7-43ac-1234-482529724970
      adx_value: ${OS.FacebookAppId} 
      adx_name: Authentication/OpenAuth/Facebook/AppId
    - adx_sitesettingid: 5ad86900-b5d7-43ac-8359-482529724979
      adx_value: contoso_sample
      adx_name: Authentication/OpenAuth/Facebook/Secret
adx_contentsnippet:
    - adx_contentsnippetid: b0a1bc03-0df1-4688-86e8-c67b34476510
      adx_name: PowerBI/contoso/sales
      adx_value:  https://powerbi.com/group/contoso/sales
```

> [!NOTE]
> To learn about all commands used in CLI in addition to portals, go to [Common commands in Microsoft Power Platform CLI](../../developer/data-platform/powerapps-cli.md#common-commands).

## Manifest files

When you download the website content using `pac paportal download` CLI command, along with downloading the site content it will also generate two manifest files;
- Environment manifest file (org-url-manifest.yml)
- Delete tracking manifest file (manifest.yml)

### Environment manifest file (org-url-manifest.yml)

The environment manifest file is generated every time when the `pac paportal download` command is run. 

After every download, PAC CLI tool reads the existing environment manifest file and updates the entries deleted in the environment, or creates the environment manifest file if it doesn’t exist. 

When you run the `pac paportal upload` command to upload the portal website content. It reads the environment manifest file and identifies the changes made since last download and only uploads the updated content. This helps in optimizing the upload process as only updated website content get uploaded, instead of uploading the all the content on every upload command.

The environment manifest file will be readonly when it connects to the same environment (environment URL matches with file name), to avoid accidental changes. 

### Delete tracking manifest file (manifest.yml)

This file is used for tracking the deleted records from the environment.

When website content is downloaded with `pac paportal download` command, this will add the deleted records from [environment manifest file (org-url-manifest.yml)](#environment-manifest-file-org-url-manifestyml) to manifest.yml file. So, when you upload the website content using the `pac paportal upload` command it will delete the files from the environment (even to a different environment).
This file is not deleted, and it get used regardless which environment you are connected.

> [!NOTE]
> In order to delete the site content records in one environment and also delete the same content records in another environment using the PAC CLI, you will need to run the `pac paportal download` command *before* and *after* the deleting the website record content. The manifest.yml will track these changes and remove the corresponding records in the target environment when the `pac paportal upload` command is run.

## Use the Visual Studio Code extension

You can also use VS Code extension **Power Platform VS Code Extension** to benefit built-in Liquid language from IntelliSense, code completion assistance, hinting, and interact with Microsoft Power Platform CLI using VS Code Integrated Terminal. More information: [Use the Visual Studio Code extension (preview)](vs-code-extension.md)

## Additional considerations

- An error is reported if your file path exceeds the maximum path length limitation. More information: [Maximum path length limitation in Windows](/windows/win32/fileio/maximum-file-path-limitation)
- For duplicate records such as a duplicate web page name, Microsoft Power Platform CLI creates two different folders&mdash;one with the name of the web page, and the other with the same name prefixed with a hash code. For example, "My-page" and "My-page-**hash-code**".

## Next steps

[Tutorial: Use Microsoft Power Platform CLI with portals](power-apps-cli-tutorial.md)

### See also

- [Microsoft Power Platform CLI](../../developer/data-platform/powerapps-cli.md)
- [Use the Visual Studio Code extension (preview)](vs-code-extension.md)

