# Power Apps Cards Designer Overview

## What is Power Apps Cards Designer?

The Power Apps Cards Designer is where Excel-level users can build out cards to suit their own needs, enabling them to optimize and automate business user tasks and to create actionable scenarios in interactive and easy-to-make cards. The Designer builds off of the designer for Adaptive Cards, introducing a few new concepts:

- PowerFX: specify an action to happen when an element is selected
- Connectors: bring data into cards (for now, only Bing Search)
- Variables: store, bind, and reuse data across a card
- Dataverse: stores each card you create and allows you to retrieve the card at send time

## What's in the Designer

The Designer is made up of the following elements:

- [Power Apps Cards Designer Overview](#power-apps-cards-designer-overview)
  - [What is Power Apps Cards Designer?](#what-is-power-apps-cards-designer)
  - [What's in the Designer](#whats-in-the-designer)
    - [Navigation](#navigation)
    - [Tool panel](#tool-panel)
      - [Elements](#elements)
      - [Inputs](#inputs)
      - [Containers](#containers)
    - [Card canvas](#card-canvas)
    - [Property pane](#property-pane)
    - [PowerFX editor](#powerfx-editor)
    - [Play button](#play-button)

   :::image type="content" source="../media/designer-overview/designer-elements.png" alt-text="Screenshot of Power Apps Cards Designer with elements highlighted." border="false":::

### Navigation

The navigation bar on the far left of the screen allows you to swap between the different tools available in the Designer. In order, these are:

- Expand toolbar: allows you to see the full name for each option in the navigation bar
- Card structure: see the card as a hierarchical outline and view the relationships of the card elements; add multiple steps to a card
- Add card element (default view): main UI for editing the card
- Data connections: add connectors to your card to use data from external sources
- Variables: store, bind, and reuse data across a card

### Tool panel

When you start making your card, you'll use items from the Add Card Element tool. There are three categories of items to choose from, as shown in the tables below:

#### Elements

These are the basic building blocks of a card, and the ones you're most likely to use.

| **Item**     | **Description**                                                                                                                                                                                              |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TextBlock    | Standard text block; supports strings and PowerFX formulas                                                                                                                                                   |
| Button       | Specify an action to occur when the button is pressed with PowerFX formula                                                                                                                                   |
| Image        | Supports addition of images to card via URL                                                                                                                                                                  |
| Media        | Supports addition of other forms of media to card via URL                                                                                                                                                    |
| Button Group | If you have multiple buttons in one location on the card, use a Button Group to manage the buttons under one parent element (visible on the Structure page). Provides an easy UI method to add more buttons. |

#### Inputs

Use an input element when you want the end user of the card to specify information.

| **Item**        | **Description**                                                                                                          |
|-----------------|--------------------------------------------------------------------------------------------------------------------------|
| Input.Text      | Allow the user to input a text response; parses as a string                                                              |
| Input.Number    | Allow the user to input a numerical response by typing a number or selecting from the up/down arrows; parses as a string |
| Input.Date      | Allow the user to input a date (mm/dd/yyyy) or choose a date from the dropdown calendar                                  |
| Input.Time      | Enter a time (HH:MM AM/PM) or select a time from the dropdown clock                                                      |
| Input.ChoiceSet | User selects a choice from the dropdown; default is two choices, but more can be added                                   |
| Input.Toggle    | Checkbox for the user to select if applicable; default is unchecked                                                      |

#### Containers

Just like with the Button Group in the Elements section, use a container when you want to group elements together, either for ease of reference or design purposes.

| **Item**  | **Description**                                                                                                                                                                                                      |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Container | A standard container, useable with any element; takes on the properties of the first element placed inside. Doesn't support multiple element types at once.                                                          |
| ImageSet  | Container for images; provides an easy UI method to add more images.                                                                                                                                                 |
| FactSet   | Creates a table of property/value pairs                                                                                                                                                                              |
| ColumnSet | Container for columns; provides an easy UI method to add more columns. Required when using columns.                                                                                                                  |
| Column    | Add to a ColumnSet to create dividers on the page. Empty columns aren't inherently visible in the final card, so you'll need to put another element (e.g., TextBlock, Input, etc.) into a column to make it visible. |

### Card canvas

The card canvas is where the magic happens – this is where you'll build the user interface for your card, using connectors, variables, and elements from the Tool Panel.

NOTE: You can't resize a card in the card canvas view because cards automatically fit themselves to the location they're placed into.

### Property pane

The property pane is used to change up specific properties for an element. Each type of element has its own property pane, including the card itself. For most of the drag-and-drop elements, you'll be able to specify things like:

- Name: the variable name of that element, referenceable in a PowerFX formula
- Label/Text: any text the user will see when they load in the card
- Default value: the initial value of a field
- Initially visible: choose if the element will be visible on load

Each property pane also contains Advanced features, which allow you to specify things like:

- Repeat for every: provide a trigger for if/when an element should be repeated
- Show when: provide a trigger to show the element
- Requires: make the element dependent on certain features, corresponding with a minimum version

You can also input PowerFX expressions into the properties, utilizing low-code solutions to make your card more powerful.

### PowerFX editor

The PowerFX editor sits at the top of the card designer and allows you to write PowerFX expressions with intellisense. When you select an element on the card, the PowerFX editor lets you select a property of that element from the dropdown that supports a code input and then assists you in writing an expression. Intellisense will also pull in any variables you've defined, and specific functions based on the data connections you've made. For more information on PowerFX and functions you can use, see the Microsoft documentation for [Prebuilt Adaptive Expressions](https://docs.microsoft.com/azure/bot-service/adaptive-expressions/adaptive-expressions-prebuilt-functions?view=azure-bot-service-4.0) and [Formula reference for Power Apps](https://docs.microsoft.com/powerapps/maker/canvas-apps/formula-reference).

### Play button

Once you've set up your card to your liking, you can preview the card with the Play button. This will open your card in a new page and allow you to test out the card's functionalities. This is also where, if needed, you'll be able to debug and troubleshoot your card.
