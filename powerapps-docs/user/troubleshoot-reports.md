---
title: Troubleshoot problems with data not displaying in a report | Microsoft Docs
description: Troubleshoot problems with data not displaying in a report
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 06/27/2019
ms.subservice: end-user
ms.author: mkaur
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---
# Troubleshoot problems with data not displaying in a report

There are several possible reasons why data that you expect to be in a report does not appear:  
  
- **Insufficient security permissions**. If you don't have permission in Microsoft Dataverse to view a row, it will not appear in the report.  
  
- **Data is not entered.** The person entering data may have left columns empty.  
  
- **Data does not match the criteria for the report.** Many reports include a default filter that displays only active rows, or you may have selected criteria that don’t have any matching row. Try changing the report filter. For more information, see [Edit the default filter of a report](edit-report-filter.md)  
  
- **You may be viewing a cached copy of the report.** By default, data in Dataverse reports is pulled from the database each time you run a report. However, your system administrator may have changed a report to run from the cache. If data you entered recently is not included in the report, you may have an older version of the report from the cache. To refresh the report, on the Report toolbar, select the **Refresh** button.  
  
- **You may not have permission to read rows in a sub-report.** If you do not have permission to read row types that are included in a sub-report, you will get an error message saying that the sub-report could not be displayed.  
  
- **Your Microsoft Internet Explorer privacy settings may block required cookies.** For chart reports, if instead of seeing the chart, you see a red letter X, your privacy settings may be blocking a cookie that is required for the chart control. To fix this problem, in your browser, enable cookies for the server that is running Reporting Services.  
  

### See Also
[Work with reports](work-with-reports.md) 

[Create a report using the Report Wizard](create-report-with-wizard.md)

[Add a existing report](add-existing-report.md)

[Edit report filter](edit-report-filter.md)



[!INCLUDE[footer-include](../includes/footer-banner.md)]