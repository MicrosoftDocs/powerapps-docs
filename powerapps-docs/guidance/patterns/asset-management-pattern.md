---
title: "Power Apps pattern: Asset management"
description: Discover how Power Apps simplifies asset management with real-world examples of finding, reserving, and managing resources like rooms, vehicles, and equipment.
#customer intent: As a business decision-maker, I want to evaluate Power Apps for asset management so that I can determine its suitability for my organization.
author: kathyos
ms.topic: concept-article
ms.custom: guidance
ms.date: 02/20/2026
ms.subservice: guidance
ms.author: kathyos
ms.reviewer: kathyos
---

# Pattern: Asset management

<!--![Collage of asset management app screenshots.](media/asset-management-collage.jpg "Collage of asset management app screenshots")
Removed Eneco since only article found describes how it moved to MCS -->

Power Apps provides a platform for managing your company's physical assets. Whether you want to know who currently has what gear or create a reservation system for limited resources like workspace or vehicles, Power Apps helps you create tools that are easy for your employees to use. It also provides timely business intelligence to help you track, manage, and analyze patterns in resource use.

The following examples showcase organizations that replaced paper and email-based systems with Power Apps solutions. Additionally, Microsoft has created templates you can use to jump-start your own asset reservation or checkout projects.

## How to recognize the asset check-out pattern

:::image type="content" source="media/asset-management-illustration.png" alt-text="Screenshot of the asset management pattern illustration showing find, reserve, and manage steps.":::

In a typical asset management scenario:

1. An employee finds an available asset (such as a room, vehicle, or gear).

1. They check out the asset right then, or reserve it for a specific time.

1. Management centrally manages and monitors available assets.

## Template: Return to the Workplace solution

[Return to the Workplace Solution blog post](https://www.microsoft.com/power-platform/blog/2020/07/21/return-to-the-workplace-with-confidence-with-the-power-platform)

Reopen responsibly, monitor intelligently, and protect continuously with solutions for a safer work environment. Equip facility managers and task force leaders to make informed decisions to safely reopen locations. Empower employees to return confidently with self-service tools for working safely and productively. Help health and safety leaders ensure the care and well-being of your workforce.

### Main modules of the Return to the Workplace solution

- **Location Readiness dashboard** helps determine the readiness of the facilities and efficiently manage their safe reopening.

- **Facility Safety Management** gives facility managers the tools they need to manage the reopening and readiness of the facilities.

- **Workplace Care Management** gives health and safety leaders the tools they need to actively manage COVID-19 cases, identify hot spots for safety improvement, and import data from external systems to support case management and manual contact tracing.

- **Employee Return to the Workplace** offers your workforce the self-service tool that they need to feel confident about returning and remain productive while onsite. They can use Employee Return to the Workplace app to check in remotely and self-screen before entering a building.

### Apps for workspace scheduling

- Facilities managers use the Facility Safety Management app to set up facilities available for booking and see a dashboard of bookings.

  :::image type="content" source="media/RTW-facility-safety-management-app.png" alt-text="Screenshot of the Facility Safety Management app.":::

- Employees use the Employee Return to the Workplace app to book a space.

  :::image type="content" source="media/RTW-facility-pass.png" alt-text="Screenshot of an employee pass.":::

### More apps and templates

- [Asset Checkout (canvas app or model-driven app)](https://community.powerplatform.com/galleries/gallery-posts/?postid=0a3b4149-c829-4b74-9f52-d9b9d3e8b50c)

-  [Book a Room (canvas app)](https://www.microsoft.com/power-platform/blog/power-apps/office-template-book-a-room-now-available/)

## How customers are using this pattern

Customers across industries are using Power Apps to manage their assets, from finding and reserving shared resources to managing check-out and return of equipment.

### Armanino Workspace Scheduler app

[Read the whole story.](https://customers.microsoft.com/story/786165-armanino-partner-professional-services-power-apps)

Sometimes it's not how much you have, but how you use it. Armanino—one of the 20 largest independent accounting and business consulting firms in the United States—is caught between a traditional office model and the need for an agile workforce. The company uses office space for teamwork and client meetings in 16 office locations in 15 major urban centers where it has bases, and it also deploys specialized professionals wherever they're needed. The firm wanted to make sure office space is always available for its highly mobile workforce, but avoid overspending on underutilized space.

Armanino created the Workspace Scheduler mobile app by using Power Apps. The firm worked with its own dedicated team of Microsoft Dynamics 365 experts—a longstanding member of the Microsoft AI Inner Circle program and a Gold Certified Partner.

The mobile app gives every staff member fast, accurate information about what space is available and a reservation capability enhanced with Microsoft Outlook, Office 365 Users, and SQL Server connectors.

:::image type="content" source="media/armanino-mobile-app.png" alt-text="Screenshot of Armanino Workplace Scheduler mobile app.":::

Every Armanino worker willing to share office space can indicate when their space is free on Workspace Scheduler, and any worker on the road can find and reserve that space ahead of time.

### Virgin Atlantic

[Read the whole story.](https://www.microsoft.com/power-platform/blog/power-apps/virgin-atlantic-drives-agile-wins-for-mobile-workforce-with-the-power-platform)

Virgin Atlantic needed to hand out iPads to 3000 cabin crew members. The IT Asset Management team created a Power Apps app to scan the barcode of the iPad and assign it to each crew member. All information was stored in SharePoint Online and later imported into their Asset Management system. Within six weeks, 90% of the iPads were handed out with the help of this app, significantly reducing the time otherwise spent manually recording serial numbers and crew payroll numbers. On some days volunteers, handed out as many as 250 iPads per day.

:::image type="content" source="media/virgin-atlantic-crew-ipad-app.png" alt-text="Screenshot of Crew iPad Asset Management app.":::

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
