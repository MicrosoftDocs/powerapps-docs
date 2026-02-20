---
title: Designing - Which type of app to make
description: Learn how to choose between model-driven and canvas apps in Power Apps. Discover their differences and decide which suits your project needs best.
#customer intent: As a Power Apps maker, I want to understand the differences between model-driven and canvas apps so that I can choose the best option for my project.
author: taiki-yoshida
ms.topic: concept-article
ms.custom: guidance
ms.date: 02/20/2026
ms.subservice: guidance
ms.author: tayoshi
ms.reviewer: jhaskett-msft
---

# Determining which type of app to make

In Power Apps, you have two options when creating apps: model-driven apps and canvas apps.

The following comparison provides a basic, high-level overview. Learn more about these two types of apps in [Overview of creating apps in Power Apps](../../maker/index.md).

:::row:::
    :::column:::
        :::image type="content" source="media/model-apps.png" alt-text="Screenshot of model-driven apps.":::

        Model-driven apps require a Microsoft Dataverse database. They're built on top of the data modeled in that database environment. Views and detail screens for model-driven apps are based on the data structure. Because of this structure, model-driven apps offer users a more consistent look and feel from one screen to the next without requiring much effort from the app creator.

        Model-driven apps are good for scenarios where the [business logic](logic.md) is complex, such as:

        -   Sophisticated data models

        -   Business process management

        -   Tracking activities associated with data
    :::column-end:::
    :::column:::
        :::image type="content" source="media/canvas-apps.png" alt-text="Screenshot of canvas apps.":::
        
        Canvas apps, on the other hand, can be built with or without a Dataverse database. They use connectors to access data and services. Canvas apps start with a blank screen, like an artist's canvas, and the creator manually lays out each screen. This approach gives the creator complete control over the placement of each element on the canvas.

        Use canvas apps if the user is expecting a customized user experience. They offer:

        -   A graphical, intuitive interface

        -   The ability to create a tailor-made UI based on user requirements

        -   Integration spanning multiple systems by using connectors
    :::column-end:::
:::row-end:::

Consider creating a model-driven app unless your users have a specific need for a canvas app. Model-driven apps enable you to make your app quickly because they don't require you to build out the UI yourself.

> [!NOTE]
> If you're creating an app for your customers to use on the web, you can also create a third type of app: [Microsoft Power Pages](/power-pages/introduction).

## Building an end-to-end solution that uses multiple apps

Your business process might require more than one app.

For example, the expense report project has several task sets that are different, so you might consider making several apps. The data they use is the same, but the user experience is tailored to the specific scenario and personas.

:::image type="content" source="media/business-process-tasks.png" alt-text="Screenshot of tasks for each step of the business process.":::

As you can see from the example, multiple types of people handle the same set of data. Canvas apps are the best fit for employees filling in the expense form. This app type enables people like Lee to submit an expense report by using an attractive mobile app that's intuitive to use and works offline.

:::image type="content" source="media/expense-canvas-app.png" alt-text="Screenshot of a canvas app for expense report creation.":::

In [Documenting the business process](understanding-current-business-process.md), Abhay's requirements are:

- Must be able to review all expense reports and receipts
- Responsible for ensuring compliance for every expense report
- Large volume of work; needs to be able to process information quickly
- Must be able to report on how expenses are balancing up to the budget

To process a large volume of work and process information quickly, the best fit is a model-driven app. It allows Abhay to quickly view all the details of the submitted expense report, assess how it affects the budget, and search for related information such as vendor details.

:::image type="content" source="media/expense-model-app.png" alt-text="Screenshot of a model-driven app for processing expense reports.":::

This example scenario uses a combination of both canvas app and model-driven app. Although they're two different types of apps, all the data is centralized in one place: Dataverse.

:::image type="content" source="media/end-to-end-apps.png" alt-text="Screenshot of two apps with data in Dataverse.":::

> [!div class="nextstepaction"]
> [Next step: Determine where to place logic](logic.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
