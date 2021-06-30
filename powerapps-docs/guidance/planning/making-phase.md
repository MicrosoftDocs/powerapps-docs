---
title:  Making Phase - Planning a Power Apps project | Microsoft Docs
description: You've now planned and designed your app. The next step is to actually make it. This article provides an overview of steps for creating canvas apps and model-driven apps.
author: taiki-yoshida
ms.service: powerapps
ms.topic: conceptual
ms.custom: guidance
ms.date: 06/16/2020
ms.author: tayoshi
ms.reviewer: kathyos

---

# Making phase

You have now planned and designed your app. The next step is to actually make it.

> [!TIP]
> In addition to the links below, you'll find a curated collection of links
at [Microsoft Power Platform: Learning Resources](https://aka.ms/PowerPlatformResources).

## Basic steps for making canvas apps

The following are the basic steps for creating canvas apps.

1. Set up the data source.

   - [Set up tables](/powerapps/maker/data-platform/data-platform-create-entity) (when using Microsoft Dataverse).

   - Set up tables (when using a database).

   - [Set up lists](https://support.office.com/article/create-a-list-in-sharepoint-0d397414-d95f-41eb-addd-5e6eff41b083)
        (when using SharePoint).

2. [Create a new
    app](../../maker/canvas-apps/getting-started.md#build-an-app).

3. [Add
    connectors](../../maker/canvas-apps/add-manage-connections.md).

4. [Create
    the following screens](../../maker/canvas-apps/add-screen-context-variables.md):

   - Home screen

   - List view

   - View form

   - Edit form

5. [Create Power Automate flows](/power-automate/get-started-logic-flow).

## Basic steps for making model-driven apps

The following are the basic steps for creating model-driven apps.

1. Create a [solution](../../maker/model-driven-apps/distribute-model-driven-app.md).

2. Set up data models by defining
    [entities](../../maker/data-platform/entity-overview.md)
    and [fields](../../maker/data-platform/fields-overview.md).

3. Set up [security roles](/power-platform/admin/security-roles-privileges).

4. Create a site map by setting up a new [model-driven app](../../maker/model-driven-apps/build-first-model-driven-app.md).

5. Customize [forms](../../maker/model-driven-apps/create-design-forms.md)
    and [views](../../maker/model-driven-apps/create-edit-views.md).

6. Set up [business process flows](/power-automate/business-process-flows-overview).

7. Set up [business rules](../../maker/model-driven-apps/create-business-rules-recommendations-apply-logic-form.md).

8. Set up [Power Automate flows](/power-automate/connection-cds).

More information: [Understand model-driven app components](../../maker/model-driven-apps/model-driven-app-components.md)

## Developing solutions collaboratively

When developing your solutions with multiple app makers, collaboration techniques depend on which type of application you're making.

### Canvas apps

You can develop canvas apps collaboratively by using [Power Apps components](../../maker/canvas-apps/create-component.md)&mdash;a
set of reusable building blocks&mdash;and also by using component libraries, which are a
repository you can use to share and collaborate with others on Power Apps
components you've created. More information: [Collaborative Development for PowerApps Canvas Apps](https://powerapps.microsoft.com/blog/collaborative-development-for-powerapps-canvas-apps/)

### Model-driven apps

When developing model-driven apps, consider using solutions and
environments designated for multiple app makers. More information: [Solutions overview](../../maker/data-platform/solutions-overview.md)

> [!div class="nextstepaction"]
> [Next step: Test the app](testing-phase.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
