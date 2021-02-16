---
title: "Add a Power BI report or dashboard to a web page in a portal | MicrosoftDocs"
description: "Instructions to add a Power BI report or dashboard to a web page in the portal."
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 02/08/2021
ms.author: nenandw
ms.reviewer: tapanm
---

# Add a Power BI report or dashboard to a web page in portal

You can add a Power BI report or dashboard to a web page in portal by using the [powerbi](../liquid/portals-entity-tags.md#powerbi) Liquid tag. Use the `powerbi` tag in the **Copy** field on a web page or in the **Source** field on a web template.

If adding a Power BI report or dashboard created in the new workspace in Power BI, you must specify the authentication type as **powerbiembedded** in the *powerbi* Liquid tag.

> [!TIP]
> This article explains how to add a Power BI report or dashboard using *powerbi* liquid tag. To add **Power BI component** on a webpage in your portal using the portals Studio, go to [Add a Power BI component to a webpage using the portals Studio](../add-powerbi.md).

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

## How to use powerbi-client JavaScript library in portals

You can use [powerbi-client JavaScript library](https://github.com/microsoft/PowerBI-JavaScript#powerbi-client) while embedding Power BI reports or dashboards in portals. For more information about powerbi-client JavaScript library, see [Power BI JavaScript wiki](https://github.com/Microsoft/PowerBI-JavaScript/wiki).

Below is a sample JavaScript to update the report settings, or to handle events. This sample disables filters pane, disables page navigation, and enables *dataSelected* event.

```javascript
$(function(){
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

To add custom JavaScript to a web page:

1. Open the [Portal Management](../configure/configure-portal.md) app.
1. Select **Web Pages** from the left-pane.
1. Select the web page that contains the Power BI report or dashboard.
1. Select **Advanced** tab.
1. Copy and paste the JavaScript inside the **Custom JavaScript** section.
1. Select **Save & Close**.

Let's understand the sample JavaScript operations, and different options.

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

You can use the settings for panes to work with Power BI panes on a portals web page. For example, you can use the filters setting to hide or show the pane. Or, use the paging with page navigation setting.

Below is the sample to remove filters pane:

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

Sample to work with both page navigation, and filters:

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