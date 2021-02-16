---
title: "Overview of Portal Management app | MicrosoftDocs"
description: "Information about Portal Management app."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 02/08/2021
ms.author: sandhan
ms.reviewer: tapanm
---

# Portal Management app overview

> [!NOTE]
> Effective November 2020:
> - Common Data Service has been renamed to Microsoft Dataverse. [Learn more](https://aka.ms/PAuAppBlog)
> - Some terminology in Microsoft Dataverse has been updated. For example, *entity* is now *table* and *field* is now *column*. [Learn more](https://go.microsoft.com/fwlink/?linkid=2147247)
>
> Power Apps portals articles will be updated soon to reflect the latest terminology.

The Portal Management app lets you do advanced configuration actions on your portal. The app is available after the database on Microsoft Dataverse is created successfully.

To open Portal Management app:

1. Go to [Power Apps](https://make.powerapps.com).

1. Select **Apps** from the left pane.

    ![Select Apps](media/configure-portal/studio-apps.png "Select Apps") 

1. Select **Portal Management** app to open.

    ![Select Portal Management app](media/configure-portal/portal-management-app.png "Select Portal Management app")

1. **Portal Management** app opens in a new browser tab.

    ![Portal Management app opened](media/configure-portal/portal-management-app-open.png "Portal Management app opened")

To get started with configuring your portal, select the relevant option from the left pane.

### Browser considerations

If your web browser has any extensions such as ad-blockers, you may see a script error when using the Portal Management app: `One of the scripts for this record has caused an error. For more details, download the log file.` In addition, the downloaded log file may reference this error: `ReferenceError: Web resource method does not exist.` 

![Script error](media/configure-portal/script-error.png "Script error") 

This error occurs for forms such as [Web pages](web-page.md), [Entity Forms](entity-forms.md), [Entity Lists](entity-lists.md), or [Web Form Steps](web-form-steps.md). To resolve this error, disable extensions such as ad-blockers in your browser. You may also use a different browser instead that doesn't have such extensions enabled.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]