---
title: DataSet Grid component | Microsoft Docs
description: This sample component shows how to change the user experience of interacting with the dataset.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 6/08/2021
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 356561d0-a36b-4b93-8b76-3e1abf9414e9
---

# Implementing data-set component

This sample component shows how to change the user experience of interacting with the dataset. For example, you only see the home page grid on a table homepage as a table. You can build your code component that can display the data as per your choice. This sample shows the records as tiles instead of the regular tabular grid. 

[!INCLUDE[cc-terminology](../../data-platform/includes/cc-terminology.md)]

> [!div class="mx-imgBorder"]
> ![Data Set Grid component.](../media/data-set-grid.png "Data Set Grid component")

## Available for 

Model-driven apps

## Code

You can download the complete sample component from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework/DataSetGrid).

> [!NOTE]
> Some of the dataset API methods are still not supported in canvas apps. See, [Dataset component for canvas apps](data-set-component-canvas.md) to learn more about how dataset type components are implemented in canvas apps.


In this sample, we have the input parameter defined in component manifest file with the data-set tag. This is the input property that gets bound to the component.  
 
This component has two important containers that are added onto the main div which is added onto the div that is passed onto the component.  The first container holds the tiles that show the record data from the view and the second container is for the `Load More button` that shows when there are records that need more area that can fit in one page. 
 
Both the containers are generated and refreshed whenever the [updateView](../reference/control/updateview.md) method is called. For the first container, we generate the tiles based on the information in the columns and the number of records. This ensures we display a tile for each record along with its information on it.  If there exists a following page for the records, the load more button is displayed i.e., the second container is visible and is hidden if there are no more pages in the result set.  
 
On the click of load more button, we load the next page of records and append it to the existing result set and the logic to hide or show the button remains same as earlier as shown in the code. This is taken care by the ***onLoadMoreButtonClick*** method which is bound to the button.
 
The ***toggleLoadMoreButtonWhenNeeded*** function takes the input as the data set and checks, whether the data set, has next page, and if the button is hidden or visible and respectively hides or shows the button.  
 
The ***onRowClick*** function attaches the context of the record using its GUID value and invokes the [openForm](../reference/navigation/openform.md) method of the `NavigationAPI` to open that respective record. This method is bound to each tile that gets generated as part of the ***createGridBody*** method.
 
The ***getSortedColumnsOnView*** method returns the list of columns based on the defined order on the view.

### Related topics

[Download sample components](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework)<br/>
[How to use the sample components](../use-sample-components.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework manifest schema reference](../manifest-schema-reference/index.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]