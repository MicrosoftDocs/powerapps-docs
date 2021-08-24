---
title: "Transaction Currency (currency) table (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about transaction table, which is a multicurrency feature enabling users to perform financial transactions in multiple currencies. Multiple records in different transaction currencies can be aggregated, compared, or analyzed with regard to a single currency using the base currency." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 07/19/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Transaction Currency (currency) table

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Dataverse is a multicurrency system, in which each record can be associated with its own currency. This currency is called the *transaction* currency. The multicurrency features enable users to perform financial transactions like opportunities, quotes, orders, and invoices in multiple currencies. This feature also provides a currency choice to the end user when a financial transaction occurs.  
  
 Multiple records in different transaction currencies can be aggregated, compared, or analyzed with regard to a single currency, by using an exchange rate. This is known as the *base currency*. You first define a base currency for the organization and then define exchange rates to associate the base currency with transaction currencies. The base currency is the currency in which other currencies are quoted. The exchange rate is the value of a transaction currency equal to one base currency.  
  
 By using the transaction currency properties, you can do the following:  
  
- Select the currency in which you want to define and transact opportunities, quotes, orders, and invoices.  
  
- Define currency exchange rates relative to the base currency.  
  
- Define transaction currencies and define an exchange rate to associate the base currency with the transaction currency.  
  
- Capture the value of the transaction in the base currency and the transaction currency in all financial transactions.  
  
- Define product pricelists for each currency.  
  
To use multiple currencies, the base currency must be defined for an organization during server installation and organization setup. After the base currency is set for an organization, it cannot be changed. This value is stored in the `Organization.BaseCurrencyID` attribute.  
  
Transaction currencies are defined as a part of the system settings. An unlimited number of transaction currencies can be defined. Transaction currencies are related to the base currency with the definition of a currency exchange rate.  
  
After the definition of base and transaction currencies, pricelists must be defined. An organization can have multiple pricelists, which are also typically defined for a target geographical market in the local currency.  
  
All tables that are involved in financial transactions support transaction currency. The currency is typically inherited from the account, opportunity, and so on, but can be changed as needed.  
  
You can specify the decimal precision for the transaction currency by using the `TransactionCurrency.CurrencyPrecision` attribute. To specify the source of the precision for the attributes of type Money, use the <xref:Microsoft.Xrm.Sdk.Metadata.MoneyAttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.MoneyAttributeMetadata.PrecisionSource> attribute.  
  
All money properties in a record share the same transaction currency, for example, see the `Account.CreditLimit` attribute. For each money attribute in a table, Dataverse automatically creates a corresponding read-only, system calculated, money attribute that is called the "base". This is a money attribute that stores the value of the corresponding attribute in a base currency equivalent, for example, see the `Account.CreditLimit_Base` attribute.  
  
The following formula is used to calculate the base value:  
  
```csharp  
creditlimit_base = creditlimit / exchangerate  
```  
  
Transaction currency can be defined for the following tables:  
  
-   Account  
  
-   AnnualFiscalCalendar  
  
-   Campaign  
  
-   CampaignActivity  
  
-   Competitor  
  
-   Contact  
  
-   Contract  
  
-   ContractDetail  
  
-   Discount  
  
-   DiscountType  
  
-   FixedMonthlyFiscalCalendar  
  
-   Invoice  
  
-   InvoiceDetail  
  
-   Lead  
  
-   List  
  
-   MonthlyFiscalCalendar  
  
-   Opportunity  
  
-   OpportunityClose  
  
-   OpportunityProduct  
  
-   PriceLevel  
  
-   Product  
  
-   ProductPriceLevel  
  
-   QuarterlyFiscalCalendar  
  
-   Quote  
  
-   QuoteDetail  
  
-   SalesOrder  
  
-   SalesOrderDetail  
  
-   SemiAnnualFiscalCalendar  
  
-   UserSettings  
  
### See also  
 [TransactionCurrency table](reference/entities/transactioncurrency.md)   
 [Sample: Retrieve Currency Exchange Rate](org-service/samples/retrieve-currency-exchange-rate.md)   
 
[!INCLUDE[footer-include](../../includes/footer-banner.md)]
