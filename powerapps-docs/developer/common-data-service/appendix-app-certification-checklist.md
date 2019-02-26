---
title: "Appendix: App certification checklist (PowerApps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Use the app design checklist to evaluate your app design in PowerApps." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 02/25/2019
ms.reviewer: "kvivek"
ms.service: "powerapps"
ms.topic: "article"
author: "omarcdoc" 
ms.author: "omarc" 
manager: "AnnBe" 
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Appendix: App certification checklist

The following checklist provides the list of validations performed by Microsoft during the certification process after you [submit](next-steps-submit-app-cloud-partner-portal.md) your app. 

<table>
<tbody>
<tr>
<th>Modules included</th>
<th>Validation Type</th>
<th>Certification checklist</th>
</tr>
<tr>
<td rowspan=3>Dynamics 365 for Customer Engagement + PowerApps + Flow<br/><br/>Dynamics 365 for Customer Engagement includes:
<ul>
<li>Dynamics 365 for Sales</li>
<li>Dynamics 365 for Customer Service</li>
<li>Dynamics 365 for Field Service</li>
<li>Dynamics 365 for Project Service Automation</li>
<li>Dynamics 365 for Marketing</li>
</td>
<td>Sanity Check</td>
<td><ul>
<li>Check for app registration type. Free, Trial or Contact me. If registered in Contact me then publisher need to enable test drive.</li>
<li>Verify the submitted [package](create-package-app-appsource.md) contains all the artifacts required to publish on AppSource.</li>
<li>Download the E2E functional document from Cloud Partner Portal and validate if document is updated with functional scenarios and user/admin journey</li>
</ul>
</td>
</tr>
<tr>
<td>Code Validation</td>
<td>Colors used in this solution are accessible by all user
groups.</td>
</tr>
<tr>
<td>3</td>
<td> Uniformity of color and design scheme </td>
<td>The color and UI design are uniform and presentable</td>
</tr>
<tr>
<td>4</td>
<td>Ease of use for users</td>
<td>The solution is intuitive and easy to use with minimal
directions</td>
</tr>
<tr>
<td>5</td>
<td>Minimum number of screens to achieve a use-case</td>
<td>All use-cases could be achieved in minimum number of
screens and steps</td>
</tr>
<tr>
<td>6</td>
<td>Performance</td>
<td>
<ul>
<li>Caching is used where needed</li>
<li>Only columns that are needed are pulled from database</li>
<li>Minimum number of calls to server is made to achieve any</li>
use-case.
</ul>
</td>
</tr>
<tr>
<td>7</td>
<td>Presentation of information</td>
<td>
<ul>
<li>Information is presented is most accessible format</li>
<li>UI layout is suitable for providing the information in
the best way</li>
<li>UI layout provides seamless experience in all the
devices that solution could be run/</li>
</ul>
</td>
</tr>
<tr>
<td>8</td>
<td>Responsiveness</td>
<td>The solution is tested in all the intended devices for
the solution</td>
</tr>
<tr>
<td>9</td>
<td>Accessible content</td>
<td>
<ul>
<li>Content provided in the solution could be rendered in
all the intended devices.<br/>Example: Do not have videos that could not render in
certain browsers.<li>
<li>Does not have unnecessary redirects</li>
<li>Does not have interstitials that interrupts the user’s
flow</li>
<li>Design is suitable for touch screen. If your intended
device is mobile or tablet, then your solution should be
designed for a touch screen</li>
</ul>
</td>
</tr>
<tr>
<td>10</td>
<td>Accuracy of information</td>
<td>The information provided in the UI should help the user
achieve the use case with minimal interruption in the
intended flow of user actions to achieve that scenario</td>
</tr>
</tbody>
</table>


For information on best practices for creating Canvas apps, see [Canvas App Coding Standard and Guidelines](https://aka.ms/powerappscanvasguidelines).

  




  

