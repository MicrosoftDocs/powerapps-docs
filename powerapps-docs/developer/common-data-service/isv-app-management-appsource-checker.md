---
title: Introduction to the AppSource checker | Microsoft Docs
description: Learn how to use app source checker.
services: ''
suite: powerapps
documentationcenter: na
author: "nkrb" # GitHub ID
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.reviewer: pehecke
ms.workload: na
ms.date: 07/11/2019
ms.author: prkoduku
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# AppSource checker

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

AppSource checker allows an ISV to check the certification criteria of their app prior to [AppSource](https://appsource.microsoft.com/) submission. The checker will let you know if your solution file has errors that need to be corrected or if AppSource certification criteria have not been met. 

In ISV Studio, an ISV can either upload a full package or solution(s) and be notified of any issues that need to be remediated. To do that:

1. In ISV Studio, navigate to menu on the left and go to **App validation**.
2. Click on **AppSource checker** and upload a solution file. 
 
   >  [!NOTE]
   > If a user has previously uploaded a solution for validation then you will see a history of submissions instead of the screenshot above.

3. Once the solution checker completes validating, a summary of results will be displayed along with the number of issues present (if any).

4. If the submission has no errors, you will see the following message:
 

5. An ISV can download the validation report for their app and include it with their AppSource submission. 

## See Also

[Home page](isv-app-management-homepage.md)<br/>
[App page](isv-app-management-apppage.md)<br/>
[Tenant page](isv-app-management-tenantpage.md)

