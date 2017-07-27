<properties
    pageTitle="Power BI tile control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the Power BI tile control"
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="fikaradz"
    manager="anneta"
    editor=""
    tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
    ms.date="07/07/2016"
   ms.author="fikaradz"/>

# Power BI tile control in PowerApps #
A control that shows a [Power BI ](https://powerbi.microsoft.com) tile inside an app.

## Description ##
Take advantage of your existing data analysis and reporting by displaying your **[Power BI tiles](https://powerbi.microsoft.com/documentation/powerbi-service-dashboard-tiles/)** inside your apps.  Choose the tile you want to show by setting its **Workspace**, **Dashboard** and **Tile** properties in the **Data** tab of the options panel.


## Sharing and security ##
Once shared, the PowerApp will be accessible by all users who have permissions to access the app.  However in order to make the Power BI content visible to those users, the dashboard where the tile comes from needs to be
[shared](https://powerbi.microsoft.com/documentation/powerbi-service-how-should-i-share-my-dashboard/) with the user on Power BI.  This ensures that Power BI sharing permissions are respected when Power BI content is accessed in an app.

## Key properties ##

**Workspace** – The Power BI workspace where the tile comes from.

**Dashboard** – The Power BI dashboard where the tile comes from.

**Tile** – The name of the Power BI tile you want to display.

## Additional properties ##

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[OnSelect](properties-core.md)** – How the app responds when the user taps or clicks a control. Default behavior takes the user to the Power BI report associated with the tile.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).


## Example ##
1. Add a **Power BI tile** control from the **Insert** tab, **Controls** menu.  
1. In the **Data** tab on options panel choose "My Workspace" for the **Workspace** setting.  Choose a dashboard from the list of dashboards, and a tile from the list of tiles.

	The control renders the Power BI tile.

	Don't know how to [add and configure a control](../add-configure-controls.md)?

  Don't have have Power BI? [Sign up](https://powerbi.microsoft.com/en-us/documentation/powerbi-service-self-service-signup-for-power-bi/).
