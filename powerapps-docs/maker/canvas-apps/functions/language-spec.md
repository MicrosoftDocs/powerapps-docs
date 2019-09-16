---
title: PowerApps formula language specification | Microsoft Docs
description: PowerApps formula language Specification
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 08/15/2019
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# PowerApps formula language specification

Formal description of the PowerApps formula language.  Use it to gain insights into how PowerApps formulas work, the design principles, and the formal semantics.

Version 0.1
August 15, 2019  

## Table of contents

* [1 Introduction](#1)
  * [1.1 Definitions](#1.1)
    * [1.1.1 Author](#1.1.1)
    * [1.1.2 Compiler](#1.1.2)
  * [1.2 Principles](#1.2)
    * [1.2.1 Excel consistency](#1.2.1)
    * [1.2.2 Declarative](#1.2.2)
    * [1.2.3 Functional](#1.2.3)
    * [1.2.4 Strongly typed](#1.2.4)
    * [1.2.5 Type inference](#1.2.5)
    * [1.2.6 Composition](#1.2.6)
    * [1.2.7 Concept count](#1.2.7)
    * [1.2.8 Not object oriented](#1.2.8)
  * [1.3 Primitive types](#1.3)
  * [1.4 Compound types](#1.4)
    * [1.4.1 Records](#1.4.1)
    * [1.4.2 Tables](#1.4.2)
* [2 Record scope](#2)
* [3 Glossary](#3)
* [4 Appendix](#4)

## <a name="1"/>1 Introduction 

### <a name="1.1"/>1.1 Definitions 

#### <a name="1.1.1"/>1.1.1 Author 

#### <a name="1.1.2"/>1.1.2 Compiler 

### <a name="1.2"/>1.2 Principles 

#### <a name="1.2.1"/>1.2.1 Excel consistency 

The PowerApps language borrows heavily from the Excel formula language.  We seek to leverage as much Excel knowledge and experience from the many makers who also use Excel.  Where present in both, types, operators, and function semantics are as close to Excel as possible.

#### <a name="1.2.2"/>1.2.2 Declarative 

The maker describes "what" they want their logic to do, not exactly "how" it is to be done.  This allows the compiler to optimize by performing operations in parallel, deferring work until needed, pre-fetching and reusing cached data, etc.

For example, in an Excel spreadsheet the author defines the relationships between cells but Excel decides when and in what order formulas are evaluated.  Similarly, formulas in an app can be thought of as "recalcing" as needed based on user actions, database changes, or timer events.  

#### <a name="1.2.3"/>1.2.3 Functional 

We favor functions that are pure without side effects.  This results in logic which is easier to understand and gives the compiler the most freedom to optimize.

However, unlike Excel, apps by their nature mutate state.  For example, apps have buttons that save changes to the record in a database.  Some functions therefore do have side effects, although we limit this as much as practical. 

#### <a name="1.2.4"/>1.2.4 Strongly typed 

The types of all values are known at compile time.  This allows for the early detection of errors and rich suggestions while authoring. 

Polymorphic types are supported, but before being used their type must be pinned to a static type and that type must be known at compile time.

#### <a name="1.2.5"/>1.2.5 Type inference 

Types are derived from their use without being declared.  For example, setting a variable to a number results in that variable's type being established as a number.

Conflicting type usage results in a compile time error.

#### <a name="1.2.6"/>1.2.6 Composition 

#### <a name="1.2.7"/>1.2.7 Concept count 

#### <a name="1.2.8"/>1.2.8 Not object oriented 

### <a name="1.3"/>1.3 Primitive types 

### <a name="1.4"/>1.4 Compound types 

#### <a name="1.4.1"/>1.4.1 Records 

#### <a name="1.4.2"/>1.4.2 Tables 

## <a name="2"/>2 Record scope 

## <a name="3"/>3 Glossary 

## <a name="4"/>4 Appendix 



