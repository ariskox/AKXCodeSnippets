AKXCodeSnippets
===============

My Xcode code snippets.## CellForRowAtIndexPath Block
**Shortcut**: cellforrow  
**File**: [1B9E3BE9-302D-4D28-A380-B8507E42C3F4.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/1B9E3BE9-302D-4D28-A380-B8507E42C3F4.codesnippet)  
**Scope**: All  
**Summary**: a Sensible tableView CellForRowAtIndexPath Block  

    ^SCCustomCell*(SCTableViewSection *section, NSIndexPath *indexPath) {  
        <#insertcodehere#>  
    };  

## Property, strong, id
**Shortcut**: @propertyStrongId  
**File**: [1BCF2B31-B0BF-438E-A532-92B9021B9563.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/1BCF2B31-B0BF-438E-A532-92B9021B9563.codesnippet)  
**Scope**: All  
**Summary**: A declaration of an strong ID property  

    /** <#comment#> */  
    @property (nonatomic, strong) id <#propertyName#>;  
      
      

## viewDidAppear: method
**Shortcut**: viewDidAppear  
**File**: [1D9AE36E-7D81-4990-A77F-627EEEC62417.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/1D9AE36E-7D81-4990-A77F-627EEEC62417.codesnippet)  
**Scope**: ClassImplementation  
**Summary**: A viewDidAppear: method implementation  

    - (void) viewDidAppear:(BOOL)animated  
    {  
        [super viewDidAppear:animated];  
        <#append your code here#>  
    }  
      

## Property, assign
**Shortcut**: @propertyAssign  
**File**: [2301C7D6-DBEA-417A-9567-10C2F9251C33.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/2301C7D6-DBEA-417A-9567-10C2F9251C33.codesnippet)  
**Scope**: ClassInterfaceMethods  
**Summary**: A declaration of an assigned property  

    /** <#comment#> */  
    @property (nonatomic, assign) <#type#> *<#propertyName#>;  
      

## viewWillAppear: method
**Shortcut**: viewWillAppear  
**File**: [2397A836-C894-4057-AA87-A1CAF0969845.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/2397A836-C894-4057-AA87-A1CAF0969845.codesnippet)  
**Scope**: ClassImplementation  
**Summary**: a viewWillAppear: method implementation  

    - (void) viewWillAppear:(BOOL)animated  
    {  
        [super viewWillAppear:animated];  
        <#append your code here#>  
    }  
      

## Property, weak
**Shortcut**: @propertyWeak  
**File**: [27FCE50E-EEDC-4A04-94ED-732EC82FB422.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/27FCE50E-EEDC-4A04-94ED-732EC82FB422.codesnippet)  
**Scope**: ClassInterfaceMethods  
**Summary**: A declaration of a weak property  

    /** <#comment#> */  
    @property (nonatomic, weak) <#type#> *<#propertyName#>;  
      

## Method implementation, returns NSString *
**Shortcut**: nsstring  
**File**: [3EFBDA27-B6B1-411C-9BF6-CE0BB585207E.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/3EFBDA27-B6B1-411C-9BF6-CE0BB585207E.codesnippet)  
**Scope**: ClassImplementation  
**Summary**: An Implementation of a method that returns an NSString *  

    - (NSString *)<#functionname#>  
    {  
        <#writecodehere#>  
          
        return <#returnValue#>;  
    }  
      

## Lazy SCTableViewSection Implementation
**Shortcut**: ls  
**File**: [51667C2A-BF9F-4663-AECB-5DA26B63337C.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/51667C2A-BF9F-4663-AECB-5DA26B63337C.codesnippet)  
**Scope**: ClassImplementation  
**Summary**: Use to implement a lazy-loaded SCTableViewSection  

    - (SCTableViewSection *)sectionName  
    {  
        if (section2)  
            return section2;  
          
          
        return section2;  
    }  
      

## viewWillDisappear: method
**Shortcut**: viewWillDisappear  
**File**: [5F52B985-9B99-442F-8E73-9712B087D012.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/5F52B985-9B99-442F-8E73-9712B087D012.codesnippet)  
**Scope**: ClassImplementation  
**Summary**: a viewWillDisappear: method implementation  

    - (void)viewWillDisappear:(BOOL)animated  
    {  
        [super viewWillDisappear:animated];  
        <#append your code here#>  
    }  
      

## Property, UILabel, strong
**Shortcut**: @propertyStrongUILabel  
**File**: [64F48D26-B477-42D1-9C3D-272CDB31558D.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/64F48D26-B477-42D1-9C3D-272CDB31558D.codesnippet)  
**Scope**: ClassInterfaceMethods  
**Summary**: A declaration of a UILabel strong property  

    /** <#comment#> */  
    @property (nonatomic, strong) <#IBOutlet#> UILabel *<#variableName#>;  
      

