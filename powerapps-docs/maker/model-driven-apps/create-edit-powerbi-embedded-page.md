---
title: "Create or edit model-driven app Power BI embedded page | MicrosoftDocs"
ms.custom: ""
ms.date: 05/08/2020
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
ms.assetid: 641885d2-4a08-41b8-b914-d9a244e4d5b1
caps.latest.revision: 10
ms.author: "aorth"
manager: "kvivek"
author: "adrianorth"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Create or edit model-driven app Power BI embedded page (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This topic will outline the setup of a system dashboard referencing a Power BI report or dashboard.  A new option has been added to the solution New > Dashboard menu called **Power BI embedded (preview)**.

To learn more about Power BI reports and dashboards, open <a href="https://docs.microsoft.com/power-bi/create-reports/">Create Power BI Reports</a>. 

> [!IMPORTANT]
> - This is a private preview feature and requires an maker & environment feature flags to be enabled to author and view a Power BI embedded page in a model-driven app.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]


## Create system dashboard with Power BI embedded

This examples sets up a Power BI embedded page for a single environment connected to a Power BI workspace.  The next example would need to be used with Environment Variables for managed solution ALM which has a different workspace for prod.

1. Create or edit a solution in <a href="https://make.powerapps.com">make.powerapps.com</a>

    > [!NOTE]
    > Append "?powerappsPortal.powerbiAllowAsSystemDashboard=true" to the URL to enable the private preview

1. Click **New** > **Dashboards** > **Power BI embedded**

    > [!div class="mx-imgBorder"] 
    > ![New Dashboard Power BI embedded menu](media/create-edit-powerbi-embedded-page/new-dashboard-powerbi-embedded-preview.png "New Dashboard Power BI embedded menu")


1. New Power BI embedded dialog appears

    > [!div class="mx-imgBorder"] 
    > ![New Dashboard Power BI embedded panel](media/create-edit-powerbi-embedded-page/new-dashboard-powerbi-embedded-panel.png "New Dashboard Power BI embedded panel")

1. Enter name for the dashboard which will be shown to the user in the selector on the **Dashboards** page

1. Select the Power BI type of Report or Dashboard

1. Select a Power BI workspace then select a Power BI report/dashboard

1. Click Create to save and publish the system dashboard

## Add Power BI embedded page into the model-driven app

1. Create or edit an existing model-driven app in the app designer

1. Select the **Dashboards** element on the canvas

    > [!div class="mx-imgBorder"] 
    > ![App designer select dashboards element](media/create-edit-powerbi-embedded-page/app-designer-select-dashboards-element.png "App designer select dashboards element")

1. In the Dashboards property pane there is a **Power BI embedded page** category

    > [!div class="mx-imgBorder"] 
    > ![App designer dashboards powerbi embedded category](media/create-edit-powerbi-embedded-page/app-designer-dashboards-powerbi-embedded-category.png "App designer dashboards powerbi embedded category")

1. By unselecting **All**, then specific dashboards can be selected.

Optionally, the Power BI embedded page can be set as the default dashboard in the sitemap.

1. Open **Sitemap** from the app designer

1. Select the existing "Dashboards" subarea or insert one

1. Open the **Default Dashboard** property and select the Power BI embedded page name

    > [!div class="mx-imgBorder"] 
    > ![Sitemap designer subarea property default dashboard](media/create-edit-powerbi-embedded-page/sitemap-designer-subarea-property-default-dashboard.png "Sitemap designer subarea property default dashboard")

Finally the model-driven app can be saved and published.

## Selecting the Power BI embedded page in the model-driven app 

  > [!Note]
  > During the private preview phase, a server feature flag needs to be enabled per environment to allow viewing the Power BI embedded page in a model-driven app 

1. Play the model-driven app

1. Select the dashboards page in the navigation

1. Open the dashboard selector and select the Power BI embedded page




<!-- Reference this section for "Use environment variable" Learn more link -->
## Create Power BI embedded page with an Environment Variable

When a solution with a Power BI embedded component will be moved to other environments turning on "Use environment variable" allows configuring the dashboard.  Each environment can specify the workspace and either dashboard or report to reference.  This allows configuration without unmanaged customizations.

1. Create or edit an existing Power BI embedded dashboard

1. Select "Use environment variable"

    > [!div class="mx-imgBorder"] 
    > ![Use environment variable](media/create-edit-powerbi-embedded-page/power-bi-embedded-use-environment-variable.png "Use environment variable")

1. Open "Power BI environment variable" selector and click **New environment variable**

    > [!div class="mx-imgBorder"] 
    > ![Select new environment variable](media/create-edit-powerbi-embedded-page/power-bi-embedded-new-environment-variable.png  "Select new environment variable")

1. Nested panel will open to allow creating the environment variable and will default the **Display Name** and **Name** based on the dashboard name

    > [!div class="mx-imgBorder"] 
    > ![Power BI embedded Environment Variable panel](media/create-edit-powerbi-embedded-page/powerbi-embedded-env-var-panel.png  "Power BI embedded Environment Variable panel")

1. Power BI embedded environment variable panel allows configuring workspace and report/dashboard whcih is stored as JSON with both values.  This is done for either the default value or the current value.

1. Saving the environment variable will then show the default and/or current values for workspace and report/dashboard

    > [!div class="mx-imgBorder"] 
    > ![Power BI embedded environment variable value preview](media/create-edit-powerbi-embedded-page/power-bi-embedded-environment-variable-value-preview.png  "Power BI embedded environment variable value preview")

## Related

* [Create or edit model-driven app dashboards](create-edit-dashboards.md)

* [View entity data in Power BI Desktop](../common-data-service/view-entity-data-power-bi.md)

* [Environment variables overview](../common-data-service/environmentvariables.md)
