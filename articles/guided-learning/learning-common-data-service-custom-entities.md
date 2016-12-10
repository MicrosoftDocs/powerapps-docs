<properties
   pageTitle="Create custom entities | Microsoft PowerApps"
   description="Extend the common data model with custom entities"
   services=""
   suite="powerapps"
   documentationCenter="na"
   authors="mgblythe"
   manager="anneta"
   editor=""
   tags=""
   featuredVideoId="qg25q3MjFBo"
   courseDuration="6m"/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="get-started-article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="12/09/2016"
   ms.author="mblythe"/>

# Create custom entities
The Common Data Service is designed for all our business customers, from the smallest shops to the largest enterprises. The common data model includes a set of standard entities that address many common business scenarios, and you saw in the previous topic that you can extend those standard entities if necessary. But sometimes you need something completely different to solve problems specific to your business. In that case you need a custom entity, and we'll show you how to build one in this topic.

There are two ways to create an entity:

- Create the entity from scratch. This is what we'll do in this topic.
- Create an entity that is based on another entity, by copying the fields and settings of that entity, but not its data.


## Creating an entity from scratch
For this example, we'll create a custom entity called Product review, from scratch. To start, on the **Entities** tab click **New Entity**. Enter an **Entity name** (no spaces or special characters), a friendly **Display name**, and a meaningful **Description**. Then click **Next**.

![New entity](./media/learning-common-data-service-custom-entities/new-entity.png)

On the next screen, you see the five default fields that all standard and custom entities contain. Click **Add field** to start adding your own.

![Default entity fields](./media/learning-common-data-service-custom-entities/default-fields.png)

For this example, let's add four fields:

- **Review Date**, which is a date field, and is required.
- **Product Rating**, which is an integer field, and is required. We could use a picklist here that allows you to specify only certain values (like 1-5), but we'll keep it simple right now.
- **Reviewer Name**, which is a text field, and isn't required
- **Reviewer Comment**, which is a text field, and also isn't required. 

When you're happy with the entity, click **Create**. When the entity is created, it doesn't have any data in it. We'll show how to import data in the next topic.

![Custom entity fields](./media/learning-common-data-service-custom-entities/custom-fields.png)


## Creating a relationship between two entities
Because we want to associate each review with a particular product, we need to create a relationship between the Product review entity and the Product entity. In the Product review entity, on the **Relationships** tab, click **New relationship**. Then select a **Related entity**, and enter a **Name**, a **Display name**, and a **Description**. Click **Save** to create the relationship.

![Create relationship between entities](./media/learning-common-data-service-custom-entities/create-entity-relationship.png)


## Connecting to a custom entity in PowerApps Studio
Connecting to a custom entity in PowerApps Studio is just like connecting to a standard entity. Click **New**, then under **Common Data Service**, click **Phone layout**. You see available data connections on the left and the list of entities on the right.

![Connect to entity in PowerApps Studio](./media/learning-common-data-service-custom-entities/connect-to-custom-entity.png)

In the next topic, we'll show you how to manage data in the Common Data Service.