# Domain Language

- Module = A unit to be assembled - this can either be a subassembly or a finished item
BOM (Bill of Materials) = A series of BOM Lines that are combined to produce a Module. A BOM has a Version.
BOM Version = an indication of which iteration of BOM is being used. The finished Module of a BOM
Item = A part with a part number and description. By itself, this does not have a revision.
BOM Line = An Item (can be raw material or WIP/subassembly) with related Parent Item, as well as a Quantity and Unit of Measure
Work Order = a request for some quantity of Modules to be built, all for the same Item
Pick List = A subset of the Line Items of a BOM of a Module, with quantities reflecting the Module quantity of a Work Order. If a WIP Line Item of a BOM is listed on the Pick List, the raw material components of that Line Item are not included on the Pick List, and vice versa.
Record = A data record stored in persistent storage for any domain entity
