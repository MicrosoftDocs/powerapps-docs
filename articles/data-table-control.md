<properties
	pageTitle="Introducing the Data table control in PowerApps"
	description="This topic introduces the Data table control in Microsoft PowerApps."
	services="powerapps"
	documentationCenter="na"
	authors="jasongre"
	manager="kfend"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="04/24/2017"
   ms.author="kfend"/>
   
# Introducing the Data table control in PowerApps
   
Imagine that you have a collection of data (such as a list sales orders, a set of service tickets, or a directory of contacts), and that you want to show this data in your Microsoft PowerApps app in a tabular format, where each column represents a field and each row represents a record. In the past, you might have been able to roughly simulate this visualization, although the process required some effort. However, by using the Data table control that was recently added to PowerApps, you can now quickly and easily achieve this very typical visualization. You just have to link your Data table to a data source and then select which fields to show. 

![Data table control](Media/dataTableExample.png "Data table control")

## What is included in the Data table control

+ **Connected data sources** – The Data table can be used in conjunction with connected data sources. 
+ **Single record selection** – Users can select only one row at a time in the Data table control. The **Selected** property can then be used to access field values from that row and provide data context to other PowerApps controls.    
+ **Read-only data** – Like the data that is shown in the Gallery control, the data that is shown in the Data table control is read-only. To enable a record to be edited, you must link the selected row in the Data table to an **Edit** form or other editable controls.  
+ **Column headings** – A row of column headings appears at the top of the Data table for reference. You can currently restyle the column headings to achieve the appearance that you want.  
+ **Broad customization support** – Several properties have been exposed that let you restyle and customize the Data table. For example, you can adjust the style for the whole set of data rows, the selected row, or the row that the mouse pointer is currently pointing to.   

To learn more about the Data table control, its properties, and how to use it, see [Data table controls in PowerApps](/power-apps-data-table-control.md).

## We want your feedback

We hope that you find the Data table control a useful tool for building apps that have the visuals that you want. As always, we are extremely interested in any feedback that you have about this new feature. You can leave your comments on this page or on [PowerApps community](http://aka.ms/powerapps-community "PowerApps community"). We look forward to incorporating your feedback and suggestions to improve the control and PowerApps as a whole!
