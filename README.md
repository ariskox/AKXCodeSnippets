AKXCodeSnippets
===============

My Xcode Code Snippets.

# Code Snippet listing

(This snippet list was generated using [Kirby Turner's](http://github.com/kirbyt) 'lscs.py')

## Property, Strong, NSMutableArray
**Shortcut**: @propertyStrongNSMutableArray  
**File**: [018F5B33-92D9-4DA6-B61D-8BBB8FC91C10.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/018F5B33-92D9-4DA6-B61D-8BBB8FC91C10.codesnippet)  
**Scope**: ClassInterfaceMethods  
**Summary**: A declaration of a strong NSMutableArray property  

    /** <#comment#> */  
    @property (nonatomic, strong) NSMutableArray *<#propertyName#>;  
      

## CellForRowAtIndexPath Block
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
      

## Property, Strong, NSString
**Shortcut**: @propertyStrongNSString  
**File**: [2853A27C-4F26-4315-8F5A-FCAF3F19B4D2.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/2853A27C-4F26-4315-8F5A-FCAF3F19B4D2.codesnippet)  
**Scope**: All  
**Summary**: A declaration of a NSString strong property  

    /** <#comment#> */  
    @property (nonatomic, strong) NSString *<#propertyName#>;  
      

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
      

## Method declaration, returns NSString *
**Shortcut**: nsstring *  
**File**: [541DB8DC-4C48-11E2-A1DE-58B035F72A9C.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/541DB8DC-4C48-11E2-A1DE-58B035F72A9C.codesnippet)  
**Scope**: ClassInterfaceMethods  
**Summary**: A declaration of a method that returns NSString *  

    /** <#comments#> */  
    - (NSString *) <#methodname#>;  
      

## Property, strong, NSArray
**Shortcut**: @propertyStrongNSArray  
**File**: [5C28E459-9EB1-4AEE-BE43-A5A92A11A10B.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/5C28E459-9EB1-4AEE-BE43-A5A92A11A10B.codesnippet)  
**Scope**: ClassInterfaceMethods  
**Summary**: A declaration of a strong NSArray property  

    /** <#comment#> */  
    @property (nonatomic, strong) NSArray *<#propertyName#>;  
      

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
      

## Method declaration, returns BOOL
**Shortcut**: BOOL  
**File**: [601395EB-4C48-11E2-9FDD-58B035F72A9C.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/601395EB-4C48-11E2-9FDD-58B035F72A9C.codesnippet)  
**Scope**: ClassInterfaceMethods  
**Summary**: A declaration of a method that returns BOOL  

    /** <#comments#> */  
    - (BOOL) <#methodname#>;  
      

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
**Shortcut**: viewDidUnload  
**File**: [665D4E24-7070-43AF-8852-D1F238B805C0.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/665D4E24-7070-43AF-8852-D1F238B805C0.codesnippet)  
**Scope**: ClassImplementation  
**Summary**: A viewDidUnload method implementation  

    - (void)viewDidUnload  
    {  
        [super viewDidUnload];  
        <#append your code here#>  
    }  
      

## NSLog
**Shortcut**: nslog  
**File**: [7FD9DEC2-EA51-4DE0-902C-8F552C1F5258.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/7FD9DEC2-EA51-4DE0-902C-8F552C1F5258.codesnippet)  
**Scope**: CodeBlock  
**Summary**: Simple NSLog snippet  

    NSLog(@"<#formatstring#>",<#variables#>);  

## Property, strong
**Shortcut**: @propertyStrong  
**File**: [8A9DBFC2-A299-4510-B648-13D7B2851F89.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/8A9DBFC2-A299-4510-B648-13D7B2851F89.codesnippet)  
**Scope**: ClassInterfaceMethods  
**Summary**: A declaration of a strong property  

    /** <#comment#> */  
    @property (nonatomic, strong) <#type#> *<#propertyName#>;  
      

## Class Comments
**Shortcut**: comment  
**File**: [8AC0941D-3E54-4F88-9591-716BCFEF6577.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/8AC0941D-3E54-4F88-9591-716BCFEF6577.codesnippet)  
**Scope**: TopLevel  
**Summary**: The standard comments for each class  

    /****************************************************************************************/  
    /*	class <#classname#>	*/  
    /****************************************************************************************/  
    /**  
     <#insert class description#>  
       
     Sample use:  
     <#insert sample use here#>  
       
     See also: <#seealso#>  
     */  
      

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
      

## Property, strong, NSNumber
**Shortcut**: @propertyStrongNSNumber  
**File**: [A1E58414-4093-41B1-BE27-6F0E99E52918.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/A1E58414-4093-41B1-BE27-6F0E99E52918.codesnippet)  
**Scope**: ClassInterfaceMethods  
**Summary**: A declaration of a strong NSNumber property  

    /** <#comment#> */  
    @property (nonatomic, strong) NSNumber *<#propertyName#>;  
      

## Method declaration, returns VOID
**Shortcut**: void  
**File**: [A5062BFB-6DC4-4D67-9FC8-BC6F4D41FF79.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/A5062BFB-6DC4-4D67-9FC8-BC6F4D41FF79.codesnippet)  
**Scope**: ClassInterfaceMethods  
**Summary**: A declaration of a method that returns void  

    /** <#comments#> */  
    - (void) <#methodname#>;  
      

## Property, strong, NSDate
**Shortcut**: @propertyStrongNSDate  
**File**: [AC21B10E-CD83-49D7-A9C0-06BB21E9067B.codesnippet](http://github.com/ariskox/AKXCodeSnippets/blob/master/AC21B10E-CD83-49D7-A9C0-06BB21E9067B.codesnippet)  
**Scope**: ClassInterfaceMethods  
**Summary**: A declaration of a strong NSDate Property  

    /** <#comment#> */  
    @property (nonatomic, strong) NSDate *<#propertyName#>;  
      

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
      

