---
title: List attributes and relationships
description: Learn about attributions and relationships for a list of records on a portal.
author: sandhangitmsft

ms.topic: conceptual
ms.custom: 
ms.date: 05/27/2022
ms.subservice: portals
ms.author: sandhan
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
    - ProfessorKendrick
---

# List attributes and relationships

The following are attributes when configuring a **list** component.

|              Name              |                                                                                                                                                                                        Description                                                                                                                                                                                         |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|              Name              |                                                                                                                                                                The descriptive name of the record. This field is required.                                                                                                                                                                 |
|          Table Name           |                                                                                                                                               The name of the table from which the Saved Query view will be loaded. This field is required.                                                                                                                                               |
|              View              |                                                                          The Saved Query view(s) of the target table that is to be rendered. This field is required. If more than one view has been specified, the webpage will contain a drop-down list to allow the user to switch between the various views.                                                                           |
|           Page Size            |                                                                                                                                            An integer value that specifies the number of records per page. This field is required. Default: 10                                                                                                                                             |
|   Web Page for Details View    |                                                                                                        An optional webpage that can be linked to for each record. The ID Query String Parameter Name and record ID will be appended to the query string of the URL to this webpage.                                                                                                        |
|      Details Button Label      |                     The text displayed for the details view button if **Web Page for Details View** has been specified. Default: View details <br>**Note**: For each language pack installed and enabled for the Microsoft Dataverse environment, a field will be available to enter the message in the associated language.                      |
|      Web Page for Create       |                                                                                                                                                             An optional webpage that will be the target of the create button.                                                                                                                                                              |
|      Create Button Label       |                              The text displayed for the create button if **Web Page for Create** has been specified. Default: Create <br>**Note**: For each language pack installed and enabled for the Dataverse environment, a field will be available to enter the message in the associated language._                              |
| ID Query String Parameter Name |                                                                                                                                           A parameter name provided in the query string of the URL to the Web Page for Details View. Default: id                                                                                                                                           |
|        Empty List Text         |  **Deprecated**.  The message displayed when there are no records.<br>**Note**: For each language pack installed and enabled for the Dataverse environment, a field will be available to enter the message in the associated language.                                                           |
|     Portal User Attribute      |                                                                                      An optional lookup attribute on the primary table that represents the portal user record, either contact or system user, to which the current user's ID can be applied to filter the data rendered in the list.                                                                                      |
|       Account Attribute        |                                                                                       An optional lookup attribute on the primary table that represents an account record to which the current user contact's parent Customer account value can be applied to filter the data rendered in the list.                                                                                       |
|       Website Attribute        |                                                                                                          An optional lookup attribute on the primary table that represents the website to which the current website's ID can be applied to filter the data rendered in the list.                                                                                                          |
|         Search Enabled         | An optional Boolean value indicating whether search should be enabled. A text box will be rendered to allow users to do a quick search for records. Use the asterisk (\*) wildcard character to search on partial text. The search appends Or condition filters for each column of the primary table in the view to the view's existing predefined filter conditions to query and return the resulting records. <br> **Note**: This option doesn't search within related table columns. |
|    Search Placeholder Text     |                                                                                                                                                      An optional string used as the label displayed in the text box on initial load.                                                                                                                                                       |
|      Search Tooltip Text       |                                                                                                                                             An optional string used as the tooltip displayed when the user points to the **Search** text box.                                                                                                                                              |


### See also

- [Work with lists](entity-lists.md)
- [Display multiple Dataverse records using lists](/training/modules/portals-access-data-platform/2-entity-lists)
- [Configure a portal](configure-portal.md)  
- [Redirect to a new URL on a portal](add-redirect-url.md)
