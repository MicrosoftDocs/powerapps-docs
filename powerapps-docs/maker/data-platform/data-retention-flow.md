---
title: Create a cloud flow to view Dataverse long term retained data
description: This article explains how you can Create a cloud flow to view Microsoft Dataverse long term retained data.
author: Mattp123
ms.author: matp
ms.service: powerapps
ms.topic: how-to 
ms.date: 04/27/2023
ms.custom: template-how-to 
---
# Create a cloud flow to view Dataverse long term retained data

Create a cloud flow to view read-only rows in long term data retention in Microsoft Dataverse. For more information about long term data retention in Dataverse, go to [Dataverse long term data retention overview (preview)](data-retention-overview.md).

The cloud flow generates an email used to retrieve retained data in Excel. If there are retained attachments associated with rows from Dataverse, it's included in Excel.

Creating the flow requires the following high level steps:

1. Pass query parameters in a FetchXML to create an Excel file with retained data.
1. Set a condition to determine if the Excel file has been created. Download the Excel file. Pass the required retrieval criteria parameters (table and FetchXml).
1. Create an Excel file with the retrieved data.
1. Send an email to recipients with the Excel file attached.  

Make sure to check your junk mail folder if you don’t see an email after running a flow successfully.
