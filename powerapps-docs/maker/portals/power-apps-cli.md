---
title: Portals support for Power Platform CLI
description: Learn how to work with Power Platform CLI for CI/CD (Continuous Integration/Continuous Deployment) improvements of a portal.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/26/2021
ms.subservice: portals
ms.author: nenandw
ms.reviewer: tapanm
contributors:
    - neerajnandwana-msft
    - tapanm-msft
---

# Portals support for Microsoft Power Platform CLI

Microsoft Power Platform CLI(Command Line Interface) is a simple, single-stop
developer command-line interface that empowers developers and app makers to
create code components.

Microsoft Power Platform CLI tooling is the first step toward a comprehensive application
life-cycle management (ALM) story where the enterprise developers and ISVs can
create, build, debug, and publish their extensions and customizations quickly
and efficiently. For more information, see [What is Microsoft Power Apps
CLI?](../../developer/data-platform/powerapps-cli.md)

With this feature, Microsoft Power Apps portals
supports Microsoft Power Platform CLI to enable CI/CD (Continuous Integration/Continuous
Deployment) of portal configuration. You can now check in the portal
configuration to source control and move portal configuration to any environment
using Microsoft Power Platform CLI.

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
      adx_contentaccesslevel
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
      adx_entitypermission_webrole
   :::column-end:::
   :::column span="":::
      adx_externalidentity
   :::column-end:::
   :::column span="":::
      adx_pagealert
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      adx_pagenotification
   :::column-end:::
   :::column span="":::
      adx_pagetag
   :::column-end:::
   :::column span="":::
      adx_pagetag_webpage
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      adx_pagetemplate
   :::column-end:::
   :::column span="":::
      adx_portallanguage
   :::column-end:::
   :::column span="":::
      adx_publishingstate
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      adx_publishingstatetransitionrule
   :::column-end:::
   :::column span="":::
      adx_publishingstatetransitionrule_webrole
   :::column-end:::
   :::column span="":::
      adx_redirect
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      adx_setting
   :::column-end:::
   :::column span="":::
      adx_shortcut
   :::column-end:::
   :::column span="":::
      adx_sitemarker
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      adx_sitesetting
   :::column-end:::
   :::column span="":::
      adx_webfile
   :::column-end:::
   :::column span="":::
      adx_webfilelog
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      adx_webform
   :::column-end:::
   :::column span="":::
      adx_webformmetadata
   :::column-end:::
   :::column span="":::
      adx_webformsession
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      adx_webformstep
   :::column-end:::
   :::column span="":::
      adx_weblink
   :::column-end:::
   :::column span="":::
      adx_weblinkset
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      adx_webnotificationentity
   :::column-end:::
   :::column span="":::
      adx_webnotificationurl
   :::column-end:::
   :::column span="":::
      adx_webpage
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      adx_webpage_tag
   :::column-end:::
   :::column span="":::
      adx_webpageaccesscontrolrule
   :::column-end:::
   :::column span="":::
      adx_webpageaccesscontrolrule_webrole
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      adx_webpagehistory
   :::column-end:::
   :::column span="":::
      adx_webpagelog
   :::column-end:::
   :::column span="":::
      adx_webrole_systemuser
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      adx_website
   :::column-end:::
   :::column span="":::
      adx_website_list
   :::column-end:::
   :::column span="":::
      adx_website_sponsor
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      adx_websiteaccess
   :::column-end:::
   :::column span="":::
      adx_websiteaccess_webrole
   :::column-end:::
   :::column span="":::
      adx_websitebinding
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      adx_websitelanguage
   :::column-end:::
   :::column span="":::
      adx_webtemplate
   :::column-end:::
   :::column span="":::
      adx_urlhistory
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
|upload|Upload portal website content to the current Dataverse environment. It has the following parameter: <br/> - *path*: Path where the website content is stored (alias: -p) <br/> -*deploymentProfile*: Upload portal data with environment details defined through [profile variables](#use-deployment-profile) in *deployment-profiles/[profile-name].depoyment.yaml* file  |`pac paportal upload --path "C:\portals\starter-portal" --deploymentProfile "profile-name"`|

##### Use deployment profile

The **deploymentProfile** switch allows you to define a set of variables for the environment in YAML format. For example, you can have different deployment profiles (such as dev, test, prod) that have different schema details defined in the profile.

If you're creating test profile, you can create file under **deployment-profiles** with the name "test.deployment.yml" (that is, \<profileTag\>.deployment.yml). And you can run command with tag (\<profileTag\>) to use this profile:

`pac paportal upload --path "C:\portals\starter-portal" --deploymentProfile test`

In this file, you can have the table (entity) name with table ID, list of attributes, and the values that you want to override while uploading the portal configuration using the `deploymentProfile` parameter.

Additionally, you can use the `OS` variable to access the operating system's environment variables.

Here's an example of this "test.deployment.yml"  profile YAML file that has unique schema details:

```yml
adx_sitesetting:
    - adx_sitesettingid: 5ad86900-b5d7-43ac-8359-482529724979
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

## Use the Visual Studio Code extension (Preview)

You can also use VS Code extension **Power Platform VS Code Extension** to benefit built-in Liquid language from IntelliSense, code completion assistance, hinting, and interact with Microsoft Power Platform CLI using VS Code Integrated Terminal. More information: [Use the Visual Studio Code extension (Preview)](vs-code-extension.md)

## Additional considerations

- An error is reported if your file path exceeds the maximum path length limitation. More information: [Maximum path length limitation in Windows](\windows\win32\fileio\maximum-file-path-limitation)
- For duplicate records such as a duplicate web page name, Microsoft Power Platform CLI creates two different folders&mdash;one with the name of the web page, and the other with the same name prefixed with a hash code. For example, "My-page" and "My-page-**hash-code**".

## Next steps

[Tutorial: Use Microsoft Power Platform CLI with portals](power-apps-cli-tutorial.md)

### See also

- [Microsoft Power Platform CLI](../../developer/data-platform/powerapps-cli.md)
- [Use the Visual Studio Code extension (Preview)](vs-code-extension.md)

