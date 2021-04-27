---
title: "Appendix: App design best practices checklist (PowerApps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Use the app design checklist to evaluate your app design in Power Apps." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/20/2019
ms.reviewer: "pehecke"
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
# Appendix: App design best practices checklist

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

Use the following checklist to evaluate your app design. 

<table>
<tbody>
<tr>
<th>S.No</th>
<th>Artifact</th>
<th>Success Criteria</th>
</tr>
<tr>
<td>1</td>
<td>Font uniformity</td>
<td><ul>
<li>Font size is uniform across the solution</li>
<li>Font color is uniform across the solution</li>
<li>Fonts are readable in all the intended device</li>
</ul>
</td>
</tr>
<tr>
<td>2</td>
<td>Color Accessibility</td>
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
<li>Does not have interstitials that interrupts the user's
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

  




  



[!INCLUDE[footer-include](../../includes/footer-banner.md)]