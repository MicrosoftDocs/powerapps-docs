---
title: Add a Power BI report or dashboard to a webpage
description: Learn how to add a Power BI report or dashboard to a webpage in the portal by using the powerbi Liquid tag.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/21/2021
ms.author: nenandw
ms.reviewer: tapanm
contributors:
    - neerajnandwana-msft
    - tapanm-msft
---

# Add a Power BI report or dashboard to a webpage in a portal

You can add a Power BI report or dashboard to a webpage in your portal by using the [powerbi Liquid tag](../liquid/portals-entity-tags.md#powerbi). Use the `powerbi` tag in the **Copy** field on a webpage or in the **Source** field on a web template.

If you're adding a Power BI report or dashboard created in the new workspace of Power BI, you must specify the authentication type as **powerbiembedded** in the *powerbi* Liquid tag.

> [!TIP]
> This article explains how to add a Power BI report or dashboard using the *powerbi* Liquid tag. To add a **Power BI component** on a webpage in your portal using portals Studio, go to [Add a Power BI component to a webpage using portals Studio](../add-powerbi.md).

For example: 

```
{% powerbi authentication_type:"powerbiembedded" path:"https://app.powerbi.com/groups/00000000-0000-0000-0000-000000000000/reports/00000000-0000-0000-0000-000000000001/ReportSection01" %}
```

> [!NOTE]
> If you have specified AAD as the authentication type in the *powerbi* Liquid tag, you must share it with the required users before adding the secure Power BI report or dashboard to a webpage in the portal. For more information, see [Share Power BI workspace](/power-bi/service-how-to-collaborate-distribute-dashboards-reports#collaborate-with-coworkers-in-an-app-workspace) and [Share Power BI dashboard and report](/power-bi/service-share-dashboards).

## Get the path of a dashboard or report

1.	Sign in to [Power BI](https://powerbi.microsoft.com/).

2.	Open the dashboard or report you want to embed in your portal.

3.	Copy the URL from the address bar.

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

## How to use powerbi-client JavaScript library in portals

You can use [powerbi-client JavaScript library](https://github.com/microsoft/PowerBI-JavaScript#powerbi-client) while embedding Power BI reports or dashboards in your portal. For more information about powerbi-client JavaScript library, see the [Power BI JavaScript wiki](https://github.com/Microsoft/PowerBI-JavaScript/wiki).

Below is a sample JavaScript to update the report settings or to handle events. This sample disables filter pane, disables page navigation, and enables *dataSelected* event.

> [!IMPORTANT]
> Use powerbi-client JavaScript library to disable or enable filter pane. However, if you want to restrict access to data or configure security, use [Row-level security (RLS) with Power BI](/power-bi/admin/service-admin-rls). Disabling filter pane doesn't restrict data access, and it can be re-enabled using JavaScript library code.

```javascript
$(window).load(function(){
    var embedContainer = $(".powerbi")[0];
    var report = powerbi.get(embedContainer);
    report.on("loaded", function(){
        report.updateSettings({
            panes: {
                filters :{
                    visible: false
                },
                pageNavigation:{
                    visible: false
                }
            }
        }).catch(function (errors) {
            console.log(errors);
        });
    })
    report.on('dataSelected', function(event){
        console.log('Event - dataSelected:');
        console.log(event.detail);
    })
})
```

To add custom JavaScript to a webpage:

1. Open the [Portal Management](../configure/configure-portal.md) app.
1. Select **Web Pages** from the left pane.
1. Select the webpage that contains the Power BI report or dashboard.
1. Select **Advanced** tab.
1. Copy and paste the JavaScript inside the **Custom JavaScript** section.
1. Select **Save & Close**.

Now, let's understand the sample JavaScript operations and different options.

### Get a reference to the embedded report HTML

Get a reference to the embedded report HTML.

```javascript
var embedContainer = $(".powerbi")[0];
```

More information: [Get a reference to an existing Power BI component given the containing element](https://github.com/microsoft/PowerBI-JavaScript/wiki/Service-Details#get-a-reference-to-an-existing-power-bi-component-given-the-containing-element)

### Get a reference to the embedded report

```javascript
var report = powerbi.get(embedContainer);
```

### Work with Power BI panes

You can use the settings for panes to work with Power BI panes on a portals webpage. For example, you can use the filters setting to hide or show the pane, or work with the page navigation setting.

Below is a sample to remove filters pane:

```javascript
report.updateSettings({
            panes: {
                filters :{
                    visible: false
                }
            }
        }).catch(function (errors) {
            console.log(errors);
        });
```

Below is a sample to work with both page navigation and filters:

```javascript
report.updateSettings({
            panes: {
                filters :{
                    visible: false
                },
                pageNavigation:{
                    visible: false
                }
            }
        }).catch(function (errors) {
            console.log(errors);
        });
```

More information: [Update settings](https://github.com/Microsoft/PowerBI-JavaScript/wiki/Update-Settings) and [Embed configuration - Settings](https://github.com/Microsoft/PowerBI-JavaScript/wiki/Embed-Configuration-Details#settings)

### Handle events

The embedded component can emit events upon invoking a completion of an executed command. For example, below is a sample for `dataSelected` event.

```javascript
//Report.off removes a given event listener if it exists
    report.off("dataSelected");
//Report.on will add an event list
    report.on('dataSelected', function(event){
        console.log('Event - dataSelected:');
        console.log(event.detail);
    })
```

More information: [Handling events](https://github.com/Microsoft/PowerBI-JavaScript/wiki/Handling-Events)

### See also

- [Add a Power BI component to a webpage using the portals Studio](../add-powerbi.md)
- [Set up Power BI integration](set-up-power-bi-integration.md)
- [powerbi Liquid tag](../liquid/portals-entity-tags.md#powerbi)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
