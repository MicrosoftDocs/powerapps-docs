---
title: Manage and create cards in solutions
description: This article helps you manage cards in solutions.
ms.date: 08/08/2023
ms.topic: overview
author: cotaylor
ms.author: cotaylor
ms.reviewer: mkaur
ms.custom: 
ms.collection: 

---

# Manage cards in solutions

[!INCLUDE[cards-deprecation-banner](~/includes/cards-deprecation-notice.md)]

Create a card from within a solution if, for example, you want to deploy the card to a different environment. Solutions can contain not only cards but also customized tables, choices, and other components. You can quickly customize an environment in various ways by creating cards and other components from within a solution, exporting the solution, and then importing it into another environment. For more information, see [Solutions overview](../../maker/data-platform/solutions-overview.md).


## Create a solution

To package cards in a solution, you need to start by creating a solution. You can skip this step if you already have a solution in which you want to link your card to. For more information, see [Create solution](../../maker/data-platform/create-solution.md).


## Create a card in a solution

You can create a blank card from within a solution.

1. Sign in to [Power Apps](https://make.powerapps.com).
1. If necessary, switch to the environment that contains the solution in which you want to create a card.
1. In the left navigation bar, select Solutions.

    :::image type="content" source="../media/manage-cards/solution-tab.PNG" alt-text="Screenshot of solution tab.":::

1. In the list of solutions, select the solution in which you want to create a card.
1. In the banner under the title bar, select New > Card.

    :::image type="content" source="../media/manage-cards/solution-new-card.PNG" alt-text="Screenshot of menu to create new card.":::

1. Type the name and optionally the description of your card and select Create

    :::image type="content" source="../media/manage-cards/create-card-modal.PNG" alt-text="Screenshot of dialog to create new card.":::

1. Create your card, save your changes, then select Back to return to your solution.

    :::image type="content" source="../media/manage-cards/card-designer.PNG" alt-text="Screenshot of card designer.":::

1. Your new card appears in the list of components for that solution. If you save any changes to your card, they're reflected in the version that's in the solution.
1. If your card has any dependencies, such as Dataverse tables, from the commands menu, select Advanced > Add required objects. You can repeat this step anytime you add more required objects to your card.

    :::image type="content" source="../media/manage-cards/add-required-objects.PNG" alt-text="Screenshot of adding required objects of card.":::

1. All required objects of your card appear in the list of components for that solution.

> [!NOTE]
> If you choose to manage the required objects of your card in separate solutions, you must ensure they're imported into your target environment prior to importing the solution containing your card.


## Add an existing card to a solution

1. Sign in to [Power Apps](https://make.powerapps.com).
1. If necessary, switch to the environment that contains the solution in which you want to create a card.
1. In the left navigation bar, select Solutions.

    :::image type="content" source="../media/manage-cards/solution-tab.PNG" alt-text="Screenshot of solution tab.":::

1. In the list of solutions, select the solution in which you want to add a card to.
1. In the banner under the title bar, select Add existing > Card

    :::image type="content" source="../media/manage-cards/add-existing-card.PNG" alt-text="Screenshot of menu to add existing card.":::

1. Select the card you want to add to your solution and select Add

    :::image type="content" source="../media/manage-cards/select-existing-card.PNG" alt-text="Screenshot of selecting existing card to add.":::

1. Your existing card appears in the list of components for that solution along with any required tables of that card. If you save any changes to your card, they're reflected in the version that's in the solution. If you add more required tables, follow the steps in "Create a card in a solution" to add the new required objects of your card to your solution.

## Add a Power Automate flow with the Cards for Power Apps connector to a solution

A common way to send cards is by using a Power Automate flow. For more information, see [Send a card automatically with a flow](../send-a-card/send-card-with-flow.md).

When creating a flow to send cards in a solution, it's important that in addition to the flow, you also include the cards and any tables the card requires in the solution as well. To add any cards and tables, start by creating your flow in a solution and adding actions from the Cards for Power Apps connector. Then, follow the instructions above for adding an existing card to add all the cards used in the flow. Any required tables will be automatically added.

## Known Limitations

### Dependencies for cards aren't displayed correctly in solution explorer

When importing a solution containing a card that depends on tables not present in the same solution, the import fails if those tables aren't already present in the target environment. Similarly, removing a solution containing tables that a card depends on fails. The dependency viewer in these scenarios is not helpful at identifying which tables or cards is causing the operation to fail.

Instead, to identify which cards depend on which tables when resolving dependency issues, start by opening the card designer. Next, navigate to Cards from the sidebar, select the card you're  interested in, and select Edit. Once the card designer opens, select Data from the sidebar to view the tables that card depends on.

### Card dependencies for flows aren't represented in solution explorer

When importing a solution containing a flow that depends on cards not present in the same solution, dependencies on cards will not be enforced. The solution maker must ensure that cards used in the flow are also present in the solution or the target environment to ensure the flow works correctly in the target environment.