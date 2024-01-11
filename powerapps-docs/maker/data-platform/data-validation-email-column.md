---
title: Email address validation for email columns in Dataverse
description: Explains address validation for email columns with Microsoft Dataverse
author: Mattp123
ms.author: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 03/30/2023
ms.custom: template-how-to
---
# Email address validation for email columns (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Get email address columns validated automatically in model-driven apps with no-code. With smart data validation, makers can build smarter and contextually aware next-gen apps for their workflows with better data quality.

Traditionally, the existing email column type had only basic email validation. With smart email address validation, the email column format comes with better validation that includes reasons for the column being invalid. Any model-driven apps using a text column with email format receives automatic validation, which is helpful in guiding users to enter better email data.

> [!IMPORTANT]
> - This is a preview feature.
> - During preview, these regions will have email address validation feature available: Asia (East, Southeast), Australia (East, Southeast), Canada (Central, East), Europe (North, West), France (Central, South), India (Central, South), Japan (East, West), South America – Brazil (South), Switzerland (North, West), UAE (North), UK (South, West), US (East, West).
> - Smart email validation currently only works for model-driven apps.
> - Smart email validation shows validation issues but won't block users from saving their record.

Email address validation detects the following issues:

- Incorrect syntax: For example, an address that doesn't contain both a username and an email domain.
- Disposable domain: An address that contains a known disposable or temporary email domain.
- Test or spam email addresses. An address that contains known indicators of a test or spam address in the email header or metadata, IP address, HTML code of the email, and email content and formatting.
- Expired email addresses: This is an email account that has expired and can no longer receive or send email.
- Emails that bounce back: This is an address that can't receive a message for any reason other than being expired.

## Prerequisites

- The **Data validation** Power Platform environment setting must be enabled. By default, this setting is disabled. More information: [Manage feature settings](/power-platform/admin/settings-features#settings)
- Email address validation only performs validation on text columns with the **Email** format type. For example, the **Email** or **Email Address 2** columns for the account table.

## Enable an email format column for address validation

1. Make sure the model-driven app has a table with a text data type column formatted for email, such as the **Email** column for the contact table.
   :::image type="content" source="media/contact-email-column.png" alt-text="Contact email column properties":::
1. In the app designer, select **Settings** on the command bar.
1. Select the Upcoming tab, and then select **Enable Smart Email Address Validation Control**.
1. Select **Save**.

## Test email address validation

1. In the app designer, select Play on the command bar.
1. Open a form that has the email column, such as the **Email** column for the accounts table.
1. Enter an invalid email address, such as a domain that doesn't exist, such as *example12345678910.com*, in the **Email** column.

Notice that the notification message **The domain is unknown** appears under the column.
:::image type="content" source="media/address-validation-test.png" alt-text="Email address with invalid domain.":::

## Known issue

The **Enable Smart Email Address Validation Control** app setting can be enabled even though the **Data Validation** Power Platform admin center environment setting is off. In this situation, email address validation won't work.

## Next steps

[Create and edit columns in Dataverse using Power Apps](create-edit-field-portal.md)
