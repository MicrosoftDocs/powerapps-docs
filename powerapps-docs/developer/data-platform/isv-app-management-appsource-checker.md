---
title: Introduction to the AppSource checker | Microsoft Docs
description: Learn how to use AppSource checker
author: "nkrb" # GitHub ID
ms.service: powerapps
ms.topic: article
ms.author: nabuthuk
ms.reviewer: pehecke
ms.workload: na
ms.date: 04/07/2020
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# AppSource checker

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

You can use the AppSource checker to verify whether your app has met certification criteria before you submit it to [AppSource](https://appsource.microsoft.com/). The checker lets you know whether your solution file has errors that need to be corrected and verifies whether AppSource certification criteria have been met. 

In ISV Studio, you can upload either a full [package](/power-platform/alm/package-deployer-tool) or solution(s). You'll be notified whether any issues need to be remediated.

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

**To run AppSource checker**

1. In ISV Studio, select **AppSource checker** in the leftmost pane, and then select **Validate your app**.

    > [!div class="mx-imgBorder"]
    > ![AppSource checker](media/appsource-checker.png "AppSource checker")

2. Select **Browse** to upload a solution file from your local machine, and then select **Run Check**.
   
   > [!div class="mx-imgBorder"]
   > ![Run check command](media/appsource-browse-solution-files.png "Run check command")
 
   > [!NOTE]
   > If you've previously uploaded a solution for validation, you'll see a history of submissions instead of the screenshot above.

3. After the validation check is complete, a summary of results is displayed with the number of issues found (if any). Double-click to select the solution file to see the issues in detail.

   > [!div class="mx-imgBorder"]
   > ![Summary of AppSource checker results](media/appsource-results-page.png "Summary of AppSource checker results")

4. If the submission has no errors, you'll see the following message:
 
   > [!div class="mx-imgBorder"]
   > ![AppSource checker success message](media/appsource-no-error-page.png "AppSource checker success message")
   
Now you can download the validation report for your app and include it with your AppSource submission. 

### See also

[Home page](isv-app-management-homepage.md)<br/>
[App page](isv-app-management-apppage.md)<br/>
[Tenant page](isv-app-management-tenantpage.md)<br/>
[Connector certification](isv-app-management-certification.md)



[!INCLUDE[footer-include](../../includes/footer-banner.md)]