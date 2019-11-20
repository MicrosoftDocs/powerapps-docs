---
title: Collaborate using SharePoint | Microsoft Docs
description: Learn how to collaborate using SharePoint within a model-driven app
documentationcenter: ''
author: Mattp123
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: conceptual
ms.component: model
ms.date: 11/20/2019
ms.author: matp
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Collaborate using SharePoint 

Manage common document types, such as Word, Excel, PowerPoint, OneNote, and create folders to save and manage those documents that are seamlessly stored in SharePoint from within a model-driven app. 

> [!NOTE]
> This feature requires that your system administrator has enabled SharePoint document management. More information: Manage your documents using SharePoint (/power-platform/admin/manage-documents-using-sharepoint)

For record types that support document management, a default document location (folder) is automatically created on SharePoint the first time you go to the Files (account and contact records) or Related > Documents (other standard or custom entity records) tab. The name of the document location is in this format: <record_name>_<record_id>.

By default, the location is set to Documents on Default Site 1.

## Add a document
1.	Open an account or contact record and select the Files tab. For other standard or custom entities that are enabled for document management, select the Related tab, and then select Documents.
2.	Choose from the following options. 
    - To create a new document, select New, and then select the document type you want, such as Word, Excel, or OneNote, enter a name, and the select Save. The blank document opens in a new tab. 
    - To add an existing document, select Upload, select Choose Dile, browse to and select the file you want, select Open, and the select OK. 

The document file appears in the Document Associated Grid view. 

<!-- insert screenshot --> 

<!-- continue -->
