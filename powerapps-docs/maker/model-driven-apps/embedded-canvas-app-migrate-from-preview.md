---
title: "Migrate embedded canvas apps on model-driven forms created using the public preview release | MicrosoftDocs"
description: Learn how to migrate your embedded canvas apps created with the public preview release
ms.custom: ""
ms.date: 06/25/2019
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "Aneesmsft"
ms.author: "matp"
manager: "kvivek"
tags: 
  - "Power Apps maker portal impact"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---

# Migrate embedded canvas apps on model-driven forms created using the public preview release

[!INCLUDE [cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

> [!IMPORTANT]
> With the latest release, embedded canvas apps on model-driven forms are generally available. Any embedded canvas apps on model-driven forms created using the public preview release should be migrated to new embedded canvas apps created using the latest release.
> Support for embedded canvas apps on model-driven forms created using the public preview release will soon be deprecated. 

To migrate an embedded canvas app on a model-driven form created using the public preview release to the latest, makers first need to create a new embedded canvas app using the latest release. Makers can then copy over the controls from the existing embedded canvas app to the new one, add required data sources and update broken references, if any. Detailed steps are provided below.

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
2. Open the embedded canvas app created using the public preview release for editing in Power Apps Studio. For steps on editing a canvas app see: [Edit a canvas app](../canvas-apps/edit-app.md).
3. In a new browser tab, follow the steps to [add a new embedded canvas app on a model-driven form](embedded-canvas-app-add-classic-designer.md).
4. Copy the controls from the embedded canvas app created using the public preview release to the new embedded canvas app, one screen at a time using the steps below.
    1. Select the browser tab from Step 2, that has the embedded canvas app, created using the public preview release, open in Power Apps Studio.
    2. Select a screen to copy controls from.
    3. Use **Ctrl + A** to select all controls on the screen.
    4. Use **Ctrl + C** to copy all selected controls.
    5. Select the browser tab from Step 3, that has the new embedded canvas app created using the latest release.
    6. Select a screen or add a new one.
    7. Use **Ctrl + V** to paste the controls on the selected screen.
    8. Repeat the steps to copy each screen.
5. When you are done copying all the screens, select the browser tab from Step 3, that has the new embedded canvas app created using the latest release.
6. Update all the places where the row from the host model-driven form is being accessed. Replace **First(ModelDrivenFormIntegration.Data)** with **ModelDrivenFormIntegration.Item**.
7. Add any missing datasources in the new embedded canvas app.
8. Update all broken references in the new embedded canvas app. 
9. When you are done making changes, select the **File** tab, and then select **Save**.
10. To make your changes available to end-users select **Publish** and then select **Publish this version**.

## Migrating embedded canvas apps on model-driven forms that use a list of rows related to the current (main form) row

In the preview release, to embed a canvas app on a model-driven form, makers had to decide up front if they wanted to pass the current (main form) row as data context or a list of rows related to the current (main form) row. They then had to add the canvas app control to either the column or sub-grid control.

With the latest release, adding an embedded canvas app on a model-driven form is simplified and streamlined to the column only. Makers can still easily access the list of related rows directly in the canvas app using the Common Data Service connector. 

To migrate an embedded canvas app on a model-driven form that uses a list of rows related to the current (main form) row, please follow the steps below.

1. Follow the steps in the section above to migrate embedded canvas apps on model-driven forms created using the public preview release to the latest.
2. Using the Common Data Service connector, add a datasource for the related table to the app. To learn how add a data source in a canvas app please refer to [Add a data connection to a canvas app in Power Apps](../canvas-apps/add-data-connection.md).
3. When using the datasource of the related table for a control such as [Gallery](../canvas-apps/controls/control-gallery.md) or [Data table](../canvas-apps/controls/control-data-table.md), use the **[Filter](../canvas-apps/functions/function-filter-lookup.md)** function to filter the rows to the ones that are related to the current (main form) row. The current (main form) row is available via **ModelDrivenFormIntegration.Item**.
	> [!NOTE]
	> The embedded canvas app has full access to row from the host model-driven form via ModelDrivenFormIntegration.Item. 
	> As an example, to get the value of a column with the name **accountnumber** and display name **Account Number**, you can use **ModelDrivenFormIntegration.Item.accountnumber** or **ModelDrivenFormIntegration.Item.'Account Number'**.
4. With recent updates Microsoft Dataverse now also provides support to use table views as a filter. See this blog post for details: [Improved data source selection and Dataverse views](https://powerapps.microsoft.com/blog/improved-data-source-selection-and-common-data-service-views/). 

## See also
[Embed a canvas app on a model-driven form](embed-canvas-app-in-form.md) <br />
[Add an embedded canvas app on a model-driven form](embedded-canvas-app-add-classic-designer.md) <br />
[Edit a canvas app embedded on a model-driven form](embedded-canvas-app-edit-classic-designer.md) <br />
[Customize the screen size and orientation of a canvas app embedded on a model-driven form](embedded-canvas-app-customize-screen.md) <br />
[Perform predefined actions on the host form from within an embedded canvas app](embedded-canvas-app-actions.md) <br />
[ModelDrivenFormIntegration control's properties and actions](embedded-canvas-app-properties-actions.md) <br />
[Share an embedded canvas app](share-embedded-canvas-app.md) <br />
[Guidelines on working with embedded canvas apps](embedded-canvas-app-guidelines.md) <br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]