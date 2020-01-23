---
title: "Add a Power BI report or dashboard to a web page in a portal | MicrosoftDocs"
description: "Instructions to add a Power BI report or dashboard to a web page in the portal."
author: tapanm-msft
manager: kumarvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 11/22/2019
ms.author: tapanm
ms.reviewer:
---


# Add a Power BI report or dashboard to a web page in portal

You can add a Power BI report or dashboard to a web page in portal by using the [powerbi](../liquid/portals-entity-tags.md#powerbi) Liquid tag. You can add the tag in the **Copy** field on a web page or in the **Source** field on a web template. If you adding a Power BI report or dashboard created in the new workspace in Power BI, you must specify the authentication type as **powerbiembedded** in the powerbi Liquid tag.

For example: 

```
{% powerbi authentication_type:"powerbiembedded" path:"https://app.powerbi.com/groups/00000000-0000-0000-0000-000000000000/reports/00000000-0000-0000-0000-000000000001/ReportSection01" %}
```

> [!NOTE]
> If you have specified AAD as the authentication type in powerbi Liquid tag, you must share it with the required users before adding the secure Power BI report or dashboard to a web page in portal. More information: [Share Power BI workspace](https://docs.microsoft.com/power-bi/service-how-to-collaborate-distribute-dashboards-reports#collaborate-with-coworkers-in-an-app-workspace) and [Share Power BI dashboard and report](https://docs.microsoft.com/power-bi/service-share-dashboards).

## Get the path of a dashboard or report

1.	Sign in to [Power BI](https://powerbi.microsoft.com/).

2.	Open the dashboard or report you want to embed in your portal.

3.	Copy URL from the address bar.

    > [!div class=mx-imgBorder]
    > ![Get the path of a Power BI dashboard](../media/powerbi-dashboard-url.png "Get the path of a Power BI dashboard")

## Get the ID of a dashboard tile

1.	Sign in to [Power BI](https://powerbi.microsoft.com/).

2.	Open the dashboard from which you want to embed a tile in your portal.

3.	Point to the tile, select **More options**, and then select **Open in focus mode**.

    > [!div class=mx-imgBorder]
    > ![Open Power BI dashboard tile in focus mode](../media/powerbi-dashboard-tile-focus.png "Open Power BI dashboard tile in focus mode")

4.	Copy the tile ID from the URL in the address bar. The tile ID is the value after /tiles/.

    > [!div class=mx-imgBorder]
    > ![Power BI dashboard tile ID](../media/powerbi-dashboard-tile-id.png "Power BI dashboard tile ID")


### See also


[powerbi Liquid tag](../liquid/portals-entity-tags.md#powerbi)<br> 
[Set up Power BI integration](set-up-power-bi-integration.md)
