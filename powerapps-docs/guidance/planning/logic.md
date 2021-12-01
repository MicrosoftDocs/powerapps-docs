---
title: Power Apps architectural design - Where to place logic | Microsoft Docs
description: "Considerations for deciding where to place the logic in your system: canvas apps, model-driven apps, Microsoft Dataverse, or Power Automate flows?"
author: taiki-yoshida
ms.service: powerapps
ms.topic: conceptual
ms.custom: guidance
ms.date: 06/16/2020
ms.subservice: guidance
ms.author: tayoshi
ms.reviewer: kathyos

---

# Where to place logic: Canvas apps, model-driven apps, Microsoft Dataverse, or Power Automate flows?

Your app will have business logic, such as data validation (using the right
format for an email address, for example), calculations, selecting the next
process step based on data, enabling a button when all required fields have
data, and so forth. This article explains some considerations for deciding where
to place the logic in your system.

## Power Apps canvas apps

You set logic in canvas apps by using formulas. All the formula logic is processed on the device the app is run on. The more
complex the logic is, the more processing power the device will require to be
able to handle all the logic.

To keep the app performant, you should consider the following when placing logic
in canvas apps:

- Use it in situations where you must make any changes immediately visible on the screen

- Use only simple logic, and avoid complex formulas with dozens of lines

- Limit it to a few data connectors in a formula

- Avoid using logic to manipulate or transform data

- Avoid processing multiple records at a time (for example, avoid using the ForAll function)

More information: [Get started with canvas-app formulas in Power Apps](../../maker/canvas-apps/working-with-formulas.md)

## Power Apps model-driven apps

Model-driven apps provide several ways to run logic. There are four types of
logic that use low-code methods that are suitable for all developers:

- Business process flows

- Workflows

- Actions

- Business rules

Additionally, the following types of logic are available for pro developers:

- Client-side scripting

- API development

- Using code with web resources

All of these options run on the device that runs the apps. Consider
placing logic in model-driven apps if:

- Logic needs to be run on the device.

- The logic requires multiple entities (tables).

- You need sophisticated logic that isn't available with out-of-the-box
    features.

In general, if you're making apps with complex logic, consider using
model-driven apps instead of trying to do everything by using canvas apps.

More information: [Apply custom business logic with business rules and flows in model-driven apps](../../maker/model-driven-apps/guide-staff-through-common-tasks-processes.md)

## Power Automate flows

For use cases where you need to run complex logic, you need multiple connectors,
or you don't want the user to wait for the action to finish, Power Automate
flows offer a good option for running logic. Consider Power Automate flows
if:

- Logic needs to run across multiple connectors.

- You're creating an approval process.

- Output is being produced in another format.

- You want to reduce dependency on device-side processing power.

More information: [Power Automate documentation](/power-automate/)

## Dataverse

You can set logic in Dataverse so that all of the logic is run in the
service rather than the devices. This makes the app more performant, and also
makes the logic independent of the apps and flows to ensure that data is used in a
particular way.

For example, if you want to require that an address is entered for all apps
and flows that use the Account entity, you should set this logic in Common Data
Service rather than in each app and flow.

There are several ways of applying logic to Dataverse. Using low code,
you can set up things such as auto-numbering fields, calculated fields, and
roll-up fields. Pro developers can apply business logic that uses code by
creating a plug-in or developing workflow extensions.

More information: [Apply business logic in Dataverse](../../maker/data-platform/processes.md)

> [!div class="nextstepaction"]
> [Next step: Secure the app and data](security.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]