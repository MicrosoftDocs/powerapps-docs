---
author: edupont04
ms.topic: include
ms.date: 04/13/2023
ms.author: edupont
---
| Process step | Process stage | Process modifiers | App, navigation, and entity |
|--|--|--|--|
| [Credit and collections parameters](/dynamics365/finance/accounts-receivable/set-up-collections) | Initialize; Base; Configuration | Gold; At least one | **FIN**: Credit and collections > Setup > Credit and collections parameters > Credit tab > Credit limit FastTab<br /></br><br /></br>**DMF**: *CustomerParameters* |
| [Establish customer terms of payment](/dynamics365/finance/general-ledger/tasks/establish-customer-payment-terms) | Design; Fundamental; Configuration | Gold; At least one is required; Multiple are recommended | **FIN**: Accounts receivable > Payments setup > Payment days<br /></br><br /></br>**DMF**: *PaymentTerm* |