## Method implementation, returns BOOL
**Shortcut**: bool  
**File**: [65BF89CA-D3B4-407E-9589-25DDF13303C8.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/65BF89CA-D3B4-407E-9589-25DDF13303C8.codesnippet)  
**Scope**: ClassImplementation  
**Summary**: An implementation of a function that returns BOOL  

    - (BOOL)<#functionname#>  
    {  
        <#writecodehere#>  
          
        return <#returnValue#>;  
    }  

## viewDidUnload method
**Shortcut**: viewdidunload  
**File**: [665D4E24-7070-43AF-8852-D1F238B805C0.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/665D4E24-7070-43AF-8852-D1F238B805C0.codesnippet)  
**Scope**: ClassImplementation  
**Summary**: A viewDidUnload method implementation  

    - (void)viewDidUnload  
    {  
        [super viewDidUnload];  
        <#append your code here#>  
    }  
      

## Property, strong
**Shortcut**: @propertyStrong  
**File**: [8A9DBFC2-A299-4510-B648-13D7B2851F89.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/8A9DBFC2-A299-4510-B648-13D7B2851F89.codesnippet)  
**Scope**: ClassInterfaceMethods  
**Summary**: A declaration of a strong property  

    /** <#comment#> */  
    @property (nonatomic, strong) <#type#> *<#propertyName#>;  
      

## Weak Self
**Shortcut**: weakself  
**File**: [9358E293-2334-4A53-829E-EC314416EAD8.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/9358E293-2334-4A53-829E-EC314416EAD8.codesnippet)  
**Scope**: CodeBlock  
**Summary**: A 'weakSelf' unsafe unretained variable to use within blocks  

    __unsafe_unretained id weakSelf = self;  
      

## viewDidDisappear: methof
**Shortcut**: viewDidDisappear  
**File**: [948940A6-C136-4302-A341-F898372C41FA.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/948940A6-C136-4302-A341-F898372C41FA.codesnippet)  
**Scope**: ClassImplementation  
**Summary**: A viewDidDisappear: method implementation  

    - (void) viewDidDisappear:(BOOL)animated  
    {  
        [super viewDidDisappear:animated];  
        <#append your code here#>  
    }  
      

## NSLog CGRect
**Shortcut**: printbounds  
**File**: [AC95A2D8-7850-4249-8F19-EAE56EA48638.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/AC95A2D8-7850-4249-8F19-EAE56EA48638.codesnippet)  
**Scope**: CodeBlock  
**Summary**: NSLog a CGRect structure  

    NSLog(@"bounds = %@", NSStringFromCGRect(<#varname#>));  
      

## Property, UIView, strong
**Shortcut**: @propertyStrongUIView  
**File**: [B403B885-94C5-4807-ACBF-82B123A2B599.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/B403B885-94C5-4807-ACBF-82B123A2B599.codesnippet)  
**Scope**: ClassInterfaceMethods  
**Summary**: A declaration of a UIView * property  

    /** <#comment#> */  
    @property (nonatomic, strong) <#IBOutlet#> UIView *<#viewName#>;  
      

## Method implementation, returns VOID
**Shortcut**: void  
**File**: [C5A71878-6161-4E86-9E01-142ED47F1AD9.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/C5A71878-6161-4E86-9E01-142ED47F1AD9.codesnippet)  
**Scope**: ClassImplementation  
**Summary**: An Implementation of a method that returns nothing  

    - (void)<#functionname#>  
    {  
        <#writecodehere#>  
    }  
      

## ARC Enforcement
**Shortcut**: arc  
**File**: [EDF72212-D99D-40DD-842C-B9DF369585F8.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/EDF72212-D99D-40DD-842C-B9DF369585F8.codesnippet)  
**Scope**: TopLevel  
**Summary**: Used on an implementation file to force compilation with ARC  

    #if ! __has_feature(objc_arc)  
    #error This Class requires ARC. Either turn on ARC for the project or use -fobjc-arc flag  
    #endif  
      

## viewDidLoad method
**Shortcut**: viewDidLoad  
**File**: [FBE9B61A-DC77-4B0C-AFF9-7F2DDF35B5CF.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/FBE9B61A-DC77-4B0C-AFF9-7F2DDF35B5CF.codesnippet)  
**Scope**: ClassImplementation  
**Summary**: A viewDidLoad method implementation  

    - (void)viewDidLoad  
    {  
        [super viewDidLoad];  
        <#append your code here#>  
    }  
      

## cellAction Block
**Shortcut**: ca  
**File**: [FE657430-F60D-4774-9DC9-8A2930F9E3BB.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/FE657430-F60D-4774-9DC9-8A2930F9E3BB.codesnippet)  
**Scope**: CodeBlock  
**Summary**: A SensibleTableView cellAction Block  

    ^(SCTableViewCell *aCell, NSIndexPath *indexPath) {  
      
    };  
      

